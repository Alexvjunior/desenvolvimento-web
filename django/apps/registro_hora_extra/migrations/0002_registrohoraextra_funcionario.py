# Generated by Django 3.2.7 on 2021-09-08 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20210908_2238'),
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='funcionario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
        ),
    ]