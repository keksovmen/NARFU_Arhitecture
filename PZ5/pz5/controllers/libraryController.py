import transaction
from pz5.forms.LibraryForms import LibraryCreateForm, LibraryEditForm
from pz5.model import DBSession
from pz5.model.Library import Library
from tg import TGController, expose, redirect, tmpl_context, validate

__all__ = ["LibraryController"]


class LibraryController(TGController):

	def _before(self, *args, **kw):
		tmpl_context.project_name = "pz5"

	@expose('pz5.templates.library/index')
	def _default(self):
		libs = DBSession.query(Library).all()
		return dict(libraries=libs)

	@expose()
	def delete(self, libId):
		lib = Library.getById(libId)
		if lib:
			DBSession.delete(lib)
			transaction.commit()
		redirect("/lib/index")

	@expose("pz5.templates.library/add_edit")
	def showCreate(self, *args, **kwargs):
		print('show create', args)
		print('show create', kwargs)
		return dict(form=LibraryCreateForm)

	@expose()
	@validate(LibraryCreateForm, error_handler=showCreate)
	def create(self, name, address, city, **kwargs):
		print('create', kwargs)
		DBSession.add(Library(name=name, address=address, city=city))
		transaction.commit()
		redirect("/lib/index")

	@expose("pz5.templates.library/add_edit")
	def showEdit(self, *args, **kwargs):
		print('show edit', args)
		print('show edit', kwargs)
		lib = Library.getById(kwargs['libId'])
		if lib:
			kwargs['msg'] = lib.name
			kwargs['address'] = lib.address
			kwargs['city'] = lib.city
		return dict(form=LibraryEditForm, **kwargs)

	@expose()
	@validate(LibraryEditForm, error_handler=showEdit)
	def edit(self, libId, name, address, city, **kwargs):
		print('edit', kwargs)
		lib = Library.getById(libId)
		lib.name = name
		lib.address = address
		lib.city = city
		transaction.commit()
		redirect("/lib/index")
