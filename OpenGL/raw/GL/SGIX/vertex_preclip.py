'''OpenGL extension SGIX.vertex_preclip

Overview (from the spec)
	
	Certain graphics subsystems are capable of performing fast
	2D viewport or, in some cases, 3D volume "scissoring" operations
	within some coordinate range much faster that the host CPU could
	re-tesselate clipped primitives.
	
	This extension introduces the notion of an extended rasterizable view
	volume that is an expansion of the clip-space view volume.	This volume
	is the space within which a particular graphics system is much more
	efficient at rejecting fragments that lie outside the view volume than
	it is at performing strict view volume clipping.
	
	Clip-checking can be turned on or off through the glEnable/glDisable
	mechanism, and can be further controlled by using glHint.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/vertex_preclip.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_vertex_preclip'
_DEPRECATED = False
GL_VERTEX_PRECLIP_SGIX = constant.Constant( 'GL_VERTEX_PRECLIP_SGIX', 0x83EE )
GL_VERTEX_PRECLIP_HINT_SGIX = constant.Constant( 'GL_VERTEX_PRECLIP_HINT_SGIX', 0x83EF )


def glInitVertexPreclipSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
