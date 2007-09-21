#!/usr/bin/env python

from distutils.core import setup, Extension
import os, subprocess

##################################################################################################

try:
  os.stat("Minuit-1_7_9")
except OSError:
  if not subprocess.call(["tar", "-xzvf", "Minuit-1_7_9.tar.gz"]) == 0:
    raise RuntimeError, "Could not untar Minuit 1.7.9.  Try doing it by hand first."

try:
  os.stat(os.path.join("Minuit-1_7_9", "config.h"))
except OSError:
  if not subprocess.call(["./configure"], cwd="Minuit-1_7_9") == 0:
    raise RuntimeError, "Could not configure Minuit 1.7.9.  Try doing it by hand first."

try:
  os.stat(os.path.join("Minuit-1_7_9", "src", ".libs"))
except OSError:
  if not subprocess.call(["make"], cwd="Minuit-1_7_9") == 0:
    raise RuntimeError, "Could not make Minuit 1.7.9.  Try doing it by hand first."

setup(name="pyMinuit",
      version="1.0.0",
      description="pyMinuit: Minuit interface for minimizing Python functions",
      author="Jim Pivarski",
      author_email="jpivarski@gmail.com",
      url="http://?",
      package_dir={"": "lib"},
      ext_modules=[Extension(os.path.join("minuit"),
                             [os.path.join("minuit.cpp")],
                             library_dirs=[os.path.join("Minuit-1_7_9", "src", ".libs")],
                             libraries=["lcg_Minuit"],
                             include_dirs=[os.path.join("Minuit-1_7_9")]
                             )])

