'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C
# Spec mixes constants from 1.0 and 1.1
from OpenGL.raw.GL.VERSION.GL_1_0 import *
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_1'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_1_1')
GL_2D=_C('GL_2D',0x0600)
GL_2_BYTES=_C('GL_2_BYTES',0x1407)
GL_3D=_C('GL_3D',0x0601)
GL_3D_COLOR=_C('GL_3D_COLOR',0x0602)
GL_3D_COLOR_TEXTURE=_C('GL_3D_COLOR_TEXTURE',0x0603)
GL_3_BYTES=_C('GL_3_BYTES',0x1408)
GL_4D_COLOR_TEXTURE=_C('GL_4D_COLOR_TEXTURE',0x0604)
GL_4_BYTES=_C('GL_4_BYTES',0x1409)
GL_ACCUM=_C('GL_ACCUM',0x0100)
GL_ACCUM_ALPHA_BITS=_C('GL_ACCUM_ALPHA_BITS',0x0D5B)
GL_ACCUM_BLUE_BITS=_C('GL_ACCUM_BLUE_BITS',0x0D5A)
GL_ACCUM_BUFFER_BIT=_C('GL_ACCUM_BUFFER_BIT',0x00000200)
GL_ACCUM_CLEAR_VALUE=_C('GL_ACCUM_CLEAR_VALUE',0x0B80)
GL_ACCUM_GREEN_BITS=_C('GL_ACCUM_GREEN_BITS',0x0D59)
GL_ACCUM_RED_BITS=_C('GL_ACCUM_RED_BITS',0x0D58)
GL_ADD=_C('GL_ADD',0x0104)
GL_ALL_ATTRIB_BITS=_C('GL_ALL_ATTRIB_BITS',0xFFFFFFFF)
GL_ALPHA=_C('GL_ALPHA',0x1906)
GL_ALPHA12=_C('GL_ALPHA12',0x803D)
GL_ALPHA16=_C('GL_ALPHA16',0x803E)
GL_ALPHA4=_C('GL_ALPHA4',0x803B)
GL_ALPHA8=_C('GL_ALPHA8',0x803C)
GL_ALPHA_BIAS=_C('GL_ALPHA_BIAS',0x0D1D)
GL_ALPHA_BITS=_C('GL_ALPHA_BITS',0x0D55)
GL_ALPHA_SCALE=_C('GL_ALPHA_SCALE',0x0D1C)
GL_ALPHA_TEST=_C('GL_ALPHA_TEST',0x0BC0)
GL_ALPHA_TEST_FUNC=_C('GL_ALPHA_TEST_FUNC',0x0BC1)
GL_ALPHA_TEST_REF=_C('GL_ALPHA_TEST_REF',0x0BC2)
GL_ALWAYS=_C('GL_ALWAYS',0x0207)
GL_AMBIENT=_C('GL_AMBIENT',0x1200)
GL_AMBIENT_AND_DIFFUSE=_C('GL_AMBIENT_AND_DIFFUSE',0x1602)
GL_AND=_C('GL_AND',0x1501)
GL_AND_INVERTED=_C('GL_AND_INVERTED',0x1504)
GL_AND_REVERSE=_C('GL_AND_REVERSE',0x1502)
GL_ATTRIB_STACK_DEPTH=_C('GL_ATTRIB_STACK_DEPTH',0x0BB0)
GL_AUTO_NORMAL=_C('GL_AUTO_NORMAL',0x0D80)
GL_AUX0=_C('GL_AUX0',0x0409)
GL_AUX1=_C('GL_AUX1',0x040A)
GL_AUX2=_C('GL_AUX2',0x040B)
GL_AUX3=_C('GL_AUX3',0x040C)
GL_AUX_BUFFERS=_C('GL_AUX_BUFFERS',0x0C00)
GL_BACK=_C('GL_BACK',0x0405)
GL_BACK_LEFT=_C('GL_BACK_LEFT',0x0402)
GL_BACK_RIGHT=_C('GL_BACK_RIGHT',0x0403)
GL_BITMAP=_C('GL_BITMAP',0x1A00)
GL_BITMAP_TOKEN=_C('GL_BITMAP_TOKEN',0x0704)
GL_BLEND=_C('GL_BLEND',0x0BE2)
GL_BLEND_DST=_C('GL_BLEND_DST',0x0BE0)
GL_BLEND_SRC=_C('GL_BLEND_SRC',0x0BE1)
GL_BLUE=_C('GL_BLUE',0x1905)
GL_BLUE_BIAS=_C('GL_BLUE_BIAS',0x0D1B)
GL_BLUE_BITS=_C('GL_BLUE_BITS',0x0D54)
GL_BLUE_SCALE=_C('GL_BLUE_SCALE',0x0D1A)
GL_BYTE=_C('GL_BYTE',0x1400)
GL_C3F_V3F=_C('GL_C3F_V3F',0x2A24)
GL_C4F_N3F_V3F=_C('GL_C4F_N3F_V3F',0x2A26)
GL_C4UB_V2F=_C('GL_C4UB_V2F',0x2A22)
GL_C4UB_V3F=_C('GL_C4UB_V3F',0x2A23)
GL_CCW=_C('GL_CCW',0x0901)
GL_CLAMP=_C('GL_CLAMP',0x2900)
GL_CLEAR=_C('GL_CLEAR',0x1500)
GL_CLIENT_ALL_ATTRIB_BITS=_C('GL_CLIENT_ALL_ATTRIB_BITS',0xFFFFFFFF)
GL_CLIENT_ATTRIB_STACK_DEPTH=_C('GL_CLIENT_ATTRIB_STACK_DEPTH',0x0BB1)
GL_CLIENT_PIXEL_STORE_BIT=_C('GL_CLIENT_PIXEL_STORE_BIT',0x00000001)
GL_CLIENT_VERTEX_ARRAY_BIT=_C('GL_CLIENT_VERTEX_ARRAY_BIT',0x00000002)
GL_CLIP_PLANE0=_C('GL_CLIP_PLANE0',0x3000)
GL_CLIP_PLANE1=_C('GL_CLIP_PLANE1',0x3001)
GL_CLIP_PLANE2=_C('GL_CLIP_PLANE2',0x3002)
GL_CLIP_PLANE3=_C('GL_CLIP_PLANE3',0x3003)
GL_CLIP_PLANE4=_C('GL_CLIP_PLANE4',0x3004)
GL_CLIP_PLANE5=_C('GL_CLIP_PLANE5',0x3005)
GL_COEFF=_C('GL_COEFF',0x0A00)
GL_COLOR=_C('GL_COLOR',0x1800)
GL_COLOR_ARRAY=_C('GL_COLOR_ARRAY',0x8076)
GL_COLOR_ARRAY_POINTER=_C('GL_COLOR_ARRAY_POINTER',0x8090)
GL_COLOR_ARRAY_SIZE=_C('GL_COLOR_ARRAY_SIZE',0x8081)
GL_COLOR_ARRAY_STRIDE=_C('GL_COLOR_ARRAY_STRIDE',0x8083)
GL_COLOR_ARRAY_TYPE=_C('GL_COLOR_ARRAY_TYPE',0x8082)
GL_COLOR_BUFFER_BIT=_C('GL_COLOR_BUFFER_BIT',0x00004000)
GL_COLOR_CLEAR_VALUE=_C('GL_COLOR_CLEAR_VALUE',0x0C22)
GL_COLOR_INDEX=_C('GL_COLOR_INDEX',0x1900)
GL_COLOR_INDEXES=_C('GL_COLOR_INDEXES',0x1603)
GL_COLOR_LOGIC_OP=_C('GL_COLOR_LOGIC_OP',0x0BF2)
GL_COLOR_MATERIAL=_C('GL_COLOR_MATERIAL',0x0B57)
GL_COLOR_MATERIAL_FACE=_C('GL_COLOR_MATERIAL_FACE',0x0B55)
GL_COLOR_MATERIAL_PARAMETER=_C('GL_COLOR_MATERIAL_PARAMETER',0x0B56)
GL_COLOR_WRITEMASK=_C('GL_COLOR_WRITEMASK',0x0C23)
GL_COMPILE=_C('GL_COMPILE',0x1300)
GL_COMPILE_AND_EXECUTE=_C('GL_COMPILE_AND_EXECUTE',0x1301)
GL_CONSTANT_ATTENUATION=_C('GL_CONSTANT_ATTENUATION',0x1207)
GL_COPY=_C('GL_COPY',0x1503)
GL_COPY_INVERTED=_C('GL_COPY_INVERTED',0x150C)
GL_COPY_PIXEL_TOKEN=_C('GL_COPY_PIXEL_TOKEN',0x0706)
GL_CULL_FACE=_C('GL_CULL_FACE',0x0B44)
GL_CULL_FACE_MODE=_C('GL_CULL_FACE_MODE',0x0B45)
GL_CURRENT_BIT=_C('GL_CURRENT_BIT',0x00000001)
GL_CURRENT_COLOR=_C('GL_CURRENT_COLOR',0x0B00)
GL_CURRENT_INDEX=_C('GL_CURRENT_INDEX',0x0B01)
GL_CURRENT_NORMAL=_C('GL_CURRENT_NORMAL',0x0B02)
GL_CURRENT_RASTER_COLOR=_C('GL_CURRENT_RASTER_COLOR',0x0B04)
GL_CURRENT_RASTER_DISTANCE=_C('GL_CURRENT_RASTER_DISTANCE',0x0B09)
GL_CURRENT_RASTER_INDEX=_C('GL_CURRENT_RASTER_INDEX',0x0B05)
GL_CURRENT_RASTER_POSITION=_C('GL_CURRENT_RASTER_POSITION',0x0B07)
GL_CURRENT_RASTER_POSITION_VALID=_C('GL_CURRENT_RASTER_POSITION_VALID',0x0B08)
GL_CURRENT_RASTER_TEXTURE_COORDS=_C('GL_CURRENT_RASTER_TEXTURE_COORDS',0x0B06)
GL_CURRENT_TEXTURE_COORDS=_C('GL_CURRENT_TEXTURE_COORDS',0x0B03)
GL_CW=_C('GL_CW',0x0900)
GL_DECAL=_C('GL_DECAL',0x2101)
GL_DECR=_C('GL_DECR',0x1E03)
GL_DEPTH=_C('GL_DEPTH',0x1801)
GL_DEPTH_BIAS=_C('GL_DEPTH_BIAS',0x0D1F)
GL_DEPTH_BITS=_C('GL_DEPTH_BITS',0x0D56)
GL_DEPTH_BUFFER_BIT=_C('GL_DEPTH_BUFFER_BIT',0x00000100)
GL_DEPTH_CLEAR_VALUE=_C('GL_DEPTH_CLEAR_VALUE',0x0B73)
GL_DEPTH_COMPONENT=_C('GL_DEPTH_COMPONENT',0x1902)
GL_DEPTH_FUNC=_C('GL_DEPTH_FUNC',0x0B74)
GL_DEPTH_RANGE=_C('GL_DEPTH_RANGE',0x0B70)
GL_DEPTH_SCALE=_C('GL_DEPTH_SCALE',0x0D1E)
GL_DEPTH_TEST=_C('GL_DEPTH_TEST',0x0B71)
GL_DEPTH_WRITEMASK=_C('GL_DEPTH_WRITEMASK',0x0B72)
GL_DIFFUSE=_C('GL_DIFFUSE',0x1201)
GL_DITHER=_C('GL_DITHER',0x0BD0)
GL_DOMAIN=_C('GL_DOMAIN',0x0A02)
GL_DONT_CARE=_C('GL_DONT_CARE',0x1100)
GL_DOUBLE=_C('GL_DOUBLE',0x140A)
GL_DOUBLEBUFFER=_C('GL_DOUBLEBUFFER',0x0C32)
GL_DRAW_BUFFER=_C('GL_DRAW_BUFFER',0x0C01)
GL_DRAW_PIXEL_TOKEN=_C('GL_DRAW_PIXEL_TOKEN',0x0705)
GL_DST_ALPHA=_C('GL_DST_ALPHA',0x0304)
GL_DST_COLOR=_C('GL_DST_COLOR',0x0306)
GL_EDGE_FLAG=_C('GL_EDGE_FLAG',0x0B43)
GL_EDGE_FLAG_ARRAY=_C('GL_EDGE_FLAG_ARRAY',0x8079)
GL_EDGE_FLAG_ARRAY_POINTER=_C('GL_EDGE_FLAG_ARRAY_POINTER',0x8093)
GL_EDGE_FLAG_ARRAY_STRIDE=_C('GL_EDGE_FLAG_ARRAY_STRIDE',0x808C)
GL_EMISSION=_C('GL_EMISSION',0x1600)
GL_ENABLE_BIT=_C('GL_ENABLE_BIT',0x00002000)
GL_EQUAL=_C('GL_EQUAL',0x0202)
GL_EQUIV=_C('GL_EQUIV',0x1509)
GL_EVAL_BIT=_C('GL_EVAL_BIT',0x00010000)
GL_EXP=_C('GL_EXP',0x0800)
GL_EXP2=_C('GL_EXP2',0x0801)
GL_EXTENSIONS=_C('GL_EXTENSIONS',0x1F03)
GL_EYE_LINEAR=_C('GL_EYE_LINEAR',0x2400)
GL_EYE_PLANE=_C('GL_EYE_PLANE',0x2502)
GL_FALSE=_C('GL_FALSE',0)
GL_FASTEST=_C('GL_FASTEST',0x1101)
GL_FEEDBACK=_C('GL_FEEDBACK',0x1C01)
GL_FEEDBACK_BUFFER_POINTER=_C('GL_FEEDBACK_BUFFER_POINTER',0x0DF0)
GL_FEEDBACK_BUFFER_SIZE=_C('GL_FEEDBACK_BUFFER_SIZE',0x0DF1)
GL_FEEDBACK_BUFFER_TYPE=_C('GL_FEEDBACK_BUFFER_TYPE',0x0DF2)
GL_FILL=_C('GL_FILL',0x1B02)
GL_FLAT=_C('GL_FLAT',0x1D00)
GL_FLOAT=_C('GL_FLOAT',0x1406)
GL_FOG=_C('GL_FOG',0x0B60)
GL_FOG_BIT=_C('GL_FOG_BIT',0x00000080)
GL_FOG_COLOR=_C('GL_FOG_COLOR',0x0B66)
GL_FOG_DENSITY=_C('GL_FOG_DENSITY',0x0B62)
GL_FOG_END=_C('GL_FOG_END',0x0B64)
GL_FOG_HINT=_C('GL_FOG_HINT',0x0C54)
GL_FOG_INDEX=_C('GL_FOG_INDEX',0x0B61)
GL_FOG_MODE=_C('GL_FOG_MODE',0x0B65)
GL_FOG_START=_C('GL_FOG_START',0x0B63)
GL_FRONT=_C('GL_FRONT',0x0404)
GL_FRONT_AND_BACK=_C('GL_FRONT_AND_BACK',0x0408)
GL_FRONT_FACE=_C('GL_FRONT_FACE',0x0B46)
GL_FRONT_LEFT=_C('GL_FRONT_LEFT',0x0400)
GL_FRONT_RIGHT=_C('GL_FRONT_RIGHT',0x0401)
GL_GEQUAL=_C('GL_GEQUAL',0x0206)
GL_GREATER=_C('GL_GREATER',0x0204)
GL_GREEN=_C('GL_GREEN',0x1904)
GL_GREEN_BIAS=_C('GL_GREEN_BIAS',0x0D19)
GL_GREEN_BITS=_C('GL_GREEN_BITS',0x0D53)
GL_GREEN_SCALE=_C('GL_GREEN_SCALE',0x0D18)
GL_HINT_BIT=_C('GL_HINT_BIT',0x00008000)
GL_INCR=_C('GL_INCR',0x1E02)
GL_INDEX_ARRAY=_C('GL_INDEX_ARRAY',0x8077)
GL_INDEX_ARRAY_POINTER=_C('GL_INDEX_ARRAY_POINTER',0x8091)
GL_INDEX_ARRAY_STRIDE=_C('GL_INDEX_ARRAY_STRIDE',0x8086)
GL_INDEX_ARRAY_TYPE=_C('GL_INDEX_ARRAY_TYPE',0x8085)
GL_INDEX_BITS=_C('GL_INDEX_BITS',0x0D51)
GL_INDEX_CLEAR_VALUE=_C('GL_INDEX_CLEAR_VALUE',0x0C20)
GL_INDEX_LOGIC_OP=_C('GL_INDEX_LOGIC_OP',0x0BF1)
GL_INDEX_MODE=_C('GL_INDEX_MODE',0x0C30)
GL_INDEX_OFFSET=_C('GL_INDEX_OFFSET',0x0D13)
GL_INDEX_SHIFT=_C('GL_INDEX_SHIFT',0x0D12)
GL_INDEX_WRITEMASK=_C('GL_INDEX_WRITEMASK',0x0C21)
GL_INT=_C('GL_INT',0x1404)
GL_INTENSITY=_C('GL_INTENSITY',0x8049)
GL_INTENSITY12=_C('GL_INTENSITY12',0x804C)
GL_INTENSITY16=_C('GL_INTENSITY16',0x804D)
GL_INTENSITY4=_C('GL_INTENSITY4',0x804A)
GL_INTENSITY8=_C('GL_INTENSITY8',0x804B)
GL_INVALID_ENUM=_C('GL_INVALID_ENUM',0x0500)
GL_INVALID_OPERATION=_C('GL_INVALID_OPERATION',0x0502)
GL_INVALID_VALUE=_C('GL_INVALID_VALUE',0x0501)
GL_INVERT=_C('GL_INVERT',0x150A)
GL_KEEP=_C('GL_KEEP',0x1E00)
GL_LEFT=_C('GL_LEFT',0x0406)
GL_LEQUAL=_C('GL_LEQUAL',0x0203)
GL_LESS=_C('GL_LESS',0x0201)
GL_LIGHT0=_C('GL_LIGHT0',0x4000)
GL_LIGHT1=_C('GL_LIGHT1',0x4001)
GL_LIGHT2=_C('GL_LIGHT2',0x4002)
GL_LIGHT3=_C('GL_LIGHT3',0x4003)
GL_LIGHT4=_C('GL_LIGHT4',0x4004)
GL_LIGHT5=_C('GL_LIGHT5',0x4005)
GL_LIGHT6=_C('GL_LIGHT6',0x4006)
GL_LIGHT7=_C('GL_LIGHT7',0x4007)
GL_LIGHTING=_C('GL_LIGHTING',0x0B50)
GL_LIGHTING_BIT=_C('GL_LIGHTING_BIT',0x00000040)
GL_LIGHT_MODEL_AMBIENT=_C('GL_LIGHT_MODEL_AMBIENT',0x0B53)
GL_LIGHT_MODEL_LOCAL_VIEWER=_C('GL_LIGHT_MODEL_LOCAL_VIEWER',0x0B51)
GL_LIGHT_MODEL_TWO_SIDE=_C('GL_LIGHT_MODEL_TWO_SIDE',0x0B52)
GL_LINE=_C('GL_LINE',0x1B01)
GL_LINEAR=_C('GL_LINEAR',0x2601)
GL_LINEAR_ATTENUATION=_C('GL_LINEAR_ATTENUATION',0x1208)
GL_LINEAR_MIPMAP_LINEAR=_C('GL_LINEAR_MIPMAP_LINEAR',0x2703)
GL_LINEAR_MIPMAP_NEAREST=_C('GL_LINEAR_MIPMAP_NEAREST',0x2701)
GL_LINES=_C('GL_LINES',0x0001)
GL_LINE_BIT=_C('GL_LINE_BIT',0x00000004)
GL_LINE_LOOP=_C('GL_LINE_LOOP',0x0002)
GL_LINE_RESET_TOKEN=_C('GL_LINE_RESET_TOKEN',0x0707)
GL_LINE_SMOOTH=_C('GL_LINE_SMOOTH',0x0B20)
GL_LINE_SMOOTH_HINT=_C('GL_LINE_SMOOTH_HINT',0x0C52)
GL_LINE_STIPPLE=_C('GL_LINE_STIPPLE',0x0B24)
GL_LINE_STIPPLE_PATTERN=_C('GL_LINE_STIPPLE_PATTERN',0x0B25)
GL_LINE_STIPPLE_REPEAT=_C('GL_LINE_STIPPLE_REPEAT',0x0B26)
GL_LINE_STRIP=_C('GL_LINE_STRIP',0x0003)
GL_LINE_TOKEN=_C('GL_LINE_TOKEN',0x0702)
GL_LINE_WIDTH=_C('GL_LINE_WIDTH',0x0B21)
GL_LINE_WIDTH_GRANULARITY=_C('GL_LINE_WIDTH_GRANULARITY',0x0B23)
GL_LINE_WIDTH_RANGE=_C('GL_LINE_WIDTH_RANGE',0x0B22)
GL_LIST_BASE=_C('GL_LIST_BASE',0x0B32)
GL_LIST_BIT=_C('GL_LIST_BIT',0x00020000)
GL_LIST_INDEX=_C('GL_LIST_INDEX',0x0B33)
GL_LIST_MODE=_C('GL_LIST_MODE',0x0B30)
GL_LOAD=_C('GL_LOAD',0x0101)
GL_LOGIC_OP=_C('GL_LOGIC_OP',0x0BF1)
GL_LOGIC_OP_MODE=_C('GL_LOGIC_OP_MODE',0x0BF0)
GL_LUMINANCE=_C('GL_LUMINANCE',0x1909)
GL_LUMINANCE12=_C('GL_LUMINANCE12',0x8041)
GL_LUMINANCE12_ALPHA12=_C('GL_LUMINANCE12_ALPHA12',0x8047)
GL_LUMINANCE12_ALPHA4=_C('GL_LUMINANCE12_ALPHA4',0x8046)
GL_LUMINANCE16=_C('GL_LUMINANCE16',0x8042)
GL_LUMINANCE16_ALPHA16=_C('GL_LUMINANCE16_ALPHA16',0x8048)
GL_LUMINANCE4=_C('GL_LUMINANCE4',0x803F)
GL_LUMINANCE4_ALPHA4=_C('GL_LUMINANCE4_ALPHA4',0x8043)
GL_LUMINANCE6_ALPHA2=_C('GL_LUMINANCE6_ALPHA2',0x8044)
GL_LUMINANCE8=_C('GL_LUMINANCE8',0x8040)
GL_LUMINANCE8_ALPHA8=_C('GL_LUMINANCE8_ALPHA8',0x8045)
GL_LUMINANCE_ALPHA=_C('GL_LUMINANCE_ALPHA',0x190A)
GL_MAP1_COLOR_4=_C('GL_MAP1_COLOR_4',0x0D90)
GL_MAP1_GRID_DOMAIN=_C('GL_MAP1_GRID_DOMAIN',0x0DD0)
GL_MAP1_GRID_SEGMENTS=_C('GL_MAP1_GRID_SEGMENTS',0x0DD1)
GL_MAP1_INDEX=_C('GL_MAP1_INDEX',0x0D91)
GL_MAP1_NORMAL=_C('GL_MAP1_NORMAL',0x0D92)
GL_MAP1_TEXTURE_COORD_1=_C('GL_MAP1_TEXTURE_COORD_1',0x0D93)
GL_MAP1_TEXTURE_COORD_2=_C('GL_MAP1_TEXTURE_COORD_2',0x0D94)
GL_MAP1_TEXTURE_COORD_3=_C('GL_MAP1_TEXTURE_COORD_3',0x0D95)
GL_MAP1_TEXTURE_COORD_4=_C('GL_MAP1_TEXTURE_COORD_4',0x0D96)
GL_MAP1_VERTEX_3=_C('GL_MAP1_VERTEX_3',0x0D97)
GL_MAP1_VERTEX_4=_C('GL_MAP1_VERTEX_4',0x0D98)
GL_MAP2_COLOR_4=_C('GL_MAP2_COLOR_4',0x0DB0)
GL_MAP2_GRID_DOMAIN=_C('GL_MAP2_GRID_DOMAIN',0x0DD2)
GL_MAP2_GRID_SEGMENTS=_C('GL_MAP2_GRID_SEGMENTS',0x0DD3)
GL_MAP2_INDEX=_C('GL_MAP2_INDEX',0x0DB1)
GL_MAP2_NORMAL=_C('GL_MAP2_NORMAL',0x0DB2)
GL_MAP2_TEXTURE_COORD_1=_C('GL_MAP2_TEXTURE_COORD_1',0x0DB3)
GL_MAP2_TEXTURE_COORD_2=_C('GL_MAP2_TEXTURE_COORD_2',0x0DB4)
GL_MAP2_TEXTURE_COORD_3=_C('GL_MAP2_TEXTURE_COORD_3',0x0DB5)
GL_MAP2_TEXTURE_COORD_4=_C('GL_MAP2_TEXTURE_COORD_4',0x0DB6)
GL_MAP2_VERTEX_3=_C('GL_MAP2_VERTEX_3',0x0DB7)
GL_MAP2_VERTEX_4=_C('GL_MAP2_VERTEX_4',0x0DB8)
GL_MAP_COLOR=_C('GL_MAP_COLOR',0x0D10)
GL_MAP_STENCIL=_C('GL_MAP_STENCIL',0x0D11)
GL_MATRIX_MODE=_C('GL_MATRIX_MODE',0x0BA0)
GL_MAX_ATTRIB_STACK_DEPTH=_C('GL_MAX_ATTRIB_STACK_DEPTH',0x0D35)
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH=_C('GL_MAX_CLIENT_ATTRIB_STACK_DEPTH',0x0D3B)
GL_MAX_CLIP_PLANES=_C('GL_MAX_CLIP_PLANES',0x0D32)
GL_MAX_EVAL_ORDER=_C('GL_MAX_EVAL_ORDER',0x0D30)
GL_MAX_LIGHTS=_C('GL_MAX_LIGHTS',0x0D31)
GL_MAX_LIST_NESTING=_C('GL_MAX_LIST_NESTING',0x0B31)
GL_MAX_MODELVIEW_STACK_DEPTH=_C('GL_MAX_MODELVIEW_STACK_DEPTH',0x0D36)
GL_MAX_NAME_STACK_DEPTH=_C('GL_MAX_NAME_STACK_DEPTH',0x0D37)
GL_MAX_PIXEL_MAP_TABLE=_C('GL_MAX_PIXEL_MAP_TABLE',0x0D34)
GL_MAX_PROJECTION_STACK_DEPTH=_C('GL_MAX_PROJECTION_STACK_DEPTH',0x0D38)
GL_MAX_TEXTURE_SIZE=_C('GL_MAX_TEXTURE_SIZE',0x0D33)
GL_MAX_TEXTURE_STACK_DEPTH=_C('GL_MAX_TEXTURE_STACK_DEPTH',0x0D39)
GL_MAX_VIEWPORT_DIMS=_C('GL_MAX_VIEWPORT_DIMS',0x0D3A)
GL_MODELVIEW=_C('GL_MODELVIEW',0x1700)
GL_MODELVIEW_MATRIX=_C('GL_MODELVIEW_MATRIX',0x0BA6)
GL_MODELVIEW_STACK_DEPTH=_C('GL_MODELVIEW_STACK_DEPTH',0x0BA3)
GL_MODULATE=_C('GL_MODULATE',0x2100)
GL_MULT=_C('GL_MULT',0x0103)
GL_N3F_V3F=_C('GL_N3F_V3F',0x2A25)
GL_NAME_STACK_DEPTH=_C('GL_NAME_STACK_DEPTH',0x0D70)
GL_NAND=_C('GL_NAND',0x150E)
GL_NEAREST=_C('GL_NEAREST',0x2600)
GL_NEAREST_MIPMAP_LINEAR=_C('GL_NEAREST_MIPMAP_LINEAR',0x2702)
GL_NEAREST_MIPMAP_NEAREST=_C('GL_NEAREST_MIPMAP_NEAREST',0x2700)
GL_NEVER=_C('GL_NEVER',0x0200)
GL_NICEST=_C('GL_NICEST',0x1102)
GL_NONE=_C('GL_NONE',0)
GL_NOOP=_C('GL_NOOP',0x1505)
GL_NOR=_C('GL_NOR',0x1508)
GL_NORMALIZE=_C('GL_NORMALIZE',0x0BA1)
GL_NORMAL_ARRAY=_C('GL_NORMAL_ARRAY',0x8075)
GL_NORMAL_ARRAY_POINTER=_C('GL_NORMAL_ARRAY_POINTER',0x808F)
GL_NORMAL_ARRAY_STRIDE=_C('GL_NORMAL_ARRAY_STRIDE',0x807F)
GL_NORMAL_ARRAY_TYPE=_C('GL_NORMAL_ARRAY_TYPE',0x807E)
GL_NOTEQUAL=_C('GL_NOTEQUAL',0x0205)
GL_NO_ERROR=_C('GL_NO_ERROR',0)
GL_OBJECT_LINEAR=_C('GL_OBJECT_LINEAR',0x2401)
GL_OBJECT_PLANE=_C('GL_OBJECT_PLANE',0x2501)
GL_ONE=_C('GL_ONE',1)
GL_ONE_MINUS_DST_ALPHA=_C('GL_ONE_MINUS_DST_ALPHA',0x0305)
GL_ONE_MINUS_DST_COLOR=_C('GL_ONE_MINUS_DST_COLOR',0x0307)
GL_ONE_MINUS_SRC_ALPHA=_C('GL_ONE_MINUS_SRC_ALPHA',0x0303)
GL_ONE_MINUS_SRC_COLOR=_C('GL_ONE_MINUS_SRC_COLOR',0x0301)
GL_OR=_C('GL_OR',0x1507)
GL_ORDER=_C('GL_ORDER',0x0A01)
GL_OR_INVERTED=_C('GL_OR_INVERTED',0x150D)
GL_OR_REVERSE=_C('GL_OR_REVERSE',0x150B)
GL_OUT_OF_MEMORY=_C('GL_OUT_OF_MEMORY',0x0505)
GL_PACK_ALIGNMENT=_C('GL_PACK_ALIGNMENT',0x0D05)
GL_PACK_LSB_FIRST=_C('GL_PACK_LSB_FIRST',0x0D01)
GL_PACK_ROW_LENGTH=_C('GL_PACK_ROW_LENGTH',0x0D02)
GL_PACK_SKIP_PIXELS=_C('GL_PACK_SKIP_PIXELS',0x0D04)
GL_PACK_SKIP_ROWS=_C('GL_PACK_SKIP_ROWS',0x0D03)
GL_PACK_SWAP_BYTES=_C('GL_PACK_SWAP_BYTES',0x0D00)
GL_PASS_THROUGH_TOKEN=_C('GL_PASS_THROUGH_TOKEN',0x0700)
GL_PERSPECTIVE_CORRECTION_HINT=_C('GL_PERSPECTIVE_CORRECTION_HINT',0x0C50)
GL_PIXEL_MAP_A_TO_A=_C('GL_PIXEL_MAP_A_TO_A',0x0C79)
GL_PIXEL_MAP_A_TO_A_SIZE=_C('GL_PIXEL_MAP_A_TO_A_SIZE',0x0CB9)
GL_PIXEL_MAP_B_TO_B=_C('GL_PIXEL_MAP_B_TO_B',0x0C78)
GL_PIXEL_MAP_B_TO_B_SIZE=_C('GL_PIXEL_MAP_B_TO_B_SIZE',0x0CB8)
GL_PIXEL_MAP_G_TO_G=_C('GL_PIXEL_MAP_G_TO_G',0x0C77)
GL_PIXEL_MAP_G_TO_G_SIZE=_C('GL_PIXEL_MAP_G_TO_G_SIZE',0x0CB7)
GL_PIXEL_MAP_I_TO_A=_C('GL_PIXEL_MAP_I_TO_A',0x0C75)
GL_PIXEL_MAP_I_TO_A_SIZE=_C('GL_PIXEL_MAP_I_TO_A_SIZE',0x0CB5)
GL_PIXEL_MAP_I_TO_B=_C('GL_PIXEL_MAP_I_TO_B',0x0C74)
GL_PIXEL_MAP_I_TO_B_SIZE=_C('GL_PIXEL_MAP_I_TO_B_SIZE',0x0CB4)
GL_PIXEL_MAP_I_TO_G=_C('GL_PIXEL_MAP_I_TO_G',0x0C73)
GL_PIXEL_MAP_I_TO_G_SIZE=_C('GL_PIXEL_MAP_I_TO_G_SIZE',0x0CB3)
GL_PIXEL_MAP_I_TO_I=_C('GL_PIXEL_MAP_I_TO_I',0x0C70)
GL_PIXEL_MAP_I_TO_I_SIZE=_C('GL_PIXEL_MAP_I_TO_I_SIZE',0x0CB0)
GL_PIXEL_MAP_I_TO_R=_C('GL_PIXEL_MAP_I_TO_R',0x0C72)
GL_PIXEL_MAP_I_TO_R_SIZE=_C('GL_PIXEL_MAP_I_TO_R_SIZE',0x0CB2)
GL_PIXEL_MAP_R_TO_R=_C('GL_PIXEL_MAP_R_TO_R',0x0C76)
GL_PIXEL_MAP_R_TO_R_SIZE=_C('GL_PIXEL_MAP_R_TO_R_SIZE',0x0CB6)
GL_PIXEL_MAP_S_TO_S=_C('GL_PIXEL_MAP_S_TO_S',0x0C71)
GL_PIXEL_MAP_S_TO_S_SIZE=_C('GL_PIXEL_MAP_S_TO_S_SIZE',0x0CB1)
GL_PIXEL_MODE_BIT=_C('GL_PIXEL_MODE_BIT',0x00000020)
GL_POINT=_C('GL_POINT',0x1B00)
GL_POINTS=_C('GL_POINTS',0x0000)
GL_POINT_BIT=_C('GL_POINT_BIT',0x00000002)
GL_POINT_SIZE=_C('GL_POINT_SIZE',0x0B11)
GL_POINT_SIZE_GRANULARITY=_C('GL_POINT_SIZE_GRANULARITY',0x0B13)
GL_POINT_SIZE_RANGE=_C('GL_POINT_SIZE_RANGE',0x0B12)
GL_POINT_SMOOTH=_C('GL_POINT_SMOOTH',0x0B10)
GL_POINT_SMOOTH_HINT=_C('GL_POINT_SMOOTH_HINT',0x0C51)
GL_POINT_TOKEN=_C('GL_POINT_TOKEN',0x0701)
GL_POLYGON=_C('GL_POLYGON',0x0009)
GL_POLYGON_BIT=_C('GL_POLYGON_BIT',0x00000008)
GL_POLYGON_MODE=_C('GL_POLYGON_MODE',0x0B40)
GL_POLYGON_OFFSET_FACTOR=_C('GL_POLYGON_OFFSET_FACTOR',0x8038)
GL_POLYGON_OFFSET_FILL=_C('GL_POLYGON_OFFSET_FILL',0x8037)
GL_POLYGON_OFFSET_LINE=_C('GL_POLYGON_OFFSET_LINE',0x2A02)
GL_POLYGON_OFFSET_POINT=_C('GL_POLYGON_OFFSET_POINT',0x2A01)
GL_POLYGON_OFFSET_UNITS=_C('GL_POLYGON_OFFSET_UNITS',0x2A00)
GL_POLYGON_SMOOTH=_C('GL_POLYGON_SMOOTH',0x0B41)
GL_POLYGON_SMOOTH_HINT=_C('GL_POLYGON_SMOOTH_HINT',0x0C53)
GL_POLYGON_STIPPLE=_C('GL_POLYGON_STIPPLE',0x0B42)
GL_POLYGON_STIPPLE_BIT=_C('GL_POLYGON_STIPPLE_BIT',0x00000010)
GL_POLYGON_TOKEN=_C('GL_POLYGON_TOKEN',0x0703)
GL_POSITION=_C('GL_POSITION',0x1203)
GL_PROJECTION=_C('GL_PROJECTION',0x1701)
GL_PROJECTION_MATRIX=_C('GL_PROJECTION_MATRIX',0x0BA7)
GL_PROJECTION_STACK_DEPTH=_C('GL_PROJECTION_STACK_DEPTH',0x0BA4)
GL_PROXY_TEXTURE_1D=_C('GL_PROXY_TEXTURE_1D',0x8063)
GL_PROXY_TEXTURE_2D=_C('GL_PROXY_TEXTURE_2D',0x8064)
GL_Q=_C('GL_Q',0x2003)
GL_QUADRATIC_ATTENUATION=_C('GL_QUADRATIC_ATTENUATION',0x1209)
GL_QUADS=_C('GL_QUADS',0x0007)
GL_QUAD_STRIP=_C('GL_QUAD_STRIP',0x0008)
GL_R=_C('GL_R',0x2002)
GL_R3_G3_B2=_C('GL_R3_G3_B2',0x2A10)
GL_READ_BUFFER=_C('GL_READ_BUFFER',0x0C02)
GL_RED=_C('GL_RED',0x1903)
GL_RED_BIAS=_C('GL_RED_BIAS',0x0D15)
GL_RED_BITS=_C('GL_RED_BITS',0x0D52)
GL_RED_SCALE=_C('GL_RED_SCALE',0x0D14)
GL_RENDER=_C('GL_RENDER',0x1C00)
GL_RENDERER=_C('GL_RENDERER',0x1F01)
GL_RENDER_MODE=_C('GL_RENDER_MODE',0x0C40)
GL_REPEAT=_C('GL_REPEAT',0x2901)
GL_REPLACE=_C('GL_REPLACE',0x1E01)
GL_RETURN=_C('GL_RETURN',0x0102)
GL_RGB=_C('GL_RGB',0x1907)
GL_RGB10=_C('GL_RGB10',0x8052)
GL_RGB10_A2=_C('GL_RGB10_A2',0x8059)
GL_RGB12=_C('GL_RGB12',0x8053)
GL_RGB16=_C('GL_RGB16',0x8054)
GL_RGB4=_C('GL_RGB4',0x804F)
GL_RGB5=_C('GL_RGB5',0x8050)
GL_RGB5_A1=_C('GL_RGB5_A1',0x8057)
GL_RGB8=_C('GL_RGB8',0x8051)
GL_RGBA=_C('GL_RGBA',0x1908)
GL_RGBA12=_C('GL_RGBA12',0x805A)
GL_RGBA16=_C('GL_RGBA16',0x805B)
GL_RGBA2=_C('GL_RGBA2',0x8055)
GL_RGBA4=_C('GL_RGBA4',0x8056)
GL_RGBA8=_C('GL_RGBA8',0x8058)
GL_RGBA_MODE=_C('GL_RGBA_MODE',0x0C31)
GL_RIGHT=_C('GL_RIGHT',0x0407)
GL_S=_C('GL_S',0x2000)
GL_SCISSOR_BIT=_C('GL_SCISSOR_BIT',0x00080000)
GL_SCISSOR_BOX=_C('GL_SCISSOR_BOX',0x0C10)
GL_SCISSOR_TEST=_C('GL_SCISSOR_TEST',0x0C11)
GL_SELECT=_C('GL_SELECT',0x1C02)
GL_SELECTION_BUFFER_POINTER=_C('GL_SELECTION_BUFFER_POINTER',0x0DF3)
GL_SELECTION_BUFFER_SIZE=_C('GL_SELECTION_BUFFER_SIZE',0x0DF4)
GL_SET=_C('GL_SET',0x150F)
GL_SHADE_MODEL=_C('GL_SHADE_MODEL',0x0B54)
GL_SHININESS=_C('GL_SHININESS',0x1601)
GL_SHORT=_C('GL_SHORT',0x1402)
GL_SMOOTH=_C('GL_SMOOTH',0x1D01)
GL_SPECULAR=_C('GL_SPECULAR',0x1202)
GL_SPHERE_MAP=_C('GL_SPHERE_MAP',0x2402)
GL_SPOT_CUTOFF=_C('GL_SPOT_CUTOFF',0x1206)
GL_SPOT_DIRECTION=_C('GL_SPOT_DIRECTION',0x1204)
GL_SPOT_EXPONENT=_C('GL_SPOT_EXPONENT',0x1205)
GL_SRC_ALPHA=_C('GL_SRC_ALPHA',0x0302)
GL_SRC_ALPHA_SATURATE=_C('GL_SRC_ALPHA_SATURATE',0x0308)
GL_SRC_COLOR=_C('GL_SRC_COLOR',0x0300)
GL_STACK_OVERFLOW=_C('GL_STACK_OVERFLOW',0x0503)
GL_STACK_UNDERFLOW=_C('GL_STACK_UNDERFLOW',0x0504)
GL_STENCIL=_C('GL_STENCIL',0x1802)
GL_STENCIL_BITS=_C('GL_STENCIL_BITS',0x0D57)
GL_STENCIL_BUFFER_BIT=_C('GL_STENCIL_BUFFER_BIT',0x00000400)
GL_STENCIL_CLEAR_VALUE=_C('GL_STENCIL_CLEAR_VALUE',0x0B91)
GL_STENCIL_FAIL=_C('GL_STENCIL_FAIL',0x0B94)
GL_STENCIL_FUNC=_C('GL_STENCIL_FUNC',0x0B92)
GL_STENCIL_INDEX=_C('GL_STENCIL_INDEX',0x1901)
GL_STENCIL_PASS_DEPTH_FAIL=_C('GL_STENCIL_PASS_DEPTH_FAIL',0x0B95)
GL_STENCIL_PASS_DEPTH_PASS=_C('GL_STENCIL_PASS_DEPTH_PASS',0x0B96)
GL_STENCIL_REF=_C('GL_STENCIL_REF',0x0B97)
GL_STENCIL_TEST=_C('GL_STENCIL_TEST',0x0B90)
GL_STENCIL_VALUE_MASK=_C('GL_STENCIL_VALUE_MASK',0x0B93)
GL_STENCIL_WRITEMASK=_C('GL_STENCIL_WRITEMASK',0x0B98)
GL_STEREO=_C('GL_STEREO',0x0C33)
GL_SUBPIXEL_BITS=_C('GL_SUBPIXEL_BITS',0x0D50)
GL_T=_C('GL_T',0x2001)
GL_T2F_C3F_V3F=_C('GL_T2F_C3F_V3F',0x2A2A)
GL_T2F_C4F_N3F_V3F=_C('GL_T2F_C4F_N3F_V3F',0x2A2C)
GL_T2F_C4UB_V3F=_C('GL_T2F_C4UB_V3F',0x2A29)
GL_T2F_N3F_V3F=_C('GL_T2F_N3F_V3F',0x2A2B)
GL_T2F_V3F=_C('GL_T2F_V3F',0x2A27)
GL_T4F_C4F_N3F_V4F=_C('GL_T4F_C4F_N3F_V4F',0x2A2D)
GL_T4F_V4F=_C('GL_T4F_V4F',0x2A28)
GL_TEXTURE=_C('GL_TEXTURE',0x1702)
GL_TEXTURE_1D=_C('GL_TEXTURE_1D',0x0DE0)
GL_TEXTURE_2D=_C('GL_TEXTURE_2D',0x0DE1)
GL_TEXTURE_ALPHA_SIZE=_C('GL_TEXTURE_ALPHA_SIZE',0x805F)
GL_TEXTURE_BINDING_1D=_C('GL_TEXTURE_BINDING_1D',0x8068)
GL_TEXTURE_BINDING_2D=_C('GL_TEXTURE_BINDING_2D',0x8069)
GL_TEXTURE_BIT=_C('GL_TEXTURE_BIT',0x00040000)
GL_TEXTURE_BLUE_SIZE=_C('GL_TEXTURE_BLUE_SIZE',0x805E)
GL_TEXTURE_BORDER=_C('GL_TEXTURE_BORDER',0x1005)
GL_TEXTURE_BORDER_COLOR=_C('GL_TEXTURE_BORDER_COLOR',0x1004)
GL_TEXTURE_COMPONENTS=_C('GL_TEXTURE_COMPONENTS',0x1003)
GL_TEXTURE_COORD_ARRAY=_C('GL_TEXTURE_COORD_ARRAY',0x8078)
GL_TEXTURE_COORD_ARRAY_POINTER=_C('GL_TEXTURE_COORD_ARRAY_POINTER',0x8092)
GL_TEXTURE_COORD_ARRAY_SIZE=_C('GL_TEXTURE_COORD_ARRAY_SIZE',0x8088)
GL_TEXTURE_COORD_ARRAY_STRIDE=_C('GL_TEXTURE_COORD_ARRAY_STRIDE',0x808A)
GL_TEXTURE_COORD_ARRAY_TYPE=_C('GL_TEXTURE_COORD_ARRAY_TYPE',0x8089)
GL_TEXTURE_ENV=_C('GL_TEXTURE_ENV',0x2300)
GL_TEXTURE_ENV_COLOR=_C('GL_TEXTURE_ENV_COLOR',0x2201)
GL_TEXTURE_ENV_MODE=_C('GL_TEXTURE_ENV_MODE',0x2200)
GL_TEXTURE_GEN_MODE=_C('GL_TEXTURE_GEN_MODE',0x2500)
GL_TEXTURE_GEN_Q=_C('GL_TEXTURE_GEN_Q',0x0C63)
GL_TEXTURE_GEN_R=_C('GL_TEXTURE_GEN_R',0x0C62)
GL_TEXTURE_GEN_S=_C('GL_TEXTURE_GEN_S',0x0C60)
GL_TEXTURE_GEN_T=_C('GL_TEXTURE_GEN_T',0x0C61)
GL_TEXTURE_GREEN_SIZE=_C('GL_TEXTURE_GREEN_SIZE',0x805D)
GL_TEXTURE_HEIGHT=_C('GL_TEXTURE_HEIGHT',0x1001)
GL_TEXTURE_INTENSITY_SIZE=_C('GL_TEXTURE_INTENSITY_SIZE',0x8061)
GL_TEXTURE_INTERNAL_FORMAT=_C('GL_TEXTURE_INTERNAL_FORMAT',0x1003)
GL_TEXTURE_LUMINANCE_SIZE=_C('GL_TEXTURE_LUMINANCE_SIZE',0x8060)
GL_TEXTURE_MAG_FILTER=_C('GL_TEXTURE_MAG_FILTER',0x2800)
GL_TEXTURE_MATRIX=_C('GL_TEXTURE_MATRIX',0x0BA8)
GL_TEXTURE_MIN_FILTER=_C('GL_TEXTURE_MIN_FILTER',0x2801)
GL_TEXTURE_PRIORITY=_C('GL_TEXTURE_PRIORITY',0x8066)
GL_TEXTURE_RED_SIZE=_C('GL_TEXTURE_RED_SIZE',0x805C)
GL_TEXTURE_RESIDENT=_C('GL_TEXTURE_RESIDENT',0x8067)
GL_TEXTURE_STACK_DEPTH=_C('GL_TEXTURE_STACK_DEPTH',0x0BA5)
GL_TEXTURE_WIDTH=_C('GL_TEXTURE_WIDTH',0x1000)
GL_TEXTURE_WRAP_S=_C('GL_TEXTURE_WRAP_S',0x2802)
GL_TEXTURE_WRAP_T=_C('GL_TEXTURE_WRAP_T',0x2803)
GL_TRANSFORM_BIT=_C('GL_TRANSFORM_BIT',0x00001000)
GL_TRIANGLES=_C('GL_TRIANGLES',0x0004)
GL_TRIANGLE_FAN=_C('GL_TRIANGLE_FAN',0x0006)
GL_TRIANGLE_STRIP=_C('GL_TRIANGLE_STRIP',0x0005)
GL_TRUE=_C('GL_TRUE',1)
GL_UNPACK_ALIGNMENT=_C('GL_UNPACK_ALIGNMENT',0x0CF5)
GL_UNPACK_LSB_FIRST=_C('GL_UNPACK_LSB_FIRST',0x0CF1)
GL_UNPACK_ROW_LENGTH=_C('GL_UNPACK_ROW_LENGTH',0x0CF2)
GL_UNPACK_SKIP_PIXELS=_C('GL_UNPACK_SKIP_PIXELS',0x0CF4)
GL_UNPACK_SKIP_ROWS=_C('GL_UNPACK_SKIP_ROWS',0x0CF3)
GL_UNPACK_SWAP_BYTES=_C('GL_UNPACK_SWAP_BYTES',0x0CF0)
GL_UNSIGNED_BYTE=_C('GL_UNSIGNED_BYTE',0x1401)
GL_UNSIGNED_INT=_C('GL_UNSIGNED_INT',0x1405)
GL_UNSIGNED_SHORT=_C('GL_UNSIGNED_SHORT',0x1403)
GL_V2F=_C('GL_V2F',0x2A20)
GL_V3F=_C('GL_V3F',0x2A21)
GL_VENDOR=_C('GL_VENDOR',0x1F00)
GL_VERSION=_C('GL_VERSION',0x1F02)
GL_VERTEX_ARRAY=_C('GL_VERTEX_ARRAY',0x8074)
GL_VERTEX_ARRAY_POINTER=_C('GL_VERTEX_ARRAY_POINTER',0x808E)
GL_VERTEX_ARRAY_SIZE=_C('GL_VERTEX_ARRAY_SIZE',0x807A)
GL_VERTEX_ARRAY_STRIDE=_C('GL_VERTEX_ARRAY_STRIDE',0x807C)
GL_VERTEX_ARRAY_TYPE=_C('GL_VERTEX_ARRAY_TYPE',0x807B)
GL_VIEWPORT=_C('GL_VIEWPORT',0x0BA2)
GL_VIEWPORT_BIT=_C('GL_VIEWPORT_BIT',0x00000800)
GL_XOR=_C('GL_XOR',0x1506)
GL_ZERO=_C('GL_ZERO',0)
GL_ZOOM_X=_C('GL_ZOOM_X',0x0D16)
GL_ZOOM_Y=_C('GL_ZOOM_Y',0x0D17)
@_f
@_p.types(_cs.GLboolean,_cs.GLsizei,arrays.GLuintArray,arrays.GLbooleanArray)
def glAreTexturesResident(n,textures,residences):pass
@_f
@_p.types(None,_cs.GLint)
def glArrayElement(i):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindTexture(target,texture):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glColorPointer(size,type,stride,pointer):pass
# Calculate length of pointer from type:ColorPointerType
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLint)
def glCopyTexImage1D(target,level,internalformat,x,y,width,border):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLint)
def glCopyTexImage2D(target,level,internalformat,x,y,width,height,border):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyTexSubImage1D(target,level,xoffset,x,y,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTexSubImage2D(target,level,xoffset,yoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteTextures(n,textures):pass
@_f
@_p.types(None,_cs.GLenum)
def glDisableClientState(array):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei)
def glDrawArrays(mode,first,count):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glDrawElements(mode,count,type,indices):pass
# Calculate length of indices from type:DrawElementsType
@_f
@_p.types(None,_cs.GLsizei,ctypes.c_void_p)
def glEdgeFlagPointer(stride,pointer):pass
@_f
@_p.types(None,_cs.GLenum)
def glEnableClientState(array):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenTextures(n,textures):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLvoidpArray)
def glGetPointerv(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glIndexPointer(type,stride,pointer):pass
# Calculate length of pointer from type:IndexPointerType
@_f
@_p.types(None,_cs.GLubyte)
def glIndexub(c):pass
@_f
@_p.types(None,arrays.GLubyteArray)
def glIndexubv(c):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glInterleavedArrays(format,stride,pointer):pass
# Calculate length of pointer from format:InterleavedArrayFormat
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsTexture(texture):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glNormalPointer(type,stride,pointer):pass
# Calculate length of pointer from type:NormalPointerType
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glPolygonOffset(factor,units):pass
@_f
@_p.types(None,)
def glPopClientAttrib():pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray,arrays.GLfloatArray)
def glPrioritizeTextures(n,textures,priorities):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glPushClientAttrib(mask):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glTexCoordPointer(size,type,stride,pointer):pass
# Calculate length of pointer from type:TexCoordPointerType
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage1D(target,level,xoffset,width,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage2D(target,level,xoffset,yoffset,width,height,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexPointer(size,type,stride,pointer):pass
# Calculate length of pointer from type:VertexPointerType
