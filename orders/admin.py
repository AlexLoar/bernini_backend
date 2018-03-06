import csv
import StringIO

from django.db.models import Sum, F
from django.contrib import admin
from django.contrib import messages

from core.utils import send_email
from .models import Article, OrderLine, Order


class OrderLineAdmin(admin.ModelAdmin):
    model = OrderLine


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    readonly_fields = ['total']


class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ['total']
    search_fields = ['client']
    list_filter = ['pay']
    inlines = [OrderLineInline]
    ordering = ['-created']
    actions = ['send_order_through_email_action']

    def save_formset(self, request, form, formset, change):
        """
        Adding the order lines to show the total of the order. 
        """
        instances = formset.save()
        ids = [inst.id for inst in instances]
        total = OrderLine.objects.filter(id__in=ids).aggregate(Sum(F('total'))).get('total__sum')
        form.instance.total = total
        form.instance.save()

    def send_order_through_email_action(self, request, queryset):
        """
         Custom action to send orders as csv through email.
        """
        try:
            opts = queryset.model._meta
            csv_str = StringIO.StringIO()
            writer = csv.writer(csv_str)
            field_names = [field.name for field in opts.fields]
            # Header row
            writer.writerow(field_names)
            # Data rows
            for obj in queryset:
                writer.writerow([unicode(getattr(obj, field)).encode("utf-8") for field in field_names])  # the wonderful world of encoding

            send_email(csv_str)
            self.message_user(request, 'Email enviado correctamente', level=messages.SUCCESS)
        except Exception:
            self.message_user(request, 'Error al enviar los mails', level=messages.ERROR)

    send_order_through_email_action.short_description = 'Enviar pedido por email'


admin.site.register(Article)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Order, OrderAdmin)
