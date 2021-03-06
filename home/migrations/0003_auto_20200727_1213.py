# Generated by Django 3.0.8 on 2020-07-27 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_background_image',
            field=models.ForeignKey(help_text='A banner background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button',
            field=models.ForeignKey(blank=True, help_text='Select an optional page to link to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text',
            field=models.CharField(default='Read More', help_text='Button text', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='Subheading text under the banner title', max_length=140),
        ),
    ]
