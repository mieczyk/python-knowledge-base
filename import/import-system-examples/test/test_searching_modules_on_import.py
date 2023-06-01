import sys
import importlib

def test_imported_module_goes_to_sys_modules_cache():
    # The module hasn't been imported, yet.
    assert not "test.my_package.my_module" in sys.modules

    # Import the module
    my_module = importlib.import_module(".my_module", "test.my_package")

    # Check if the "my_package" has been loaded.
    print(sys.modules)
    assert "test.my_package.my_module" in sys.modules

def test_sys_modules_dict_contains_intermediate_paths():
    FULL_MODULE_PATH = "test.my_package.my_package_A.my_module_A"

    my_module_A = importlib.import_module(".my_module_A", "test.my_package.my_package_A")

    assert "test" in sys.modules
    assert "test.my_package" in sys.modules
    assert "test.my_package.my_package_A" in sys.modules
    assert "test.my_package.my_package_A.my_module_A" in sys.modules