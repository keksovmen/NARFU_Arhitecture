import tw2.core as twc
import tw2.forms as twf
from formencode.compound import Pipe
from formencode.validators import NotEmpty, Number
from pz5.forms.CustomValidators import *
from pz5.model.LiteratyreType import LiteratyreType

__all__ = ["LiteratureTypeCreateForm", "LiteratureTypeEditForm"]


class LiteratureTypeCreateFields(twf.TableLayout):
	typeName = twf.TextField(validator=Pipe(NotEmpty, Number))


class LiteratureTypeEditFields(twf.TableLayout):
	idName = twf.HiddenField(validator=twc.Required)
	typeName = twf.TextField(validator=Pipe(NotEmpty, Number))


class LiteratureTypeCreateForm(twf.Form):
	child = LiteratureTypeCreateFields()
	action = "create"
	validator = NotExistance(LiteratyreType, 'typeName')


class LiteratureTypeEditForm(twf.Form):
	child = LiteratureTypeEditFields()
	action = "edit"
	validator = NotExistance(LiteratyreType, 'typeName')
