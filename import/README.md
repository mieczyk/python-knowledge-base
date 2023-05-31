# Python import system
- Offical documentation: https://docs.python.org/3/reference/import.html#packages
- `import` vs `importlib.import_module()` vs `__import__()`
- We can think of modules and packages in Python as of files in directories in the file system (for simplicity).
- Every package is a module but not every module is a package. Any model with the `__path__` attribute is considered a package.
- Regular packages are typicall implemented as directories containing the `__init__.py` file that's executed implicitly once the package or a module within the package is imported.
- `regular-package-import-init` - PoC showing how the `__init__` files are executed while importing packages.
- `import-system-examples` - repository with examples showing different aspects of the import system in Python (according to the official documentation). *Code as a Documentation* (CaaD) approach.

## Namespace packages
- Consists of various portions which may reside in different locations of filesystem (might be also in ZIP files or in a network location). Might be also a virtual modules with no concrete implementation.
- *portion* = A set of files in a single directory (possibly stored in a zip file) that contribute to a namespace package, as defined in PEP 420.
- [Packaging namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/).    
    - *Native (PEP420)* - available since Python 3.3. No `__init__.py` file in the namespace directories - they are treated as namespace packages automatically. In order to find packages, the `setuptools.find_namespace_packages()` is required instead of `setuptools.find_packages()`.

## Searching
- `import x.y.z` - Python first tries to import `x`, then `y` and finally `z`. If any of the intermediate imports fail, a `ModuleNotFoundError` is raised.
    - `x.y.z` = fully qualified name.