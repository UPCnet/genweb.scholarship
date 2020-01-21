# -*- coding: utf-8 -*-
from five import grok
from genweb.scholarship import _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.directives import dexterity
from plone.directives import form
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implements


class IScholarship(form.Schema):
    """ Scholarship schema """

    organism = RichText(
        title=_(u"Responsible Organism"),
        description=_(u""),
        required=False,
    )

    recipients = RichText(
        title=_(u"Recipients"),
        description=_(u""),
        required=False,
    )

    regulations = RichText(
        title=_(u"Regulations"),
        description=_(u""),
        required=False,
    )

    fieldset('requirements',
             label=_(u'Requirements tab'),
             fields=['general_requirements', 'academic_requirements',
                     'economic_requirements', 'incompatibilities',
                     'start_date', 'deadline', 'submission', 'documentation',
                     'amount', 'additional_amount', 'duration', 'payment',
                     'beneficiaries', 'criteria', 'award_date',
                     'award_resolution', 'allegations'],
             required=True,
             )

    general_requirements = RichText(
        title=_(u"General requirements"),
        description=_(u""),
        required=True,
    )

    academic_requirements = RichText(
        title=_(u"Academic requirements"),
        description=_(u""),
        required=False,
    )

    economic_requirements = RichText(
        title=_(u"Economic requirements"),
        description=_(u""),
        required=False,
    )

    incompatibilities = RichText(
        title=_(u"Incompatibilities"),
        description=_(u""),
        required=False,
    )

    start_date = schema.Date(
        title=_(u"Application start date"),
        description=_(u""),
        required=False,
    )

    deadline = schema.Date(
        title=_(u"Application deadline"),
        description=_(u""),
        required=False,
    )

    submission = RichText(
        title=_(u"Application submission"),
        description=_(u""),
        required=False,
    )

    documentation = RichText(
        title=_(u"Additional documentation"),
        description=_(u""),
        required=False,
    )

    amount = schema.Float(
        title=_(u"General amount of scholarship"),
        description=_(u""),
        required=False,
    )

    additional_amount = schema.Float(
        title=_(u"Additional amounts of scholarship"),
        description=_(u""),
        required=False,
    )

    duration = RichText(
        title=_(u"Duration of the grant"),
        description=_(u""),
        required=False,
    )

    payment = RichText(
        title=_(u"Payment"),
        description=_(u""),
        required=False,
    )

    beneficiaries = RichText(
        title=_(u"Obligations of the beneficiaries"),
        description=_(u""),
        required=False,
    )

    criteria = RichText(
        title=_(u"Award criteria"),
        description=_(u""),
        required=False,
    )

    award_date = schema.Date(
        title=_(u"Award's resolution date"),
        description=_(u""),
        required=False,
    )

    award_resolution = RichText(
        title=_(u"Award's resolution"),
        description=_(u""),
        required=False,
    )

    allegations = RichText(
        title=_(u"Allegations"),
        description=_(u""),
        required=False,
    )


class Scholarship(Item):
    implements(IScholarship)


class ScholarshipView(grok.View):
    grok.context(IScholarship)
    grok.name('view')

    def render(self):
        self.template = ViewPageTemplateFile('scholarship_templates/view.pt')
        return self.template(self)


class Edit(dexterity.EditForm):
    """A standard edit form. """
    grok.context(IScholarship)
