from django.db import models

class Page(models.Model):
    '''
    Stores a single blog entry, related to :model:`blog.Blog` and :model:`auth.User`.
    '''

    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title
