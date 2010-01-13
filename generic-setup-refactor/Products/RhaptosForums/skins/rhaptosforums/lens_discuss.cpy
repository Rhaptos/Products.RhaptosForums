## Script (Python) "lens_discuss"
##parameters=
##
## Ensure a dicsussion forum exists for the lens that is our context.

import logging
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger()

if context.get('lens_forum', None) is None:
    #context.invokeFactory('PloneboardForum', 'lens_forum') 

    # create a forum if it does not exist
    context.restrictedTraverse('@@RhaptosForums.create-forum')('lens_forum')
    forum = getattr(context, 'lens_forum', None)
    if forum is not None:
        # Make forum private to members only if lens is private, else
        # leave in initial workflow state.
        wf = getToolByName(context, 'portal_workflow')
        lens = forum.aq_parent
        if wf.getInfoFor(lens, 'review_state') in ('private', 'private_open'):
            wf.doActionFor(forum, 'make_private')
        # Edit. Also does a reindex.
        new_title = "%s Forum" % forum.aq_parent.Title()
        forum.edit(title=new_title) 

return state
