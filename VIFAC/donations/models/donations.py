# -*- coding: utf-8 -*-
from .categories import Category
from django.db import models
from .donors import Donor


class Donation(models.Model):
    
    donor = models.ForeignKey(Donor,
        related_name = 'donations',
        related_query_name = 'donation',
        on_delete = models.PROTECT
    )
    
    description = models.CharField(
        max_length = 1024,
        default = '',
        help_text = 'a small description of the donation',
    )
    
    category = models.ForeignKey(Category,
        verbose_name = 'Category',
        help_text = 'How one would classify the donation: money, food, etc.',
        related_name = 'donations',
        related_query_name = 'donation',
        on_delete = models.PROTECT
    )

    date = models.DateField(
        auto_now = True,
    )
    
    
    def __str__(self) -> str:
        return '%s-%s' % (self.donor, self.category)
    
    class Meta(object):
        verbose_name = 'donation'
        verbose_name_plural = 'donations'
