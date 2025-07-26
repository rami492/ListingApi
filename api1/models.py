from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Listing(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey('auth.User', related_name='listings', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']