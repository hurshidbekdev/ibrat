# Generated by Django 4.0.2 on 2022-03-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0012_uzgarishyangiliklar'),
    ]

    operations = [
        migrations.CreateModel(
            name='KomisHodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/media')),
                ('ismi', models.CharField(max_length=60)),
                ('TurarJoi', models.TextField(max_length=60)),
                ('lavozimi', models.TextField(max_length=1000)),
            ],
        ),
    ]
