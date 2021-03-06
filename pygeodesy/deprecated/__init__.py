
# -*- coding: utf-8 -*-

u'''DEPRECATED classes, functions, etc. exported for backward compatibility,
including deprecated modules C{pygeodesy.bases}, C{pygeodesy.datum} and
C{pygeodesy,nvector}, previously inside the C{pygeodesy} package.

Use either C{from pygeodesy import bases} or C{from pygeodesy.deprecated import
bases}.  Likewise for C{datum} and C{nvector}.
'''
from pygeodesy.heights import HeightIDWequirectangular as _HeightIDWequirectangular, \
                              HeightIDWeuclidean as _HeightIDWeuclidean, \
                              HeightIDWhaversine as _HeightIDWhaversine
from pygeodesy.errors import TRFError as _TRFError
from pygeodesy.interns import EPS, NN, R_M, _COMMASPACE_, _easting_, _hemipole_, \
                             _northing_, _scalar_, _sep_, _SPACE_,  _UNDER_, _zone_
from pygeodesy.lazily import _ALL_LAZY, isLazy
from pygeodesy.named import _NamedTuple
from pygeodesy.streprs import Fmt as _Fmt
from pygeodesy.units import Easting, Northing, Str
if isLazy:  # force import of the deprecated modules
    import pygeodesy.deprecated.bases as bases, \
           pygeodesy.deprecated.datum as datum, \
           pygeodesy.deprecated.nvector as nvector  # PYCHOK unused

__all__ = _ALL_LAZY.deprecated
__version__ = '20.11.05'

OK      = 'OK'  # OK for test like I{if ... is OK: ...}
_value_ = 'value'
_WGS84  = _UTM = object()


# DEPRECATED classes, for export only
class HeightIDW(_HeightIDWeuclidean):  # PYCHOK exported
    '''DEPRECATED, use class L{HeightIDWeuclidean}.
    '''
    pass


class HeightIDW2(_HeightIDWequirectangular):  # PYCHOK exported
    '''DEPRECATED, use class L{HeightIDWequirectangular}.
    '''
    pass


class HeightIDW3(_HeightIDWhaversine):  # PYCHOK exported
    '''DEPRECATED, use class L{HeightIDWhaversine}.
    '''
    pass


class RefFrameError(_TRFError):  # PYCHOK exported
    '''DEPRECATED, use class L{TRFError}.
    '''
    pass


class UtmUps4Tuple(_NamedTuple):
    '''OBSOLETE, expect a L{UtmUps5Tuple} from method C{Mgrs.toUtm(utm=None)}.

       4-Tuple C{(zone, hemipole, easting, northing)} as C{str},
       C{str}, C{meter} and C{meter}.
    '''
    _Names_ = (_zone_, _hemipole_, _easting_, _northing_)  # band
    _Units_ = ( Str,    Str,        Easting,   Northing)


def anStr(name, OKd='._-', sub=_UNDER_):
    '''DEPRECATED, use function L{anstr}.
    '''
    from pygeodesy.streprs import anstr
    return anstr(name, OKd=OKd, sub=sub)


def areaof(points, adjust=True, radius=R_M, wrap=True):
    '''DEPRECATED, use function L{areaOf}.
    '''
    from pygeodesy.points import areaOf
    return areaOf(points, adjust=adjust, radius=radius, wrap=wrap)


def bounds(points, wrap=True, LatLon=None):
    '''DEPRECATED, use function L{boundsOf}.

       @return: 2-Tuple C{(latlonSW, latlonNE)} as B{C{LatLon}}
                or 4-Tuple C{(latS, lonW, latN, lonE)} if
                B{C{LatLon}} is C{None}.
    '''
    from pygeodesy.points import boundsOf
    return tuple(boundsOf(points, wrap=wrap, LatLon=LatLon))


def clipDMS(deg, limit):  # PYCHOK no cover
    '''DEPRECATED, use function L{clipDegrees}.
    '''
    from pygeodesy.dms import clipDegrees
    return clipDegrees(deg, limit)


def clipStr(bstr, limit=50, white=NN):
    '''DEPRECATED, use function L{clips}.
    '''
    from pygeodesy.basics import clips
    return clips(bstr, limit=limit, white=white)


