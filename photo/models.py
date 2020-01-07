from django.db import models
from django.http import JsonResponse

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
# Create your models here.


class PhotoIndexPage(Page):
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        photopages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = photopages
        return context


class PhotoPage(Page):
    date = models.DateField("Post date")
    search_fields = Page.search_fields + [
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class PhotoPageGalleryImage(Orderable):
    page = ParentalKey(PhotoPage, on_delete=models.SET_NULL,
                       blank=True, null=True, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, blank=True, null=True, related_name='+'
    )

    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


# class PhotoDetailPage(Page):

#     def serve(self, request):
#         return JsonResponse({
#             'title': self.title,
#             'body': self.body,
#             'date': self.date,
#             # Resizes the image to 300px width and gets a URL to it
#             'feed_image': self.feed_image.get_rendition('width-300').url,
#         })
