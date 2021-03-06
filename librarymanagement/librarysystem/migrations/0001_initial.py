# Generated by Django 4.0.4 on 2022-05-04 09:07

from django.db import migrations, models
import django.db.models.deletion
import enum


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=500)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_address', models.TextField(max_length=50)),
                ('issued_date', models.DateTimeField(verbose_name=enum.auto)),
                ('return_date', models.DateTimeField()),
                ('charge_per_day', models.PositiveIntegerField()),
                ('total_charge', models.PositiveIntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarysystem.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarysystem.category'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=500)),
                ('book', models.ManyToManyField(to='librarysystem.book')),
            ],
        ),
    ]
