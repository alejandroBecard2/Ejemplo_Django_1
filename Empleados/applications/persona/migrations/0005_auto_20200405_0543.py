# Generated by Django 3.0.4 on 2020-04-05 05:43

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_auto_20200403_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres completos'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='hoja_vida',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Hoja de Vida'),
        ),
    ]
