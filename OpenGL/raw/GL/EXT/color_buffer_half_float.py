'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_color_buffer_half_float'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_color_buffer_half_float')
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT',0x8211)
GL_R16F_EXT=_C('GL_R16F_EXT',0x822D)
GL_RG16F_EXT=_C('GL_RG16F_EXT',0x822F)
GL_RGB16F_EXT=_C('GL_RGB16F_EXT',0x881B)
GL_RGBA16F_EXT=_C('GL_RGBA16F_EXT',0x881A)
GL_UNSIGNED_NORMALIZED_EXT=_C('GL_UNSIGNED_NORMALIZED_EXT',0x8C17)

