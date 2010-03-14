'''OpenGL extension ARB.texture_swizzle

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_swizzle'
_DEPRECATED = False
GL_TEXTURE_SWIZZLE_R = constant.Constant( 'GL_TEXTURE_SWIZZLE_R', 0x8E42 )
GL_TEXTURE_SWIZZLE_G = constant.Constant( 'GL_TEXTURE_SWIZZLE_G', 0x8E43 )
GL_TEXTURE_SWIZZLE_B = constant.Constant( 'GL_TEXTURE_SWIZZLE_B', 0x8E44 )
GL_TEXTURE_SWIZZLE_A = constant.Constant( 'GL_TEXTURE_SWIZZLE_A', 0x8E45 )
GL_TEXTURE_SWIZZLE_RGBA = constant.Constant( 'GL_TEXTURE_SWIZZLE_RGBA', 0x8E46 )


def glInitTextureSwizzleARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
