# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):

    name = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        verbose_name = "Category name",
        help_text = "How one would call this donation category"
    )

    description = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        verbose_name = "Description",
        help_text = "A small description of the category and its contents"
    )
    
    def __str__(self) -> str:
        return '%s-%s' % (self.name, self.description)
    
    class Meta(object):
        verbose_name = 'category'
        verbose_name_plural = 'categories'
