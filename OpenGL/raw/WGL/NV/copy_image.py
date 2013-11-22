'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_NV_copy_image'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_NV_copy_image')

@_f
@_p.types(_cs.BOOL,_cs.HGLRC,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.HGLRC,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei)
def wglCopyImageSubDataNV(hSrcRC,srcName,srcTarget,srcLevel,srcX,srcY,srcZ,hDstRC,dstName,dstTarget,dstLevel,dstX,dstY,dstZ,width,height,depth):pass
