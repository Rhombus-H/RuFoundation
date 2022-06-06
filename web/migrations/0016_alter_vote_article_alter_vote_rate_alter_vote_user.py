# Generated by Django 4.0.4 on 2022-06-03 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0015_alter_vote_article_alter_vote_rate_alter_vote_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='rate',
            field=models.IntegerField(verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]