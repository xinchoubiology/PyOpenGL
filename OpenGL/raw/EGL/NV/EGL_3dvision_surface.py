'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_NV_EGL_3dvision_surface'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_NV_EGL_3dvision_surface')
EGL_AUTO_STEREO_NV=_C('EGL_AUTO_STEREO_NV',0x3136)

