import uuid

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class ModelbasedPage(Page):
    """Want to generate Slug and set Title based on value of optional 'name' field."""

    name = models.CharField(blank=True, max_length=64, unique=False,
                            help_text="Optional, sets title")

    # Remove Promote tab with slug, and Title from content tab since we set them
    promote_panels = []
    content_panels = [
        FieldPanel('name'),
    ]

    def clean(self):
        """Set the slug to a unique number, and Title to name (if set) or slug.

        Since our panels have removed Title and Slug, they come here as empty
        strings the first time. clean() is called multiple times for some
        reason, so check if they're already set and only set once.

        If they initially publish or save draft with no name, the title will be
        set to the slug. If they later provide a name, set the title to that
        instead.
        """
        super().clean()
        if self.slug == "":
            self.slug = uuid.uuid4().hex
        if self.name:
            self.title = self.name
        else:
            self.title = self.slug
