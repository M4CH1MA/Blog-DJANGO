# Generated by Django 5.0.4 on 2024-05-03 23:30

import utils.models_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_alter_sitesetup_options_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m', validators=[utils.models_validators.validate_png]),
        ),
    ]