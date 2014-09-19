# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

from zeit.website.interfaces import IWebsiteSection, IWebsiteFolder
import gocept.httpserverlayer.wsgi
import gocept.selenium
import pkg_resources
import plone.testing
import zeit.cms.repository.interfaces
import zeit.cms.testing
import zeit.content.article.testing
import zope.component
import zope.interface


# XXX appending to product config is not very well supported right now
cms_product_config = zeit.cms.testing.cms_product_config.replace(
    '</product-config>', """\
  website-preview-prefix http://localhost/website-preview-prefix
</product-config>""")

product_config = """\
<product-config zeit.website>
  article-template-source file://{base}/tests/article-templates.xml
</product-config>
""".format(base=pkg_resources.resource_filename(__name__, ''))


ZCML_LAYER = zeit.cms.testing.ZCMLLayer(
    'ftesting.zcml', product_config=(
        product_config
        + cms_product_config
        + zeit.content.article.testing.product_config))


class Layer(plone.testing.Layer):

    defaultBases = (ZCML_LAYER,)

    def testSetUp(self):
        with zeit.cms.testing.site(self['functional_setup'].getRootFolder()):
            repository = zope.component.getUtility(
                zeit.cms.repository.interfaces.IRepository)
            website = zeit.cms.repository.folder.Folder()
            zope.interface.alsoProvides(website, IWebsiteSection)
            zope.interface.alsoProvides(website, IWebsiteFolder)
            repository['website'] = website

LAYER = Layer()


WSGI_LAYER = zeit.cms.testing.WSGILayer(name='WSGILayer', bases=(LAYER,))
HTTP_LAYER = gocept.httpserverlayer.wsgi.Layer(
    name='HTTPLayer', bases=(WSGI_LAYER,))
SELENIUM_LAYER = gocept.selenium.RCLayer(
    name='SeleniumLayer', bases=(HTTP_LAYER,))
