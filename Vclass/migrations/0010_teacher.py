# Generated by Django 4.2.4 on 2023-08-17 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vclass', '0009_alter_course_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('teacher_id', models.CharField(default='000000', max_length=20)),
                ('mobile_number', models.CharField(max_length=11, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_taken', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Vclass.course')),
            ],
        ),
    ]