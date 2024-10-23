from typing import Any
from dataclasses import dataclass


@dataclass(slots=True)
class BlBaseData:
	"""
	Base abastraction for any Blender data container (Modiferes and nodes)
	"""

	def set_attr(self, attrib_name: str, value: Any):
		_attrib = getattr(self, attrib_name)
		_value_type = type(value)
		if type(_attrib) != _value_type:
			print(f"The type {_attrib} not matching {_value_type}")
			return

		setattr(self, attrib_name, value)

	def clear_attr(self, attrib_name: str):
		if hasattr(self, attrib_name):
			setattr(self, attrib_name, None)
		else:
			print(f"{attrib_name} does not exist.")


