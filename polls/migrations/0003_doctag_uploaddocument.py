# Generated by Django 3.1.7 on 2021-10-15 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210928_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UploadDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='pdfs/')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.doctag')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]