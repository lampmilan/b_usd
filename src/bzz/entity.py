from dataclasses import dataclass, field
import bpy
from .data_utils import createn_new_abs_rep
from .modifiers import Modifier
from .bl_contexts import Modifiers

@dataclass
class Mesh:
	points: list[list[float]] = field(default_factory=list)
	normals: list[list[float]] = field(default_factory=list)

class Entity:
	@staticmethod
	def _extract_modifiers(object) -> list[Modifier]:
		mods: list[Modifier] = []
		if len(object.modifiers) == 0:
			return mods

		for modifier in object.modifiers:
			abs_mod = createn_new_abs_rep(modifier, Modifiers())
			mods.append(abs_mod)
		return mods


	@staticmethod
	def _extract_mesh_information(object, mesh_container: Mesh):
		point_pos = [(object.matrix_world @ v.co) for v in object.data.vertices]
		[mesh_container.points.append(list(point)) for point in point_pos] # Convert mathutils.Vector to a list and add the result to the Mesh dataclass

		return mesh_container


	def __init__(self, object: bpy.data):
		self.mesh_info: Mesh = Mesh()
		Entity._extract_mesh_information(object , self.mesh_info)

		self.modifiers: list[Modifier] = Entity._extract_modifiers(object)
		# There shoud be a self.modifiers and self.mesh
		# No need to set modifiers here since it's already set in __new__
		print(self.mesh_info)



