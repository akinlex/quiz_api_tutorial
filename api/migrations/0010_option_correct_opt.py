# Generated by Django 3.0.8 on 2020-07-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_option_correct_opt'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='correct_opt',
            field=models.BooleanField(default=False),
        ),
    ]
