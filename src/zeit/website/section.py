import zeit.website.interfaces
from zeit.cms.section.interfaces import ISectionMarker
import grokcore.component as grok
import zeit.cms.checkout.interfaces
import zeit.cms.content.interfaces
import zope.interface


@grok.subscribe(
    zeit.cms.content.interfaces.ICommonMetadata,
    zeit.cms.checkout.interfaces.IBeforeCheckinEvent)
def provide_website_content(content, event):
    content = zope.security.proxy.getObject(content)
    if not content.rebrush_website_content:
        zope.interface.noLongerProvides(content,
            zeit.website.interfaces.IWebsiteSection)
        return
    for iface in zope.interface.providedBy(content):
        if issubclass(iface, ISectionMarker):
            zope.interface.noLongerProvides(content, iface)
    zope.interface.alsoProvides(content, zeit.website.interfaces.IWebsiteSection)
