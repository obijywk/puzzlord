from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save


def add_to_default_group(sender, **kwargs):
    from django.contrib.auth.models import Group

    user = kwargs["instance"]
    if kwargs["created"]:
        try:
            group = Group.objects.get(name="Testsolvers")
            user.groups.add(group)
        except ObjectDoesNotExist:
            pass


class PuzzleEditingConfig(AppConfig):
    name = "puzzle_editing"
    verbose_name = "Puzzle Editing"

    def ready(self):
        post_save.connect(add_to_default_group, sender=settings.AUTH_USER_MODEL)
