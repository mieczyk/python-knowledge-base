# I had to set the proper Python3 inerpreter in Visual Studio Code to supress the warnings.
# The parent mypackage's init file was executed only once.
from mypackage.subpackagea import settings as asettings
from mypackage.subpackageb import settings as bsettings

print(f"A = {asettings.PACKAGE_NAME}")
print(f"B = {bsettings.PACKAGE_NAME}")