from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("articles", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("title", models.CharField(max_length=80)),
                ("content", models.TextField(max_length=500)),
                (
                    "grade",
                    models.IntegerField(
                        choices=[
                            (1, "★"),
                            (2, "★★"),
                            (3, "★★★"),
                            (4, "★★★★"),
                            (5, "★★★★★"),
                        ]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("hits", models.PositiveIntegerField(default=0, verbose_name="조회수")),
                (
                    "bookmark_users",
                    models.ManyToManyField(
                        related_name="bookmark_reivew", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "keyboard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.keyboard",
                    ),
                ),
                (
                    "like_users",
                    models.ManyToManyField(
                        related_name="like_review", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("image", models.ImageField(blank=True, upload_to="images/")),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="reviews.review"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.CharField(max_length=80)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "like_users",
                    models.ManyToManyField(
                        related_name="like_comment", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="reviews.review"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
