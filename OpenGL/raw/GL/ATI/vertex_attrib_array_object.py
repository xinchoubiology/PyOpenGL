'''OpenGL extension ATI.vertex_attrib_array_object

Overview (from the spec)
	
	This extension defines an interface that allows multiple sets of
	generic vertex attribute data to be cached in persistent server-side
	memory.  It is intended to allow client data to be stored in memory
	that can be directly accessed by graphics hardware.
	

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ATI/vertex_attrib_array_object.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_vertex_attrib_array_object'
_DEPRECATED = False

glVertexAttribArrayObjectATI = platform.createExtensionFunction( 
	'glVertexAttribArrayObjectATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLint, constants.GLenum, constants.GLboolean, constants.GLsizei, constants.GLuint, constants.GLuint,),
	doc = 'glVertexAttribArrayObjectATI( GLuint(index), GLint(size), GLenum(type), GLboolean(normalized), GLsizei(stride), GLuint(buffer), GLuint(offset) ) -> None',
	argNames = ('index', 'size', 'type', 'normalized', 'stride', 'buffer', 'offset',),
	deprecated = _DEPRECATED,
)

glGetVertexAttribArrayObjectfvATI = platform.createExtensionFunction( 
	'glGetVertexAttribArrayObjectfvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetVertexAttribArrayObjectfvATI( GLuint(index), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('index', 'pname', 'params',),
	deprecated = _DEPRECATED,
)

glGetVertexAttribArrayObjectivATI = platform.createExtensionFunction( 
	'glGetVertexAttribArrayObjectivATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetVertexAttribArrayObjectivATI( GLuint(index), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('index', 'pname', 'params',),
	deprecated = _DEPRECATED,
)


def glInitVertexAttribArrayObjectATI():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
