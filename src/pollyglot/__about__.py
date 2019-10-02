import os.path

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__commit__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "pollyglot"
__summary__ = "Small example datasets of annotated vocalizations"
__uri__ = "https://github.com/NickleDave/pollyglot"

__version__ = "0.1.1"

if base_dir is not None and os.path.exists(os.path.join(base_dir, ".commit")):
    with open(os.path.join(base_dir, ".commit")) as fp:
        __commit__ = fp.read().strip()
else:
    __commit__ = None

__author__ = "David Nicholson"
__email__ = "nicholdav@gmail.com"

__license__ = "BSD"
__copyright__ = "2019 %s" % __author__
