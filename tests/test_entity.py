import sys
import unittest
import bpy
from bzz import Entity, entity
from bzz.modifiers import Skin
from bzz import create_usd

class TestEntity(unittest.TestCase):

    @staticmethod
    def grab_default_cube():
        object_name = "Cube"
        bl_object = bpy.data.objects[object_name]
        #

        return bl_object

    def test_entity_creation(self):
        """
        Test if an empty modifiers reutrn []
        """
        bl_object = TestEntity.grab_default_cube()
        my_entity = Entity(bl_object)

        self.assertEqual(my_entity.modifiers, [])

    def test_non_empty_creation(self):
        """
        If the first modifers in thr stack is a Skin type, the Entity holds it properly as a Skin
        """
        bl_object = TestEntity.grab_default_cube()
        bl_object.modifiers.new(name="mode", type='SKIN')
        my_entity = Entity(bl_object)

        self.assertEqual(type(my_entity.modifiers[0]), Skin)


    def test_usd_call(self):
        """
        Test USD exporter
        """
        bl_object = TestEntity.grab_default_cube()
        skin_mod = bl_object.modifiers.new(name="mode", type='SKIN')
        skin_mod.branch_smoothing = 0.25
        my_entity = Entity(bl_object)

        create_usd(my_entity)

        self.assertIsNotNone(my_entity)