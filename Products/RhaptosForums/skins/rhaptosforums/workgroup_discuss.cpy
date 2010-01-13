## Script (Python) "workgroup_discuss"
##parameters=
##
## Ensure a dicsussion forum exists for the workgroup that is our context.

import logging
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger()
if context.get('workgroup_forum', None) is None:
    #context.invokeFactory('PloneboardForum', 'workgroup_forum') 
    context.restrictedTraverse('@@RhaptosForums.create-forum')('workgroup_forum')
    forum = getattr(context, 'workgroup_forum', None)
    if forum is not None:
        # Make forum private to members only
        wf = getToolByName(context, 'portal_workflow')
        wf.doActionFor(forum, 'make_private')
        # Edit. Also does a reindex.
        new_title = "%s Forum" % forum.aq_parent.Title()
        forum.edit(title=new_title) 

return state
