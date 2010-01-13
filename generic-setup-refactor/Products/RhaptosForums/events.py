"""
events.py - event handlers.

Author: Hedley Roos (hedley@upfrontsystems.co.za)
Copyright (C) 2007 Rice University. All rights reserved.

This software is subject to the provisions of the GNU Lesser General
Public License Version 2.1 (LGPL).  See LICENSE.txt for details.
"""

from Products.CMFCore.utils import getToolByName

def afterTransitionContentSelectionLens(lens, event):
    """
    Modify the lens_forum item contained in lens's workflow
    state if needed.
    """

    def force_review_state(forum, review_state):
        """
        Force the review state since the Owner is never allowed
        to perform a transition.
        """
        info = wf.getInfoFor(forum, 'review_history')
        di = info[-1].copy()
        di['review_state'] = review_state
        wf.setStatusOf('ploneboard_forum_workflow', forum, di)
        # Set review history
        forum.workflow_history['ploneboard_forum_workflow'] = tuple(list(info) + [di])
        forum.reindexObject(idxs=['review_state'])      

    if lens.isTemporary():
        return
    # Forums are created lazily, so check for existence
    if 'lens_forum' not in lens.objectIds():
        return
    
    forum = lens._getOb('lens_forum')

    wf = getToolByName(lens, 'portal_workflow')
    lens_review_state = wf.getInfoFor(lens, 'review_state')
    forum_review_state = wf.getInfoFor(forum, 'review_state')

    if (lens_review_state in ('private', 'private_open')) and (forum_review_state != 'private'):
        force_review_state(forum, 'private')
        return

    if (lens_review_state in ('published', 'published_open')) and (forum_review_state != 'memberposting'):
        force_review_state(forum, 'memberposting')
        return
