#!/usr/bin/env python
import sys, os

def options(opt):
    pass

def configure(cfg):
    pass

def build(bld):
    bld(
        target          = 'ZTL',
        export_includes = '.',
    )
