# Generated by Django 2.2.24 on 2021-08-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0144_add_create_org_problem_permission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'permissions': (('see_private_problem', 'See hidden problems'), ('edit_own_problem', 'Edit own problems'), ('create_organization_problem', 'Create organization problem'), ('edit_all_problem', 'Edit all problems'), ('edit_public_problem', 'Edit all public problems'), ('suggest_new_problem', 'Suggest new problem'), ('problem_full_markup', 'Edit problems with full markup'), ('clone_problem', 'Clone problem'), ('upload_file_statement', 'Upload file-type statement'), ('change_public_visibility', 'Change is_public field'), ('change_manually_managed', 'Change is_manually_managed field'), ('see_organization_problem', 'See organization-private problems')), 'verbose_name': 'problem', 'verbose_name_plural': 'problems'},
        ),
        migrations.AlterField(
            model_name='problem',
            name='pdf_url',
            field=models.CharField(blank=True, help_text='URL to PDF statement. The PDF file must be embeddable (Mobile web browsersmay not support embedding). Fallback included.', max_length=200, verbose_name='PDF statement URL'),
        ),
    ]
