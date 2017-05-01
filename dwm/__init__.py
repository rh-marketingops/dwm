""" dwm (Data Washing Machine) is a collection of functions that carry out Red Hat's Marketing Operations
    best practices for maintaining data in a marketing contact database. """

from .dwm import dwmAll, _CollectHistory_, _CollectHistoryAgg_

from .dwmmain import Dwm

__version__ = '0.0.8'
