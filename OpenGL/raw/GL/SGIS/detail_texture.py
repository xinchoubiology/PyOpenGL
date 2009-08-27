'''OpenGL extension SGIS.detail_texture

Overview (from the spec)
	
	    This extension introduces texture magnification filters that blend
	    between the level 0 image and a separately defined "detail" image.
	    The detail image represents the characteristics of the high frequency
	    subband image above the band-limited level 0 image.  The detail image is
	    typically a rectangular portion of the subband image which is modified
	    so that it can be repeated without discontinuities along its edges.
	    Detail blending can be enabled for all color channels, for the alpha
	    channel only, or for the red, green, and blue channels only.  It is
	    available only for 2D textures.
	
	    WARNING - Silicon Graphics has filed for patent protection for some
		      of the techniques described in this extension document.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIS/detail_texture.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_detail_texture'
_DEPRECATED = False
GL_DETAIL_TEXTURE_2D_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_2D_SGIS', 0x8095 )
GL_DETAIL_TEXTURE_2D_BINDING_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_2D_BINDING_SGIS', 0x8096 )
GL_LINEAR_DETAIL_SGIS = constant.Constant( 'GL_LINEAR_DETAIL_SGIS', 0x8097 )
GL_LINEAR_DETAIL_ALPHA_SGIS = constant.Constant( 'GL_LINEAR_DETAIL_ALPHA_SGIS', 0x8098 )
GL_LINEAR_DETAIL_COLOR_SGIS = constant.Constant( 'GL_LINEAR_DETAIL_COLOR_SGIS', 0x8099 )
GL_DETAIL_TEXTURE_LEVEL_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_LEVEL_SGIS', 0x809A )
GL_DETAIL_TEXTURE_MODE_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_MODE_SGIS', 0x809B )
GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS', 0x809C )
glDetailTexFuncSGIS = platform.createExtensionFunction( 
	'glDetailTexFuncSGIS', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glDetailTexFuncSGIS( GLenum(target), GLsizei(n), GLfloatArray(points) ) -> None',
	argNames = ('target', 'n', 'points',),
	deprecated = _DEPRECATED,
)

glGetDetailTexFuncSGIS = platform.createExtensionFunction( 
	'glGetDetailTexFuncSGIS', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetDetailTexFuncSGIS( GLenum(target), GLfloatArray(points) ) -> None',
	argNames = ('target', 'points',),
	deprecated = _DEPRECATED,
)


def glInitDetailTextureSGIS():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
