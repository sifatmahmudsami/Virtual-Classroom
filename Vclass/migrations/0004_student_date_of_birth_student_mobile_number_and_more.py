# Generated by Django 4.2.4 on 2023-08-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vclass', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='000000', max_length=20),
        ),
    ]
