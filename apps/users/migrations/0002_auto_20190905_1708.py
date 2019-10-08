from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='staff_no',
            field=models.CharField(blank=True, max_length=15, verbose_name='工号'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.IntegerField(default=1, verbose_name='是否在职'),
        ),
    ]
