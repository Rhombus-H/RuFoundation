# Generated by Django 4.1.2 on 2022-11-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_merge_20220906_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='articlelogentry',
            name='type',
            field=models.TextField(choices=[('source', 'Source'), ('title', 'Title'), ('name', 'Name'), ('tags', 'Tags'), ('new', 'New'), ('parent', 'Parent'), ('file_added', 'Fileadded'), ('file_deleted', 'Filedeleted'), ('file_renamed', 'Filerenamed'), ('wikidot', 'Wikidot'), ('revert', 'Revert')], verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='forumthread',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время изменения'),
        ),
    ]