
from Products.CMFCore.utils import getToolByName
from Products.SimpleAttachment.setuphandlers import registerAttachmentsFormControllerActions
from Products.SimpleAttachment.setuphandlers import registerImagesFormControllerActions

def setupRhaptosForums(context):
    if context.readDataFile('rhaptosforums.txt') is None:
        return

    portal = context.getSite()
    portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
    portal_types = getToolByName(portal, 'portal_types')
    portal_setup = getToolByName(portal, 'portal_setup')

    import_context = portal_setup.getImportContextID()
    portal_setup.setImportContext(
            'profile-Products.SimpleAttachment:SimpleAttachment')
    portal_setup.runAllImportSteps()
    import_context = portal_setup.getImportContextID()

    registerAttachmentsFormControllerActions(portal)
    registerImagesFormControllerActions(portal)

    portal_quickinstaller.installProduct('Ploneboard')

    # remove Ploneboard from globally allowed content types
    fti = portal_types.getTypeInfo('Ploneboard')
    fti.global_allow = False
