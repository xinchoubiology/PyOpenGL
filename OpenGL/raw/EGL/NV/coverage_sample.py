'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_NV_coverage_sample'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_NV_coverage_sample')
EGL_COVERAGE_BUFFERS_NV=_C('EGL_COVERAGE_BUFFERS_NV',0x30E0)
EGL_COVERAGE_SAMPLES_NV=_C('EGL_COVERAGE_SAMPLES_NV',0x30E1)

