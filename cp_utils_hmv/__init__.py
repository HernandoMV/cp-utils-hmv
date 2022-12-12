from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("cp-utils-hmv")
except PackageNotFoundError:
    # package is not installed
    pass
