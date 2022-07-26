# Generated by Django 4.0.6 on 2022-07-26 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبد خرید',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='کد تخفیف')),
                ('discount', models.PositiveSmallIntegerField(verbose_name='درصد تخفیف')),
                ('valid_to', models.DateTimeField(verbose_name='تاریخ انقضا')),
                ('active', models.BooleanField(default=True, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کد تخفیف',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=100, verbose_name='نام گیرنده')),
                ('recipient_phone_number', models.CharField(max_length=11, verbose_name='شماره تماس گیرنده')),
                ('recipient_address', models.CharField(max_length=250, verbose_name='آدرس گیرنده')),
                ('coupon_code', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='کد تخفیف')),
                ('coupon_discount', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='درصد تخفیف')),
                ('paid', models.BooleanField(default=False, verbose_name='وضعیت پرداخت')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
                'ordering': ('paid', '-id'),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='مبلغ')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('tracking_code', models.CharField(max_length=100, verbose_name='کد رهگیری')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order', verbose_name='سفارش')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تراکنش',
                'verbose_name_plural': 'تراکنش\u200cها',
                'ordering': ('status', '-id'),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='تعداد')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='سفارش')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'آیتم\u200cهای سفارش',
                'verbose_name_plural': 'آیتم\u200cهای سفارش',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='تعداد')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.cart', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'آیتم\u200cهای سبد خرید',
                'verbose_name_plural': 'آیتم\u200cهای سبد خرید',
                'ordering': ('-id',),
            },
        ),
    ]
