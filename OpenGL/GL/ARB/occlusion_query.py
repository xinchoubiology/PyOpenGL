'''OpenGL extension ARB.occlusion_query

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.occlusion_query to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/occlusion_query.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.occlusion_query import *
from OpenGL.raw.GL.ARB.occlusion_query import _EXTENSION_NAME

def glInitOcclusionQueryARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy as _lazy
from OpenGL.GL import glget
from OpenGL import converters
@_lazy( glDeleteQueriesARB )
def glDeleteQueriesARB( baseOperation, n, ids=None ):
    """Delete the given queries 
    
    n -- either the number of queries to delete, or an array of query values 
    ids -- if provided, the array/pointer to the queries to delete 
    """
    if ids is None:
        ids = arrays.GLuintArray.asArray( n )
        n = arrays.GLuintArray.arraySize( ids )
    else:
        ids = arrays.GLuintArray.asArray( ids )
    return baseOperation( n,ids )
@_lazy( glGenQueriesARB )
def glGenQueriesARB( baseOperation, n, ids=None ):
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
    'glGetQueryivARB','glGetQueryObjectivARB','glGetQueryObjectuivARB',
):
    globals()[func] = wrapper.wrapper(globals()[func]).setOutput(
        "params", (1,), orPassIn=True
    )
try:
    del func, glget
except NameError as err:
    pass
