import configparser
import pathlib

_CONFIG_FILE = pathlib.Path(__file__).parent.parent / "setup.cfg"


def _get_config():
    config = configparser.ConfigParser()
    config.read(_CONFIG_FILE)
    return config


_config = _get_config()

__version__ = _config["metadata"]["version"]
__author__ = _config["metadata"]["author"]
__author_email__ = _config["metadata"]["author_email"]
__license__ = _config["metadata"]["license"]


from arithmetic_eval.utils import evaluate
from arithmetic_eval.exceptions import MaliciousInputError

__all__ = [
    "__version__",
    "__author__",
    "__author_email__",
    "__license__",
    "evaluate",
    "MaliciousInputError",
]
