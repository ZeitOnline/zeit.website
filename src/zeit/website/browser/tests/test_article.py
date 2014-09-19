# coding: utf-8
# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

import zeit.cms.testing
import zeit.content.article.edit.browser.testing
import zeit.website.testing


class ArticleTemplateTest(
        zeit.content.article.edit.browser.testing.EditorHelper,
        zeit.cms.testing.SeleniumTestCase):

    layer = zeit.website.testing.SELENIUM_LAYER

    def setUp(self):
        super(ArticleTemplateTest, self).setUp()
        self.add_article('/repository/website')
        self.selenium.waitForElementPresent('id=options-website.template')

    def test_changing_template_should_update_header_layout_list(self):
        s = self.selenium
        s.click('css=#edit-form-misc .edit-bar .fold-link')

        s.assertSelectedLabel(
            'id=options-website.template', '(nothing selected)')
        s.assertNotVisible('css=.fieldname-header_layout')
        s.select('id=options-website.template', 'Kolumne')
        s.pause(100)

        kolumne_layouts = [
            u'(nothing selected)',
            u'Heiter bis glücklich',
            u'Ich habe einen Traum',
            u'Martenstein',
            u'Standard',
            u'Von A nach B',
        ]

        s.assertVisible('css=.fieldname-header_layout')
        self.assertEqual(
            kolumne_layouts,
            s.getSelectOptions('id=options-website.header_layout'))
        s.click('options-website.actions.apply')
        s.pause(250)
        self.assertEqual(
            kolumne_layouts,
            s.getSelectOptions('id=options-website.header_layout'))
