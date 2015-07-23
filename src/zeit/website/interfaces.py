import zeit.cms.interfaces
import zeit.cms.section.interfaces
import zeit.content.article.interfaces
import zeit.content.cp.interfaces


class IWebsiteSection(zeit.cms.section.interfaces.ISection):
    pass


class IWebsiteContent(
        zeit.cms.interfaces.ICMSContent,
        zeit.cms.section.interfaces.ISectionMarker):
    pass


class IWebsiteFolder(
        zeit.cms.repository.interfaces.IFolder,
        zeit.cms.section.interfaces.ISectionMarker):
    pass


class IWebsiteArticle(
        zeit.content.article.interfaces.IArticle,
        zeit.cms.section.interfaces.ISectionMarker):
    pass


class IWebsiteCenterPage(
        zeit.content.cp.interfaces.ICenterPage,
        zeit.cms.section.interfaces.ISectionMarker):
    pass
