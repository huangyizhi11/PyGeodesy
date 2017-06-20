
# -*- coding: utf-8 -*-

# Script to run some or all PyGeodesy tests with Python 2 or 3.

# Tested with 64-bit Python 3.6.1 on macOS 10.12.5 Sierra and
# with Pythonista 3.1 on iOS 10.3.2.

from glob import glob
from os import linesep as NL
from os.path import abspath, dirname, join
from time import time
import sys

_test_dir = dirname(abspath(__file__))
# extend sys.path to include the .. directory
if _test_dir not in sys.path:
    sys.path.insert(0, _test_dir)

from base import isiOS, PyGeodesy_dir, Python_O, \
          runs, tilda, versions  # PYCHOK expected

__all__ = ()
__version__ = '17.06.19'

# command line options
_failedonly = False
_raiser     = False
_results    = False
_verbose    = False

if __name__ == '__main__':  # MCCABE 25

    def _write(text):
        _results.write(text.encode('utf-8'))

    argv0, args = tilda(sys.argv[0]), sys.argv[1:]

    if isiOS and not args:
        # allow this script to be used
        # with options inside Pythonista
        try:
            _input = raw_input  # old name
        except NameError:  # Python 3+
            _input = input
        args = _input('enter %s args: ' % (argv0,)).split()

    while args and args[0].startswith('-'):
        arg = args.pop(0)
        if '-help'.startswith(arg):
            print('usage: %s [-failedonly] [-raiser] [-results] [-verbose] [test/test...py ...]' % (argv0,))
            sys.exit(0)
        elif '-failedonly'.startswith(arg):
            _failedonly = True
        elif '-raiser'.startswith(arg):
            _raiser = True  # break on error
        elif '-results'.startswith(arg):
            _results = True
        elif '-verbose'.startswith(arg):
            _verbose = True
        else:
            print('%s invalid option: %s' % (argv0, arg))
            sys.exit(1)

    # shorten Python path [-OO]
    if len(Python_O) > 32:
        Python_O = Python_O[:16] + '...' + Python_O[-16:]

    # PyGeodesy and Python versions, size, OS name and release
    v = versions()

#   import pygeodesy
#   v = ' '.join((v, tilda(pygeodesy.__file__)))

    if _results:  # save all test results
        t = '-'.join(['testresults'] + v.split()) + '.txt'
        t = join(PyGeodesy_dir, 'testresults', t)
        _results = open(t, 'wb')  # note, 'b' not 't'!
        _write('%s typical test results (%s)%s' % (argv0, v, NL))

    if not args:  # no tests specified, get all test*.py
        # scripts in the same directory as this one
        args = sorted(glob(join(_test_dir, 'test*.py')))

    T, X, s = 0, 0, time()
    for arg in args:

        t = tilda('running %s %s' % (Python_O, arg))
        print(t)

        x, r = runs(arg)
        X += x  # failures, excl KNOWN ones

        if _results:
            _write(NL + t + NL)
            _write(r)

        if not X:  # count tests
            T += r.count('\n    test ')

        if 'Traceback' in r:
            print('%s\n' % (r,))
            if not x:  # count as failure
                X += 1
            if _raiser:
                break

        elif _failedonly:
            for t in r.split('\n'):
                # print failures and totals
                if 'FAILED' in t or 'passed' in t:
                    print(t.rstrip())
            print('')

        elif _verbose:
            print('%s\n' % (r,))

    if X:
        x = '%d FAILED' % (X,)
    elif T > 0:
        x = 'all %s tests OK' % (T,)
    else:
        x = 'all OK'
    s = time() - s
    t = '%s %s %s (%s) %.3f sec' % (argv0, Python_O, x, v, s)
    print(t)
    if _results:
        _write(NL + t + NL)
        _results.close()