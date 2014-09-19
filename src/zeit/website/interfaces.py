from zeit.cms.i18n import MessageFactory as _
import zeit.cms.interfaces
import zeit.cms.related.interfaces
import zeit.cms.section.interfaces
import zeit.content.article.interfaces
import zeit.content.cp.interfaces
import zeit.content.portraitbox.interfaces
import zeit.website.sources
import zope.interface


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


class IArticleTemplateSettings(zope.interface.Interface):

    template = zope.schema.Choice(
        title=_("Template"),
        source=zeit.website.sources.ArticleTemplateSource(),
        required=False)

    header_layout = zope.schema.Choice(
        title=_("Header layout"),
        source=zeit.website.sources.ArticleHeaderSource(),
        required=False)


class IRelatedLayout(zope.interface.Interface):

    related_layout = zope.schema.Choice(
        title=_("Related layout"),
        source=zeit.website.sources.ArticleRelatedLayoutSource(),
        required=False)

    nextread_layout = zope.schema.Choice(
        title=_("Next read layout"),
        source=zeit.website.sources.ArticleRelatedLayoutSource(),
        required=False)
