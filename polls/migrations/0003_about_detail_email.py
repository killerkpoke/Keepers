# Generated by Django 4.0.1 on 2022-12-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_about_detail_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_detail',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
