'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_geometry_program4'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_geometry_program4')
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT',0x8DA7)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT',0x8CD4)
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT',0x8DA9)
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT',0x8DA8)
GL_GEOMETRY_INPUT_TYPE_EXT=_C('GL_GEOMETRY_INPUT_TYPE_EXT',0x8DDB)
GL_GEOMETRY_OUTPUT_TYPE_EXT=_C('GL_GEOMETRY_OUTPUT_TYPE_EXT',0x8DDC)
GL_GEOMETRY_PROGRAM_NV=_C('GL_GEOMETRY_PROGRAM_NV',0x8C26)
GL_GEOMETRY_VERTICES_OUT_EXT=_C('GL_GEOMETRY_VERTICES_OUT_EXT',0x8DDA)
GL_LINES_ADJACENCY_EXT=_C('GL_LINES_ADJACENCY_EXT',0x000A)
GL_LINE_STRIP_ADJACENCY_EXT=_C('GL_LINE_STRIP_ADJACENCY_EXT',0x000B)
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT=_C('GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT',0x8C29)
GL_MAX_PROGRAM_OUTPUT_VERTICES_NV=_C('GL_MAX_PROGRAM_OUTPUT_VERTICES_NV',0x8C27)
GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV=_C('GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV',0x8C28)
GL_PROGRAM_POINT_SIZE_EXT=_C('GL_PROGRAM_POINT_SIZE_EXT',0x8642)
GL_TRIANGLES_ADJACENCY_EXT=_C('GL_TRIANGLES_ADJACENCY_EXT',0x000C)
GL_TRIANGLE_STRIP_ADJACENCY_EXT=_C('GL_TRIANGLE_STRIP_ADJACENCY_EXT',0x000D)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTextureEXT(target,attachment,texture,level):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLenum)
def glFramebufferTextureFaceEXT(target,attachment,texture,level,face):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTextureLayerEXT(target,attachment,texture,level,layer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glProgramVertexLimitNV(target,limit):pass
