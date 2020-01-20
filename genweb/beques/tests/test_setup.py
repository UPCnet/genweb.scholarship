# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from genweb.beques.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of genweb.beques into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if genweb.beques is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('genweb.beques'))

    def test_uninstall(self):
        """Test if genweb.beques is cleanly uninstalled."""
        self.installer.uninstallProducts(['genweb.beques'])
        self.assertFalse(self.installer.isProductInstalled('genweb.beques'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IGenwebBequesLayer is registered."""
        from genweb.beques.interfaces import IGenwebBequesLayer
        from plone.browserlayer import utils
        self.failUnless(IGenwebBequesLayer in utils.registered_layers())
