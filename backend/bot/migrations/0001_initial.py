# Generated by Django 2.1.7 on 2019-11-14 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.TextField(blank=True, null=True, verbose_name='Экран')),
                ('date', models.DateField(auto_now=True, verbose_name='Время')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.TextField(blank=True, null=True, verbose_name='Экран')),
                ('date', models.DateField(auto_now=True, verbose_name='Время')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(default='', max_length=300, primary_key=True, serialize=False, verbose_name='ID Пользователя')),
                ('messenger', models.IntegerField(choices=[(0, 'Telegram'), (1, 'Viber'), (2, 'VK'), (3, 'Facebook')], verbose_name='Мессенджер')),
                ('first_name', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Фамилия')),
                ('state', models.CharField(blank=True, max_length=300, null=True, verbose_name='Место нахождение пользователя')),
                ('prev_state', models.CharField(blank=True, max_length=300, null=True, verbose_name='Предыдущее состояние')),
                ('telegram_slug', models.CharField(blank=True, max_length=300, null=True, verbose_name='Телеграм ник')),
                ('language', models.IntegerField(choices=[(0, 'Русский'), (1, 'English')], default=0)),
                ('group', models.CharField(default='', max_length=300, verbose_name='Номер группы')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bot.User', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='error',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bot.User', verbose_name='Пользователь'),
        ),
    ]
