'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_index_array_formats'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_index_array_formats')
GL_IUI_N3F_V2F_EXT=_C('GL_IUI_N3F_V2F_EXT',0x81AF)
GL_IUI_N3F_V3F_EXT=_C('GL_IUI_N3F_V3F_EXT',0x81B0)
GL_IUI_V2F_EXT=_C('GL_IUI_V2F_EXT',0x81AD)
GL_IUI_V3F_EXT=_C('GL_IUI_V3F_EXT',0x81AE)
GL_T2F_IUI_N3F_V2F_EXT=_C('GL_T2F_IUI_N3F_V2F_EXT',0x81B3)
GL_T2F_IUI_N3F_V3F_EXT=_C('GL_T2F_IUI_N3F_V3F_EXT',0x81B4)
GL_T2F_IUI_V2F_EXT=_C('GL_T2F_IUI_V2F_EXT',0x81B1)
GL_T2F_IUI_V3F_EXT=_C('GL_T2F_IUI_V3F_EXT',0x81B2)

