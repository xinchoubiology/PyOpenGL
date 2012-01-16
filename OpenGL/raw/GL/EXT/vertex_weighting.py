'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_vertex_weighting'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_vertex_weighting',False)
_p.unpack_constants( """GL_MODELVIEW1_STACK_DEPTH_EXT 0x8502
GL_MODELVIEW1_MATRIX_EXT 0x8506
GL_VERTEX_WEIGHTING_EXT 0x8509
GL_MODELVIEW1_EXT 0x850A
GL_CURRENT_VERTEX_WEIGHT_EXT 0x850B
GL_VERTEX_WEIGHT_ARRAY_EXT 0x850C
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT 0x850D
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT 0x850E
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT 0x850F
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT 0x8510""", globals())
glget.addGLGetConstant( GL_MODELVIEW1_STACK_DEPTH_EXT, (1,) )
glget.addGLGetConstant( GL_MODELVIEW1_MATRIX_EXT, (4,4) )
glget.addGLGetConstant( GL_CURRENT_VERTEX_WEIGHT_EXT, (1,) )
glget.addGLGetConstant( GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT, (1,) )
glget.addGLGetConstant( GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT, (1,) )
glget.addGLGetConstant( GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT, (1,) )
@_f
@_p.types(None,_cs.GLfloat)
def glVertexWeightfEXT( weight ):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glVertexWeightfvEXT( weight ):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexWeightPointerEXT( size,type,stride,pointer ):pass


def glInitVertexWeightingEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
