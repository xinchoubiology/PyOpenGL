'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIS_point_line_texgen'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_point_line_texgen')
GL_EYE_DISTANCE_TO_LINE_SGIS=_C('GL_EYE_DISTANCE_TO_LINE_SGIS',0x81F2)
GL_EYE_DISTANCE_TO_POINT_SGIS=_C('GL_EYE_DISTANCE_TO_POINT_SGIS',0x81F0)
GL_EYE_LINE_SGIS=_C('GL_EYE_LINE_SGIS',0x81F6)
GL_EYE_POINT_SGIS=_C('GL_EYE_POINT_SGIS',0x81F4)
GL_OBJECT_DISTANCE_TO_LINE_SGIS=_C('GL_OBJECT_DISTANCE_TO_LINE_SGIS',0x81F3)
GL_OBJECT_DISTANCE_TO_POINT_SGIS=_C('GL_OBJECT_DISTANCE_TO_POINT_SGIS',0x81F1)
GL_OBJECT_LINE_SGIS=_C('GL_OBJECT_LINE_SGIS',0x81F7)
GL_OBJECT_POINT_SGIS=_C('GL_OBJECT_POINT_SGIS',0x81F5)

