# -*- coding: utf-8 -*-

from plone import api
from plone.formwidget.autocomplete.widget import AutocompleteSelectionWidget

import z3c.form.browser.text
import z3c.form.interfaces
import z3c.form.widget
import zope.interface
import zope.schema.interfaces


class IFieldsetWidget(z3c.form.interfaces.ITextWidget):
    pass


class FieldsetWidget(z3c.form.browser.text.TextWidget):
    zope.interface.implementsOnly(IFieldsetWidget)

    klass = u'fieldset-widget'

    def update(self):
        super(z3c.form.browser.text.TextWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)


@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def FieldsetFieldWidget(field, request):
    return z3c.form.widget.FieldWidget(field, FieldsetWidget(request))
