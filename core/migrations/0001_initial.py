# Generated by Django 2.0.2 on 2018-04-07 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=140)),
                ('score', models.IntegerField(default=0)),
                ('rankings', models.IntegerField(default=200000)),
                ('phone', models.IntegerField(default=0)),
                ('student_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_user', to=settings.AUTH_USER_MODEL)),
                ('teachers', models.ManyToManyField(related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=140)),
                ('ratings', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('rankings', models.IntegerField(default=200000)),
                ('students', models.ManyToManyField(related_name='students_of_teacher', to=settings.AUTH_USER_MODEL)),
                ('teacher_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_details_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
