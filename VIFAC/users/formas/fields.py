# -*- coding: utf-8 -*-
from django.forms import ModelChoiceField as BaseChoiceField
from django.utils.encoding import smart_text
from django.db.models import Model
from typing import Callable

__all__ = ['ModelChoiceField']


class ModelChoiceField(BaseChoiceField):
	def __init__(self, *args, label_fn: Callable[[Model], str] = smart_text, **kwargs):
		self._label_fn = label_fn or smart_text
		super().__init__(*args, **kwargs)
	
	def label_from_instance(self, obj: Model) -> str:
		label_fn = self._label_fn
		return label_fn(obj)

