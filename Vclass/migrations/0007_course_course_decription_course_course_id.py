# Generated by Django 4.2.4 on 2023-08-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vclass', '0006_remove_student_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_decription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=0),
        ),
    ]