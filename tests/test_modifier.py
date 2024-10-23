import sys
import unittest
import bpy
from bzz import BlDataManager, Modifiers, createn_new_abs_rep
from bzz import BlBaseData

"""
def add_skin():
    object_name = "Cube"
    if object_name in bpy.data.objects:
        cube = bpy.data.objects[object_name]
        bpy.context.view_layer.objects.active = cube
        cube.select_set(True)
        skin_modifier = cube.modifiers.new(name="Skin", type='NODES')

        for prop in dir(skin_modifier):
            value = getattr(skin_modifier, prop)
            print(f"{prop}: {type(value).__name__} = {value}")



        smooth_modifier = cube.modifiers.new(name="test", type='NORMAL_EDIT')
        index = list(cube.modifiers).index(smooth_modifier)

        abs_smooth_mod = BlDataManager.get_abstract_modifier(smooth_modifier, DataContext().modifiers_context, index)
        print(abs_smooth_mod)

        BlDataManager.pack_modifier(abs_smooth_mod)
        #ModifierManager.pack_modifier(abs_skin_mod)

        print(abs_smooth_mod)
        #print(abs_skin_mod)


        #D:\\python\blender_shot_system> blender --background --python tests\run_tests.py
"""

class TestModifiers(unittest.TestCase):

    @staticmethod
    def create_modifier(type: str):
        object_name = "Cube"
        if object_name in bpy.data.objects:
            cube = bpy.data.objects[object_name]
            bpy.context.view_layer.objects.active = cube
            cube.select_set(True)

            skin_modifier = cube.modifiers.new(name=f"{type}_name", type=type)

            return skin_modifier

    def test_modifier_packing_set_to_none(self):
        """
        Test if the dataclass item is set to None when the field is equal to the default parm value
        """
        modifier = TestModifiers.create_modifier("NORMAL_EDIT")
        abs_modifier = createn_new_abs_rep(modifier, Modifiers())

        self.assertEqual(abs_modifier.mix_mode, None) # When the parm is default, the dataclass value shoud be "None"
        print(f"{abs_modifier}\n")



    def test_second_mod_with_same_type(self):
        """
        Test if a new object created if there's already one with the same type
        """
        modifier = TestModifiers.create_modifier("NORMAL_EDIT")
        abs_modifier = createn_new_abs_rep(modifier, Modifiers())

        self.assertEqual(abs_modifier.mix_mode, None) # When the parm is default, the dataclass value shoud be "None"
        print(f"{abs_modifier}\n")



    def test_modifier_packing_float(self):
        """
        Test case for float values.
        Most default floats is not a whole value (ea. thresh: float = 0.009999999776482582).
        Need to test if this value is always the same
        """
        modifier = TestModifiers.create_modifier("WEIGHTED_NORMAL")
        abs_modifier = createn_new_abs_rep(modifier, Modifiers())

        self.assertEqual(abs_modifier.thresh, None) # When the parm is default, the dataclass value shoud be "None"
        print(f"{abs_modifier}\n")


    def test_modifier_value_change(self):
        """
        Test if the non default parm is not set to None
        """
        modifier2 = TestModifiers.create_modifier("SKIN")
        modifier2.branch_smoothing = 0.25
        print(modifier2.branch_smoothing)

        abs_modifier = createn_new_abs_rep(modifier2, Modifiers())

        self.assertEqual(abs_modifier.branch_smoothing, 0.25)
        print(f"{abs_modifier}\n")
