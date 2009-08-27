'''OpenGL extension NV.register_combiners2

Overview (from the spec)
	
	The NV_register_combiners extension provides a powerful fragment
	coloring mechanism.  This specification extends the register combiners
	functionality to support more color constant values that are unique
	for each general combiner stage.
	
	The base register combiners functionality supports only two color
	constants.  These two constants are available in every general
	combiner stage and in the final combiner.
	
	When many general combiner stages are supported, more than two
	unique color constants is often required.  The obvious way to extend
	the register combiners is to add several more color constant
	registers.  But adding new unique color constant registers is
	expensive for hardware implementation because every color constant
	register must be available as an input to any stage.
	
	In practice however, it is the total set of general combiner stages
	that requires more color constants, not each and every individual
	general combiner stage.  Each individual general combiner stage
	typically requires only one or two color constants.
	
	By keeping two color constant registers but making these two registers
	contain two unique color constant values for each general combiner
	stage, the hardware expense of supporting multiple color constants
	is minimized.  Additionally, this scheme scales appropriately as
	more general combiner stages are added.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/register_combiners2.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_register_combiners2'
_DEPRECATED = False
GL_PER_STAGE_CONSTANTS_NV = constant.Constant( 'GL_PER_STAGE_CONSTANTS_NV', 0x8535 )
glget.addGLGetConstant( GL_PER_STAGE_CONSTANTS_NV, (1,) )
glCombinerStageParameterfvNV = platform.createExtensionFunction( 
	'glCombinerStageParameterfvNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glCombinerStageParameterfvNV( GLenum(stage), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('stage', 'pname', 'params',),
	deprecated = _DEPRECATED,
)

glGetCombinerStageParameterfvNV = platform.createExtensionFunction( 
	'glGetCombinerStageParameterfvNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetCombinerStageParameterfvNV( GLenum(stage), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('stage', 'pname', 'params',),
	deprecated = _DEPRECATED,
)


def glInitRegisterCombiners2NV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
