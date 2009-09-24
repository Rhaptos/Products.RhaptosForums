
from Products.CMFCore.utils import getToolByName
from Products.SimpleAttachment.setuphandlers import registerAttachmentsFormControllerActions
from Products.SimpleAttachment.setuphandlers import registerImagesFormControllerActions

def setupRhaptosForums(context):
    if context.readDataFile('rhaptosforums.txt') is None:
        return

    portal = context.getSite()
    portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
    portal_types = getToolByName(portal, 'portal_types')

    registerAttachmentsFormControllerActions(portal)
    registerImagesFormControllerActions(portal)

    portal_quickinstaller.installProduct('Ploneboard')

    # remove Ploneboard from globally allowed content types
    fti = portal_types.getTypeInfo('Ploneboard')
    fti.global_allow = False
