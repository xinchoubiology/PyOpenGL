'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_NV_coverage_sample_resolve'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_NV_coverage_sample_resolve')
EGL_COVERAGE_SAMPLE_RESOLVE_DEFAULT_NV=_C('EGL_COVERAGE_SAMPLE_RESOLVE_DEFAULT_NV',0x3132)
EGL_COVERAGE_SAMPLE_RESOLVE_NONE_NV=_C('EGL_COVERAGE_SAMPLE_RESOLVE_NONE_NV',0x3133)
EGL_COVERAGE_SAMPLE_RESOLVE_NV=_C('EGL_COVERAGE_SAMPLE_RESOLVE_NV',0x3131)

