# Generated by Django 3.1.1 on 2020-09-25 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelbasedPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('name', models.CharField(blank=True, help_text='Optional, sets title', max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
