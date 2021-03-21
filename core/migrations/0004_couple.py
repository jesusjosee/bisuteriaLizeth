# Generated by Django 3.1.7 on 2021-03-21 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_men'),
    ]

    operations = [
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='cuople', verbose_name='Imagen')),
                ('link', models.URLField(blank=True, null=True, verbose_name='link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Pulseras para pareja',
                'verbose_name_plural': 'Pulseras para parejas',
                'ordering': ['-created'],
            },
        ),
    ]