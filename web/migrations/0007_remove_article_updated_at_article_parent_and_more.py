# Generated by Django 4.0.3 on 2022-05-24 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_article_updated_at_alter_articlelogentry_meta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.article'),
        ),
        migrations.AlterField(
            model_name='articlelogentry',
            name='type',
            field=models.TextField(choices=[('source', 'Source'), ('title', 'Title'), ('name', 'Name'), ('new', 'New'), ('parent', 'Parent')]),
        ),
    ]
