
# -*- coding: utf-8 -*-

u'''Error, exception classes and functions to format PyGeodesy errors,
    including the setting of I{exception chaining} in Python 3+.

    By default, I{exception chaining} is turned off.  Set environment
    variable C{PYGEODESY_EXCEPTION_CHAINING} to 'std' or any other
    non-empty string to enable I{exception chaining}.
'''
from pygeodesy.interns import MISSING, NN, _a_,_an_, _COLON_, \
                             _COMMA_, _COMMASPACE_, _datum_, \
                             _ellipsoidal_, _EQUAL_, _invalid_, \
                             _len_, _name_, _no_, _not_, _or_, \
                             _SPACE_, _UNDER_
from pygeodesy.lazily import _ALL_LAZY, _environ

__all__ = _ALL_LAZY.errors  # _ALL_DOCS('_InvalidError', '_IsnotError')
__version__ = '20.12.02'

_limiterrors =  True  # imported by .formy
_multiple_   = 'multiple'
_name_value_ =  repr('name=value')
_rangerrors  =  True  # imported by .dms
_specified_  = 'specified'

try:
    _exception_chaining = None  # not available

    _ = Exception().__cause__   # Python 3+ exception chaining

    if _environ.get('PYGEODESY_EXCEPTION_CHAINING', None):  # == _std_
        _exception_chaining = True  # turned on, std
        raise AttributeError  # allow exception chaining

    _exception_chaining = False  # turned off

    def _error_chain(inst, other=None):
        '''(INTERNAL) Set or avoid Python 3+ exception chaining.

           Setting C{inst.__cause__ = None} is equivalent to syntax
           C{raise Error(...) from None} to avoid exception chaining.

           @arg inst: An error instance (C{Exception}).
           @kwarg other: The previous error instance (C{Exception}) or
                         C{None} to avoid exception chaining.

           @see: Alex Martelli, et.al., "Python in a Nutshell", 3rd Ed., page 163,
                 O'Reilly, 2017, U{PEP-3134<https://www.Python.org/dev/peps/pep-3134>},
                 U{here <https://StackOverflow.com/questions/17091520/how-can-i-more-
                 easily-suppress-previous-exceptions-when-i-raise-my-own-exception>}
                 and U{here<https://StackOverflow.com/questions/1350671/
                 inner-exception-with-traceback-in-python>}.
        '''
        inst.__cause__ = other  # None, no exception chaining
        return inst

except AttributeError:  # Python 2+

    def _error_chain(inst, **unused):  # PYCHOK expected
        return inst  # no-op


class _AssertionError(AssertionError):
    '''(INTERNAL) Format an C{AssertionError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):  # txt=_invalid_
        _error_init(AssertionError, self, name_value, **txt_name_values)


class _AttributeError(AttributeError):
    '''(INTERNAL) Format an C{AttributeError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):  # txt=_invalid_
        _error_init(AttributeError, self, name_value, **txt_name_values)


class _IndexError(IndexError):
    '''(INTERNAL) Format an C{IndexError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):  # txt=_invalid_
        _error_init(IndexError, self, name_value, **txt_name_values)


class _NameError(NameError):
    '''(INTERNAL) Format a C{NameError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):  # txt=_invalid_
        _error_init(NameError, self, name_value, **txt_name_values)


class _NotImplementedError(NotImplementedError):
    '''(INTERNAL) Format a C{NotImplementedError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):  # txt=_invalid_
        _error_init(NotImplementedError, self, name_value, **txt_name_values)


class _OverflowError(OverflowError):
    '''(INTERNAL) Format an C{OverflowError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):  # txt=_invalid_
        _error_init(OverflowError, self, name_value, **txt_name_values)


