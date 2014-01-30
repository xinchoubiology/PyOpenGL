'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_shader_storage_buffer_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_shader_storage_buffer_object')
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS=_C('GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS',0x8F39)
GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES=_C('GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES',0x8F39)
GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS=_C('GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS',0x90DC)
GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS=_C('GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS',0x90DB)
GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS=_C('GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS',0x90DA)
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS=_C('GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS',0x90D7)
GL_MAX_SHADER_STORAGE_BLOCK_SIZE=_C('GL_MAX_SHADER_STORAGE_BLOCK_SIZE',0x90DE)
GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS=_C('GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS',0x90DD)
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS=_C('GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS',0x90D8)
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS=_C('GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS',0x90D9)
GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS=_C('GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS',0x90D6)
GL_SHADER_STORAGE_BARRIER_BIT=_C('GL_SHADER_STORAGE_BARRIER_BIT',0x00002000)
GL_SHADER_STORAGE_BUFFER=_C('GL_SHADER_STORAGE_BUFFER',0x90D2)
GL_SHADER_STORAGE_BUFFER_BINDING=_C('GL_SHADER_STORAGE_BUFFER_BINDING',0x90D3)
GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT=_C('GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT',0x90DF)
GL_SHADER_STORAGE_BUFFER_SIZE=_C('GL_SHADER_STORAGE_BUFFER_SIZE',0x90D5)
GL_SHADER_STORAGE_BUFFER_START=_C('GL_SHADER_STORAGE_BUFFER_START',0x90D4)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glShaderStorageBlockBinding(program,storageBlockIndex,storageBlockBinding):pass
