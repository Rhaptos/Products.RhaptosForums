from zope.interface import Interface
from zope.app.publisher.interfaces.browser import IBrowserView

class ICreateForum(IBrowserView):
    """ 
    Create forum view
    """

    def doit(self, id):
        """
        Create PloneboardForum in context and return newly created object
        """
