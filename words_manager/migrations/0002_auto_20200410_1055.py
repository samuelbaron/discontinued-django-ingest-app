# Generated by Django 3.0.3 on 2020-04-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='foreign_example',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='native_example',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='native_word_other',
            field=models.TextField(null=True),
        ),
    ]
