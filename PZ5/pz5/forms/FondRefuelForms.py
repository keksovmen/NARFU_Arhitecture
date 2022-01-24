import tw2.forms as twf
from formencode.compound import Pipe
from formencode.validators import NotEmpty, Number, DateConverter
from pz5.forms.CustomValidators import *
from pz5.model.Fond import Fond
from pz5.model.Stuff import Stuff
from pz5.model.LiteratyreType import LiteratyreType

__all__ = ["FondRefuelCreateForm", "FondRefuelEditForm"]


class CreateFields(twf.TableLayout):
	source = twf.TextField(validator=Pipe(NotEmpty))
	publisher = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	amount = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	publishDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	refuelDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	fondId = twf.SingleSelectField(options=Fond.getAllIds(),
								   validator=Pipe(NotEmpty, Number,
												  ExistByPrimaryKey(Fond)))
	stuffId = twf.SingleSelectField(options=Stuff.getAllIds(),
									validator=Pipe(NotEmpty, Number,
												   ExistByPrimaryKey(Stuff)))
	litType = twf.SingleSelectField(options=LiteratyreType.getAllIds(),
									validator=Pipe(NotEmpty, ExistByPrimaryKey(
										LiteratyreType)))


class EditFields(twf.TableLayout):
	refuelId = twf.HiddenField(validator=Pipe(NotEmpty, Number))
	source = twf.TextField(validator=Pipe(NotEmpty))
	publisher = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	amount = twf.TextField(validator=Pipe(NotEmpty, Number), value=0)
	publishDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	refuelDate = twf.CalendarDatePicker(
		validator=Pipe(NotEmpty, DateConverter(month_style="dmy")))
	fondId = twf.SingleSelectField(options=Fond.getAllIds(),
								   validator=Pipe(NotEmpty, Number,
												  ExistByPrimaryKey(Fond)))
	stuffId = twf.SingleSelectField(options=Stuff.getAllIds(),
									validator=Pipe(NotEmpty, Number,
												   ExistByPrimaryKey(Stuff)))
	litType = twf.SingleSelectField(options=LiteratyreType.getAllIds(),
									validator=Pipe(NotEmpty, ExistByPrimaryKey(
										LiteratyreType)))


class FondRefuelCreateForm(twf.Form):
	child = CreateFields()
	action = "create"


class FondRefuelEditForm(twf.Form):
	child = EditFields()
	action = "edit"
