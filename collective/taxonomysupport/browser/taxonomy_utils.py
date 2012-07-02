# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from collective.taxonomysupport.interfaces import ITaxonomyLevel
from Products.statusmessages.interfaces import IStatusMessage
from zope.interface import alsoProvides, noLongerProvides


class CheckTaxonomyAction(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def check_taxonomy_action_add(self):
        return not ITaxonomyLevel.providedBy(self.context)

    def check_taxonomy_action_remove(self):
        return ITaxonomyLevel.providedBy(self.context)


class ToggleMarkTaxonomyRoot(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def add_interface(self):
        messages = IStatusMessage(self.request)
        if not ITaxonomyLevel.providedBy(self.context):
            alsoProvides(self.context, ITaxonomyLevel)
            self.context.reindexObject()
            messages.addStatusMessage(u"L'oggetto è marcato come radice di tassonomia",
                                      type='info')
        else:
            messages.addStatusMessage(u"L'oggetto è già marcato come radice di tassonomia",
                                      type='warning')
        self.request.response.redirect(self.context.absolute_url())

    def remove_interface(self):
        messages = IStatusMessage(self.request)
        if ITaxonomyLevel.providedBy(self.context):
            noLongerProvides(self.context, ITaxonomyLevel)
            self.context.reindexObject()
            messages.addStatusMessage(u"L'oggetto non è più marcato come radice di tassonomia",
                                      type='info')
        else:
            messages.addStatusMessage(u"L'oggetto non era marcato come radice di tassonomia",
                                      type='warning')
        self.request.response.redirect(self.context.absolute_url())
