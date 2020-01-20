# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from zope.interface import implements
from plone.directives import form
from plone.dexterity.content import Item
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from genweb.scholarship import _


class IScholarship(form.Schema):
    """ scholarship schema """

    title = schema.TextLine(
        title=_(u'title'),
        description=_(u'_description'),
        required=True
    )


class Scholarship(Item):
    implements(IScholarship)


class ScholarshipView(grok.View):
    grok.context(IScholarship)
    grok.name('view')

    def render(self):
        self.template = ViewPageTemplateFile('scholarship_templates/view.pt')
        return self.template(self)

    def getTitle(self):
        return self.context.title
