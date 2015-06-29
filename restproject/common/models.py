from django.db import models
from django.utils.translation import ugettext_lazy as _


class BackScratcher(models.Model):
    """
    A model to represent the data of a back scratcher.
    """
    SIZES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    )
    name = models.CharField(verbose_name=_("name"), max_length=80)
    description = models.TextField(verbose_name=_("description"), )
    size = models.CharField(
        verbose_name=_("size"), max_length=100, choices=SIZES
    )
    price = models.DecimalField(
        verbose_name=_("price"), decimal_places=2, max_digits=5
    )

    def __unicode__(self):
        return (
            u'BackScratcher: name {0}, '
            u'size {1}'.format(self.name, self.size)
        )

    class Meta:
        verbose_name = u"Back Scratcher"
        verbose_name_plural = u"Back Scratchers"
