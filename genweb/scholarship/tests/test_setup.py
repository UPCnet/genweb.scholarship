# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from genweb.scholarship.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of genweb.scholarship into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if genweb.scholarship is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('genweb.scholarship'))

    def test_uninstall(self):
        """Test if genweb.scholarship is cleanly uninstalled."""
        self.installer.uninstallProducts(['genweb.scholarship'])
        self.assertFalse(self.installer.isProductInstalled('genweb.scholarship'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IGenwebscholarshipLayer is registered."""
        from genweb.scholarship.interfaces import IGenwebscholarshipLayer
        from plone.browserlayer import utils
        self.failUnless(IGenwebscholarshipLayer in utils.registered_layers())
