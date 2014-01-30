'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_VERSION_EGL_1_3'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_VERSION_EGL_1_3')
EGL_CONFORMANT=_C('EGL_CONFORMANT',0x3042)
EGL_CONTEXT_CLIENT_VERSION=_C('EGL_CONTEXT_CLIENT_VERSION',0x3098)
EGL_MATCH_NATIVE_PIXMAP=_C('EGL_MATCH_NATIVE_PIXMAP',0x3041)
EGL_OPENGL_ES2_BIT=_C('EGL_OPENGL_ES2_BIT',0x0004)
EGL_VG_ALPHA_FORMAT=_C('EGL_VG_ALPHA_FORMAT',0x3088)
EGL_VG_ALPHA_FORMAT_NONPRE=_C('EGL_VG_ALPHA_FORMAT_NONPRE',0x308B)
EGL_VG_ALPHA_FORMAT_PRE=_C('EGL_VG_ALPHA_FORMAT_PRE',0x308C)
EGL_VG_ALPHA_FORMAT_PRE_BIT=_C('EGL_VG_ALPHA_FORMAT_PRE_BIT',0x0040)
EGL_VG_COLORSPACE=_C('EGL_VG_COLORSPACE',0x3087)
EGL_VG_COLORSPACE_LINEAR=_C('EGL_VG_COLORSPACE_LINEAR',0x308A)
EGL_VG_COLORSPACE_LINEAR_BIT=_C('EGL_VG_COLORSPACE_LINEAR_BIT',0x0020)
EGL_VG_COLORSPACE_sRGB=_C('EGL_VG_COLORSPACE_sRGB',0x3089)

