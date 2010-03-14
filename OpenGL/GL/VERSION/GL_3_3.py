'''OpenGL extension VERSION.GL_3_3

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_3_3 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_3_3.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_3_3 import *
### END AUTOGENERATED SECTION