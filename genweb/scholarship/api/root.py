# -*- coding: utf-8 -*-
from five import grok
from zope.event import notify

from Products.CMFPlone.interfaces import IPloneSiteRoot

from infrae.rest.components import ALLOWED_REST_METHODS
from infrae.rest.components import lookupREST
from infrae.rest.interfaces import RESTMethodPublishedEvent
from genweb.scholarship.api import queryRESTComponent
from zExceptions import NotFound


class APIRoot(grok.View):
    grok.context(IPloneSiteRoot)
    grok.require('genweb.authenticated')
    grok.name('api')

    def publishTraverse(self, request, name):
        """You can traverse to a method called the same way that the
        HTTP method name, or a sub view
        """
        if name in ALLOWED_REST_METHODS and name == request.method:
            if hasattr(self, name):
                notify(RESTMethodPublishedEvent(self, name))
                return getattr(self, name)

        view = queryRESTComponent(
            (self, self.context),
            (self.context, request),
            name=name,
            parent=self)
        if view is None:
            raise NotFound(name)
        return view

    def render(self):
        return 'Genweb Scholarship REST API'
        return lookupREST(self.context, self.request, 'api_root')
