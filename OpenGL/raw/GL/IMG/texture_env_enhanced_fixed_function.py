'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_IMG_texture_env_enhanced_fixed_function'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_IMG_texture_env_enhanced_fixed_function')
GL_ADD_BLEND_IMG=_C('GL_ADD_BLEND_IMG',0x8C09)
GL_DOT3_RGBA_IMG=_C('GL_DOT3_RGBA_IMG',0x86AF)
GL_FACTOR_ALPHA_MODULATE_IMG=_C('GL_FACTOR_ALPHA_MODULATE_IMG',0x8C07)
GL_FRAGMENT_ALPHA_MODULATE_IMG=_C('GL_FRAGMENT_ALPHA_MODULATE_IMG',0x8C08)
GL_MODULATE_COLOR_IMG=_C('GL_MODULATE_COLOR_IMG',0x8C04)
GL_RECIP_ADD_SIGNED_ALPHA_IMG=_C('GL_RECIP_ADD_SIGNED_ALPHA_IMG',0x8C05)
GL_TEXTURE_ALPHA_MODULATE_IMG=_C('GL_TEXTURE_ALPHA_MODULATE_IMG',0x8C06)

