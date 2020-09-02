"""Separating local and production settings."""
from .prod_conf import ProdConf

try:
    from .local_conf import LocalConf
except ImportError:
    pass
