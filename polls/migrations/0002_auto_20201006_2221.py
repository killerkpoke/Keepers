# Generated by Django 3.1 on 2020-10-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='works',
            name='created',
            field=models.DateTimeField(verbose_name='date uploaded'),
        ),
    ]
