# Generated by Django 3.1.7 on 2021-09-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='multiimage',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='multiimage',
            name='name',
            field=models.CharField(default='test', max_length=100),
        ),
    ]