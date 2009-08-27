'''OpenGL extension EXT.stencil_two_side

Overview (from the spec)
	
	This extension provides two-sided stencil testing where the
	stencil-related state (stencil operations, reference value, compare
	mask, and write mask) may be different for front- and back-facing
	polygons.  Two-sided stencil testing may improve the performance
	of stenciled shadow volume and Constructive Solid Geometry (CSG)
	rendering algorithms.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/stencil_two_side.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_stencil_two_side'
_DEPRECATED = False
GL_STENCIL_TEST_TWO_SIDE_EXT = constant.Constant( 'GL_STENCIL_TEST_TWO_SIDE_EXT', 0x8910 )
glget.addGLGetConstant( GL_STENCIL_TEST_TWO_SIDE_EXT, (1,) )
GL_ACTIVE_STENCIL_FACE_EXT = constant.Constant( 'GL_ACTIVE_STENCIL_FACE_EXT', 0x8911 )
glget.addGLGetConstant( GL_ACTIVE_STENCIL_FACE_EXT, (1,) )
glActiveStencilFaceEXT = platform.createExtensionFunction( 
	'glActiveStencilFaceEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum,),
	doc = 'glActiveStencilFaceEXT( GLenum(face) ) -> None',
	argNames = ('face',),
	deprecated = _DEPRECATED,
)


def glInitStencilTwoSideEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
