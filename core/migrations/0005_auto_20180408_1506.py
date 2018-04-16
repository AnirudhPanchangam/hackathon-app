# Generated by Django 2.0.2 on 2018-04-08 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180408_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='student_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_details_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
