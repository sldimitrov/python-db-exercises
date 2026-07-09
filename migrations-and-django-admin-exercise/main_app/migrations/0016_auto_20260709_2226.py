from django.db import migrations
from datetime import timedelta


def update_orders(apps, schema_editor):
    Order = apps.get_model('main_app', 'Order')
    orders = Order.objects.all()

    for order in orders:
        if order.status == 'Pending':
            order.delivery = order.order_date + timedelta(days=3)
            order.save()
        elif order.status == 'Completed':
            order.warranty = '24 months'
            order.save()
        elif order.status == 'Cancelled':
            order.delete()


def rollback_orders(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_order'),
    ]

    operations = [
        migrations.RunPython(update_orders, reverse_code=rollback_orders),
    ]