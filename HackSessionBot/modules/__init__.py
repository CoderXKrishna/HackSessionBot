import glob
from os.path import basename, dirname, isfile, splitext

def list_all_modules():
    mod_paths = glob.glob(f"{dirname(__file__)}/*.py")

    all_modules = [
        splitext(basename(f))[0]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and f != f"{dirname(__file__)}/__init__.py"
    ]

    return sorted(all_modules)

ALL_MODULES = list_all_modules()
__all__ = ALL_MODULES + ["list_all_modules", "ALL_MODULES"]
