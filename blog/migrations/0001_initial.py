# Generated by Django 2.2.5 on 2021-01-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True, max_length=100)),
                ('preco', models.FloatField(default=0)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
