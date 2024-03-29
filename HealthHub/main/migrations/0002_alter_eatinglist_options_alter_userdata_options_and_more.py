# Generated by Django 5.0 on 2023-12-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eatinglist',
            options={'verbose_name': 'Список приемов пищи', 'verbose_name_plural': 'Списки приемов пищи'},
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
        migrations.AlterField(
            model_name='eatinglist',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Пользователь'),
        ),
    ]
