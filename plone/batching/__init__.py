# -*- coding: utf-8 -*-
from AccessControl import allow_class
from AccessControl import allow_module
from plone.batching.batch import Batch

allow_module('plone.batching')
allow_class(Batch)
