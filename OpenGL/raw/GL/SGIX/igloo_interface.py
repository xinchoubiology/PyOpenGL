'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_igloo_interface'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_igloo_interface')

@_f
@_p.types(None,_cs.GLenum,ctypes.c_void_p)
def glIglooInterfaceSGIX(pname,params):pass
# Calculate length of params from pname:IglooFunctionSelectSGIX
