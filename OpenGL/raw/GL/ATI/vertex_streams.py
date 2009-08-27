'''OpenGL extension ATI.vertex_streams

Overview (from the spec)
	
	This extension adds the ability to handle sets of auxilliary
	vertex and normal coordinates. These sets of auxilliary
	coordinates are termed streams, and can be routed selectively
	into the blend stages provided by the vertex blending extension.
	This functionality enables software animation techniques such
	as keyframe vertex morphing.
	
	

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ATI/vertex_streams.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_vertex_streams'
_DEPRECATED = False
GL_MAX_VERTEX_STREAMS_ATI = constant.Constant( 'GL_MAX_VERTEX_STREAMS_ATI', 0x876B )
GL_VERTEX_STREAM0_ATI = constant.Constant( 'GL_VERTEX_STREAM0_ATI', 0x876C )
GL_VERTEX_STREAM1_ATI = constant.Constant( 'GL_VERTEX_STREAM1_ATI', 0x876D )
GL_VERTEX_STREAM2_ATI = constant.Constant( 'GL_VERTEX_STREAM2_ATI', 0x876E )
GL_VERTEX_STREAM3_ATI = constant.Constant( 'GL_VERTEX_STREAM3_ATI', 0x876F )
GL_VERTEX_STREAM4_ATI = constant.Constant( 'GL_VERTEX_STREAM4_ATI', 0x8770 )
GL_VERTEX_STREAM5_ATI = constant.Constant( 'GL_VERTEX_STREAM5_ATI', 0x8771 )
GL_VERTEX_STREAM6_ATI = constant.Constant( 'GL_VERTEX_STREAM6_ATI', 0x8772 )
GL_VERTEX_STREAM7_ATI = constant.Constant( 'GL_VERTEX_STREAM7_ATI', 0x8773 )
GL_VERTEX_SOURCE_ATI = constant.Constant( 'GL_VERTEX_SOURCE_ATI', 0x8774 )
glVertexStream1sATI = platform.createExtensionFunction( 
	'glVertexStream1sATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLshort,),
	doc = 'glVertexStream1sATI( GLenum(stream), GLshort(x) ) -> None',
	argNames = ('stream', 'x',),
	deprecated = _DEPRECATED,
)

glVertexStream1svATI = platform.createExtensionFunction( 
	'glVertexStream1svATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLshortArray,),
	doc = 'glVertexStream1svATI( GLenum(stream), GLshortArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream1iATI = platform.createExtensionFunction( 
	'glVertexStream1iATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint,),
	doc = 'glVertexStream1iATI( GLenum(stream), GLint(x) ) -> None',
	argNames = ('stream', 'x',),
	deprecated = _DEPRECATED,
)

glVertexStream1ivATI = platform.createExtensionFunction( 
	'glVertexStream1ivATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray,),
	doc = 'glVertexStream1ivATI( GLenum(stream), GLintArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream1fATI = platform.createExtensionFunction( 
	'glVertexStream1fATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat,),
	doc = 'glVertexStream1fATI( GLenum(stream), GLfloat(x) ) -> None',
	argNames = ('stream', 'x',),
	deprecated = _DEPRECATED,
)

glVertexStream1fvATI = platform.createExtensionFunction( 
	'glVertexStream1fvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glVertexStream1fvATI( GLenum(stream), GLfloatArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream1dATI = platform.createExtensionFunction( 
	'glVertexStream1dATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLdouble,),
	doc = 'glVertexStream1dATI( GLenum(stream), GLdouble(x) ) -> None',
	argNames = ('stream', 'x',),
	deprecated = _DEPRECATED,
)

glVertexStream1dvATI = platform.createExtensionFunction( 
	'glVertexStream1dvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLdoubleArray,),
	doc = 'glVertexStream1dvATI( GLenum(stream), GLdoubleArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream2sATI = platform.createExtensionFunction( 
	'glVertexStream2sATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLshort, constants.GLshort,),
	doc = 'glVertexStream2sATI( GLenum(stream), GLshort(x), GLshort(y) ) -> None',
	argNames = ('stream', 'x', 'y',),
	deprecated = _DEPRECATED,
)

glVertexStream2svATI = platform.createExtensionFunction( 
	'glVertexStream2svATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLshortArray,),
	doc = 'glVertexStream2svATI( GLenum(stream), GLshortArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream2iATI = platform.createExtensionFunction( 
	'glVertexStream2iATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint, constants.GLint,),
	doc = 'glVertexStream2iATI( GLenum(stream), GLint(x), GLint(y) ) -> None',
	argNames = ('stream', 'x', 'y',),
	deprecated = _DEPRECATED,
)

glVertexStream2ivATI = platform.createExtensionFunction( 
	'glVertexStream2ivATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray,),
	doc = 'glVertexStream2ivATI( GLenum(stream), GLintArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream2fATI = platform.createExtensionFunction( 
	'glVertexStream2fATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat, constants.GLfloat,),
	doc = 'glVertexStream2fATI( GLenum(stream), GLfloat(x), GLfloat(y) ) -> None',
	argNames = ('stream', 'x', 'y',),
	deprecated = _DEPRECATED,
)

glVertexStream2fvATI = platform.createExtensionFunction( 
	'glVertexStream2fvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glVertexStream2fvATI( GLenum(stream), GLfloatArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream2dATI = platform.createExtensionFunction( 
	'glVertexStream2dATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLdouble, constants.GLdouble,),
	doc = 'glVertexStream2dATI( GLenum(stream), GLdouble(x), GLdouble(y) ) -> None',
	argNames = ('stream', 'x', 'y',),
	deprecated = _DEPRECATED,
)

glVertexStream2dvATI = platform.createExtensionFunction( 
	'glVertexStream2dvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLdoubleArray,),
	doc = 'glVertexStream2dvATI( GLenum(stream), GLdoubleArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream3sATI = platform.createExtensionFunction( 
	'glVertexStream3sATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glVertexStream3sATI( GLenum(stream), GLshort(x), GLshort(y), GLshort(z) ) -> None',
	argNames = ('stream', 'x', 'y', 'z',),
	deprecated = _DEPRECATED,
)

glVertexStream3svATI = platform.createExtensionFunction( 
	'glVertexStream3svATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLshortArray,),
	doc = 'glVertexStream3svATI( GLenum(stream), GLshortArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream3iATI = platform.createExtensionFunction( 
	'glVertexStream3iATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glVertexStream3iATI( GLenum(stream), GLint(x), GLint(y), GLint(z) ) -> None',
	argNames = ('stream', 'x', 'y', 'z',),
	deprecated = _DEPRECATED,
)

glVertexStream3ivATI = platform.createExtensionFunction( 
	'glVertexStream3ivATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray,),
	doc = 'glVertexStream3ivATI( GLenum(stream), GLintArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream3fATI = platform.createExtensionFunction( 
	'glVertexStream3fATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glVertexStream3fATI( GLenum(stream), GLfloat(x), GLfloat(y), GLfloat(z) ) -> None',
	argNames = ('stream', 'x', 'y', 'z',),
	deprecated = _DEPRECATED,
)

glVertexStream3fvATI = platform.createExtensionFunction( 
	'glVertexStream3fvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glVertexStream3fvATI( GLenum(stream), GLfloatArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream3dATI = platform.createExtensionFunction( 
	'glVertexStream3dATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glVertexStream3dATI( GLenum(stream), GLdouble(x), GLdouble(y), GLdouble(z) ) -> None',
	argNames = ('stream', 'x', 'y', 'z',),
	deprecated = _DEPRECATED,
)

glVertexStream3dvATI = platform.createExtensionFunction( 
	'glVertexStream3dvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLdoubleArray,),
	doc = 'glVertexStream3dvATI( GLenum(stream), GLdoubleArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream4sATI = platform.createExtensionFunction( 
	'glVertexStream4sATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLshort, constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glVertexStream4sATI( GLenum(stream), GLshort(x), GLshort(y), GLshort(z), GLshort(w) ) -> None',
	argNames = ('stream', 'x', 'y', 'z', 'w',),
	deprecated = _DEPRECATED,
)

glVertexStream4svATI = platform.createExtensionFunction( 
	'glVertexStream4svATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLshortArray,),
	doc = 'glVertexStream4svATI( GLenum(stream), GLshortArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream4iATI = platform.createExtensionFunction( 
	'glVertexStream4iATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint, constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glVertexStream4iATI( GLenum(stream), GLint(x), GLint(y), GLint(z), GLint(w) ) -> None',
	argNames = ('stream', 'x', 'y', 'z', 'w',),
	deprecated = _DEPRECATED,
)

glVertexStream4ivATI = platform.createExtensionFunction( 
	'glVertexStream4ivATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray,),
	doc = 'glVertexStream4ivATI( GLenum(stream), GLintArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream4fATI = platform.createExtensionFunction( 
	'glVertexStream4fATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glVertexStream4fATI( GLenum(stream), GLfloat(x), GLfloat(y), GLfloat(z), GLfloat(w) ) -> None',
	argNames = ('stream', 'x', 'y', 'z', 'w',),
	deprecated = _DEPRECATED,
)

glVertexStream4fvATI = platform.createExtensionFunction( 
	'glVertexStream4fvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glVertexStream4fvATI( GLenum(stream), GLfloatArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glVertexStream4dATI = platform.createExtensionFunction( 
	'glVertexStream4dATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLdouble, constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glVertexStream4dATI( GLenum(stream), GLdouble(x), GLdouble(y), GLdouble(z), GLdouble(w) ) -> None',
	argNames = ('stream', 'x', 'y', 'z', 'w',),
	deprecated = _DEPRECATED,
)

glVertexStream4dvATI = platform.createExtensionFunction( 
	'glVertexStream4dvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLdoubleArray,),
	doc = 'glVertexStream4dvATI( GLenum(stream), GLdoubleArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glNormalStream3bATI = platform.createExtensionFunction( 
	'glNormalStream3bATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLbyte, constants.GLbyte, constants.GLbyte,),
	doc = 'glNormalStream3bATI( GLenum(stream), GLbyte(nx), GLbyte(ny), GLbyte(nz) ) -> None',
	argNames = ('stream', 'nx', 'ny', 'nz',),
	deprecated = _DEPRECATED,
)

glNormalStream3bvATI = platform.createExtensionFunction( 
	'glNormalStream3bvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLbyteArray,),
	doc = 'glNormalStream3bvATI( GLenum(stream), GLbyteArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glNormalStream3sATI = platform.createExtensionFunction( 
	'glNormalStream3sATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glNormalStream3sATI( GLenum(stream), GLshort(nx), GLshort(ny), GLshort(nz) ) -> None',
	argNames = ('stream', 'nx', 'ny', 'nz',),
	deprecated = _DEPRECATED,
)

glNormalStream3svATI = platform.createExtensionFunction( 
	'glNormalStream3svATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLshortArray,),
	doc = 'glNormalStream3svATI( GLenum(stream), GLshortArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glNormalStream3iATI = platform.createExtensionFunction( 
	'glNormalStream3iATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glNormalStream3iATI( GLenum(stream), GLint(nx), GLint(ny), GLint(nz) ) -> None',
	argNames = ('stream', 'nx', 'ny', 'nz',),
	deprecated = _DEPRECATED,
)

glNormalStream3ivATI = platform.createExtensionFunction( 
	'glNormalStream3ivATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray,),
	doc = 'glNormalStream3ivATI( GLenum(stream), GLintArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glNormalStream3fATI = platform.createExtensionFunction( 
	'glNormalStream3fATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glNormalStream3fATI( GLenum(stream), GLfloat(nx), GLfloat(ny), GLfloat(nz) ) -> None',
	argNames = ('stream', 'nx', 'ny', 'nz',),
	deprecated = _DEPRECATED,
)

glNormalStream3fvATI = platform.createExtensionFunction( 
	'glNormalStream3fvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glNormalStream3fvATI( GLenum(stream), GLfloatArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glNormalStream3dATI = platform.createExtensionFunction( 
	'glNormalStream3dATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glNormalStream3dATI( GLenum(stream), GLdouble(nx), GLdouble(ny), GLdouble(nz) ) -> None',
	argNames = ('stream', 'nx', 'ny', 'nz',),
	deprecated = _DEPRECATED,
)

glNormalStream3dvATI = platform.createExtensionFunction( 
	'glNormalStream3dvATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLdoubleArray,),
	doc = 'glNormalStream3dvATI( GLenum(stream), GLdoubleArray(coords) ) -> None',
	argNames = ('stream', 'coords',),
	deprecated = _DEPRECATED,
)

glClientActiveVertexStreamATI = platform.createExtensionFunction( 
	'glClientActiveVertexStreamATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum,),
	doc = 'glClientActiveVertexStreamATI( GLenum(stream) ) -> None',
	argNames = ('stream',),
	deprecated = _DEPRECATED,
)

glVertexBlendEnviATI = platform.createExtensionFunction( 
	'glVertexBlendEnviATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint,),
	doc = 'glVertexBlendEnviATI( GLenum(pname), GLint(param) ) -> None',
	argNames = ('pname', 'param',),
	deprecated = _DEPRECATED,
)

glVertexBlendEnvfATI = platform.createExtensionFunction( 
	'glVertexBlendEnvfATI', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat,),
	doc = 'glVertexBlendEnvfATI( GLenum(pname), GLfloat(param) ) -> None',
	argNames = ('pname', 'param',),
	deprecated = _DEPRECATED,
)


def glInitVertexStreamsATI():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
