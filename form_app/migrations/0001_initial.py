# Generated by Django 4.1.3 on 2023-03-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registeration_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('field', models.CharField(choices=[('Manager', 'Manager'), ('Cashier', 'Cashier'), ('Operator', 'Operator')], max_length=20)),
            ],
        ),
    ]
