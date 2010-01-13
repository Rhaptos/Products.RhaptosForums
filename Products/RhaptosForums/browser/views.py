from zope.interface import implements
from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType

from interfaces import ICreateForum

class CreateForum(BrowserView):

    implements(ICreateForum)

    def doit(self, id):
        context = aq_inner(self.context)
        obj = _createObjectByType('PloneboardForum', context, id)
        pu = getToolByName(context, 'plone_utils')
        pu.changeOwnershipOf(obj, context.Creator())
        return obj

    __call__ = doit
