# Generated by Django 3.1.5 on 2021-01-09 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uid', models.SlugField(help_text='Unique name to identify facility. Also required by login process.', max_length=15, unique=True, verbose_name='Unique Identifier')),
                ('name', models.CharField(help_text='Facility string representation.', max_length=70)),
                ('segment', model_utils.fields.StatusField(choices=[('subscriptions', 'subscriptions'), ('markets', 'markets')], db_index=True, default='subscriptions', help_text='Facility related business segment, to determine facility accountant type.', max_length=100, no_check_for_status=True, verbose_name='Business Segment')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this facility should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_chief', models.BooleanField(default=False, help_text='Designates whether the user have permission cross all branches.')),
                ('facility', models.ForeignKey(help_text='Determine the associated facility.', on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='corporations.facility')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='facility_staff', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='String representation for facility branch.', max_length=50)),
                ('is_main', models.BooleanField(default=False, help_text='Designates whether this branch is the main branch.')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='corporations.facility')),
            ],
        ),
        migrations.AddConstraint(
            model_name='branch',
            constraint=models.UniqueConstraint(condition=models.Q(is_main=True), fields=('facility',), name='unique_facility_with_is_main'),
        ),
    ]