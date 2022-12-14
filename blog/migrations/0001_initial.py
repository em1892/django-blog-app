# Generated by Django 4.0.2 on 2022-08-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='ブログ記事のタイトル')),
                ('content', models.TextField(verbose_name='ブログ記事の本文')),
                ('created_at', models.DateField(verbose_name='作成日時')),
                ('updated_at', models.DateField(verbose_name='更新日時')),
                ('is_published', models.BooleanField(default=False, verbose_name='記事の公開設定')),
            ],
        ),
    ]
