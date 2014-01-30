'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES3 import _types as _cs
# End users want this...
from OpenGL.raw.GLES3._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES3_VERSION_GLES3_3_0'
def _f( function ):
    return _p.createFunction( function,_p.GLES3,'GLES3_VERSION_GLES3_3_0')
GL_ACTIVE_UNIFORM_BLOCKS=_C('GL_ACTIVE_UNIFORM_BLOCKS',0x8A36)
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH=_C('GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH',0x8A35)
GL_ALREADY_SIGNALED=_C('GL_ALREADY_SIGNALED',0x911A)
GL_ANY_SAMPLES_PASSED=_C('GL_ANY_SAMPLES_PASSED',0x8C2F)
GL_ANY_SAMPLES_PASSED_CONSERVATIVE=_C('GL_ANY_SAMPLES_PASSED_CONSERVATIVE',0x8D6A)
GL_BLUE=_C('GL_BLUE',0x1905)
GL_BUFFER_ACCESS_FLAGS=_C('GL_BUFFER_ACCESS_FLAGS',0x911F)
GL_BUFFER_MAPPED=_C('GL_BUFFER_MAPPED',0x88BC)
GL_BUFFER_MAP_LENGTH=_C('GL_BUFFER_MAP_LENGTH',0x9120)
GL_BUFFER_MAP_OFFSET=_C('GL_BUFFER_MAP_OFFSET',0x9121)
GL_BUFFER_MAP_POINTER=_C('GL_BUFFER_MAP_POINTER',0x88BD)
GL_COLOR=_C('GL_COLOR',0x1800)
GL_COLOR_ATTACHMENT1=_C('GL_COLOR_ATTACHMENT1',0x8CE1)
GL_COLOR_ATTACHMENT10=_C('GL_COLOR_ATTACHMENT10',0x8CEA)
GL_COLOR_ATTACHMENT11=_C('GL_COLOR_ATTACHMENT11',0x8CEB)
GL_COLOR_ATTACHMENT12=_C('GL_COLOR_ATTACHMENT12',0x8CEC)
GL_COLOR_ATTACHMENT13=_C('GL_COLOR_ATTACHMENT13',0x8CED)
GL_COLOR_ATTACHMENT14=_C('GL_COLOR_ATTACHMENT14',0x8CEE)
GL_COLOR_ATTACHMENT15=_C('GL_COLOR_ATTACHMENT15',0x8CEF)
GL_COLOR_ATTACHMENT2=_C('GL_COLOR_ATTACHMENT2',0x8CE2)
GL_COLOR_ATTACHMENT3=_C('GL_COLOR_ATTACHMENT3',0x8CE3)
GL_COLOR_ATTACHMENT4=_C('GL_COLOR_ATTACHMENT4',0x8CE4)
GL_COLOR_ATTACHMENT5=_C('GL_COLOR_ATTACHMENT5',0x8CE5)
GL_COLOR_ATTACHMENT6=_C('GL_COLOR_ATTACHMENT6',0x8CE6)
GL_COLOR_ATTACHMENT7=_C('GL_COLOR_ATTACHMENT7',0x8CE7)
GL_COLOR_ATTACHMENT8=_C('GL_COLOR_ATTACHMENT8',0x8CE8)
GL_COLOR_ATTACHMENT9=_C('GL_COLOR_ATTACHMENT9',0x8CE9)
GL_COMPARE_REF_TO_TEXTURE=_C('GL_COMPARE_REF_TO_TEXTURE',0x884E)
GL_COMPRESSED_R11_EAC=_C('GL_COMPRESSED_R11_EAC',0x9270)
GL_COMPRESSED_RG11_EAC=_C('GL_COMPRESSED_RG11_EAC',0x9272)
GL_COMPRESSED_RGB8_ETC2=_C('GL_COMPRESSED_RGB8_ETC2',0x9274)
GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2=_C('GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2',0x9276)
GL_COMPRESSED_RGBA8_ETC2_EAC=_C('GL_COMPRESSED_RGBA8_ETC2_EAC',0x9278)
GL_COMPRESSED_SIGNED_R11_EAC=_C('GL_COMPRESSED_SIGNED_R11_EAC',0x9271)
GL_COMPRESSED_SIGNED_RG11_EAC=_C('GL_COMPRESSED_SIGNED_RG11_EAC',0x9273)
GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC=_C('GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC',0x9279)
GL_COMPRESSED_SRGB8_ETC2=_C('GL_COMPRESSED_SRGB8_ETC2',0x9275)
GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2=_C('GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2',0x9277)
GL_CONDITION_SATISFIED=_C('GL_CONDITION_SATISFIED',0x911C)
GL_COPY_READ_BUFFER=_C('GL_COPY_READ_BUFFER',0x8F36)
GL_COPY_READ_BUFFER_BINDING=_C('GL_COPY_READ_BUFFER_BINDING',0x8F36)
GL_COPY_WRITE_BUFFER=_C('GL_COPY_WRITE_BUFFER',0x8F37)
GL_COPY_WRITE_BUFFER_BINDING=_C('GL_COPY_WRITE_BUFFER_BINDING',0x8F37)
GL_CURRENT_QUERY=_C('GL_CURRENT_QUERY',0x8865)
GL_DEPTH=_C('GL_DEPTH',0x1801)
GL_DEPTH24_STENCIL8=_C('GL_DEPTH24_STENCIL8',0x88F0)
GL_DEPTH32F_STENCIL8=_C('GL_DEPTH32F_STENCIL8',0x8CAD)
GL_DEPTH_COMPONENT24=_C('GL_DEPTH_COMPONENT24',0x81A6)
GL_DEPTH_COMPONENT32F=_C('GL_DEPTH_COMPONENT32F',0x8CAC)
GL_DEPTH_STENCIL=_C('GL_DEPTH_STENCIL',0x84F9)
GL_DEPTH_STENCIL_ATTACHMENT=_C('GL_DEPTH_STENCIL_ATTACHMENT',0x821A)
GL_DRAW_BUFFER0=_C('GL_DRAW_BUFFER0',0x8825)
GL_DRAW_BUFFER1=_C('GL_DRAW_BUFFER1',0x8826)
GL_DRAW_BUFFER10=_C('GL_DRAW_BUFFER10',0x882F)
GL_DRAW_BUFFER11=_C('GL_DRAW_BUFFER11',0x8830)
GL_DRAW_BUFFER12=_C('GL_DRAW_BUFFER12',0x8831)
GL_DRAW_BUFFER13=_C('GL_DRAW_BUFFER13',0x8832)
GL_DRAW_BUFFER14=_C('GL_DRAW_BUFFER14',0x8833)
GL_DRAW_BUFFER15=_C('GL_DRAW_BUFFER15',0x8834)
GL_DRAW_BUFFER2=_C('GL_DRAW_BUFFER2',0x8827)
GL_DRAW_BUFFER3=_C('GL_DRAW_BUFFER3',0x8828)
GL_DRAW_BUFFER4=_C('GL_DRAW_BUFFER4',0x8829)
GL_DRAW_BUFFER5=_C('GL_DRAW_BUFFER5',0x882A)
GL_DRAW_BUFFER6=_C('GL_DRAW_BUFFER6',0x882B)
GL_DRAW_BUFFER7=_C('GL_DRAW_BUFFER7',0x882C)
GL_DRAW_BUFFER8=_C('GL_DRAW_BUFFER8',0x882D)
GL_DRAW_BUFFER9=_C('GL_DRAW_BUFFER9',0x882E)
GL_DRAW_FRAMEBUFFER=_C('GL_DRAW_FRAMEBUFFER',0x8CA9)
GL_DRAW_FRAMEBUFFER_BINDING=_C('GL_DRAW_FRAMEBUFFER_BINDING',0x8CA6)
GL_DYNAMIC_COPY=_C('GL_DYNAMIC_COPY',0x88EA)
GL_DYNAMIC_READ=_C('GL_DYNAMIC_READ',0x88E9)
GL_FLOAT_32_UNSIGNED_INT_24_8_REV=_C('GL_FLOAT_32_UNSIGNED_INT_24_8_REV',0x8DAD)
GL_FLOAT_MAT2x3=_C('GL_FLOAT_MAT2x3',0x8B65)
GL_FLOAT_MAT2x4=_C('GL_FLOAT_MAT2x4',0x8B66)
GL_FLOAT_MAT3x2=_C('GL_FLOAT_MAT3x2',0x8B67)
GL_FLOAT_MAT3x4=_C('GL_FLOAT_MAT3x4',0x8B68)
GL_FLOAT_MAT4x2=_C('GL_FLOAT_MAT4x2',0x8B69)
GL_FLOAT_MAT4x3=_C('GL_FLOAT_MAT4x3',0x8B6A)
GL_FRAGMENT_SHADER_DERIVATIVE_HINT=_C('GL_FRAGMENT_SHADER_DERIVATIVE_HINT',0x8B8B)
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE',0x8215)
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE',0x8214)
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING=_C('GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING',0x8210)
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE=_C('GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE',0x8211)
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE',0x8216)
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE',0x8213)
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE',0x8212)
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE=_C('GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE',0x8217)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER',0x8CD4)
GL_FRAMEBUFFER_DEFAULT=_C('GL_FRAMEBUFFER_DEFAULT',0x8218)
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE=_C('GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE',0x8D56)
GL_FRAMEBUFFER_UNDEFINED=_C('GL_FRAMEBUFFER_UNDEFINED',0x8219)
GL_GREEN=_C('GL_GREEN',0x1904)
GL_HALF_FLOAT=_C('GL_HALF_FLOAT',0x140B)
GL_INTERLEAVED_ATTRIBS=_C('GL_INTERLEAVED_ATTRIBS',0x8C8C)
GL_INT_2_10_10_10_REV=_C('GL_INT_2_10_10_10_REV',0x8D9F)
GL_INT_SAMPLER_2D=_C('GL_INT_SAMPLER_2D',0x8DCA)
GL_INT_SAMPLER_2D_ARRAY=_C('GL_INT_SAMPLER_2D_ARRAY',0x8DCF)
GL_INT_SAMPLER_3D=_C('GL_INT_SAMPLER_3D',0x8DCB)
GL_INT_SAMPLER_CUBE=_C('GL_INT_SAMPLER_CUBE',0x8DCC)
GL_INVALID_INDEX=_C('GL_INVALID_INDEX',0xFFFFFFFF)
GL_MAJOR_VERSION=_C('GL_MAJOR_VERSION',0x821B)
GL_MAP_FLUSH_EXPLICIT_BIT=_C('GL_MAP_FLUSH_EXPLICIT_BIT',0x0010)
GL_MAP_INVALIDATE_BUFFER_BIT=_C('GL_MAP_INVALIDATE_BUFFER_BIT',0x0008)
GL_MAP_INVALIDATE_RANGE_BIT=_C('GL_MAP_INVALIDATE_RANGE_BIT',0x0004)
GL_MAP_READ_BIT=_C('GL_MAP_READ_BIT',0x0001)
GL_MAP_UNSYNCHRONIZED_BIT=_C('GL_MAP_UNSYNCHRONIZED_BIT',0x0020)
GL_MAP_WRITE_BIT=_C('GL_MAP_WRITE_BIT',0x0002)
GL_MAX=_C('GL_MAX',0x8008)
GL_MAX_3D_TEXTURE_SIZE=_C('GL_MAX_3D_TEXTURE_SIZE',0x8073)
GL_MAX_ARRAY_TEXTURE_LAYERS=_C('GL_MAX_ARRAY_TEXTURE_LAYERS',0x88FF)
GL_MAX_COLOR_ATTACHMENTS=_C('GL_MAX_COLOR_ATTACHMENTS',0x8CDF)
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS',0x8A33)
GL_MAX_COMBINED_UNIFORM_BLOCKS=_C('GL_MAX_COMBINED_UNIFORM_BLOCKS',0x8A2E)
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS',0x8A31)
GL_MAX_DRAW_BUFFERS=_C('GL_MAX_DRAW_BUFFERS',0x8824)
GL_MAX_ELEMENTS_INDICES=_C('GL_MAX_ELEMENTS_INDICES',0x80E9)
GL_MAX_ELEMENTS_VERTICES=_C('GL_MAX_ELEMENTS_VERTICES',0x80E8)
GL_MAX_ELEMENT_INDEX=_C('GL_MAX_ELEMENT_INDEX',0x8D6B)
GL_MAX_FRAGMENT_INPUT_COMPONENTS=_C('GL_MAX_FRAGMENT_INPUT_COMPONENTS',0x9125)
GL_MAX_FRAGMENT_UNIFORM_BLOCKS=_C('GL_MAX_FRAGMENT_UNIFORM_BLOCKS',0x8A2D)
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS=_C('GL_MAX_FRAGMENT_UNIFORM_COMPONENTS',0x8B49)
GL_MAX_PROGRAM_TEXEL_OFFSET=_C('GL_MAX_PROGRAM_TEXEL_OFFSET',0x8905)
GL_MAX_SAMPLES=_C('GL_MAX_SAMPLES',0x8D57)
GL_MAX_SERVER_WAIT_TIMEOUT=_C('GL_MAX_SERVER_WAIT_TIMEOUT',0x9111)
GL_MAX_TEXTURE_LOD_BIAS=_C('GL_MAX_TEXTURE_LOD_BIAS',0x84FD)
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS=_C('GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS',0x8C8A)
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS=_C('GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS',0x8C8B)
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS=_C('GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS',0x8C80)
GL_MAX_UNIFORM_BLOCK_SIZE=_C('GL_MAX_UNIFORM_BLOCK_SIZE',0x8A30)
GL_MAX_UNIFORM_BUFFER_BINDINGS=_C('GL_MAX_UNIFORM_BUFFER_BINDINGS',0x8A2F)
GL_MAX_VARYING_COMPONENTS=_C('GL_MAX_VARYING_COMPONENTS',0x8B4B)
GL_MAX_VERTEX_OUTPUT_COMPONENTS=_C('GL_MAX_VERTEX_OUTPUT_COMPONENTS',0x9122)
GL_MAX_VERTEX_UNIFORM_BLOCKS=_C('GL_MAX_VERTEX_UNIFORM_BLOCKS',0x8A2B)
GL_MAX_VERTEX_UNIFORM_COMPONENTS=_C('GL_MAX_VERTEX_UNIFORM_COMPONENTS',0x8B4A)
GL_MIN=_C('GL_MIN',0x8007)
GL_MINOR_VERSION=_C('GL_MINOR_VERSION',0x821C)
GL_MIN_PROGRAM_TEXEL_OFFSET=_C('GL_MIN_PROGRAM_TEXEL_OFFSET',0x8904)
GL_NUM_EXTENSIONS=_C('GL_NUM_EXTENSIONS',0x821D)
GL_NUM_PROGRAM_BINARY_FORMATS=_C('GL_NUM_PROGRAM_BINARY_FORMATS',0x87FE)
GL_NUM_SAMPLE_COUNTS=_C('GL_NUM_SAMPLE_COUNTS',0x9380)
GL_OBJECT_TYPE=_C('GL_OBJECT_TYPE',0x9112)
GL_PACK_ROW_LENGTH=_C('GL_PACK_ROW_LENGTH',0x0D02)
GL_PACK_SKIP_PIXELS=_C('GL_PACK_SKIP_PIXELS',0x0D04)
GL_PACK_SKIP_ROWS=_C('GL_PACK_SKIP_ROWS',0x0D03)
GL_PIXEL_PACK_BUFFER=_C('GL_PIXEL_PACK_BUFFER',0x88EB)
GL_PIXEL_PACK_BUFFER_BINDING=_C('GL_PIXEL_PACK_BUFFER_BINDING',0x88ED)
GL_PIXEL_UNPACK_BUFFER=_C('GL_PIXEL_UNPACK_BUFFER',0x88EC)
GL_PIXEL_UNPACK_BUFFER_BINDING=_C('GL_PIXEL_UNPACK_BUFFER_BINDING',0x88EF)
GL_PRIMITIVE_RESTART_FIXED_INDEX=_C('GL_PRIMITIVE_RESTART_FIXED_INDEX',0x8D69)
GL_PROGRAM_BINARY_FORMATS=_C('GL_PROGRAM_BINARY_FORMATS',0x87FF)
GL_PROGRAM_BINARY_LENGTH=_C('GL_PROGRAM_BINARY_LENGTH',0x8741)
GL_PROGRAM_BINARY_RETRIEVABLE_HINT=_C('GL_PROGRAM_BINARY_RETRIEVABLE_HINT',0x8257)
GL_QUERY_RESULT=_C('GL_QUERY_RESULT',0x8866)
GL_QUERY_RESULT_AVAILABLE=_C('GL_QUERY_RESULT_AVAILABLE',0x8867)
GL_R11F_G11F_B10F=_C('GL_R11F_G11F_B10F',0x8C3A)
GL_R16F=_C('GL_R16F',0x822D)
GL_R16I=_C('GL_R16I',0x8233)
GL_R16UI=_C('GL_R16UI',0x8234)
GL_R32F=_C('GL_R32F',0x822E)
GL_R32I=_C('GL_R32I',0x8235)
GL_R32UI=_C('GL_R32UI',0x8236)
GL_R8=_C('GL_R8',0x8229)
GL_R8I=_C('GL_R8I',0x8231)
GL_R8UI=_C('GL_R8UI',0x8232)
GL_R8_SNORM=_C('GL_R8_SNORM',0x8F94)
GL_RASTERIZER_DISCARD=_C('GL_RASTERIZER_DISCARD',0x8C89)
GL_READ_BUFFER=_C('GL_READ_BUFFER',0x0C02)
GL_READ_FRAMEBUFFER=_C('GL_READ_FRAMEBUFFER',0x8CA8)
GL_READ_FRAMEBUFFER_BINDING=_C('GL_READ_FRAMEBUFFER_BINDING',0x8CAA)
GL_RED=_C('GL_RED',0x1903)
GL_RED_INTEGER=_C('GL_RED_INTEGER',0x8D94)
GL_RENDERBUFFER_SAMPLES=_C('GL_RENDERBUFFER_SAMPLES',0x8CAB)
GL_RG=_C('GL_RG',0x8227)
GL_RG16F=_C('GL_RG16F',0x822F)
GL_RG16I=_C('GL_RG16I',0x8239)
GL_RG16UI=_C('GL_RG16UI',0x823A)
GL_RG32F=_C('GL_RG32F',0x8230)
GL_RG32I=_C('GL_RG32I',0x823B)
GL_RG32UI=_C('GL_RG32UI',0x823C)
GL_RG8=_C('GL_RG8',0x822B)
GL_RG8I=_C('GL_RG8I',0x8237)
GL_RG8UI=_C('GL_RG8UI',0x8238)
GL_RG8_SNORM=_C('GL_RG8_SNORM',0x8F95)
GL_RGB10_A2=_C('GL_RGB10_A2',0x8059)
GL_RGB10_A2UI=_C('GL_RGB10_A2UI',0x906F)
GL_RGB16F=_C('GL_RGB16F',0x881B)
GL_RGB16I=_C('GL_RGB16I',0x8D89)
GL_RGB16UI=_C('GL_RGB16UI',0x8D77)
GL_RGB32F=_C('GL_RGB32F',0x8815)
GL_RGB32I=_C('GL_RGB32I',0x8D83)
GL_RGB32UI=_C('GL_RGB32UI',0x8D71)
GL_RGB8=_C('GL_RGB8',0x8051)
GL_RGB8I=_C('GL_RGB8I',0x8D8F)
GL_RGB8UI=_C('GL_RGB8UI',0x8D7D)
GL_RGB8_SNORM=_C('GL_RGB8_SNORM',0x8F96)
GL_RGB9_E5=_C('GL_RGB9_E5',0x8C3D)
GL_RGBA16F=_C('GL_RGBA16F',0x881A)
GL_RGBA16I=_C('GL_RGBA16I',0x8D88)
GL_RGBA16UI=_C('GL_RGBA16UI',0x8D76)
GL_RGBA32F=_C('GL_RGBA32F',0x8814)
GL_RGBA32I=_C('GL_RGBA32I',0x8D82)
GL_RGBA32UI=_C('GL_RGBA32UI',0x8D70)
GL_RGBA8=_C('GL_RGBA8',0x8058)
GL_RGBA8I=_C('GL_RGBA8I',0x8D8E)
GL_RGBA8UI=_C('GL_RGBA8UI',0x8D7C)
GL_RGBA8_SNORM=_C('GL_RGBA8_SNORM',0x8F97)
GL_RGBA_INTEGER=_C('GL_RGBA_INTEGER',0x8D99)
GL_RGB_INTEGER=_C('GL_RGB_INTEGER',0x8D98)
GL_RG_INTEGER=_C('GL_RG_INTEGER',0x8228)
GL_SAMPLER_2D_ARRAY=_C('GL_SAMPLER_2D_ARRAY',0x8DC1)
GL_SAMPLER_2D_ARRAY_SHADOW=_C('GL_SAMPLER_2D_ARRAY_SHADOW',0x8DC4)
GL_SAMPLER_2D_SHADOW=_C('GL_SAMPLER_2D_SHADOW',0x8B62)
GL_SAMPLER_3D=_C('GL_SAMPLER_3D',0x8B5F)
GL_SAMPLER_BINDING=_C('GL_SAMPLER_BINDING',0x8919)
GL_SAMPLER_CUBE_SHADOW=_C('GL_SAMPLER_CUBE_SHADOW',0x8DC5)
GL_SEPARATE_ATTRIBS=_C('GL_SEPARATE_ATTRIBS',0x8C8D)
GL_SIGNALED=_C('GL_SIGNALED',0x9119)
GL_SIGNED_NORMALIZED=_C('GL_SIGNED_NORMALIZED',0x8F9C)
GL_SRGB=_C('GL_SRGB',0x8C40)
GL_SRGB8=_C('GL_SRGB8',0x8C41)
GL_SRGB8_ALPHA8=_C('GL_SRGB8_ALPHA8',0x8C43)
GL_STATIC_COPY=_C('GL_STATIC_COPY',0x88E6)
GL_STATIC_READ=_C('GL_STATIC_READ',0x88E5)
GL_STENCIL=_C('GL_STENCIL',0x1802)
GL_STREAM_COPY=_C('GL_STREAM_COPY',0x88E2)
GL_STREAM_READ=_C('GL_STREAM_READ',0x88E1)
GL_SYNC_CONDITION=_C('GL_SYNC_CONDITION',0x9113)
GL_SYNC_FENCE=_C('GL_SYNC_FENCE',0x9116)
GL_SYNC_FLAGS=_C('GL_SYNC_FLAGS',0x9115)
GL_SYNC_FLUSH_COMMANDS_BIT=_C('GL_SYNC_FLUSH_COMMANDS_BIT',0x00000001)
GL_SYNC_GPU_COMMANDS_COMPLETE=_C('GL_SYNC_GPU_COMMANDS_COMPLETE',0x9117)
GL_SYNC_STATUS=_C('GL_SYNC_STATUS',0x9114)
GL_TEXTURE_2D_ARRAY=_C('GL_TEXTURE_2D_ARRAY',0x8C1A)
GL_TEXTURE_3D=_C('GL_TEXTURE_3D',0x806F)
GL_TEXTURE_BASE_LEVEL=_C('GL_TEXTURE_BASE_LEVEL',0x813C)
GL_TEXTURE_BINDING_2D_ARRAY=_C('GL_TEXTURE_BINDING_2D_ARRAY',0x8C1D)
GL_TEXTURE_BINDING_3D=_C('GL_TEXTURE_BINDING_3D',0x806A)
GL_TEXTURE_COMPARE_FUNC=_C('GL_TEXTURE_COMPARE_FUNC',0x884D)
GL_TEXTURE_COMPARE_MODE=_C('GL_TEXTURE_COMPARE_MODE',0x884C)
GL_TEXTURE_IMMUTABLE_FORMAT=_C('GL_TEXTURE_IMMUTABLE_FORMAT',0x912F)
GL_TEXTURE_IMMUTABLE_LEVELS=_C('GL_TEXTURE_IMMUTABLE_LEVELS',0x82DF)
GL_TEXTURE_MAX_LEVEL=_C('GL_TEXTURE_MAX_LEVEL',0x813D)
GL_TEXTURE_MAX_LOD=_C('GL_TEXTURE_MAX_LOD',0x813B)
GL_TEXTURE_MIN_LOD=_C('GL_TEXTURE_MIN_LOD',0x813A)
GL_TEXTURE_SWIZZLE_A=_C('GL_TEXTURE_SWIZZLE_A',0x8E45)
GL_TEXTURE_SWIZZLE_B=_C('GL_TEXTURE_SWIZZLE_B',0x8E44)
GL_TEXTURE_SWIZZLE_G=_C('GL_TEXTURE_SWIZZLE_G',0x8E43)
GL_TEXTURE_SWIZZLE_R=_C('GL_TEXTURE_SWIZZLE_R',0x8E42)
GL_TEXTURE_WRAP_R=_C('GL_TEXTURE_WRAP_R',0x8072)
GL_TIMEOUT_EXPIRED=_C('GL_TIMEOUT_EXPIRED',0x911B)
GL_TIMEOUT_IGNORED=_C('GL_TIMEOUT_IGNORED',0xFFFFFFFFFFFFFFFF)
GL_TRANSFORM_FEEDBACK=_C('GL_TRANSFORM_FEEDBACK',0x8E22)
GL_TRANSFORM_FEEDBACK_ACTIVE=_C('GL_TRANSFORM_FEEDBACK_ACTIVE',0x8E24)
GL_TRANSFORM_FEEDBACK_BINDING=_C('GL_TRANSFORM_FEEDBACK_BINDING',0x8E25)
GL_TRANSFORM_FEEDBACK_BUFFER=_C('GL_TRANSFORM_FEEDBACK_BUFFER',0x8C8E)
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING=_C('GL_TRANSFORM_FEEDBACK_BUFFER_BINDING',0x8C8F)
GL_TRANSFORM_FEEDBACK_BUFFER_MODE=_C('GL_TRANSFORM_FEEDBACK_BUFFER_MODE',0x8C7F)
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE=_C('GL_TRANSFORM_FEEDBACK_BUFFER_SIZE',0x8C85)
GL_TRANSFORM_FEEDBACK_BUFFER_START=_C('GL_TRANSFORM_FEEDBACK_BUFFER_START',0x8C84)
GL_TRANSFORM_FEEDBACK_PAUSED=_C('GL_TRANSFORM_FEEDBACK_PAUSED',0x8E23)
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN=_C('GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN',0x8C88)
GL_TRANSFORM_FEEDBACK_VARYINGS=_C('GL_TRANSFORM_FEEDBACK_VARYINGS',0x8C83)
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH=_C('GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH',0x8C76)
GL_UNIFORM_ARRAY_STRIDE=_C('GL_UNIFORM_ARRAY_STRIDE',0x8A3C)
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS=_C('GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS',0x8A42)
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES=_C('GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES',0x8A43)
GL_UNIFORM_BLOCK_BINDING=_C('GL_UNIFORM_BLOCK_BINDING',0x8A3F)
GL_UNIFORM_BLOCK_DATA_SIZE=_C('GL_UNIFORM_BLOCK_DATA_SIZE',0x8A40)
GL_UNIFORM_BLOCK_INDEX=_C('GL_UNIFORM_BLOCK_INDEX',0x8A3A)
GL_UNIFORM_BLOCK_NAME_LENGTH=_C('GL_UNIFORM_BLOCK_NAME_LENGTH',0x8A41)
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER=_C('GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER',0x8A46)
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER=_C('GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER',0x8A44)
GL_UNIFORM_BUFFER=_C('GL_UNIFORM_BUFFER',0x8A11)
GL_UNIFORM_BUFFER_BINDING=_C('GL_UNIFORM_BUFFER_BINDING',0x8A28)
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT=_C('GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT',0x8A34)
GL_UNIFORM_BUFFER_SIZE=_C('GL_UNIFORM_BUFFER_SIZE',0x8A2A)
GL_UNIFORM_BUFFER_START=_C('GL_UNIFORM_BUFFER_START',0x8A29)
GL_UNIFORM_IS_ROW_MAJOR=_C('GL_UNIFORM_IS_ROW_MAJOR',0x8A3E)
GL_UNIFORM_MATRIX_STRIDE=_C('GL_UNIFORM_MATRIX_STRIDE',0x8A3D)
GL_UNIFORM_NAME_LENGTH=_C('GL_UNIFORM_NAME_LENGTH',0x8A39)
GL_UNIFORM_OFFSET=_C('GL_UNIFORM_OFFSET',0x8A3B)
GL_UNIFORM_SIZE=_C('GL_UNIFORM_SIZE',0x8A38)
GL_UNIFORM_TYPE=_C('GL_UNIFORM_TYPE',0x8A37)
GL_UNPACK_IMAGE_HEIGHT=_C('GL_UNPACK_IMAGE_HEIGHT',0x806E)
GL_UNPACK_ROW_LENGTH=_C('GL_UNPACK_ROW_LENGTH',0x0CF2)
GL_UNPACK_SKIP_IMAGES=_C('GL_UNPACK_SKIP_IMAGES',0x806D)
GL_UNPACK_SKIP_PIXELS=_C('GL_UNPACK_SKIP_PIXELS',0x0CF4)
GL_UNPACK_SKIP_ROWS=_C('GL_UNPACK_SKIP_ROWS',0x0CF3)
GL_UNSIGNALED=_C('GL_UNSIGNALED',0x9118)
GL_UNSIGNED_INT_10F_11F_11F_REV=_C('GL_UNSIGNED_INT_10F_11F_11F_REV',0x8C3B)
GL_UNSIGNED_INT_24_8=_C('GL_UNSIGNED_INT_24_8',0x84FA)
GL_UNSIGNED_INT_2_10_10_10_REV=_C('GL_UNSIGNED_INT_2_10_10_10_REV',0x8368)
GL_UNSIGNED_INT_5_9_9_9_REV=_C('GL_UNSIGNED_INT_5_9_9_9_REV',0x8C3E)
GL_UNSIGNED_INT_SAMPLER_2D=_C('GL_UNSIGNED_INT_SAMPLER_2D',0x8DD2)
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY=_C('GL_UNSIGNED_INT_SAMPLER_2D_ARRAY',0x8DD7)
GL_UNSIGNED_INT_SAMPLER_3D=_C('GL_UNSIGNED_INT_SAMPLER_3D',0x8DD3)
GL_UNSIGNED_INT_SAMPLER_CUBE=_C('GL_UNSIGNED_INT_SAMPLER_CUBE',0x8DD4)
GL_UNSIGNED_INT_VEC2=_C('GL_UNSIGNED_INT_VEC2',0x8DC6)
GL_UNSIGNED_INT_VEC3=_C('GL_UNSIGNED_INT_VEC3',0x8DC7)
GL_UNSIGNED_INT_VEC4=_C('GL_UNSIGNED_INT_VEC4',0x8DC8)
GL_UNSIGNED_NORMALIZED=_C('GL_UNSIGNED_NORMALIZED',0x8C17)
GL_VERTEX_ARRAY_BINDING=_C('GL_VERTEX_ARRAY_BINDING',0x85B5)
GL_VERTEX_ATTRIB_ARRAY_DIVISOR=_C('GL_VERTEX_ATTRIB_ARRAY_DIVISOR',0x88FE)
GL_VERTEX_ATTRIB_ARRAY_INTEGER=_C('GL_VERTEX_ATTRIB_ARRAY_INTEGER',0x88FD)
GL_WAIT_FAILED=_C('GL_WAIT_FAILED',0x911D)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBeginQuery(target,id):pass
@_f
@_p.types(None,_cs.GLenum)
def glBeginTransformFeedback(primitiveMode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBindBufferBase(target,index,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glBindBufferRange(target,index,buffer,offset,size):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glBindSampler(unit,sampler):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindTransformFeedback(target,id):pass
@_f
@_p.types(None,_cs.GLuint)
def glBindVertexArray(array):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLbitfield,_cs.GLenum)
def glBlitFramebuffer(srcX0,srcY0,srcX1,srcY1,dstX0,dstY0,dstX1,dstY1,mask,filter):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLfloat,_cs.GLint)
def glClearBufferfi(buffer,drawbuffer,depth,stencil):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLfloatArray)
def glClearBufferfv(buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLintArray)
def glClearBufferiv(buffer,drawbuffer,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLuintArray)
def glClearBufferuiv(buffer,drawbuffer,value):pass
@_f
@_p.types(_cs.GLenum,_cs.GLsync,_cs.GLbitfield,_cs.GLuint64)
def glClientWaitSync(sync,flags,timeout):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTexImage3D(target,level,internalformat,width,height,depth,border,imageSize,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTexSubImage3D(target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLintptr,_cs.GLintptr,_cs.GLsizeiptr)
def glCopyBufferSubData(readTarget,writeTarget,readOffset,writeOffset,size):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTexSubImage3D(target,level,xoffset,yoffset,zoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteQueries(n,ids):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteSamplers(count,samplers):pass
@_f
@_p.types(None,_cs.GLsync)
def glDeleteSync(sync):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteTransformFeedbacks(n,ids):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteVertexArrays(n,arrays):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glDrawArraysInstanced(mode,first,count,instancecount):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDrawBuffers(n,bufs):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei)
def glDrawElementsInstanced(mode,count,type,indices,instancecount):pass
# Calculate length of indices from type:DrawElementsType
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glDrawRangeElements(mode,start,end,count,type,indices):pass
# Calculate length of indices from type:DrawElementsType
@_f
@_p.types(None,_cs.GLenum)
def glEndQuery(target):pass
@_f
@_p.types(None,)
def glEndTransformFeedback():pass
@_f
@_p.types(_cs.GLsync,_cs.GLenum,_cs.GLbitfield)
def glFenceSync(condition,flags):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr)
def glFlushMappedBufferRange(target,offset,length):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTextureLayer(target,attachment,texture,level,layer):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenQueries(n,ids):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenSamplers(count,samplers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenTransformFeedbacks(n,ids):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenVertexArrays(n,arrays):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetActiveUniformBlockName(program,uniformBlockIndex,bufSize,length,uniformBlockName):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetActiveUniformBlockiv(program,uniformBlockIndex,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,_cs.GLenum,arrays.GLintArray)
def glGetActiveUniformsiv(program,uniformCount,uniformIndices,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLint64Array)
def glGetBufferParameteri64v(target,pname,params):pass
# Calculate length of params from pname:BufferPNameARB
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLvoidpArray)
def glGetBufferPointerv(target,pname,params):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetFragDataLocation(program,name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLint64Array)
def glGetInteger64i_v(target,index,data):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLint64Array)
def glGetInteger64v(pname,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glGetIntegeri_v(target,index,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLsizei,arrays.GLintArray)
def glGetInternalformativ(target,internalformat,pname,bufSize,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLuintArray,ctypes.c_void_p)
def glGetProgramBinary(program,bufSize,length,binaryFormat,binary):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetQueryObjectuiv(id,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetQueryiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetSamplerParameterfv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetSamplerParameteriv(sampler,pname,params):pass
@_f
@_p.types(arrays.GLubyteArray,_cs.GLenum,_cs.GLuint)
def glGetStringi(name,index):pass
@_f
@_p.types(None,_cs.GLsync,_cs.GLenum,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLintArray)
def glGetSynciv(sync,pname,bufSize,length,values):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLcharArray)
def glGetTransformFeedbackVarying(program,index,bufSize,length,size,type,name):pass
@_f
@_p.types(_cs.GLuint,_cs.GLuint,arrays.GLcharArray)
def glGetUniformBlockIndex(program,uniformBlockName):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER( ctypes.POINTER( _cs.GLchar )),arrays.GLuintArray)
def glGetUniformIndices(program,uniformCount,uniformNames,uniformIndices):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLuintArray)
def glGetUniformuiv(program,location,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexAttribIiv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetVertexAttribIuiv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray)
def glInvalidateFramebuffer(target,numAttachments,attachments):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glInvalidateSubFramebuffer(target,numAttachments,attachments,x,y,width,height):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsQuery(id):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsSampler(sampler):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLsync)
def glIsSync(sync):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsTransformFeedback(id):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsVertexArray(array):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr,_cs.GLbitfield)
def glMapBufferRange(target,offset,length,access):pass
@_f
@_p.types(None,)
def glPauseTransformFeedback():pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei)
def glProgramBinary(program,binaryFormat,binary,length):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glProgramParameteri(program,pname,value):pass
@_f
@_p.types(None,_cs.GLenum)
def glReadBuffer(mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageMultisample(target,samples,internalformat,width,height):pass
@_f
@_p.types(None,)
def glResumeTransformFeedback():pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLfloat)
def glSamplerParameterf(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glSamplerParameterfv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glSamplerParameteri(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glSamplerParameteriv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage3D(target,level,internalformat,width,height,depth,border,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glTexStorage2D(target,levels,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei)
def glTexStorage3D(target,levels,internalformat,width,height,depth):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage3D(target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER( ctypes.POINTER( _cs.GLchar )),_cs.GLenum)
def glTransformFeedbackVaryings(program,count,varyings,bufferMode):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint)
def glUniform1ui(location,v0):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform1uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint)
def glUniform2ui(location,v0,v1):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform2uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniform3ui(location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform3uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniform4ui(location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform4uiv(location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniformBlockBinding(program,uniformBlockIndex,uniformBlockBinding):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix2x3fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix2x4fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix3x2fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix3x4fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix4x2fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix4x3fv(location,count,transpose,value):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum)
def glUnmapBuffer(target):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribDivisor(index,divisor):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexAttribI4i(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI4iv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI4ui(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI4uiv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribIPointer(index,size,type,stride,pointer):pass
# Calculate length of pointer from type:VertexAttribEnum
@_f
@_p.types(None,_cs.GLsync,_cs.GLbitfield,_cs.GLuint64)
def glWaitSync(sync,flags,timeout):pass
