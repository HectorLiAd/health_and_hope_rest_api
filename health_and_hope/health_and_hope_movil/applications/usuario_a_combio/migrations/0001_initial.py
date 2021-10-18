# Generated by Django 3.2.8 on 2021-10-14 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAnalisisMed',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre del tipo de analisis medico')),
            ],
            options={
                'verbose_name': 'Tipo de analisis clinico',
                'verbose_name_plural': 'Tipos de nalisis clinico',
            },
        ),
        migrations.CreateModel(
            name='UsuarioACambio',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario a cambio',
                'verbose_name_plural': 'Usuarios a cambio',
            },
        ),
        migrations.CreateModel(
            name='InfoAnalisisMedUsuario',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('archivo', models.FileField(upload_to='infoAnalisisMedUsuario')),
                ('tipoAnalisisMed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario_a_combio.tipoanalisismed')),
                ('usuarioACambio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario_a_combio.usuarioacambio')),
            ],
            options={
                'verbose_name': 'Analisis medico del usuario',
                'verbose_name_plural': 'Analisis medicos de los usuarios',
            },
        ),
    ]
