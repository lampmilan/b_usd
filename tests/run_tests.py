import sys
import os
import unittest

# Add the directory containing your module to the Python path
test_module_path = r'D:\python\blender_shot_system'
if test_module_path not in sys.path:
    sys.path.append(test_module_path)

bzz_module_path = r'D:\python\blender_shot_system\src'
if bzz_module_path not in sys.path:
    sys.path.append(bzz_module_path)


# Now you can import your module
import tests

if __name__ == "__main__":
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(tests)

    # Create a test runner and run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)