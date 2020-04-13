# Generated by Django 3.0.5 on 2020-04-12 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoNotificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigNotificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdUsuario', models.IntegerField()),
                ('Activas', models.BooleanField()),
                ('IdTipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.TipoNotificacion')),
            ],
        ),
    ]