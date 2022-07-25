# Generated by Django 4.0.4 on 2022-07-25 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.course')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('lecture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='classes.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('lecture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='classes.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('courses', models.ManyToManyField(related_name='tags', to='classes.course')),
            ],
        ),
    ]
