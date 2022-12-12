# Generated by Django 4.1.4 on 2022-12-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recharge", "0006_plan_sms_type_alter_plan_sms"),
    ]

    operations = [
        migrations.AddField(
            model_name="plan",
            name="validity_type",
            field=models.CharField(
                choices=[("Days", "Days")], default=1, max_length=20
            ),
            preserve_default=False,
        ),
    ]