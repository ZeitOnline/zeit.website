import zeit.cms.interfaces
import grokcore.component as grok
import zeit.cms.checkout.interfaces
import zope.interface
from zeit.cms.section.interfaces import ISectionMarker

@grok.subscribe(
    zeit.cms.interfaces.ICMSContent,
    zeit.cms.checkout.interfaces.IBeforeCheckinEvent)
def provide_website_content(content, event):
    content = zope.security.proxy.getObject(content)
    if not content.rebrush_website_content:
        return
    for iface in zope.interface.providedBy(content):
        if issubclass(iface, ISectionMarker):
            zope.interface.noLongerProvides(content, iface)
    zope.interface.alsoProvides(content, zeit.website.interfaces.IWebsiteContent)
