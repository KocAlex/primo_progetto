# Generated by Django 4.2.5 on 2023-11-10 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articolo',
            options={'verbose_name': 'Articolo', 'verbose_name_plural': 'Articoli'},
        ),
        migrations.AlterModelOptions(
            name='giornalista',
            options={'verbose_name': 'Giornalista', 'verbose_name_plural': 'Giornalisti'},
        ),
        migrations.AddField(
            model_name='articolo',
            name='data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='articolo',
            name='visualizzazioni',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='giornalista',
            name='anno_di_nascita',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
