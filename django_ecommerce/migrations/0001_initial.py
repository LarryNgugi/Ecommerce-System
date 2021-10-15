# Generated by Django 3.2.8 on 2021-10-15 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(null=True)),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('pin', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNumber', models.CharField(max_length=20, null=True)),
                ('cost', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=50)),
                ('shippingCost', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image_url', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('inventory', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('business_name', models.CharField(max_length=100)),
                ('business_reg_no', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=50)),
                ('external_url', models.SlugField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.customer')),
                ('productId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=50, null=True)),
                ('amountDeducted', models.IntegerField(blank=True, default=0)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('limit', models.DateTimeField()),
                ('productId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customerAddressId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.customeraddress')),
                ('orderId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.customer')),
                ('productId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.seller'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('invoiceNumber', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orderId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orderId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.order')),
                ('productId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerAmount', models.IntegerField()),
                ('startDate', models.DateTimeField(null=True)),
                ('endDate', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('productId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_ecommerce.product')),
            ],
        ),
    ]