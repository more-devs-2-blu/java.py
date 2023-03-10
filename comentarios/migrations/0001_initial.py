# Generated by Django 4.1.7 on 2023-03-11 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('resumo', models.CharField(max_length=50)),
                ('topico', models.IntegerField()),
                ('cidadao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comentarios', to=settings.AUTH_USER_MODEL)),
                ('comentario_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='comentarios.comentario')),
            ],
        ),
    ]
