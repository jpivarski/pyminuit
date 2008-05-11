#!/usr/bin/env python

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
                             library_dirs=[os.path.join("Minuit-1_7_9", "src", ".libs")],
                             libraries=["lcg_Minuit"],
                             include_dirs=[os.path.join("Minuit-1_7_9")]
                             )])

