from .itertoolz import *

from .functoolz import *

from .dicttoolz import *

from .recipes import *

from functools import partial, reduce

sorted = sorted
map = map
filter = filter

# Aliases
comp = compose

# Always-curried functions
flip = functoolz.flip = curry(functoolz.flip)
memoize = functoolz.memoize = curry(functoolz.memoize)

from . import curried  # sandbox

functoolz._sigs.update_signature_registry()

from ._version import __version__, __toolz_version__
