'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_EXT_image_dma_buf_import'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_EXT_image_dma_buf_import')
EGL_DMA_BUF_PLANE0_FD_EXT=_C('EGL_DMA_BUF_PLANE0_FD_EXT',0x3272)
EGL_DMA_BUF_PLANE0_OFFSET_EXT=_C('EGL_DMA_BUF_PLANE0_OFFSET_EXT',0x3273)
EGL_DMA_BUF_PLANE0_PITCH_EXT=_C('EGL_DMA_BUF_PLANE0_PITCH_EXT',0x3274)
EGL_DMA_BUF_PLANE1_FD_EXT=_C('EGL_DMA_BUF_PLANE1_FD_EXT',0x3275)
EGL_DMA_BUF_PLANE1_OFFSET_EXT=_C('EGL_DMA_BUF_PLANE1_OFFSET_EXT',0x3276)
EGL_DMA_BUF_PLANE1_PITCH_EXT=_C('EGL_DMA_BUF_PLANE1_PITCH_EXT',0x3277)
EGL_DMA_BUF_PLANE2_FD_EXT=_C('EGL_DMA_BUF_PLANE2_FD_EXT',0x3278)
EGL_DMA_BUF_PLANE2_OFFSET_EXT=_C('EGL_DMA_BUF_PLANE2_OFFSET_EXT',0x3279)
EGL_DMA_BUF_PLANE2_PITCH_EXT=_C('EGL_DMA_BUF_PLANE2_PITCH_EXT',0x327A)
EGL_ITU_REC2020_EXT=_C('EGL_ITU_REC2020_EXT',0x3281)
EGL_ITU_REC601_EXT=_C('EGL_ITU_REC601_EXT',0x327F)
EGL_ITU_REC709_EXT=_C('EGL_ITU_REC709_EXT',0x3280)
EGL_LINUX_DMA_BUF_EXT=_C('EGL_LINUX_DMA_BUF_EXT',0x3270)
EGL_LINUX_DRM_FOURCC_EXT=_C('EGL_LINUX_DRM_FOURCC_EXT',0x3271)
EGL_SAMPLE_RANGE_HINT_EXT=_C('EGL_SAMPLE_RANGE_HINT_EXT',0x327C)
EGL_YUV_CHROMA_HORIZONTAL_SITING_HINT_EXT=_C('EGL_YUV_CHROMA_HORIZONTAL_SITING_HINT_EXT',0x327D)
EGL_YUV_CHROMA_SITING_0_5_EXT=_C('EGL_YUV_CHROMA_SITING_0_5_EXT',0x3285)
EGL_YUV_CHROMA_SITING_0_EXT=_C('EGL_YUV_CHROMA_SITING_0_EXT',0x3284)
EGL_YUV_CHROMA_VERTICAL_SITING_HINT_EXT=_C('EGL_YUV_CHROMA_VERTICAL_SITING_HINT_EXT',0x327E)
EGL_YUV_COLOR_SPACE_HINT_EXT=_C('EGL_YUV_COLOR_SPACE_HINT_EXT',0x327B)
EGL_YUV_FULL_RANGE_EXT=_C('EGL_YUV_FULL_RANGE_EXT',0x3282)
EGL_YUV_NARROW_RANGE_EXT=_C('EGL_YUV_NARROW_RANGE_EXT',0x3283)

