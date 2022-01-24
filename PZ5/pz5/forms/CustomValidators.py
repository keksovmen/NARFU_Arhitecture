import formencode
import tw2.core as twc
from formencode import validators

__all__ = ["NotExistance", "ExistByPrimaryKey"]


class NotExistance(validators.FancyValidator):
	messages = {
		"already_exists": "Such type already exists"
	}

	def __init__(self, modelType, *args):
		self.modelType = modelType
		self.fields = args

	def _validate_python(self, value, state=None):
		print('value =', value)
		if twc.Invalid in value.values():
			return value
		cryteria = dict([(i, value[i]) for i in self.fields])
		print(cryteria)
		if self.modelType.checkIsExists(**cryteria):
			raise formencode.Invalid(
				self.message("already_exists", state),
				value, state)
		return value


class ExistByPrimaryKey(validators.FancyValidator):
	messages = {
		"not_exists": "Object with given key not exists"
	}

	def __init__(self, modelType):
		self.modelType = modelType

	def _validate_python(self, value, state=None):
		print('value =', value)
		if not self.modelType.getById(value):
			raise formencode.Invalid(
				self.message("not_exists", state),
				value, state)
		return value
