# Generated by Django 3.0.5 on 2020-05-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapperPublicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagina', models.CharField(max_length=100)),
                ('cantidad_comentarios', models.CharField(max_length=100)),
            ],
        ),
    ]
