'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ATI_meminfo'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ATI_meminfo')
GL_RENDERBUFFER_FREE_MEMORY_ATI=_C('GL_RENDERBUFFER_FREE_MEMORY_ATI',0x87FD)
GL_TEXTURE_FREE_MEMORY_ATI=_C('GL_TEXTURE_FREE_MEMORY_ATI',0x87FC)
GL_VBO_FREE_MEMORY_ATI=_C('GL_VBO_FREE_MEMORY_ATI',0x87FB)

