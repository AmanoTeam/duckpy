# Just used for backwards compatibility.
from warnings import warn
from .. import AsyncClient as Client


warn("The duckpy.aio module has been deprecated in version 3.0.0 and will be removed in a future release. Please use duckpy.AsyncClient instead.", DeprecationWarning, 2)
