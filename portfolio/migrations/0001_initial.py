# Generated by Django 4.0.6 on 2022-07-14 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TechStack",
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
                    models.CharField(max_length=63, unique=True, verbose_name="Name"),
                ),
            ],
            options={
                "verbose_name": "Techstack",
                "verbose_name_plural": "Techstacks",
            },
        ),
        migrations.CreateModel(
            name="Tool",
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
                    models.CharField(max_length=63, unique=True, verbose_name="Name"),
                ),
            ],
            options={
                "verbose_name": "Tool",
                "verbose_name_plural": "Tools",
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
                (
                    "title",
                    models.CharField(max_length=63, unique=True, verbose_name="Title"),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Unique identifying part of the URL",
                        max_length=63,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        max_length=63, unique=True, verbose_name="Subtitle"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Recommended resolution: 800px * 450px",
                        null=True,
                        upload_to="projects/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        help_text="Recommended resolution: 150px * 150px",
                        null=True,
                        upload_to="projects/",
                        verbose_name="Thumbnail",
                    ),
                ),
                ("content", models.TextField()),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")],
                        default=1,
                        verbose_name="Status",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created at"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "seo",
                    models.TextField(
                        blank=True,
                        default=None,
                        max_length=255,
                        null=True,
                        verbose_name="SEO Description",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("techstack", models.ManyToManyField(to="portfolio.techstack")),
                ("tools", models.ManyToManyField(to="portfolio.tool")),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
                "ordering": ["-created"],
            },
        ),
    ]
