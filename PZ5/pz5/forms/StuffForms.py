import tw2.forms as twf
from formencode.compound import Pipe
from formencode.validators import NotEmpty, Number, DateConverter
from pz5.forms.CustomValidators import *
from pz5.model.Library import Library

__all__ = ["StuffCreateForm", "StuffEditForm"]


class CreateFields(twf.TableLayout):
	lastName = twf.TextField(validator=Pipe(NotEmpty))
	position = twf.TextField(validator=Pipe(NotEmpty))
	education = twf.TextField(validator=Pipe(NotEmpty))
	salary = twf.TextField(validator=Pipe(NotEmpty, Number))
	birthDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	hireDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	libId = twf.SingleSelectField(options=Library.getAllIds(),
								  validator=Pipe(NotEmpty, Number,
												 ExistByPrimaryKey(Library)))


class EditFields(twf.TableLayout):
	stuffId = twf.HiddenField(validator=Pipe(NotEmpty, Number))
	lastName = twf.TextField(validator=Pipe(NotEmpty))
	position = twf.TextField(validator=Pipe(NotEmpty))
	education = twf.TextField(validator=Pipe(NotEmpty))
	salary = twf.TextField(validator=Pipe(NotEmpty))
	birthDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	hireDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	libId = twf.SingleSelectField(options=Library.getAllIds(),
								  validator=Pipe(NotEmpty, Number,
												 ExistByPrimaryKey(Library)))


class StuffCreateForm(twf.Form):
	child = CreateFields()
	action = "create"


class StuffEditForm(twf.Form):
	child = EditFields()
	action = "edit"
