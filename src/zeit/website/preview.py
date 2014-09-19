# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

import grokcore.component as grok
import zeit.cms.browser.preview
import zeit.website.interfaces


@grok.adapter(zeit.website.interfaces.IWebsiteContent, basestring)
@grok.implementer(zeit.cms.browser.interfaces.IPreviewURL)
def preview_url(content, preview_type):
    return zeit.cms.browser.preview.prefixed_url(
        'website-%s-prefix' % preview_type, content.uniqueId)
