import sys
import os
import unittest

from tests.test_meshdata import test

# Add the directory containing your module to the Python path
test_module_path = r'D:\python\blender_shot_system'
if test_module_path not in sys.path:
    sys.path.append(test_module_path)

bzz_module_path = r'D:\python\blender_shot_system\src'
if bzz_module_path not in sys.path:
    sys.path.append(bzz_module_path)


# Now you can import your module
import tests
tests.test()