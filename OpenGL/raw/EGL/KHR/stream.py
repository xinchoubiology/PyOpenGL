'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_KHR_stream'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_KHR_stream')
EGL_BAD_STATE_KHR=_C('EGL_BAD_STATE_KHR',0x321C)
EGL_BAD_STREAM_KHR=_C('EGL_BAD_STREAM_KHR',0x321B)
EGL_CONSUMER_FRAME_KHR=_C('EGL_CONSUMER_FRAME_KHR',0x3213)
EGL_CONSUMER_LATENCY_USEC_KHR=_C('EGL_CONSUMER_LATENCY_USEC_KHR',0x3210)
# EGL_NO_STREAM_KHR=_C('EGL_NO_STREAM_KHR',((EGLStreamKHR)0))
EGL_PRODUCER_FRAME_KHR=_C('EGL_PRODUCER_FRAME_KHR',0x3212)
EGL_STREAM_STATE_CONNECTING_KHR=_C('EGL_STREAM_STATE_CONNECTING_KHR',0x3216)
EGL_STREAM_STATE_CREATED_KHR=_C('EGL_STREAM_STATE_CREATED_KHR',0x3215)
EGL_STREAM_STATE_DISCONNECTED_KHR=_C('EGL_STREAM_STATE_DISCONNECTED_KHR',0x321A)
EGL_STREAM_STATE_EMPTY_KHR=_C('EGL_STREAM_STATE_EMPTY_KHR',0x3217)
EGL_STREAM_STATE_KHR=_C('EGL_STREAM_STATE_KHR',0x3214)
EGL_STREAM_STATE_NEW_FRAME_AVAILABLE_KHR=_C('EGL_STREAM_STATE_NEW_FRAME_AVAILABLE_KHR',0x3218)
EGL_STREAM_STATE_OLD_FRAME_AVAILABLE_KHR=_C('EGL_STREAM_STATE_OLD_FRAME_AVAILABLE_KHR',0x3219)
@_f
@_p.types(_cs.EGLStreamKHR,_cs.EGLDisplay,arrays.GLintArray)
def eglCreateStreamKHR(dpy,attrib_list):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLStreamKHR)
def eglDestroyStreamKHR(dpy,stream):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLStreamKHR,_cs.EGLenum,arrays.GLintArray)
def eglQueryStreamKHR(dpy,stream,attribute,value):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLStreamKHR,_cs.EGLenum,arrays.GLuint64Array)
def eglQueryStreamu64KHR(dpy,stream,attribute,value):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLStreamKHR,_cs.EGLenum,_cs.EGLint)
def eglStreamAttribKHR(dpy,stream,attribute,value):pass
