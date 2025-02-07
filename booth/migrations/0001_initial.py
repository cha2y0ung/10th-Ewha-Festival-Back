# Generated by Django 4.1 on 2022-08-12 06:53

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
            name='Booth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('college', models.CharField(blank=True, max_length=20)),
                ('name', models.TextField()),
                ('image', models.URLField(blank=True)),
                ('notice', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일')], max_length=5)),
                ('date', models.IntegerField(choices=[(14, 14), (15, 15), (16, 16)])),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu', models.TextField()),
                ('image', models.URLField(blank=True)),
                ('price', models.PositiveIntegerField()),
                ('is_soldout', models.BooleanField(default=False)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='booth.booth')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.booth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='booth',
            name='day',
            field=models.ManyToManyField(related_name='booths', to='booth.day'),
        ),
        migrations.AddField(
            model_name='booth',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='booths', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booth',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
