#!/usr/bin/env python

import sys, getopt

minuitdir = "../Minuit-1_7_9"
otherargs = []
for arg in sys.argv:
  if arg.find("with-minuit") != -1:
    optlist, argv = getopt.getopt([arg], "", ["with-minuit="])
    for name, value in optlist:
      if name == "--with-minuit":
        minuitdir = value
  else:
    otherargs.append(arg)
sys.argv = otherargs

print "************************************************************************************************"
print "Assuming Minuit directory is: %s" % minuitdir
print "************************************************************************************************"

from distutils.core import setup, Extension
import os, subprocess

##################################################################################################

setup(name="pyMinuit",
      version="1.0.2",
      description="pyMinuit: Minuit interface for minimizing Python functions",
      author="Jim Pivarski",
      author_email="jpivarski@gmail.com",
      url="http://code.google.com/p/pyminuit/",
      package_dir={"": "lib"},
      ext_modules=[Extension(os.path.join("minuit"),
                             [os.path.join("minuit.cpp")],
                             library_dirs=[os.path.join(minuitdir, "src", ".libs")],
                             libraries=["lcg_Minuit"],
                             include_dirs=[minuitdir]
                             )])
