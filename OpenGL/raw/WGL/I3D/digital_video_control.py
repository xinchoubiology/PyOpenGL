'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_I3D_digital_video_control'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_I3D_digital_video_control')
WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D=_C('WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D',0x2050)
WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D=_C('WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D',0x2051)
WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D=_C('WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D',0x2052)
WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D=_C('WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D',0x2053)
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.c_int,ctypes.POINTER(_cs.c_int))
def wglGetDigitalVideoParametersI3D(hDC,iAttribute,piValue):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.c_int,ctypes.POINTER(_cs.c_int))
def wglSetDigitalVideoParametersI3D(hDC,iAttribute,piValue):pass
