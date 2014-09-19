# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

from zeit.cms.testcontenttype.testcontenttype import TestContentType
import zeit.cms.browser.interfaces
import zeit.cms.testing
import zeit.website.interfaces
import zeit.website.testing
import zope.component


class PreviewURLTest(zeit.cms.testing.FunctionalTestCase):

    layer = zeit.website.testing.LAYER

    def test_zmo_content_gets_different_url(self):
        content = self.repository['website']['test'] = TestContentType()
        self.assertEqual(
            'http://localhost/website-preview-prefix/website/test',
            zope.component.getMultiAdapter(
                (content, 'preview'),
                zeit.cms.browser.interfaces.IPreviewURL))