class _TypeError(TypeError):
    '''(INTERNAL) Format a C{TypeError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):
        _error_init(TypeError, self, name_value, fmt_name_value='type(%s) (%r)',
                                               **txt_name_values)


class _TypesError(_TypeError):
    '''(INTERNAL) Format a C{TypeError} without exception chaining.
    '''
    def __init__(self, name, value, *Types):
        t = _not_(_an(_or(*(t.__name__ for t in Types))))
        _TypeError.__init__(self, name, value, txt=t)


class _ValueError(ValueError):
    '''(INTERNAL) Format a C{ValueError} without exception chaining.
    '''
    def __init__(self, *name_value, **txt_name_values):  # name, value, txt=_invalid_
        _error_init(ValueError, self, name_value, **txt_name_values)


class CrossError(_ValueError):
    '''Error raised for zero or near-zero vectorial cross products,
       occurring for coincident or colinear points, paths or bearings.
    '''
    pass


class IntersectionError(_ValueError):
    '''Error raised for path or circle intersection issues.
    '''
    def __init__(self, txt=_invalid_, **kwds):
        '''New L{IntersectionError}.
        '''
        _ValueError.__init__(self, txt=txt, **kwds)


class LenError(_ValueError):
    '''Error raised for mis-matching C{len} values.
    '''
    def __init__(self, where, **lens_txt):  # txt=None
        '''New L{LenError}.

           @arg where: Object with C{.__name__} attribute
                       (C{class}, C{method}, or C{function}).
           @kwarg lens_txt: Two or more C{name=len(name)} pairs
                            (C{keyword arguments}).
        '''
        from pygeodesy.streprs import Fmt as _Fmt
        x = _xkwds_pop(lens_txt, txt=_invalid_)
        ns, vs = zip(*sorted(lens_txt.items()))
        ns = _COMMASPACE_.join(ns)
        vs = ' vs '.join(map(str, vs))
        t  = _SPACE_(_Fmt.PAREN(where.__name__, ns), _len_, vs)
        _ValueError.__init__(self, t, txt=x)


class LimitError(_ValueError):
    '''Error raised for lat- or longitudinal deltas exceeding
       the B{C{limit}} in functions L{equirectangular} and
       L{equirectangular_} and C{nearestOn*} and C{simplify*}
       functions or methods.
    '''
    pass


class ParseError(_ValueError):
    '''Error parsing degrees, radians or several other formats.
    '''
    pass


class PointsError(_ValueError):
    '''Error for an insufficient number of points.
    '''
    pass


class RangeError(_ValueError):
    '''Error raised for lat- or longitude values outside the B{C{clip}},
       B{C{clipLat}}, B{C{clipLon}} or B{C{limit}} range in function
       L{clipDegrees}, L{clipRadians}, L{parse3llh}, L{parseDMS},
       L{parseDMS2} or L{parseRad}.

       @see: Function L{rangerrors}.
    '''
    pass


class SciPyError(PointsError):
    '''Error raised for C{SciPy} errors.
    '''
    pass


class SciPyWarning(PointsError):
    '''Error thrown for C{SciPy} warnings.

       To raise C{SciPy} warnings as L{SciPyWarning} exceptions, Python
       C{warnings} must be filtered as U{warnings.filterwarnings('error')
       <https://docs.Python.org/3/library/warnings.html#the-warnings-filter>}
       I{prior to} C{import scipy} or by setting environment variable
       U{PYTHONWARNINGS<https://docs.Python.org/3/using/cmdline.html
       #envvar-PYTHONWARNINGS>} or with C{python} command line option
       U{-W<https://docs.Python.org/3/using/cmdline.html#cmdoption-w>}
       as C{error}.
    '''
    pass


class TRFError(_ValueError):
    '''Terrestrial Reference Frame (TRF), L{Epoch}, L{RefFrame}
       or L{RefFrame} conversion issue.
    '''
    pass


class UnitError(_ValueError):
    '''Default exception for L{units} issues.
    '''
    pass


def _an(noun):
    '''(INTERNAL) Prepend an article to a noun based
       on the pronounciation of the first letter.
    '''
    return _SPACE_((_an_ if noun[:1].lower() in 'aeinoux' else _a_), noun)


def crosserrors(raiser=None):
    '''Report or ignore vectorial cross product errors.

       @kwarg raiser: Use C{True} to throw or C{False} to ignore
                      L{CrossError} exceptions.  Use C{None} to
                      leave the setting unchanged.

       @return: Previous setting (C{bool}).

       @see: Property C{Vector3d.crosserrors}.
    '''
    from pygeodesy.vector3d import Vector3d
    t = Vector3d._crosserrors  # XXX class attr!
    if raiser in (True, False):
        Vector3d._crosserrors = raiser
    return t


def _datum_datum(datum1, datum2, Error=None):
    '''(INTERNAL) Check for datum or ellipsoid match.
    '''
    if Error:
        E1, E2 = datum1.ellipsoid, datum2.ellipsoid
        if E1 != E2:
            raise Error(E2.named2, txt=_incompatible(E1.named2))
    elif datum1 != datum2:
        t = _SPACE_(_datum_, repr(datum1.name), _not_, repr(datum2.name))
        raise _AssertionError(t)


def _error_init(Error, inst, name_value, fmt_name_value='%s (%r)',
                                         txt=_invalid_, **name_values):  # by .lazily
    '''(INTERNAL) Format an error text and initialize an C{Error} instance.

       @arg Error: The error super-class (C{Exception}).
       @arg inst: Sub-class instance to be initialized (C{_Exception}).
       @arg name_value: Either just a value or several name, value, ...
                        positional arguments (C{str}, any C{type}), in
                        particular for name conflicts with keyword
                        arguments of C{error_init} or which can't be
                        used as C{name=value} keyword arguments.
       @kwarg name_value_fmt: Format for (name, value) (C{str}).
       @kwarg txt: Optional explanation of the error (C{str}).
       @kwarg name_values: One or more B{C{name=value}} pairs overriding
                           any B{C{name_value}} positional arguments.
    '''
    if name_values:
        t = _or(*sorted(fmt_name_value % t for t in name_values.items()))
    elif len(name_value) > 1:
        t = _or(*sorted(fmt_name_value % t for t in zip(name_value[0::2],
                                                        name_value[1::2])))
    elif name_value:
        t = str(name_value[0])
    else:
        t = _SPACE_(_name_value_, str(MISSING))

    if txt is None:
        x = NN
    else:
        x =  str(txt) or _invalid_
        c = _COMMA_ if _COLON_ in t else _COLON_
        t = _SPACE_(t + c, x)
    Error.__init__(inst, t)
#   inst.__x_txt__ = x  # hold explanation
    _error_chain(inst)  # no Python 3+ exception chaining
    _error_under(inst)


def _error_under(inst):
    '''(INTERNAL) Remove leading underscore from instance' class name.
    '''
    n = inst.__class__.__name__
    if n.startswith(_UNDER_):
        inst.__class__.__name__ = n.lstrip(_UNDER_)
    return inst


def exception_chaining(error=None):
    '''Get the previous exception's or exception chaining setting.

       @kwarg error: An error instance (C{Exception}) or C{None}.

       @return: If B{C{error=None}}, return C{True} if exception
                chaining is enabled for PyGeodesy errors, C{False}
                if turned off and C{None} if not available.  If
                B{C{error}} is not C{None}, return the previous,
                chained error or C{None} otherwise.

       @note: Set C{env} variable C{PYGEODESY_EXCEPTION_CHAINING}
              to any non-empty value prior to C{import pygeodesy}
              to enable exception chaining for C{pygeodesy} errors.
    '''
    return _exception_chaining if error is None else \
            getattr(error, '__cause__', None)


def _incompatible(this):
    '''(INTERNAL) Format an incompatible text.
    '''
    return 'incompatible with ' + str(this)


def _InvalidError(Error=_ValueError, **txt_name_values):  # txt=_invalid_, name=value [, ...]
    '''(INTERNAL) Create an C{Error} instance.

       @kwarg Error: The error class or sub-class (C{Exception}).
       @kwarg txt_name_values: One or more B{C{name=value}} pairs
                               and optionally, a B{C{txt=...}}
                               keyword argument to override the
                               default B{C{txt='invalid'}}

       @return: An B{C{Error}} instance.
    '''
    try:
        e = Error(**txt_name_values)
    except TypeError:  # std *Error takes no keyword arguments
        e = _ValueError(**txt_name_values)
        e = Error(str(e))
        _error_chain(e)
        _error_under(e)
    return e


def _IsnotError(*nouns, **name_value_Error):  # name=value [, Error=TypeeError]
    '''Create a C{TypeError} for an invalid C{name=value} type.

       @arg nouns: One or more expected class or type names,
                   usually nouns (C{str}).
       @kwarg name_value_Error: One B{C{name=value}} pair and
                                optionally, an B{C{Error=...}}
                                keyword argument to override
                                the default B{C{Error=TypeError}}.

       @return: A C{TypeError} or an B{C{Error}} instance.
    '''
    from pygeodesy.streprs import Fmt as _Fmt
    Error = _xkwds_pop(name_value_Error, Error=TypeError)
    n, v  = _xkwds_popitem(name_value_Error) if name_value_Error else (
                          _name_value_, MISSING)  # XXX else tuple(...)
    t = _or(*nouns) or _specified_
    if len(nouns) > 1:
        t = _an(t)
    e = Error(_SPACE_(n, _Fmt.PAREN(repr(v)), _not_, t))
    _error_chain(e)
    _error_under(e)
    return e


def limiterrors(raiser=None):
    '''Get/set the throwing of L{LimitError}s.

       @kwarg raiser: Choose C{True} to raise or C{False} to
                      ignore L{LimitError} exceptions.  Use
                      C{None} to leave the setting unchanged.

       @return: Previous setting (C{bool}).
    '''
    global _limiterrors
    t = _limiterrors
    if raiser in (True, False):
        _limiterrors = raiser
    return t


def _or(*words):
    '''(INTERNAL) Join C{words} with C{", "} and C{" or "}.
    '''
    t, w = NN, list(words)
    if w:
        t = w.pop()
        if w:
            w = _COMMASPACE_.join(w)
            t = _SPACE_(w, _or_, t)
    return t


def _parseX(parser, *args, **name_values_Error):  # name=value[, ..., Error=ParseError]
    '''(INTERNAL) Invoke a parser and handle exceptions.

       @arg parser: The parser (C{callable}).
       @arg args: Any parser positional arguments (any C{type}s).
       @kwarg name_values_Error: One or more B{C{name=value}} pairs
                                 and optionally, an B{C{Error=...}}
                                 keyword argument to override the
                                 default B{C{Error=ParseError}}.

       @return: Parser result.

       @raise ParseError: Or the specified B{C{Error=...}}.

       @raise RangeError: If that error occurred.
    '''
    try:
        return parser(*args)

    except RangeError as x:
        t = str(x)
        E = type(x)
        _ = _xkwds_pop(name_values_Error, Error=None)
    except (AttributeError, IndexError, TypeError, ValueError) as x:
        t = str(x)
        E = _xkwds_pop(name_values_Error, Error=ParseError)
    raise _InvalidError(Error=E, txt=t, **name_values_Error)


def rangerrors(raiser=None):
    '''Get/set the throwing of L{RangeError}s.

       @kwarg raiser: Choose C{True} to raise or C{False} to ignore
                      L{RangeError} exceptions.  Use C{None} to leave
                      the setting unchanged.

       @return: Previous setting (C{bool}).
    '''
    global _rangerrors
    t = _rangerrors
    if raiser in (True, False):
        _rangerrors = raiser
    return t


def _SciPyIssue(x, *extras):  # PYCHOK no cover
    t = map(str, extras) if extras else []
    t = _SPACE_.join(str(x).strip().split() + t)
    if isinstance(x, (RuntimeWarning, UserWarning)):
        X = SciPyWarning
    else:
        X = SciPyError  # PYCHOK not really
    return _error_chain(X(t), other=x)


def _xellipsoidal(**name_value):
    '''(INTERNAL) Check an I{ellipsoidal} item.

       @return: The B{C{value}} if ellipsoidal.

       @raise TypeError: Not ellipsoidal B{C{value}}.
    '''
    try:
        for n, v in name_value.items():
            if v.isEllipsoidal:
                return v
            break
        else:
            n = v = MISSING
    except AttributeError:
        pass
    raise _TypeError(n, v, txt=_not_(_ellipsoidal_))


try:
    _ = {}.__or__  # Python 3.9+

    def _xkwds(kwds, **dflts):
        '''(INTERNAL) Override C{dflts} with specified C{kwds}.
        '''
        return (dflts | kwds) if kwds else dflts

except AttributeError:

    from copy import copy as _copy

    def _xkwds(kwds, **dflts):  # PYCHOK expected
        '''(INTERNAL) Override C{dflts} with specified C{kwds}.
        '''
        d = dflts
        if kwds:
            d = _copy(d)
            d.update(kwds)
        return d


def _xkwds_Error(_xkwds_func, kwds, name_txt, txt='default'):
    # Helper for _xkwds_get and _xkwds_pop below
    from pygeodesy.streprs import Fmt, pairs
    f = _COMMASPACE_.join(pairs(kwds) + pairs(name_txt))
    f =  Fmt.PAREN(_xkwds_func.__name__, f)
    t = _multiple_ if name_txt else _no_
    t = _SPACE_(t, _EQUAL_(_name_, txt), 'kwargs')
    return _AssertionError(f, txt=t)


def _xkwds_get(kwds, **name_default):
    '''(INTERNAL) Get a C{kwds} value by C{name}, or the C{default}.
    '''
    if len(name_default) == 1:
        for n, d in name_default.items():
            return kwds.get(n, d)

    raise _xkwds_Error(_xkwds_get, kwds, name_default)


def _xkwds_pop(kwds, **name_default):
    '''(INTERNAL) Pop a C{kwds} value by C{name}, or the C{default}.
    '''
    if len(name_default) == 1:
        return kwds.pop(*name_default.popitem())

    raise _xkwds_Error(_xkwds_pop, kwds, name_default)


def _xkwds_popitem(name_value):
    '''(INTERNAL) Return exactly one C{(name, value)} item.
    '''
    t = name_value.popitem()  # XXX AttributeError, KeyError
    if not name_value:
        return t

    raise _xkwds_Error(_xkwds_popitem, (t,), name_value, txt='value')


def _xkwds_strs(kwds):
    '''(INTERNAL) Force C{kwds} keys to C{str}.
    '''
    return dict(sorted((str(k), v) for k, v in kwds.items()))

# **) MIT License
#
# Copyright (C) 2016-2020 -- mrJean1 at Gmail -- All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
