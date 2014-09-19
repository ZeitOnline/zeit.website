# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

import grokcore.component as grok
import zeit.cms.content.dav
import zeit.cms.content.reference
import zeit.cms.interfaces
import zeit.website.interfaces


class TemplateSettings(zeit.cms.content.dav.DAVPropertiesAdapter):

    grok.implements(zeit.website.interfaces.IArticleTemplateSettings)

    zeit.cms.content.dav.mapProperties(
        zeit.website.interfaces.IArticleTemplateSettings,
        zeit.cms.interfaces.DOCUMENT_SCHEMA_NS,
        ('template', 'header_layout'))


class RelatedLayout(zeit.cms.content.dav.DAVPropertiesAdapter):

    grok.implements(zeit.website.interfaces.IRelatedLayout)

    zeit.cms.content.dav.mapProperties(
        zeit.website.interfaces.IRelatedLayout,
        zeit.cms.interfaces.DOCUMENT_SCHEMA_NS,
        ('related_layout', 'nextread_layout'))
