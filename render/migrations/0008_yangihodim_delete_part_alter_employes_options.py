# Generated by Django 4.0.2 on 2022-03-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0007_alter_employes_options_alter_newvideo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YangiHodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.TextField(max_length=60)),
                ('haqida', models.CharField(max_length=200)),
                ('rasmi', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.AlterModelOptions(
            name='employes',
            options={'verbose_name_plural': 'hodimlar'},
        ),
    ]