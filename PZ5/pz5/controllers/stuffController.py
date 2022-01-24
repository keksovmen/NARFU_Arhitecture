import transaction
from pz5.forms.StuffForms import StuffCreateForm, StuffEditForm
from pz5.model import DBSession
from pz5.model.Stuff import Stuff
from tg import TGController, expose, redirect, tmpl_context, validate

__all__ = ["StuffController"]


class StuffController(TGController):

	def _before(self, *args, **kw):
		tmpl_context.project_name = "pz5"

	@expose('pz5.templates.stuff/index')
	def _default(self):
		data = DBSession.query(Stuff).all()
		return dict(stuff=data)

	@expose()
	def delete(self, stuffId):
		d = Stuff.getById(stuffId)
		if d:
			DBSession.delete(d)
			transaction.commit()
		redirect("/stuff/index")

	@expose("pz5.templates.stuff/add_edit")
	def showCreate(self, *args, **kwargs):
		print('show create', args)
		print('show create', kwargs)
		return dict(form=StuffCreateForm)

	@expose()
	@validate(StuffCreateForm, error_handler=showCreate)
	def create(self, lastName, position, education, salary,
			   birthDate, hireDate, libId, **kwargs):
		print('create', kwargs)
		DBSession.add(
			Stuff(lastName=lastName, position=position, education=education,
				  salary=salary, birthDate=birthDate, hireDate=hireDate,
				  libId=libId))
		transaction.commit()
		redirect("/stuff/index")

	@expose("pz5.templates.stuff/add_edit")
	def showEdit(self, *args, **kwargs):
		print('show edit', args)
		print('show edit', kwargs)
		d = Stuff.getById(kwargs['stuffId'])
		if d:
			kwargs['lastName'] = d.lastName
			kwargs['position'] = d.position
			kwargs['education'] = d.education
			kwargs['salary'] = d.salary
			kwargs['birthDate'] = d.birthDate
			kwargs['hireDate'] = d.hireDate
			kwargs['libId'] = d.libId
		return dict(form=StuffEditForm, **kwargs)

	@expose()
	@validate(StuffEditForm, error_handler=showEdit)
	def edit(self, stuffId, lastName, position, education, salary,
			 birthDate, hireDate, libId, **kwargs):
		print('edit', kwargs)
		d = Stuff.getById(stuffId)
		d.lastName = lastName
		d.position = position
		d.education = education
		d.salary = salary
		d.birthDate = birthDate
		d.hireDate = hireDate
		d.libId = libId
		transaction.commit()
		redirect("/stuff/index")
