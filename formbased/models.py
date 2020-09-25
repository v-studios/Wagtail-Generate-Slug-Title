import uuid

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.core.models import Page


class FormbasedForm(WagtailAdminPageForm):
    def clean(self):            # self is an HTML table
        cleaned_data = super().clean()
        # Do validation on the form...
        # Setting cleaned_data slug and title seems to have no effect
        return cleaned_data

    def save(self, commit=True):
        """If we don't have slug, create; set title to name (if set) or slug."""
        page = super().save(commit=False)

        if not page.slug:
            page.slug = uuid.uuid4().hex
        page.title = page.name or page.slug

        if commit:
            page.save()
        return page


class FormbasedPage(Page):
    base_form_class = FormbasedForm

    name = models.CharField(blank=True, max_length=128)

    content_panels = [
        FieldPanel('name'),
    ]
    promote_panels = []         # remove the field to capture slug
