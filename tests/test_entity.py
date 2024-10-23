import sys
import unittest
import bpy
from bzz import Entity, entity
from bzz.modifiers import Skin

class TestEntity(unittest.TestCase):

	@staticmethod
	def create_modifier():
		object_name = "Cube"
		bl_object = bpy.data.objects[object_name]
		#bl_object.modifiers.new(name="mode", type='SKIN')

		return bl_object

	def test_entity_creation(self):
		"""
		Test if an empty modifiers reutrn []
		"""
		bl_object = TestEntity.create_modifier()
		my_entity = Entity(bl_object)
		print(my_entity.modifiers)
		self.assertEqual(my_entity.modifiers, [])

	def test_non_empty_creation(self):
		"""
		If the first modifers in thr stack is a Skin type, the Entity holds it properly as a Skin
		"""
		bl_object = TestEntity.create_modifier()
		bl_object.modifiers.new(name="mode", type='SKIN')
		my_entity = Entity(bl_object)
		print(my_entity.modifiers)
		self.assertEqual(type(my_entity.modifiers[0]), Skin)