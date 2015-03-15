# PyMinuit #
_Minuit numerical function minimization in Python_

**Before you start:** note that PyMinuit has been re-written by Christoph Deil and Piti Ongmongkolkul for modern systems, yet with the same interface: their project is called [iminuit](http://iminuit.github.io/iminuit/index.html).  PyMinuit is over 6 years old with little development since the initial product.  If PyMinuit doesn't work on your newfangled operating system or you want better IPython or Cython integration (or just the satisfaction of using actively maintained code), try iminuit.

## Minuit ##

Minuit has been the standard package for minimizing general N-dimensional functions in high-energy physics since its introduction in 1972.  It features a robust set of algorithms for optimizing the search, correcting mistakes, and measuring non-linear error bounds.  It is the minimization engine used behind-the-scenes in most high-energy physics curve fitting applications.

**New:** more robust [installation instructions](HowToInstall.md)!

**New:** version 1.2.1 should work with Python 3.

## Python interface ##

PyMinuit is an extension module for Python that passes low-level Minuit functionality to Python functions.  Interaction and data exploration is more user-friendly, in the sense that the user is protected from segmentation faults and index errors, parameters are referenced by their names, even in correlation matrices, and Python exceptions can be passed from the objective function during the minimization process.  This extension module also makes it easier to calculate Minos errors and contour curves at an arbitrary number of sigmas from the minimum, and features a new N-dimensional scanning utility.

## PyMinuit versus PyMinuit2 versus iminuit ##

There are two versions of Minuit, both of which are C++ re-writes of the original Fortran Minuit.  The first of these, "[SEAL-Minuit](http://seal.web.cern.ch/seal/snapshot/work-packages/mathlibs/minuit/)", is an independent software package that has all the functionality of the original Minuit, but is no longer maintained.  The second, "[Minuit2](http://seal.web.cern.ch/seal/MathLibs/5_0_8/Minuit2/html/)", is a part of the [ROOT](http://root.cern.ch) package and is actively being developed.  There are correspondingly two versions of PyMinuit, which appeal to different users:

  * PyMinuit (this package): contains SEAL-Minuit 1.7.9 and the Python interface to it; installs in one step.  Use this if you don't have ROOT (or don't know what it is) and you just want to find the minimum of functions.

  * [PyMinuit2](http://code.google.com/p/pyminuit2) (click the link): only contains an interface to Minuit2 and must be linked to an existing ROOT distribution.  Use this if you want to use the algorithms contained in a specific ROOT version.

PyMinuit and PyMinuit2 present the same interface to the Python user, so the documentation on this site applies to PyMinuit2. See [Minuit2Features](http://code.google.com/p/pyminuit2/wiki/Minuit2Features) for extra features specific to PyMinuit2.

**New:** If you're using IPython (notebook interface) or Cython (compiler-optimized Python), take a look at [iminuit](http://iminuit.github.io/iminuit/index.html).  It is a separate project (that I'm not involved in and, until recently, didn't know about) to provide this same interface with better support for modern Python-based analysis tools.  It could be especially useful for speeding up evaluation of the objective function by orders of magnitude.  PyMinuit calls the objective function using the Python interpreter, but iminuit can call the objective function as compiled C code.

## Examples ##

Here is an example interactive session.  See [Features](Features.md) for a complete list of features.
```
>>> import minuit
```
Provide any function or lambda expression
```
>>> def f(x, y):
...   return ((x-2) / 3)**2 + y**2 + y**4
... 
>>> m = minuit.Minuit(f, x=10, y=10)
```
Watch the minimization call-by-call
```
>>> m.printMode = 1
>>> m.migrad()
  FCN Result | Parameter values
-------------+--------------------------------------------------------
     10107.1 |           10           10
     10107.1 |      10.0049           10
     10107.1 |      9.99509           10
  .
    .
      .

 1.49272e-06 |      2.00231  0.000948002
 1.16063e-06 |      2.00231  0.000752745
 3.37671e-06 |      2.00378   0.00133852
>>> m.printMode = 0
```
Access all the fit information
```
>>> m.fval, m.ncalls, m.edm
(3.376717443623469e-06, 72, 1.317141520434002e-06)
>>> m.values["x"], m.values["y"]
(2.0023781572817986, 0.00133852332346628303)
```
Full parameter errors with correlations
```
>>> m.hesse()
>>> m.errors
{'y': 0.99999733060860929, 'x': 2.9999999999998779}
>>> m.covariance
{('y', 'x'): 3.17636386e-16, ('x', 'y'): 3.17636386e-16, ('y', 'y'): 0.99999466122434422, ('x', 'x'): 8.9999999999992681}
>>> m.matrix(correlation=True)
((1.0, 1.0587907808231194e-16), (1.0587907808231194e-16, 1.0))
```
Non-linear error measurement
```
>>> m.minos()
>>> m.merrors
{('y', 1.0): 0.78583633002473874, ('y', -1.0): -0.78583633325395974, ('x', -1.0): -3.0, ('x', 1.0): 3.0000000000000004}
```
Contour lines and scans for plots
```
>>> m.contour("x", "y", 1.)
[(-1.0, 1.6093607605426052e-09), (-0.77000687450165384, -0.35921924433026176), (-0.38156620163194066, -0.53542692886885834), ...]
>>> m.scan(("x", 5, 0, 10), ("y", 5, 0, 10), corners=True)
[[5.9400792175e-07, 20.000000594007922, 272.00000059400793, 1332.0000005940078, 4160.0000005940083], [5.9400792175e-07, ...]]
```

## Versions and system requirements ##

PyMinuit requires Python 2.4 or later, and has been tested on Linux and Windows.  In principle, it should also compile and run on Mac OS X or any other Unix-based operating system.