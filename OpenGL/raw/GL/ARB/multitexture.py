'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_multitexture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_multitexture',False)
_p.unpack_constants( """GL_TEXTURE0_ARB 0x84C0
GL_TEXTURE1_ARB 0x84C1
GL_TEXTURE2_ARB 0x84C2
GL_TEXTURE3_ARB 0x84C3
GL_TEXTURE4_ARB 0x84C4
GL_TEXTURE5_ARB 0x84C5
GL_TEXTURE6_ARB 0x84C6
GL_TEXTURE7_ARB 0x84C7
GL_TEXTURE8_ARB 0x84C8
GL_TEXTURE9_ARB 0x84C9
GL_TEXTURE10_ARB 0x84CA
GL_TEXTURE11_ARB 0x84CB
GL_TEXTURE12_ARB 0x84CC
GL_TEXTURE13_ARB 0x84CD
GL_TEXTURE14_ARB 0x84CE
GL_TEXTURE15_ARB 0x84CF
GL_TEXTURE16_ARB 0x84D0
GL_TEXTURE17_ARB 0x84D1
GL_TEXTURE18_ARB 0x84D2
GL_TEXTURE19_ARB 0x84D3
GL_TEXTURE20_ARB 0x84D4
GL_TEXTURE21_ARB 0x84D5
GL_TEXTURE22_ARB 0x84D6
GL_TEXTURE23_ARB 0x84D7
GL_TEXTURE24_ARB 0x84D8
GL_TEXTURE25_ARB 0x84D9
GL_TEXTURE26_ARB 0x84DA
GL_TEXTURE27_ARB 0x84DB
GL_TEXTURE28_ARB 0x84DC
GL_TEXTURE29_ARB 0x84DD
GL_TEXTURE30_ARB 0x84DE
GL_TEXTURE31_ARB 0x84DF
GL_ACTIVE_TEXTURE_ARB 0x84E0
GL_CLIENT_ACTIVE_TEXTURE_ARB 0x84E1
GL_MAX_TEXTURE_UNITS_ARB 0x84E2""", globals())
@_f
@_p.types(None,_cs.GLenum)
def glActiveTextureARB( texture ):pass
@_f
@_p.types(None,_cs.GLenum)
def glClientActiveTextureARB( texture ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble)
def glMultiTexCoord1dARB( target,s ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMultiTexCoord1dvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glMultiTexCoord1fARB( target,s ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMultiTexCoord1fvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glMultiTexCoord1iARB( target,s ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glMultiTexCoord1ivARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort)
def glMultiTexCoord1sARB( target,s ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glMultiTexCoord1svARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble)
def glMultiTexCoord2dARB( target,s,t ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMultiTexCoord2dvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat)
def glMultiTexCoord2fARB( target,s,t ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMultiTexCoord2fvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint)
def glMultiTexCoord2iARB( target,s,t ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glMultiTexCoord2ivARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort,_cs.GLshort)
def glMultiTexCoord2sARB( target,s,t ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glMultiTexCoord2svARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMultiTexCoord3dARB( target,s,t,r ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMultiTexCoord3dvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMultiTexCoord3fARB( target,s,t,r ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMultiTexCoord3fvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint)
def glMultiTexCoord3iARB( target,s,t,r ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glMultiTexCoord3ivARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glMultiTexCoord3sARB( target,s,t,r ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glMultiTexCoord3svARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMultiTexCoord4dARB( target,s,t,r,q ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMultiTexCoord4dvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMultiTexCoord4fARB( target,s,t,r,q ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMultiTexCoord4fvARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glMultiTexCoord4iARB( target,s,t,r,q ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glMultiTexCoord4ivARB( target,v ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glMultiTexCoord4sARB( target,s,t,r,q ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glMultiTexCoord4svARB( target,v ):pass


def glInitMultitextureARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
