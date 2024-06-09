# Generated by Django 5.0.6 on 2024-06-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0002_alter_quote_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=models.JSONField(),
        ),
    ]
