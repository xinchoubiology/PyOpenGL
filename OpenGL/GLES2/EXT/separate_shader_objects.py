'''OpenGL extension EXT.separate_shader_objects

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.separate_shader_objects to provide a more 
Python-friendly API

Overview (from the spec)
	
	Prior to this extension, GLSL requires multiple shader domains
	(vertex, fragment, geometry) to be linked into a single monolithic
	program object to specify a GLSL shader for each domain.
	
	While GLSL's monolithic approach has some advantages for
	optimizing shaders as a unit that span multiple domains, all
	existing GPU hardware supports the more flexible mix-and-match
	approach.
	
	HLSL9, Cg, the prior OpenGL assembly program extensions, and game
	console programmers favor a more flexible "mix-and-match" approach to
	specifying shaders independently for these different shader domains.
	Many developers build their shader content around the mix-and-match
	approach where they can use a single vertex shader with multiple
	fragment shaders (or vice versa).
	
	This keep-it-simple extension adapts the "mix-and-match" shader
	domain model for GLSL so different GLSL program objects can be bound
	to different shader domains.
	
	This extension redefines the operation of glUseProgram(GLenum program)
	to be equivalent to:
	
	    glUseShaderProgramEXT(GL_VERTEX_SHADER, program);
	    glUseShaderProgramEXT(GL_GEOMETRY_SHADER_EXT, program);
	    glUseShaderProgramEXT(GL_FRAGMENT_SHADER, program);
	    glActiveProgramEXT(program);
	
	You can also call these commands separately to bind each respective
	domain.  The GL_VERTEX_SHADER, GL_GEOMETRY_SHADER_EXT, and
	GL_FRAGMENT_SHADER tokens refer to the conventional vertex, geometry,
	and fragment domains respectively.  glActiveProgramEXT specifies
	the program that glUniform* commands will update.
	
	Separate linking creates the possibility that certain output varyings
	of a shader may go unread by the subsequent shader inputting varyings.
	In this case, the output varyings are simply ignored.  It is also
	possible input varyings from a shader may not be written as output
	varyings of a preceding shader.  In this case, the unwritten input
	varying values are undefined.  Implementations are encouraged to
	zero these undefined input varying values.
	
	This extension is a proof-of-concept that separate shader objects
	can work for GLSL and a response to repeated requests for this
	functionality.  There are various loose ends, particularly when
	dealing with user-defined varyings.  The hope is a future extension
	will improve this situation.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/separate_shader_objects.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.EXT.separate_shader_objects import *
from OpenGL.raw.GLES2.EXT.separate_shader_objects import _EXTENSION_NAME

def glInitSeparateShaderObjectsEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION