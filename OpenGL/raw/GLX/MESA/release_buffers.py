'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_MESA_release_buffers'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_MESA_release_buffers')

@_f
@_p.types(_cs.Bool,ctypes.POINTER(_cs.Display),_cs.GLXDrawable)
def glXReleaseBuffersMESA(dpy,drawable):pass
