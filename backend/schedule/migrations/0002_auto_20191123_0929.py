# Generated by Django 2.1.7 on 2019-11-23 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='has_answer',
            field=models.BooleanField(default=False, verbose_name='Был ответ'),
        ),
        migrations.AlterField(
            model_name='help',
            name='category',
            field=models.CharField(choices=[('schedule', 'Расписание'), ('bot', 'Бот'), ('other', 'Другое')], max_length=300),
        ),
        migrations.AlterField(
            model_name='help',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.User', verbose_name='Пользователь'),
        ),
    ]