from AccessControl import allow_class
from AccessControl import ModuleSecurityInfo
from plone.batching.batch import Batch


# Only declare Batch public.  Do not use allow_module here: that would make
# every name in this module available to restricted code, including
# imported names like allow_class.
ModuleSecurityInfo("plone.batching").declarePublic("Batch")
allow_class(Batch)
