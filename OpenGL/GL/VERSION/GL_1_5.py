'''OpenGL extension VERSION.GL_1_5

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_5 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_1_5.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.VERSION.GL_1_5 import *
from OpenGL.raw.GL.VERSION.GL_1_5 import _EXTENSION_NAME

def glInitGl15VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGenQueries=wrapper.wrapper(glGenQueries).setOutput(#
    'ids',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glGetQueryiv=wrapper.wrapper(glGetQueryiv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetQueryObjectiv=wrapper.wrapper(glGetQueryObjectiv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetQueryObjectuiv=wrapper.wrapper(glGetQueryObjectuiv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGenBuffers=wrapper.wrapper(glGenBuffers).setOutput(#
    'buffers',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glGetBufferSubData=wrapper.wrapper(glGetBufferSubData).setOutput(#
    'data',size=lambda x:(x,),pnameArg='size',orPassIn=True
)
glGetBufferParameteriv=wrapper.wrapper(glGetBufferParameteriv).setOutput(#
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetBufferPointerv=wrapper.wrapper(glGetBufferPointerv).setOutput(#
    'params',size=(1,),orPassIn=True
)
### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy as _lazy
from OpenGL.arrays import ArrayDatatype
from OpenGL._bytes import long, integer_types

glDeleteBuffers = arrays.setInputArraySizeType(
    glDeleteBuffers,
    None,
    arrays.GLuintArray,
    'buffers',
)

glGenBuffers = wrapper.wrapper( glGenBuffers ).setOutput(
    'buffers', lambda n: (n,), 'n', orPassIn=True
)

def _sizeOfArrayInput( pyArgs, index, wrapper ):
    return (
        arrays.ArrayDatatype.arrayByteCount( pyArgs[index] )
    )

@_lazy( glBufferData )
def glBufferData( baseOperation, target, size, data=None, usage=None ):
    """Copy given data into the currently bound vertex-buffer-data object

    target -- the symbolic constant indicating which buffer type is intended
    size -- if provided, the count-in-bytes of the array
    data -- data-pointer to be used, may be None to initialize without
        copying over a data-set
    usage -- hint to the driver as to how to set up access to the buffer

    Note: parameter "size" can be omitted, which makes the signature
        glBufferData( target, data, usage )
    instead of:
        glBufferData( target, size, data, usage )
    """
    if usage is None:
        usage = data
        data = size
        size = None
    data = ArrayDatatype.asArray( data )
    if size is None:
        size = ArrayDatatype.arrayByteCount( data )
    return baseOperation( target, size, data, usage )

@_lazy( glBufferSubData )
def glBufferSubData( baseOperation, target, offset, size=None, data=None ):
    """Copy subset of data into the currently bound vertex-buffer-data object

    target -- the symbolic constant indicating which buffer type is intended
    offset -- offset from beginning of buffer at which to copy bytes
    size -- the count-in-bytes of the array (if an int/long), if None,
        calculate size from data, if an array and data is None, use as
        data (i.e. the parameter can be omitted and calculated)
    data -- data-pointer to be used, may be None to initialize without
        copying over a data-set

    Note that if size is not an int/long it is considered to be data
    *iff* data is None
    """
    if size is None:
        if data is None:
            raise TypeError( "Need data or size" )
    elif (not isinstance( size, integer_types)) and (data is None):
        data = size 
        size = None
    try:
        if size is not None:
            size = int( size )
    except TypeError as err:
        if data is not None:
            raise TypeError(
                """Expect an integer size *or* a data-array, not both"""
            )
        data = size
        size = None
    data = ArrayDatatype.asArray( data )
    if size is None:
        size = ArrayDatatype.arrayByteCount( data )
    return baseOperation( target, offset, size, data )

glGetBufferParameteriv = wrapper.wrapper(glGetBufferParameteriv).setOutput(
    "params",(1,), orPassIn=True
)
@_lazy( glGetBufferPointerv )
def glGetBufferPointerv( baseOperation, target, pname, params=None ):
    """Retrieve a ctypes pointer to buffer's data"""
    if params is None:
        size = glGetBufferParameteriv( target, GL_BUFFER_SIZE )
        data = arrays.ArrayDatatype.zeros( (size,), GL_UNSIGNED_BYTE )
        result = baseOperation( target, pname, ctypes.byref( data ) )
        return data
    else:
        return baseOperation( target, pname, params )

@_lazy( glDeleteQueries )
def glDeleteQueries( baseOperation, n, ids=None ):
    if ids is None:
        ids = arrays.GLuintArray.asArray( n )
        n = arrays.GLuintArray.arraySize( ids )
    else:
        ids = arrays.GLuintArray.asArray( ids )
    return baseOperation( n,ids )
@_lazy( glGenQueries )
def glGenQueries( baseOperation, n, ids=None ):
    """Generate n queries, if ids is None, is allocated

    returns array of ids
    """
    if ids is None:
        ids = arrays.GLuintArray.zeros( (n,))
    else:
        ids = arrays.GLuintArray.asArray( ids )
    baseOperation( n, ids )
    return ids

for func in (
    'glGetQueryiv','glGetQueryObjectiv','glGetQueryObjectuiv',
):
    globals()[func] = wrapper.wrapper(globals()[func]).setOutput(
        "params", (1,), orPassIn=True
    )
try:
    del func, glget
except NameError as err:
    pass
