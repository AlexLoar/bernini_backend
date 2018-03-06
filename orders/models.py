# coding: utf-8

from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name='Nombre')
    description = models.CharField(max_length=200, blank=False, verbose_name='Descripción')
    price = models.FloatField(blank=False, verbose_name='Precio (€)')

    def __unicode__(self):
        return u'{} - {}€'.format(self.name, self.price)

    class Meta:
        verbose_name = 'Artículos'
        verbose_name_plural = 'Artículos'


class OrderLine(models.Model):
    order = models.ForeignKey('Order', blank=False, related_name='lines', verbose_name='Factura')
    article = models.ForeignKey(Article, blank=False, related_name='billing_lines', verbose_name='Artículo')
    quantity = models.PositiveIntegerField(blank=False, verbose_name='Cantidad')
    total = models.FloatField(blank=True, verbose_name='Total')

    def __unicode__(self):
        return u'{}'.format(self.article)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.article.price
        super(OrderLine, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Línea de pedido'
        verbose_name_plural = 'Líneas de pedido'


class Order(models.Model):
    client = models.CharField(max_length=200, blank=False, verbose_name='Cliente')
    total = models.FloatField(blank=True, null=True, default=0.0)
    pay = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'{}: {}'.format(self.client, self.created.strftime('%B').title(), self.total)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
