# Python import system

Offical documentation: https://docs.python.org/3/reference/import.html#packages
- `import` vs `importlib.import_module()` vs `__import__()`
- We can think of modules and packages in Python as of files in directories in the file system (for simplicity).
- Every package is a module but not every module is a package. Any model with the `__path__` attribute is considered a package.
- Regular packages are typicall implemented as directories containing the `__init__.py` file that's executed implicitly once the package or a module within the package is imported.
- `regular-package-import-init` - PoC showing how the `__init__` files are executed while importing packages.