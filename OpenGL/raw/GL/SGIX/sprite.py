'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_sprite'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_sprite')
GL_SPRITE_AXIAL_SGIX=_C('GL_SPRITE_AXIAL_SGIX',0x814C)
GL_SPRITE_AXIS_SGIX=_C('GL_SPRITE_AXIS_SGIX',0x814A)
GL_SPRITE_EYE_ALIGNED_SGIX=_C('GL_SPRITE_EYE_ALIGNED_SGIX',0x814E)
GL_SPRITE_MODE_SGIX=_C('GL_SPRITE_MODE_SGIX',0x8149)
GL_SPRITE_OBJECT_ALIGNED_SGIX=_C('GL_SPRITE_OBJECT_ALIGNED_SGIX',0x814D)
GL_SPRITE_SGIX=_C('GL_SPRITE_SGIX',0x8148)
GL_SPRITE_TRANSLATION_SGIX=_C('GL_SPRITE_TRANSLATION_SGIX',0x814B)
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glSpriteParameterfSGIX(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glSpriteParameterfvSGIX(pname,params):pass
# Calculate length of params from pname:SpriteParameterNameSGIX
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glSpriteParameteriSGIX(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glSpriteParameterivSGIX(pname,params):pass
# Calculate length of params from pname:SpriteParameterNameSGIX
