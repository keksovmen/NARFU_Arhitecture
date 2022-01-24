import transaction
from pz5.forms.FondForms import FondCreateForm, FondEditForm
from pz5.model import DBSession
from pz5.model.Fond import Fond
from tg import TGController, expose, redirect, tmpl_context, validate

__all__ = ["FondController"]


class FondController(TGController):

	def _before(self, *args, **kw):
		tmpl_context.project_name = "pz5"

	@expose('pz5.templates.fond/index')
	def _default(self):
		data = DBSession.query(Fond).all()
		return dict(fonds=data)

	@expose()
	def delete(self, fondId):
		d = Fond.getById(fondId)
		if d:
			DBSession.delete(d)
			transaction.commit()
		redirect("/fond/index")

	@expose("pz5.templates.fond/add_edit")
	def showCreate(self, *args, **kwargs):
		print('show create', args)
		print('show create', kwargs)
		return dict(form=FondCreateForm)

	@expose()
	@validate(FondCreateForm, error_handler=showCreate)
	def create(self, name, books, magazines, papers,
			   dictinaries, dissertations, referats, libId, **kwargs):
		print('create', kwargs)
		DBSession.add(
			Fond(name=name, books=books, magazines=magazines, papers=papers,
				 dictinaries=dictinaries, dissertations=dissertations,
				 referats=referats, libId=libId))
		transaction.commit()
		redirect("/fond/index")

	@expose("pz5.templates.fond/add_edit")
	def showEdit(self, *args, **kwargs):
		print('show edit', args)
		print('show edit', kwargs)
		d = Fond.getById(kwargs['fondId'])
		if d:
			kwargs['name'] = d.name
			kwargs['books'] = d.books
			kwargs['magazines'] = d.magazines
			kwargs['papers'] = d.papers
			kwargs['dictinaries'] = d.dictinaries
			kwargs['dissertations'] = d.dissertations
			kwargs['referats'] = d.referats
			kwargs['libId'] = d.libId
		return dict(form=FondEditForm, **kwargs)

	@expose()
	@validate(FondEditForm, error_handler=showEdit)
	def edit(self, fondId, name, books, magazines, papers,
			 dictinaries, dissertations, referats, libId, **kwargs):
		print('edit', kwargs)
		d = Fond.getById(fondId)
		d.name = name
		d.books = books
		d.magazines = magazines
		d.papers = papers
		d.dictinaries = dictinaries
		d.dissertations = dissertations
		d.referats = referats
		d.libId = libId
		transaction.commit()
		redirect("/fond/index")
