# Generated by Django 3.0.5 on 2020-05-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_scrappercomentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrappercomentarios',
            name='tipo_comentario',
            field=models.CharField(choices=[('Más relevantes', 'Más relevantes'), ('Más recientes', 'Más recientes'), ('Todos los comentarios', 'Todos los comentarios')], default='Más relevantes', max_length=21),
        ),
    ]
