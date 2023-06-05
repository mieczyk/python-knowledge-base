import sys
import importlib
from pathlib import Path

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

    # The sys.module dict contains all intermediate paths.
    assert "test" in sys.modules
    assert "test.my_package" in sys.modules
    assert "test.my_package.my_package_A" in sys.modules
    assert "test.my_package.my_package_A.my_module_A" in sys.modules

def test_invalidate_cache():
    MY_MODULE_PATH = "test.my_package.my_module"

    # Load the module
    my_module = importlib.import_module(MY_MODULE_PATH)

    # Invalidate the cache, but the module itself is not destroyed, as
    # we still keep the reference to it (my_module variable).
    del sys.modules[MY_MODULE_PATH]

    # Newly imported module is a totally different object.
    my_new_module = importlib.import_module(MY_MODULE_PATH)

    assert id(my_module) != id(my_new_module)

def test_reload_the_same_module_object_with_importlib_reload():
    MY_MODULE_PATH = "test.my_package.my_module"

    # Load the module
    my_module = importlib.import_module(MY_MODULE_PATH)

    # Reload the module. It's useful when we've edited a module's source file
    # and we want to apply the changes without leaving the Python interpreter.
    # However, once I tried to invalidate the sys.modules caches first, I got
    # the ImportError exception saying that the module is not present in sys.modules.
    my_new_module = importlib.reload(my_module)

    # It's not always the case!
    assert id(my_module) == id(my_new_module)
    
def test_script_directory_path_inserted_into_sys_path():
    # The pathlib module is a recommended way of dealing with file system paths since Python 3.4
    test_file_path = Path(__file__).absolute()
    main_script_dir_path = test_file_path.parent.parent
    
    assert str(main_script_dir_path) in sys.path