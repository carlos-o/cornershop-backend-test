from cerberus import Validator
from datetime import datetime
from django.utils.translation import gettext as _
import json
import logging

# Standard instance of a logger with __name__
logger = logging.getLogger(__name__)


def validate_option(option: dict) -> bool:
	"""
		validate option data

		:param option: option data
		:type option: dict
		:return: True
		:raise: ValueError
	"""
	v = Validator()
	schema = {'description': {'type': 'string', 'required': True, 'empty': False, 'minlength': 10, 'maxlength': 255}}
	if not v.validate(option, schema):
		raise ValueError(json.dumps(v.errors))
	return True


class ValidatorMenu(Validator):
	"""
		Validate class to register a menu.
	"""

	schema = {
		'name': {'type': 'string', 'required': True, 'empty': False, 'minlength': 5, 'maxlength': 100},
		'description': {'type': 'string', 'required': False, 'empty': False, 'nullable': True, 'maxlength': 255},
		'start_date': {'type': 'string', 'required': True, 'empty': False, 'time': True}
	}

	def __init__(self, data, *args, **kwargs):
		"""
			initialize cerberus with the user information to register in weedmatch.

			:param data: user information.
			:type data: dict.
		"""
		super(ValidatorMenu, self).__init__(*args, **kwargs)
		self.data = data
		self.schema = self.__class__.schema

	def validation(self):
		"""
			:return: none if data is correct
		"""
		return self.validate(self.data, self.schema)

	def _validate_time(self, time, field, value):
		""" Validate date field

		The rule's arguments are validated against this schema:
		{'type': 'boolean'}
		"""
		if time and value:
			try:
				datetime.strptime(value, '%Y-%m-%d')
			except ValueError as e:
				self._error(field, str(_("Is not a valid date")))

	def change_value(self, data: list) -> list:
		"""
			this method covers all cerberus error messages from English to Spanish,
			depends on the Accept-Language header.

			:param data: error messages of cerberus.
			:return: list with error messages.
		"""
		for i in range(0, len(data)):
			if data[i][0:15] == "unallowed value":
				convert = str(data[i])
				data[i] = str(_(convert[0:15])) + convert[15:]
			elif data[i][:26] == "value does not match regex":
				convert = str(data[i])
				data[i] = str(_(data[i][:26]))
			else:
				convert = str(data[i])
				data[i] = str(_(convert))
		return data

	def mistakes(self):
		"""
			This method returns the error when, the information sent by the user does not comply
			with the rules in the validation with cerberus

			:return: error of cerberus
		"""
		return self.errors
