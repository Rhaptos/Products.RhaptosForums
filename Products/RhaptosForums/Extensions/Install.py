"""
Installation script for QuickInstaller use, including upgrades.

Author: Jurgen Blignaut (jurgen@upfrontsystems.co.za)
Copyright (C) 2008 Upfront Systems. All rights reserved.

This software is subject to the provisions of the GNU Lesser General
Public License Version 2.1 (LGPL).  See LICENSE.txt for details.
"""

from Products.RhaptosForums.config import PROJECTNAME, GLOBALS

from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.CMFCore.utils import getToolByName

from StringIO import StringIO
    

def install(self):
    """Install method for this product. 
    It should be kept idempotent; running it at any time should be safe.
    Also, necessary upgrades to existing data should be accomplished 
    with a reinstall (running this!) if at all possible.
    """

    out = StringIO()

    print >> out, "Installing dependent Products"
    quickinstaller = getToolByName (self, 'portal_quickinstaller')
    quickinstaller.installProduct('SimpleAttachment')
    quickinstaller.installProduct('Ploneboard')

    print >> out, "Starting %s install" % PROJECTNAME
    
    print >> out, "Installing subsksins"
    install_subskin(self, out, GLOBALS)

    print >> out, "Modifying allowed types for ContentSelectionLens"
    types_tool = getToolByName(self, 'portal_types')

    # remove Ploneboard from globally allowed content types
    fti = types_tool.getTypeInfo('Ploneboard')
    fti.global_allow = False
    
    print >> out, "Adding Ploneboard permissions"
    # add permissions
    self.manage_permission('Ploneboard: Add Forum', \
            ('Manager',), acquire=1)
    self.manage_permission('Ploneboard: Add Comment', \
            ('Manager','Owner', 'Member'), acquire=1)
    self.manage_permission('Ploneboard: Add Comment Attachment', \
            ('Manager','Owner', 'Member'), acquire=1)
    self.manage_permission('Ploneboard: Add Conversation', \
            ('Manager','Owner', 'Member'), acquire=1)

    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()
