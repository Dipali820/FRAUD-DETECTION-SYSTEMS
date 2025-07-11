# Generated by Django 5.2 on 2025-04-06 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delete_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_frauds', models.IntegerField(default=0)),
                ('total_transactions', models.IntegerField(default=0)),
                ('total_funds', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_lost_funds', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
