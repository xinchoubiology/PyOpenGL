'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_texture_scale_bias'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_texture_scale_bias')
GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX=_C('GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX',0x817B)
GL_POST_TEXTURE_FILTER_BIAS_SGIX=_C('GL_POST_TEXTURE_FILTER_BIAS_SGIX',0x8179)
GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX=_C('GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX',0x817C)
GL_POST_TEXTURE_FILTER_SCALE_SGIX=_C('GL_POST_TEXTURE_FILTER_SCALE_SGIX',0x817A)

