'''OpenGL extension EXT.index_texture

Overview (from the spec)
	
	This extends the definition of texturing so that it is supported
	in color index mode.  This extension builds on the notion of
	texture images which have color index internal formats which was
	introduced in EXT_paletted_texture.
	
	This extension also introduces a new texture environment function
	ADD which is useful for combining lighting and texturing in
	color index mode.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/index_texture.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_index_texture'
_DEPRECATED = False



def glInitIndexTextureEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
