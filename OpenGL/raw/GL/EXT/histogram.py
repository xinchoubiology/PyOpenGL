'''OpenGL extension EXT.histogram

Overview (from the spec)
	
	This extension defines pixel operations that count occurences of
	specific color component values (histogram) and that track the minimum
	and maximum color component values (minmax).  An optional mode allows
	pixel data to be discarded after the histogram and/or minmax operations
	are completed.  Otherwise the pixel data continue on to the next
	operation unaffected.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/histogram.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_histogram'
_DEPRECATED = False
GL_HISTOGRAM_EXT = constant.Constant( 'GL_HISTOGRAM_EXT', 0x8024 )
glget.addGLGetConstant( GL_HISTOGRAM_EXT, (1,) )
GL_PROXY_HISTOGRAM_EXT = constant.Constant( 'GL_PROXY_HISTOGRAM_EXT', 0x8025 )
GL_HISTOGRAM_WIDTH_EXT = constant.Constant( 'GL_HISTOGRAM_WIDTH_EXT', 0x8026 )
GL_HISTOGRAM_FORMAT_EXT = constant.Constant( 'GL_HISTOGRAM_FORMAT_EXT', 0x8027 )
GL_HISTOGRAM_RED_SIZE_EXT = constant.Constant( 'GL_HISTOGRAM_RED_SIZE_EXT', 0x8028 )
GL_HISTOGRAM_GREEN_SIZE_EXT = constant.Constant( 'GL_HISTOGRAM_GREEN_SIZE_EXT', 0x8029 )
GL_HISTOGRAM_BLUE_SIZE_EXT = constant.Constant( 'GL_HISTOGRAM_BLUE_SIZE_EXT', 0x802A )
GL_HISTOGRAM_ALPHA_SIZE_EXT = constant.Constant( 'GL_HISTOGRAM_ALPHA_SIZE_EXT', 0x802B )
GL_HISTOGRAM_LUMINANCE_SIZE_EXT = constant.Constant( 'GL_HISTOGRAM_LUMINANCE_SIZE_EXT', 0x802C )
GL_HISTOGRAM_SINK_EXT = constant.Constant( 'GL_HISTOGRAM_SINK_EXT', 0x802D )
GL_MINMAX_EXT = constant.Constant( 'GL_MINMAX_EXT', 0x802E )
glget.addGLGetConstant( GL_MINMAX_EXT, (1,) )
GL_MINMAX_FORMAT_EXT = constant.Constant( 'GL_MINMAX_FORMAT_EXT', 0x802F )
GL_MINMAX_SINK_EXT = constant.Constant( 'GL_MINMAX_SINK_EXT', 0x8030 )
GL_TABLE_TOO_LARGE_EXT = constant.Constant( 'GL_TABLE_TOO_LARGE_EXT', 0x8031 )
glGetHistogramEXT = platform.createExtensionFunction( 
	'glGetHistogramEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLboolean, constants.GLenum, constants.GLenum, ctypes.c_void_p,),
	doc = 'glGetHistogramEXT( GLenum(target), GLboolean(reset), GLenum(format), GLenum(type), c_void_p(values) ) -> None',
	argNames = ('target', 'reset', 'format', 'type', 'values',),
	deprecated = _DEPRECATED,
)

glGetHistogramParameterfvEXT = platform.createExtensionFunction( 
	'glGetHistogramParameterfvEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetHistogramParameterfvEXT( GLenum(target), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('target', 'pname', 'params',),
	deprecated = _DEPRECATED,
)

glGetHistogramParameterivEXT = platform.createExtensionFunction( 
	'glGetHistogramParameterivEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetHistogramParameterivEXT( GLenum(target), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('target', 'pname', 'params',),
	deprecated = _DEPRECATED,
)

glGetMinmaxEXT = platform.createExtensionFunction( 
	'glGetMinmaxEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLboolean, constants.GLenum, constants.GLenum, ctypes.c_void_p,),
	doc = 'glGetMinmaxEXT( GLenum(target), GLboolean(reset), GLenum(format), GLenum(type), c_void_p(values) ) -> None',
	argNames = ('target', 'reset', 'format', 'type', 'values',),
	deprecated = _DEPRECATED,
)

glGetMinmaxParameterfvEXT = platform.createExtensionFunction( 
	'glGetMinmaxParameterfvEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetMinmaxParameterfvEXT( GLenum(target), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('target', 'pname', 'params',),
	deprecated = _DEPRECATED,
)

glGetMinmaxParameterivEXT = platform.createExtensionFunction( 
	'glGetMinmaxParameterivEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetMinmaxParameterivEXT( GLenum(target), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('target', 'pname', 'params',),
	deprecated = _DEPRECATED,
)

glHistogramEXT = platform.createExtensionFunction( 
	'glHistogramEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, constants.GLenum, constants.GLboolean,),
	doc = 'glHistogramEXT( GLenum(target), GLsizei(width), GLenum(internalformat), GLboolean(sink) ) -> None',
	argNames = ('target', 'width', 'internalformat', 'sink',),
	deprecated = _DEPRECATED,
)

glMinmaxEXT = platform.createExtensionFunction( 
	'glMinmaxEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, constants.GLboolean,),
	doc = 'glMinmaxEXT( GLenum(target), GLenum(internalformat), GLboolean(sink) ) -> None',
	argNames = ('target', 'internalformat', 'sink',),
	deprecated = _DEPRECATED,
)

glResetHistogramEXT = platform.createExtensionFunction( 
	'glResetHistogramEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum,),
	doc = 'glResetHistogramEXT( GLenum(target) ) -> None',
	argNames = ('target',),
	deprecated = _DEPRECATED,
)

glResetMinmaxEXT = platform.createExtensionFunction( 
	'glResetMinmaxEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum,),
	doc = 'glResetMinmaxEXT( GLenum(target) ) -> None',
	argNames = ('target',),
	deprecated = _DEPRECATED,
)


def glInitHistogramEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
