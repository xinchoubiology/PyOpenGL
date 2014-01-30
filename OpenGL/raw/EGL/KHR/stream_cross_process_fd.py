'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_KHR_stream_cross_process_fd'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_KHR_stream_cross_process_fd')
# EGL_NO_FILE_DESCRIPTOR_KHR=_C('EGL_NO_FILE_DESCRIPTOR_KHR',((EGLNativeFileDescriptorKHR)(-1)))
@_f
@_p.types(_cs.EGLStreamKHR,_cs.EGLDisplay,_cs.EGLNativeFileDescriptorKHR)
def eglCreateStreamFromFileDescriptorKHR(dpy,file_descriptor):pass
@_f
@_p.types(_cs.EGLNativeFileDescriptorKHR,_cs.EGLDisplay,_cs.EGLStreamKHR)
def eglGetStreamFileDescriptorKHR(dpy,stream):pass
