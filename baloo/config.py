import os
import platform

import tabulate

def library_ext():
    """Returns the platform-dependent extension for dynamic libraries. """
    system = platform.system()
    if system == 'Linux':
        ext = "so"
    elif system == 'Darwin':
        ext = "dylib"
    else:
        raise OSError("Unsupported platform {}", system)
    return ext

# While not explicit, the code here gets executed on baloo import because of pyweld and convertors importing from here
tabulate.PRESERVE_WHITESPACE = True

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LIBS_DIR = ROOT_DIR + '/weld/libs'
WELD_PATH = os.path.join(LIBS_DIR, 'libweld.' + library_ext())
ENCODERS_PATH = os.path.join(LIBS_DIR, 'numpy_weld_convertor.' + library_ext())
