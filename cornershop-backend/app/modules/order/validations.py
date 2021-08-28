from cerberus import Validator
import json


def validate_order(data: dict) -> bool:
	"""
		validate order data

		:param data: order information
		:type data: dict
		:return: True
		:raise: ValueError
	"""
	v = Validator()
	schema = {
		'optionId': {'type': 'integer', 'required': True, 'empty': False},
		'customization': {'type': 'string', 'required': False, 'empty': False, 'nullable': True, 'maxlength': 255}
	}
	if not v.validate(data, schema):
		raise ValueError(json.dumps(v.errors))
	return True
