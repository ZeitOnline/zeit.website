# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

import zeit.cms.content.sources


class ArticleTemplateSource(zeit.cms.content.sources.XMLSource):

    product_configuration = 'zeit.website'
    config_url = 'article-template-source'
    attribute = 'name'
    title_xpath = '/templates/template'

    def _get_title_for(self, node):
        return unicode(node['title'])


class ArticleHeaderSource(zeit.cms.content.sources.MasterSlaveSource):

    product_configuration = 'zeit.website'
    config_url = ArticleTemplateSource.config_url
    attribute = 'name'
    slave_tag = 'header'
    master_node_xpath = '/templates/template'
    master_value_key = 'template'

    @property
    def master_value_iface(self):
        # prevent circular import
        import zeit.website.interfaces
        return zeit.website.interfaces.IArticleTemplateSettings

    def _get_title_for(self, node):
        return unicode(node['title'])


class ArticleRelatedLayoutSource(zeit.cms.content.sources.XMLSource):

    product_configuration = 'zeit.website'
    config_url = 'article-related-layout-source'
    attribute = 'id'
