# Generated by Django 5.0.6 on 2024-06-19 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UsuarioModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.TextField(max_length=100, verbose_name="Nome")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("senha", models.TextField(verbose_name="Senha")),
            ],
            options={
                "verbose_name": "Usuario",
                "verbose_name_plural": "Usuarios",
                "ordering": ["nome"],
            },
        ),
    ]
