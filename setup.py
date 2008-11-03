#!/usr/bin/env python

# Shoebot setup script
#
# 'python setup.py install', or
# 'python setup.py --help' for more options

from distutils.core import setup
import os

# dir globbing approach taken from Mercurial's setup.py
datafiles = [(os.path.join('share/shoebot/', root) ,[os.path.join(root, file_)
for file_ in files]) for root,dir,files in os.walk('examples')]
datafiles.append(('share/pixmaps', ['assets/icon.png']))
datafiles.append(('share/applications', ['assets/shoebot-ide.desktop']))

setup(name = "shoebot",
    version = "0.1",
    description = "A vector graphics scripting application",
    author = "Ricardo Lafuente",
    author_email = "r@sollec.org",
    license = 'GPL v3',
    url = "http://tinkerhouse.net/shoebot",
    packages = ["shoebot"],
    data_files = datafiles,
    scripts = ["sbot", "shoebot-ide"],
    long_description = """
 Shoebot is a pure Python graphics robot: It takes a Python script as input,
 which describes a drawing process, and outputs a graphic in a common open
 standard format (SVG, PDF, PostScript, or PNG). It has a simple text editor
 GUI, and scripts can describe their own GUIs for controlling variables
 interactively. Being pure Python, it can also be used as a Python module,
 a plugin for Python-scriptable tools such as Inkscape, and run from the
 command line.

"""
)

