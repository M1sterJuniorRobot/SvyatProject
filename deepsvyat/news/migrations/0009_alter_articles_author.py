# Generated by Django 4.1.3 on 2023-06-03 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('w_users', '0001_initial'),
        ('news', '0008_remove_articles_author_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='w_users.profile'),
        ),
    ]