def decodeEPSG2(arg):
    '''DEPRECATED, use function L{epsg.decode2}.

       @return: 2-Tuple C{(zone, hemipole)}
    '''
    from pygeodesy.epsg import decode2
    return tuple(decode2(arg))


def encodeEPSG(zone, hemipole=NN, band=NN):
    '''DEPRECATED, use function L{epsg.encode}.

       @return: C{EPSG} code (C{int}).
    '''
    from pygeodesy.epsg import encode
    return int(encode(zone, hemipole=hemipole, band=band))


def enStr2(easting, northing, prec, *extras):  # PYCHOK no cover
    '''DEPRECATED, use function L{enstr2}.
    '''
    from pygeodesy.streprs import enstr2
    return enstr2(easting, northing, prec, *extras)


def equirectangular3(lat1, lon1, lat2, lon2, **options):
    '''DEPRECATED, use function C{equirectangular_}.

       @return: 3-Tuple C{(distance2, delta_lat, delta_lon)}.
    '''
    from pygeodesy.formy import equirectangular_
    return tuple(equirectangular_(lat1, lon1, lat2, lon2, **options)[:3])


def false2f(value, name=_value_, false=True, Error=ValueError):  # PYCHOK no cover
    '''DEPRECATED, use function L{falsed2f}.
    '''
    return falsed2f(falsed=false, Error=Error, **{name: value})


def falsed2f(falsed=True, Error=ValueError, **name_value):  # PYCHOK no cover
    '''DEPRECATED, use class L{Easting} or L{Northing}.

       Convert a falsed east-/northing to non-negative C{float}.

       @kwarg falsed: Value includes false origin (C{bool}).
       @kwarg Error: Optional, overriding error (C{Exception}).
       @kwarg name_value: One B{C{name=value}} pair.

       @return: The value (C{float}).

       @raise Error: Invalid or negative B{C{name=value}}.
    '''
    t = NN
    if len(name_value) == 1:
        try:
            for f in name_value.values():
                f = float(f)
                if falsed and f < 0:
                    break
                return f
            t = 'falsed, negative'
        except (TypeError, ValueError) as x:
            t = str(x)
    from pygeodesy.errors import _InvalidError
    raise _InvalidError(Error=Error, txt=t, **name_value)


def fStr(floats, prec=6, fmt=_Fmt.f, ints=False, sep=_COMMASPACE_):
    '''DEPRECATED, use function L{fstr}.
    '''
    from pygeodesy.streprs import fstr
    return fstr(floats, prec=prec, fmt=fmt, ints=ints, sep=sep)


def fStrzs(floatstr):  # PYCHOK no cover
    '''DEPRECATED, use function L{fstrzs}.
    '''
    from pygeodesy.streprs import fstrzs
    return fstrzs(floatstr)


def hypot3(x, y, z):
    '''DEPRECATED, use function L{hypot_}.
    '''
    from pygeodesy.fmath import hypot_
    return hypot_(x, y, z)


def inStr(inst, *args, **kwds):  # PYCHOK no cover
    '''DEPRECATED, use function L{instr}.
    '''
    from pygeodesy.streprs import instr
    return instr(inst, *args, **kwds)


def isenclosedby(point, points, wrap=False):
    '''DEPRECATED, use function L{isenclosedBy}.
    '''
    from pygeodesy.points import isenclosedBy
    return isenclosedBy(point, points, wrap=wrap)


def joined(*words, **sep):  # sep=NN
    '''DEPRECATED, use C{NN(...)}, C{NN.join_} or C{B{sep}.join}.
    '''
    return sep.get(_sep_, NN).join(map(str, words))


def joined_(*words, **sep):  # sep=" "
    '''DEPRECATED, use C{_SPACE_(...)}, C{_SPACE_.join_} or C{B{sep}.join}.
    '''
    return sep.get(_sep_, _SPACE_).join(map(str, words))


def nearestOn3(point, points, closed=False, wrap=False, **options):
    '''DEPRECATED, use function L{nearestOn5}.

       @return: 3-Tuple C{(lat, lon, distance)}
    '''
    from pygeodesy.points import nearestOn5  # no name conflict
    return tuple(nearestOn5(point, points, closed=closed, wrap=wrap, **options)[:3])


