# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-24 14:41:30 UTC+08:00
"""

from fairylandfuture.interface.toolkits.validation import AbstractValidator
from fairylandfuture.exceptions.general import ValidationError


class Validator(AbstractValidator):

    def __init__(self, required, typedef, validator_factory=None):
        self.required = required
        self.typedef = typedef
        self.validator_factory = validator_factory

    def validate(self, value):
        if self.required and value is None:
            raise ValidationError("Required parameter is missing.")

        if value is not None and not isinstance(value, self.typedef):
            raise ValidationError(f"Parameter type error. Expected type: {self.typedef}")

        if self.validator_factory is not None and not self.validator_factory(value):
            raise ValidationError("Parameter validation failed.")

        return value


class RequestValidator:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, request_data):
        validated_data = dict()
        for key, validator in self.schema.items():
            validated_data.update({key: validator.validate(request_data.get(key))})

        return validated_data
