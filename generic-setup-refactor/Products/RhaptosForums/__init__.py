"""
Initialization and package-wide constants.

Author: Jurgen Blignaut (jurgen@upfrontsytems.co.za)
Copyright (C) 2008 Upfront Systems. All rights reserved.

This software is subject to the provisions of the GNU Lesser General
Public License Version 2.1 (LGPL).  See LICENSE.txt for details.
"""

from Products.CMFCore.DirectoryView import registerDirectory

from config import SKINS_DIR, GLOBALS, PROJECTNAME


registerDirectory(SKINS_DIR, GLOBALS)
