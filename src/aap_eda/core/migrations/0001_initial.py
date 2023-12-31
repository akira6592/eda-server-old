# Generated by Django 3.2.18 on 2023-06-06 13:07

import uuid

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import aap_eda.core.enums
import aap_eda.core.utils.crypto.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        verbose_name="email address",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Activation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("description", models.TextField(default="")),
                ("is_enabled", models.BooleanField(default=True)),
                (
                    "restart_policy",
                    models.TextField(
                        choices=[
                            ("always", "always"),
                            ("on-failure", "on-failure"),
                            ("never", "never"),
                        ],
                        default=aap_eda.core.enums.RestartPolicy["ON_FAILURE"],
                    ),
                ),
                ("restart_count", models.IntegerField(default=0)),
                ("failure_count", models.IntegerField(default=0)),
                ("is_valid", models.BooleanField(default=False)),
                (
                    "rulebook_name",
                    models.TextField(
                        help_text="Name of the referenced rulebook"
                    ),
                ),
                (
                    "rulebook_rulesets",
                    models.TextField(
                        help_text="Content of the last referenced rulebook"
                    ),
                ),
                ("ruleset_stats", models.JSONField(default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "core_activation",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="ActivationInstance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(default="")),
                (
                    "status",
                    models.TextField(
                        choices=[
                            ("starting", "starting"),
                            ("running", "running"),
                            ("pending", "pending"),
                            ("failed", "failed"),
                            ("stopping", "stopping"),
                            ("stopped", "stopped"),
                            ("completed", "completed"),
                            ("unresponsive", "unresponsive"),
                        ],
                        default=aap_eda.core.enums.ActivationStatus["PENDING"],
                    ),
                ),
                ("started_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(null=True)),
                ("ended_at", models.DateTimeField(null=True)),
                ("activation_pod_id", models.TextField(null=True)),
            ],
            options={
                "db_table": "core_activation_instance",
                "ordering": ("-started_at",),
            },
        ),
        migrations.CreateModel(
            name="ActivationInstanceJobInstance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "core_activation_instance_job_instance",
            },
        ),
        migrations.CreateModel(
            name="ActivationInstanceLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("line_number", models.IntegerField()),
                ("log", models.TextField()),
            ],
            options={
                "db_table": "core_activation_instance_log",
            },
        ),
        migrations.CreateModel(
            name="AuditAction",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("status", models.TextField(blank=True)),
                ("url", models.URLField(blank=True)),
                ("fired_at", models.DateTimeField()),
                ("rule_fired_at", models.DateTimeField(null=True)),
            ],
            options={
                "db_table": "core_audit_action",
                "ordering": ("-fired_at", "-rule_fired_at"),
            },
        ),
        migrations.CreateModel(
            name="AuditEvent",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("source_name", models.TextField()),
                ("source_type", models.TextField()),
                ("received_at", models.DateTimeField()),
                ("payload", models.JSONField(null=True)),
                ("rule_fired_at", models.DateTimeField(null=True)),
            ],
            options={
                "db_table": "core_audit_event",
                "ordering": ("-rule_fired_at", "-received_at"),
            },
        ),
        migrations.CreateModel(
            name="AuditRule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("description", models.TextField()),
                ("status", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("fired_at", models.DateTimeField()),
                ("rule_uuid", models.UUIDField(null=True)),
                ("ruleset_uuid", models.UUIDField(null=True)),
                ("ruleset_name", models.TextField(null=True)),
                ("definition", models.JSONField(default=dict)),
            ],
            options={
                "db_table": "core_audit_rule",
                "ordering": ("-fired_at",),
            },
        ),
        migrations.CreateModel(
            name="AwxToken",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("description", models.TextField(blank=True, default="")),
                (
                    "token",
                    aap_eda.core.utils.crypto.fields.EncryptedTextField(),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Credential",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "credential_type",
                    models.TextField(
                        choices=[
                            ("Container Registry", "Container Registry"),
                            (
                                "GitHub Personal Access Token",
                                "GitHub Personal Access Token",
                            ),
                            (
                                "GitLab Personal Access Token",
                                "GitLab Personal Access Token",
                            ),
                        ],
                        default=aap_eda.core.enums.CredentialType["REGISTRY"],
                    ),
                ),
                ("username", models.TextField(null=True)),
                (
                    "secret",
                    aap_eda.core.utils.crypto.fields.EncryptedTextField(
                        null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "core_credential",
            },
        ),
        migrations.CreateModel(
            name="DecisionEnvironment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("description", models.TextField(blank=True, default="")),
                ("image_url", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "core_decision_environment",
            },
        ),
        migrations.CreateModel(
            name="ExtraVar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.TextField(default=None, null=True, unique=True),
                ),
                ("extra_var", models.TextField()),
            ],
            options={
                "db_table": "core_extra_var",
            },
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("description", models.TextField(default="", null=True)),
                ("inventory", models.TextField(null=True)),
                (
                    "inventory_source",
                    models.TextField(
                        choices=[
                            ("project", "project"),
                            ("collection", "collection"),
                            ("user_defined", "user_defined"),
                            ("execution_env", "execution_env"),
                        ]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "core_inventory",
            },
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField()),
            ],
            options={
                "db_table": "core_job",
            },
        ),
        migrations.CreateModel(
            name="JobInstance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField()),
                ("action", models.TextField()),
                ("name", models.TextField()),
                ("ruleset", models.TextField()),
                ("rule", models.TextField()),
                ("hosts", models.TextField()),
            ],
            options={
                "db_table": "core_job_instance",
            },
        ),
        migrations.CreateModel(
            name="JobInstanceEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_uuid", models.UUIDField()),
                ("counter", models.IntegerField()),
                ("stdout", models.TextField()),
                ("type", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "core_job_instance_event",
            },
        ),
        migrations.CreateModel(
            name="JobInstanceHost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_uuid", models.UUIDField()),
                ("playbook", models.TextField()),
                ("play", models.TextField()),
                ("task", models.TextField()),
                ("status", models.TextField()),
            ],
            options={
                "db_table": "core_job_instance_host",
            },
        ),
        migrations.CreateModel(
            name="Permission",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "resource_type",
                    models.TextField(
                        choices=[
                            ("activation", "activation"),
                            ("activation_instance", "activation_instance"),
                            ("audit_rule", "audit_rule"),
                            ("audit_event", "audit_event"),
                            ("task", "task"),
                            ("user", "user"),
                            ("project", "project"),
                            ("inventory", "inventory"),
                            ("extra_var", "extra_var"),
                            ("playbook", "playbook"),
                            ("rulebook", "rulebook"),
                            ("role", "role"),
                            ("decision_environment", "decision_environment"),
                            ("credential", "credential"),
                        ]
                    ),
                ),
                (
                    "action",
                    models.TextField(
                        choices=[
                            ("create", "create"),
                            ("read", "read"),
                            ("update", "update"),
                            ("delete", "delete"),
                            ("enable", "enable"),
                            ("disable", "disable"),
                            ("restart", "restart"),
                        ]
                    ),
                ),
            ],
            options={
                "db_table": "core_permission",
                "unique_together": {("resource_type", "action")},
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("description", models.TextField(blank=True, default="")),
                ("url", models.TextField()),
                ("git_hash", models.TextField()),
                ("archive_file", models.FileField(upload_to="projects/")),
                (
                    "import_state",
                    models.TextField(
                        choices=[
                            ("pending", "Pending"),
                            ("running", "Running"),
                            ("failed", "Failed"),
                            ("completed", "Completed"),
                        ],
                        default="pending",
                    ),
                ),
                ("import_task_id", models.UUIDField(default=None, null=True)),
                ("import_error", models.TextField(default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "credential",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.credential",
                    ),
                ),
            ],
            options={
                "db_table": "core_project",
            },
        ),
        migrations.CreateModel(
            name="Rulebook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("description", models.TextField(default="", null=True)),
                ("rulesets", models.TextField(default="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.project",
                    ),
                ),
            ],
            options={
                "db_table": "core_rulebook",
            },
        ),
        migrations.CreateModel(
            name="Ruleset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("sources", models.JSONField(default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "rulebook",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.rulebook",
                    ),
                ),
            ],
            options={
                "db_table": "core_ruleset",
            },
        ),
        migrations.CreateModel(
            name="Rule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("action", models.JSONField(default=dict)),
                (
                    "ruleset",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.ruleset",
                    ),
                ),
            ],
            options={
                "db_table": "core_rule",
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("description", models.TextField(default="")),
                ("is_default", models.BooleanField(default=False, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "permissions",
                    models.ManyToManyField(
                        related_name="roles", to="core.Permission"
                    ),
                ),
            ],
            options={
                "db_table": "core_role",
            },
        ),
        migrations.CreateModel(
            name="Playbook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
                ("playbook", models.TextField()),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.project",
                    ),
                ),
            ],
            options={
                "db_table": "core_playbook",
            },
        ),
        migrations.AddIndex(
            model_name="jobinstancehost",
            index=models.Index(
                fields=["job_uuid"], name="ix_job_host_job_uuid"
            ),
        ),
        migrations.AddIndex(
            model_name="jobinstanceevent",
            index=models.Index(
                fields=["job_uuid"], name="ix_job_instance_event_job_uuid"
            ),
        ),
        migrations.AddIndex(
            model_name="jobinstance",
            index=models.Index(fields=["name"], name="ix_job_instance_name"),
        ),
        migrations.AddIndex(
            model_name="jobinstance",
            index=models.Index(fields=["uuid"], name="ix_job_instance_uuid"),
        ),
        migrations.AddIndex(
            model_name="job",
            index=models.Index(fields=["uuid"], name="ix_job_uuid"),
        ),
        migrations.AddField(
            model_name="inventory",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.project",
            ),
        ),
        migrations.AddField(
            model_name="extravar",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.project",
            ),
        ),
        migrations.AddField(
            model_name="decisionenvironment",
            name="credential",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.credential",
            ),
        ),
        migrations.AddConstraint(
            model_name="credential",
            constraint=models.CheckConstraint(
                check=models.Q(("name", ""), _negated=True),
                name="ck_empty_credential_name",
            ),
        ),
        migrations.AddField(
            model_name="awxtoken",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="auditrule",
            name="activation_instance",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.activationinstance",
            ),
        ),
        migrations.AddField(
            model_name="auditrule",
            name="job_instance",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.jobinstance",
            ),
        ),
        migrations.AddField(
            model_name="auditevent",
            name="audit_actions",
            field=models.ManyToManyField(
                related_name="audit_events", to="core.AuditAction"
            ),
        ),
        migrations.AddField(
            model_name="auditaction",
            name="audit_rule",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.auditrule",
            ),
        ),
        migrations.AddField(
            model_name="activationinstancelog",
            name="activation_instance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.activationinstance",
            ),
        ),
        migrations.AddField(
            model_name="activationinstancejobinstance",
            name="activation_instance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.activationinstance",
            ),
        ),
        migrations.AddField(
            model_name="activationinstancejobinstance",
            name="job_instance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.jobinstance",
            ),
        ),
        migrations.AddField(
            model_name="activationinstance",
            name="activation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.activation",
            ),
        ),
        migrations.AddField(
            model_name="activation",
            name="decision_environment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.decisionenvironment",
            ),
        ),
        migrations.AddField(
            model_name="activation",
            name="extra_var",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.extravar",
            ),
        ),
        migrations.AddField(
            model_name="activation",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.project",
            ),
        ),
        migrations.AddField(
            model_name="activation",
            name="rulebook",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.rulebook",
            ),
        ),
        migrations.AddField(
            model_name="activation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="roles",
            field=models.ManyToManyField(related_name="users", to="core.Role"),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ruleset",
            unique_together={("rulebook_id", "name")},
        ),
        migrations.AddConstraint(
            model_name="rulebook",
            constraint=models.CheckConstraint(
                check=models.Q(("name", ""), _negated=True),
                name="ck_rulebook_name_not_empty",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="rulebook",
            unique_together={("project_id", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="rule",
            unique_together={("ruleset", "name")},
        ),
        migrations.AddConstraint(
            model_name="project",
            constraint=models.CheckConstraint(
                check=models.Q(("name", ""), _negated=True),
                name="ck_empty_project_name",
            ),
        ),
        migrations.AddIndex(
            model_name="inventory",
            index=models.Index(
                fields=["inventory_source"], name="ix_inventory_inv_src"
            ),
        ),
        migrations.AddConstraint(
            model_name="inventory",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "inventory_source__in",
                        (
                            "project",
                            "collection",
                            "user_defined",
                            "execution_env",
                        ),
                    )
                ),
                name="ck_inventory_source_values",
            ),
        ),
        migrations.AddConstraint(
            model_name="inventory",
            constraint=models.CheckConstraint(
                check=models.Q(("name", ""), _negated=True),
                name="ck_empty_inventory_name",
            ),
        ),
        migrations.AddConstraint(
            model_name="decisionenvironment",
            constraint=models.CheckConstraint(
                check=models.Q(("name", ""), _negated=True),
                name="ck_empty_decision_env_name",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="awxtoken",
            unique_together={("user", "name")},
        ),
        migrations.AddIndex(
            model_name="auditrule",
            index=models.Index(fields=["name"], name="ix_audit_rule_name"),
        ),
        migrations.AddIndex(
            model_name="auditrule",
            index=models.Index(
                fields=["fired_at"], name="ix_audit_rule_fired_at"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="auditaction",
            unique_together={("id", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="activationinstancejobinstance",
            unique_together={("activation_instance", "job_instance")},
        ),
        migrations.AddIndex(
            model_name="activation",
            index=models.Index(fields=["name"], name="ix_activation_name"),
        ),
    ]