def nearestOn4(point, points, closed=False, wrap=False, **options):
    '''DEPRECATED, use function L{nearestOn5}.

       @return: 4-Tuple C{(lat, lon, distance, angle)}
    '''
    from pygeodesy.points import nearestOn5  # no name conflict
    return tuple(nearestOn5(point, points, closed=closed, wrap=wrap, **options)[:4])


def parseUTM(strUTM, datum=_WGS84, Utm=_UTM, name=NN):  # PYCHOK datum
    '''DEPRECATED, use function L{parseUTM5}.

       @return: The UTM coordinate (B{L{Utm}}) or 4-tuple C{(zone,
                hemisphere, easting, northing)} if B{C{Utm}} is C{None}.
    '''
    from pygeodesy.datums import Datums  # PYCHOK shadows?
    from pygeodesy.utm import parseUTM5, Utm as _Utm
    d = Datums.WGS84 if datum is _WGS84 else datum  # PYCHOK shadows?
    U = _Utm if Utm is _UTM else Utm
    r = parseUTM5(strUTM, datum=d, Utm=U, name=name)
    if isinstance(r, tuple):  # UtmUps5Tuple
        r = r.zone, r.hemipole, r.easting, r.northing  # no band
    return r


def perimeterof(points, closed=False, adjust=True, radius=R_M, wrap=True):
    '''DEPRECATED, use function L{perimeterOf}.
    '''
    from pygeodesy.points import perimeterOf
    return perimeterOf(points, closed=closed, adjust=adjust, radius=radius, wrap=wrap)


def polygon(points, closed=True, base=None):
    '''DEPRECATED, use function L{points2}.
    '''
    from pygeodesy.deprecated.bases import points2  # PYCHOK deprecated
    return points2(points, closed=closed, base=base)


def scalar(value, low=EPS, high=1.0, name=_scalar_, Error=ValueError):  # PYCHOK no cover
    '''DEPRECATED, use class L{Number_} or L{Scalar_}.

       @arg value: The value (C{scalar}).
       @kwarg low: Optional lower bound (C{scalar}).
       @kwarg high: Optional upper bound (C{scalar}).
       @kwarg name: Optional name of value (C{str}).
       @kwarg Error: Exception to raise (C{ValueError}).

       @return: New value (C{float} or C{int} for C{int} B{C{low}}).

       @raise Error: Invalid B{C{value}}.
    '''
    from pygeodesy.basics import isint
    from pygeodesy.units import Number_, Scalar_
    C_ = Number_ if isint(low) else Scalar_
    return C_(value, name=name, Error=Error, low=low, high=high)


def simplify2(points, pipe, radius=R_M, shortest=False, indices=False, **options):
    '''DEPRECATED, use function L{simplifyRW}.
    '''
    from pygeodesy.simplify import simplifyRW
    return simplifyRW(points, pipe, radius=radius, shortest=shortest, indices=indices, **options)


def toUtm(latlon, lon=None, datum=None, Utm=_UTM, cmoff=True, name=NN):  # PYCHOK datum
    '''DEPRECATED, use function L{toUtm8}.

       @return: The UTM coordinate (B{C{Utm}}) or a 6-tuple C{(zone,
                easting, northing, band, convergence, scale)} if
                B{C{Utm}} is C{None} or B{C{cmoff}} is C{False}.
    '''
    from pygeodesy.utm import toUtm8, Utm as _Utm
    U = _Utm if Utm is _UTM else Utm
    r = toUtm8(latlon, lon=lon, datum=datum, Utm=U, name=name, falsed=cmoff)
    if isinstance(r, tuple):  # UtmUps8Tuple
        # no hemisphere/pole and datum
        r = r.zone, r.easting, r.northing, r.band, r.convergence, r.scale
    return r


def unStr(name, *args, **kwds):
    '''DEPRECATED, use function L{unstr}.
    '''
    from pygeodesy.streprs import unstr
    return unstr(name, *args, **kwds)


def utmZoneBand2(lat, lon):
    '''DEPRECATED, use function L{utmZoneBand5}.

       @return: 2-Tuple C{(zone, band)}.
    '''
    from pygeodesy.utm import utmZoneBand5
    r = utmZoneBand5(lat, lon)  # UtmUpsLatLon5Tuple
    return r.zone, r.band

# **) MIT License
#
# Copyright (C) 2018-2020 -- mrJean1 at Gmail -- All Rights Reserved.
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
