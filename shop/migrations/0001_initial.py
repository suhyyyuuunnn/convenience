# Generated by Django 3.1.6 on 2021-02-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='상품명')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트시간')),
                ('_type', models.PositiveSmallIntegerField(choices=[(0, '7eleven'), (1, 'CU'), (2, 'GS25')], verbose_name='상호')),
                ('price', models.IntegerField(default=0, verbose_name='가격')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
