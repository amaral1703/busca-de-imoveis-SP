# Generated by Django 5.0.3 on 2024-03-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_imoveis_sp', '0002_alter_imovel_bairro_imovel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='area_tereno',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='metro_quad_terreno',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='num_imovel',
            field=models.FloatField(),
        ),
    ]
