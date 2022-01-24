import tw2.core as twc
import tw2.forms as twf
from formencode.compound import Pipe
from formencode.validators import NotEmpty, Number
from pz5.forms.CustomValidators import *
from pz5.model.Library import Library

__all__ = ["LibraryCreateForm", "LibraryEditForm"]


class LibraryCreateFields(twf.TableLayout):
	name = twf.TextField(validator=Pipe(NotEmpty))
	address = twf.TextField(validator=Pipe(NotEmpty))
	city = twf.TextField(validator=Pipe(NotEmpty))


class LibraryEditFields(twf.TableLayout):
	libId = twf.HiddenField(validator=Pipe(NotEmpty, Number))
	name = twf.TextField(validator=Pipe(NotEmpty))
	address = twf.TextField(validator=Pipe(NotEmpty))
	city = twf.TextField(validator=Pipe(NotEmpty))


class LibraryCreateForm(twf.Form):
	child = LibraryCreateFields()
	action = "create"
	validator = NotExistance(Library, 'msg', 'address', 'city')


class LibraryEditForm(twf.Form):
	child = LibraryEditFields()
	action = "edit"
	validator = NotExistance(Library, 'msg', 'address', 'city')
