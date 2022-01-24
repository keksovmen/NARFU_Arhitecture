import transaction
from pz5.forms.FondRefuelForms import FondRefuelCreateForm, FondRefuelEditForm
from pz5.model import DBSession
from pz5.model.FondRefuel import FondRefuel
from tg import TGController, expose, redirect, tmpl_context, validate

__all__ = ["FondRefuelController"]


class FondRefuelController(TGController):

	def _before(self, *args, **kw):
		tmpl_context.project_name = "pz5"

	@expose('pz5.templates.fr/index')
	def _default(self):
		data = DBSession.query(FondRefuel).all()
		return dict(refuels=data)

	@expose()
	def delete(self, refuelId):
		d = FondRefuel.getById(refuelId)
		if d:
			DBSession.delete(d)
			transaction.commit()
		redirect("/fr/index")

	@expose("pz5.templates.fr/add_edit")
	def showCreate(self, *args, **kwargs):
		print('show create', args)
		print('show create', kwargs)
		return dict(form=FondRefuelCreateForm)

	@expose()
	@validate(FondRefuelCreateForm, error_handler=showCreate)
	def create(self, source, publisher, amount, publishDate,
			   refuelDate, fondId, stuffId, litType, **kwargs):
		print('create', kwargs)
		DBSession.add(
			FondRefuel(source=source, publisher=publisher, amount=amount,
					   publishDate=publishDate, refuelDate=refuelDate,
					   fondId=fondId, stuffId=stuffId, litType=litType))
		transaction.commit()
		redirect("/fr/index")

	@expose("pz5.templates.fr/add_edit")
	def showEdit(self, *args, **kwargs):
		print('show edit', args)
		print('show edit', kwargs)
		d = FondRefuel.getById(kwargs['refuelId'])
		if d:
			kwargs['source'] = d.source
			kwargs['publisher'] = d.publisher
			kwargs['amount'] = d.amount
			kwargs['publishDate'] = d.publishDate
			kwargs['refuelDate'] = d.refuelDate
			kwargs['fondId'] = d.fondId
			kwargs['stuffId'] = d.stuffId
			kwargs['litType'] = d.litType
		return dict(form=FondRefuelEditForm, **kwargs)

	@expose()
	@validate(FondRefuelEditForm, error_handler=showEdit)
	def edit(self, refuelId, source, publisher, amount, publishDate,
			 refuelDate, fondId, stuffId, litType, **kwargs):
		print('edit', kwargs)
		d = FondRefuel.getById(refuelId)
		d.source = source
		d.publisher = publisher
		d.amount = amount
		d.publishDate = publishDate
		d.refuelDate = refuelDate
		d.fondId = fondId
		d.stuffId = stuffId
		d.litType = litType
		transaction.commit()
		redirect("/fr/index")
