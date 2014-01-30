'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_OES_matrix_palette'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_matrix_palette')
GL_CURRENT_PALETTE_MATRIX_OES=_C('GL_CURRENT_PALETTE_MATRIX_OES',0x8843)
GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES=_C('GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES',0x8B9E)
GL_MATRIX_INDEX_ARRAY_OES=_C('GL_MATRIX_INDEX_ARRAY_OES',0x8844)
GL_MATRIX_INDEX_ARRAY_POINTER_OES=_C('GL_MATRIX_INDEX_ARRAY_POINTER_OES',0x8849)
GL_MATRIX_INDEX_ARRAY_SIZE_OES=_C('GL_MATRIX_INDEX_ARRAY_SIZE_OES',0x8846)
GL_MATRIX_INDEX_ARRAY_STRIDE_OES=_C('GL_MATRIX_INDEX_ARRAY_STRIDE_OES',0x8848)
GL_MATRIX_INDEX_ARRAY_TYPE_OES=_C('GL_MATRIX_INDEX_ARRAY_TYPE_OES',0x8847)
GL_MATRIX_PALETTE_OES=_C('GL_MATRIX_PALETTE_OES',0x8840)
GL_MAX_PALETTE_MATRICES_OES=_C('GL_MAX_PALETTE_MATRICES_OES',0x8842)
GL_MAX_VERTEX_UNITS_OES=_C('GL_MAX_VERTEX_UNITS_OES',0x86A4)
GL_WEIGHT_ARRAY_BUFFER_BINDING_OES=_C('GL_WEIGHT_ARRAY_BUFFER_BINDING_OES',0x889E)
GL_WEIGHT_ARRAY_OES=_C('GL_WEIGHT_ARRAY_OES',0x86AD)
GL_WEIGHT_ARRAY_POINTER_OES=_C('GL_WEIGHT_ARRAY_POINTER_OES',0x86AC)
GL_WEIGHT_ARRAY_SIZE_OES=_C('GL_WEIGHT_ARRAY_SIZE_OES',0x86AB)
GL_WEIGHT_ARRAY_STRIDE_OES=_C('GL_WEIGHT_ARRAY_STRIDE_OES',0x86AA)
GL_WEIGHT_ARRAY_TYPE_OES=_C('GL_WEIGHT_ARRAY_TYPE_OES',0x86A9)
@_f
@_p.types(None,_cs.GLuint)
def glCurrentPaletteMatrixOES(matrixpaletteindex):pass
@_f
@_p.types(None,)
def glLoadPaletteFromModelViewMatrixOES():pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glMatrixIndexPointerOES(size,type,stride,pointer):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glWeightPointerOES(size,type,stride,pointer):pass
