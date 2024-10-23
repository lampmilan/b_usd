from .bl_data import BlBaseData
from .modifiers import Modifier
from bzz import modifiers
from abc import ABC, abstractmethod


class ContainerFactory(ABC):
	def __init__(self, type: str) -> None:
		self.type = type

	@abstractmethod
	def get_bl_modifier(self, modifier: str) -> BlBaseData:
		pass



class Modifiers(ContainerFactory):
	def __init__(self) -> None:
		type = "Modifier"
		super().__init__(type)


	def get_bl_modifier(self, modifier: str) -> BlBaseData :
		modifier.upper()

		available_modifiers = {
		"DATA_TRANSFER": modifiers.DataTransfer,
		"SMOOTH": modifiers.Smooth,
		"SKIN": modifiers.Skin,
		"UV_WARP": modifiers.UvWarp,
		"NORMAL_EDIT": modifiers.NormalEdit,
		"MESH_SEQUENCE_CACHE": modifiers.MeshSequenceCache,
		"WEIGHTED_NORMAL": modifiers.WeightedNormal
		}

		return available_modifiers[modifier]()