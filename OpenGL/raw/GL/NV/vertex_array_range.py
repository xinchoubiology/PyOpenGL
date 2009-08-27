'''OpenGL extension NV.vertex_array_range

Overview (from the spec)
	
	The goal of this extension is to permit extremely high vertex
	processing rates via OpenGL vertex arrays even when the CPU lacks
	the necessary data movement bandwidth to keep up with the rate
	at which the vertex engine can consume vertices.  CPUs can keep
	up if they can just pass vertex indices to the hardware and
	let the hardware "pull" the actual vertex data via Direct Memory
	Access (DMA).  Unfortunately, the current OpenGL 1.1 vertex array
	functionality has semantic constraints that make such an approach
	hard.  Hence, the vertex array range extension.
	
	This extension provides a mechanism for deferring the pulling of
	vertex array elements to facilitate DMAed pulling of vertices for
	fast, efficient vertex array transfers.  The OpenGL client need only
	pass vertex indices to the hardware which can DMA the actual index's
	vertex data directly out of the client address space.
	
	The OpenGL 1.1 vertex array functionality specifies a fairly strict
	coherency model for when OpenGL extracts vertex data from a vertex
	array and when the application can update the in memory
	vertex array data.  The OpenGL 1.1 specification says "Changes
	made to array data between the execution of Begin and the
	corresponding execution of End may affect calls to ArrayElement
	that are made within the same Begin/End period in non-sequential
	ways.  That is, a call to ArrayElement that precedes a change to
	array data may access the changed data, and a call that follows
	a change to array data may access the original data."
	
	This means that by the time End returns (and DrawArrays and
	DrawElements return since they have implicit Ends), the actual vertex
	array data must be transferred to OpenGL.  This strict coherency model
	prevents us from simply passing vertex element indices to the hardware
	and having the hardware "pull" the vertex data out (which is often
	long after the End for the primitive has returned to the application).
	
	Relaxing this coherency model and bounding the range from which
	vertex array data can be pulled is key to making OpenGL vertex
	array transfers faster and more efficient.
	
	The first task of the vertex array range extension is to relax
	the coherency model so that hardware can indeed "pull" vertex
	data from the OpenGL client's address space long after the application
	has completed sending the geometry primitives requiring the vertex
	data.
	
	The second problem with the OpenGL 1.1 vertex array functionality is
	the lack of any guidance from the API about what region of memory
	vertices can be pulled from.  There is no size limit for OpenGL 1.1
	vertex arrays.  Any vertex index that points to valid data in all
	enabled arrays is fair game.  This makes it hard for a vertex DMA
	engine to pull vertices since they can be potentially pulled from
	anywhere in the OpenGL client address space.
	
	The vertex array range extension specifies a range of the OpenGL
	client's address space where vertices can be pulled.  Vertex indices
	that access any array elements outside the vertex array range
	are specified to be undefined.  This permits hardware to DMA from
	finite regions of OpenGL client address space, making DMA engine
	implementation tractable.
	
	The extension is specified such that an (error free) OpenGL client
	using the vertex array range functionality could no-op its vertex
	array range commands and operate equivalently to using (if slower
	than) the vertex array range functionality.
	
	Because different memory types (local graphics memory, AGP memory)
	have different DMA bandwidths and caching behavior, this extension
	includes a window system dependent memory allocator to allocate
	cleanly the most appropriate memory for constructing a vertex array
	range.  The memory allocator provided allows the application to
	tradeoff the desired CPU read frequency, CPU write frequency, and
	memory priority while still leaving it up to OpenGL implementation
	the exact memory type to be allocated.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/vertex_array_range.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_vertex_array_range'
_DEPRECATED = False
GL_VERTEX_ARRAY_RANGE_NV = constant.Constant( 'GL_VERTEX_ARRAY_RANGE_NV', 0x851D )
GL_VERTEX_ARRAY_RANGE_LENGTH_NV = constant.Constant( 'GL_VERTEX_ARRAY_RANGE_LENGTH_NV', 0x851E )
glget.addGLGetConstant( GL_VERTEX_ARRAY_RANGE_LENGTH_NV, (1,) )
GL_VERTEX_ARRAY_RANGE_VALID_NV = constant.Constant( 'GL_VERTEX_ARRAY_RANGE_VALID_NV', 0x851F )
glget.addGLGetConstant( GL_VERTEX_ARRAY_RANGE_VALID_NV, (1,) )
GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV = constant.Constant( 'GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV', 0x8520 )
glget.addGLGetConstant( GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV, (1,) )
GL_VERTEX_ARRAY_RANGE_POINTER_NV = constant.Constant( 'GL_VERTEX_ARRAY_RANGE_POINTER_NV', 0x8521 )
glFlushVertexArrayRangeNV = platform.createExtensionFunction( 
	'glFlushVertexArrayRangeNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(),
	doc = 'glFlushVertexArrayRangeNV(  ) -> None',
	argNames = (),
	deprecated = _DEPRECATED,
)

glVertexArrayRangeNV = platform.createExtensionFunction( 
	'glVertexArrayRangeNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, ctypes.c_void_p,),
	doc = 'glVertexArrayRangeNV( GLsizei(length), c_void_p(pointer) ) -> None',
	argNames = ('length', 'pointer',),
	deprecated = _DEPRECATED,
)


def glInitVertexArrayRangeNV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
