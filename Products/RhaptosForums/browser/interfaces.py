from zope.interface import Interface
from zope.browser.interfaces import IBrowserView

class ICreateForum(IBrowserView):
    """ 
    Create forum view
    """

    def doit(self, id):
        """
        Create PloneboardForum in context and return newly created object
        """
