import tw2.forms as twf
from formencode.compound import Pipe
from formencode.validators import NotEmpty, Number
from pz5.forms.CustomValidators import *
from pz5.model.Library import Library

__all__ = ["FondCreateForm", "FondEditForm"]


class CreateFields(twf.TableLayout):
	name = twf.TextField(validator=Pipe(NotEmpty))
	books = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	magazines = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	papers = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	dictinaries = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	dissertations = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	referats = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	libId = twf.SingleSelectField(options=Library.getAllIds(),
								  validator=Pipe(NotEmpty, Number,
												 ExistByPrimaryKey(Library)))


class EditFields(twf.TableLayout):
	fondId = twf.HiddenField(validator=Pipe(NotEmpty, Number))
	name = twf.TextField(validator=Pipe(NotEmpty))
	books = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	magazines = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	papers = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	dictinaries = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	dissertations = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	referats = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	libId = twf.SingleSelectField(options=Library.getAllIds(),
								  validator=Pipe(NotEmpty, Number,
												 ExistByPrimaryKey(Library)))


class FondCreateForm(twf.Form):
	child = CreateFields()
	action = "create"


class FondEditForm(twf.Form):
	child = EditFields()
	action = "edit"
