'''OpenGL extension SGIX.texture_scale_bias

Overview (from the spec)
	
	This extension adds scale, bias, and clamp to [0, 1] operations to the 
	texture pipeline.
	These operations are applied to the filtered result of a texture lookup,
	before that result is used in the texture environment equations and
	before the texture color lookup table of SGI_texture_color_table, 
	if that extension exists.
	These operations are distinct from the scale, bias, and clamp operations
	that appear in the SGI_color_table extension, which are used to
	define a color lookup table.
	
	Scale and bias operations on texels can be used to better utilize the
	color resolution of a particular texture internal format (see EXT_texture).

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_scale_bias.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_texture_scale_bias'
_DEPRECATED = False
GL_POST_TEXTURE_FILTER_BIAS_SGIX = constant.Constant( 'GL_POST_TEXTURE_FILTER_BIAS_SGIX', 0x8179 )
GL_POST_TEXTURE_FILTER_SCALE_SGIX = constant.Constant( 'GL_POST_TEXTURE_FILTER_SCALE_SGIX', 0x817A )
GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX = constant.Constant( 'GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX', 0x817B )
glget.addGLGetConstant( GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX, (1,) )
GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX = constant.Constant( 'GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX', 0x817C )
glget.addGLGetConstant( GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX, (1,) )


def glInitTextureScaleBiasSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
