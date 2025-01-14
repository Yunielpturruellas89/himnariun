# Generated by Django 5.1.3 on 2024-11-22 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hymn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField(unique=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('verse', 'Verse'), ('chorus', 'Chorus'), ('bridge', 'Bridge')], default='verse', max_length=50)),
                ('hymn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses', to='hymns.hymn')),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('verse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='hymns.verse')),
            ],
        ),
    ]
