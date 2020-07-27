from django.db import models
from django.core.exceptions import ValidationError

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.
class ServiceListingPage(Page):
    """ show all available services """    
    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle")
    ]

    def get_context(self, request, *args, **kwargs):
        """override of a Page method"""
        context = super().get_context(request, *args, **kwargs)
        context['HELLO'] = "DUDE, YOU'RE GETTIN A DELL"

        # collect all of the available services for listing in the page
        # this uses Django's standard ORM
        context['services'] = ServicePage.objects.live().public()

        return context


class ServicePage(Page):
    """ service details page """

    # a template property is available to specify a template not derived from the class name
    # tempate = "services/service_page_special.html"
    tempate = "services/service_page.html"    
    description = models.TextField(
        blank=True,
        max_length=500,
    )
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text="Select an internal wagtail page",
        on_delete=models.SET_NULL,
    )
    external_page = models.URLField(
        blank=True,
    )
    button_text = models.CharField(
        blank=True,
        max_length=50,
    )
    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text= ('This image will be used on the Service Listing Page' 
                    'and wil be cropped to 570px to 370px on this page'),
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        PageChooserPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("button_text"),
        ImageChooserPanel("service_image"),
    ]

    def clean(self):
        """
        Wagtail's ability to do input validation and error checking - from Custom Page Validation
        """ 
        super().clean()

        # format
        # if something:
        #     cause an error

        if self.internal_page and self.external_page:
            message = "Please only select a page OR enter an external URL"
            raise ValidationError(
                {
                    'internal_page': ValidationError(message),
                    'external_page': ValidationError(message),
                }
            )

        if not self.internal_page and not self.external_page:
            message = "Please include at least a page OR an external URL, both cannot be blank"
            raise ValidationError(
                {
                    'internal_page': ValidationError(message),
                    'external_page': ValidationError(message),
                }
            )

