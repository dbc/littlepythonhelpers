"""littlepythonhelpers.py, a collection of useful generic utilities.
"""

# Copyright (C) 2017-2019 David B. Curtis
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__version__ = '1.2'
__license__ = '2-clause BSD'

import sys


def eprint(*args, **kwargs):
    """Convenience function to print to stderr. A simple slick layer on
    print().
    """
    print(*args, file=sys.stderr, **kwargs)


def static_var(var_name, value):
    """Decorator that creates and initializes a static variable inside
    a function definition.  The variable can be accessed within the
    function as: <funcname>.<varname>

    :param varname: The name of the static variable to create (string).
    :param value: The initial value of the static variable.
    """
    def decorate(f):
        setattr(f, var_name, value)
        return f
    return decorate


class ReprMixin:
    """Implements repr() boilerplate for non-self-referential data
    structures.  Does no compression or pretty-printing, nor does it check
    for recursion."""
    def __repr__(self):
        arg_text = [repr(x) for x in self.repr_args()]
        kwarg_keys = [(kwa, getattr(self, kwa), None)
            if isinstance(kwa, str)
                else (kwa if len(kwa) == 3 else (kwa[0], kwa[1], None))
                    for kwa in self.repr_kwargs()]
        arg_text.extend(['='.join([kw, repr(arg)])
            for kw, arg, default in kwarg_keys
                if arg != default])
        return ''.join([self.__class__.__name__,
            '(', ', '.join(arg_text), ')'])

    def repr_args(self):
        """Return a list of positional argument values for Repr()."""
        return []

    def repr_kwargs(self):
        """Return a list where each element is either:
        - a string
        - a of tuple: ('name', value, optional-default-value)
        - a of tuple: ('name', value)  -- the default is assumed to be None.
        """
        return []


if __name__ == '__main__':
    pass
