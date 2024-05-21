# Generated by Django 4.2.8 on 2024-05-21 11:14

import datetime
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
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_image', models.URLField(blank=True, max_length=255, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('profile_image', models.URLField(blank=True, max_length=255, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('tagline', models.CharField(blank=True, max_length=255, null=True)),
                ('poster_image', models.URLField(max_length=255)),
                ('backdrop_image', models.URLField(max_length=255)),
                ('popularity', models.FloatField()),
                ('release_date', models.DateField(default=datetime.date.today, null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director')),
                ('dislike_users', models.ManyToManyField(related_name='dislike_movies', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.genre')),
                ('keywords', models.ManyToManyField(related_name='movies', to='movies.keyword')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_keywords', to='movies.keyword')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_keywords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'keyword')},
            },
        ),
    ]
