import transaction

from tg import TGController, request, expose, redirect, tmpl_context, validate
from pz5.model import DBSession

from pz5.model.LiteratyreType import LiteratyreType
from pz5.forms.LiteratureTypeForms import LiteratureTypeCreateForm, LiteratureTypeEditForm

__all__ = ["LiteratureTypeController"]


class LiteratureTypeController(TGController):

    def _before(self, *args, **kw):
        tmpl_context.project_name = "pz5"

    @expose('pz5.templates.litType/index')
    def _default(self):
        litTypes = DBSession.query(LiteratyreType).all()
        return dict(types=litTypes)

    @expose()
    def delete(self, idName):
        litType = LiteratyreType.getById(idName)
        if litType:
            DBSession.delete(litType)
            transaction.commit()
        redirect("/litType/index")


    @expose("pz5.templates.litType/add_edit")
    def showCreate(self, *args, **kwargs):
        print('show create', args)
        print('show create', kwargs)
        return dict(form=LiteratureTypeCreateForm)

    @expose()
    @validate(LiteratureTypeCreateForm, error_handler=showCreate)
    def create(self, **kwargs):
        print('create', kwargs)
        DBSession.add(LiteratyreType(typeName=kwargs['typeName']))
        transaction.commit()
        redirect("/litType/index")

    @expose("pz5.templates.litType/add_edit")
    def showEdit(self, *args, **kwargs):
        print('show edit', args)
        print('show edit', kwargs)
        t = LiteratyreType.getById(kwargs['idName'])
        if t:
            kwargs['typeName'] = t.typeName
        return dict(form=LiteratureTypeEditForm, **kwargs)

    @expose()
    @validate(LiteratureTypeEditForm, error_handler=showEdit)
    def edit(self, **kwargs):
        print('edit', kwargs)
        LiteratyreType.getById(kwargs['idName']).typeName = kwargs['typeName']
        transaction.commit()
        redirect("/litType/index")
