# Generated by Django 4.2.3 on 2023-07-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('idEmploye', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('poste', models.CharField(max_length=100)),
                ('dateEmbauche', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=130)),
            ],
        ),
    ]