Little Python Helpers
=====================

Just a personal collection of little snippets of Python that
are useful infrastructure.  Nothing here is particular new
or sophisticated.  

eprint
------

eprint() simply wraps print() and sends output to stderr. 
It saves a few characters of typing.

static_var
----------

static_var() creates and initializes a static variable inside
a function.  Just a little scoping hack.

ReprMixin
---------

ReprMixin is a mixin class that implements some standard 
boilerplate because writing __repr__() methods over and over is 
tedious.  ReprMixin does not check for self-referential data
structures, so is not suitable for general graphs and circular
data structures. 

To use:

For positional args, override def repr_args(self) to return
a list of values.

For keyword args, override repr_kwargs(self) to return a list
of keyword argument specifications, where each list element is
one of:

- A string.  This will emit <name>=self.<name> in the keyword
  arguments, and suppress None values.
- A tuple of (<name>, <expr>).  This will emit <name>=<expr> 
  in the keyword arguments, and suppress None values.
- A tuple of (<name>, <expr>, <value>).  This will emit <name>=<expr>
  and suppress <value> values.

See the tests for examples.



