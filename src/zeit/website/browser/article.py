# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

from zeit.cms.i18n import MessageFactory as _
from zeit.content.article.edit.browser.form import FormFields
import zeit.cms.browser.interfaces
import zeit.cms.content.browser.widget
import zeit.edit.browser.form


class EditTemplate(zeit.edit.browser.form.InlineForm):

    legend = _('ZEIT ONLINE')
    prefix = 'options-website'
    undo_description = _('edit options')
    form_fields = FormFields(
        zeit.website.interfaces.IArticleTemplateSettings).select(
        'template', 'header_layout')

    def render(self):
        result = super(EditTemplate, self).render()
        if result:
            result += """\
<script type="text/javascript">
    zeit.cms.configure_master_slave(
        "%s.", "template", "header_layout",
        "@@zeit.website.update_articletemplate.json");
</script>""" % self.prefix
        return result


class TemplateUpdater(
        zeit.cms.content.browser.widget.MasterSlaveDropdownUpdater):

    master_source = zeit.website.sources.ArticleTemplateSource()
    slave_source = zeit.website.sources.ArticleHeaderSource()
