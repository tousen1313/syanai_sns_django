# Generated by Django 4.1.7 on 2023-03-19 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_alter_boardmodel_good_alter_boardmodel_read_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='context',
            new_name='content',
        ),
    ]
