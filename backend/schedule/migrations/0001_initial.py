# Generated by Django 2.1 on 2019-11-19 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot', '0002_auto_20191119_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Время')),
                ('category', models.CharField(choices=[('r', 'Расписание'), ('b', 'Бот')], max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bot.User', verbose_name='Пользователь')),
            ],
        ),
    ]