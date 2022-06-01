from uuid import UUID

from django.core.management.base import BaseCommand

from accounts.models import User
from syntax.models import Release, ReleaseChange, ReleaseChangeType

data = {
    'modelschema': [
        {'model_name': 'Book', 'fields': []},
    ],
}


class Command(BaseCommand):
    help = 'Setup testing environment'

    def handle(self, *args, **options):
        user = User.objects.create_superuser(email='admin@email.com', password=None)  # type: ignore
        user.set_password('superuser')
        user.save()

        initial_release = Release.objects.create(
            release_version='0.0.0',
            release_notes='Application Initialisation Release',
        )

        for model_type, definitions in data.items():
            for definition in definitions:
                ReleaseChange.objects.create(
                    parent_release=initial_release,
                    change_type=ReleaseChangeType.CREATE,
                    model_type=model_type,
                    syntax_json=definition,
                )

        second_release = Release.objects.create(
            parent=initial_release,
            release_version='0.1.0',
            release_notes='Initial release',
        )

        # ReleaseChange.objects.create(
        #     parent_release=second_release,
        #     change_type=ReleaseChangeType.DELETE,
        #     object_id=UUID(second_release.modelschemas[0]['id'], version=4),
        #     model_type='modelschema',
        #     syntax_json={},
        # )
        ReleaseChange.objects.create(
            parent_release=second_release,
            change_type=ReleaseChangeType.UPDATE,
            object_id=UUID(second_release.modelschemas[0]['id'], version=4),
            model_type='modelschema',
            syntax_json={'model_name': 'Horror Book', 'fields': []},
        )
        # ReleaseChange.objects.create(
        #     parent_release=second_release,
        #     change_type=ReleaseChangeType.CREATE,
        #     model_type='modelschema',
        #     syntax_json={'model_name': 'Rental', 'fields': []},
        # )

        # third_release = Release.objects.create(
        #     parent=second_release,
        #     release_version='0.2.0',
        #     release_notes='Second release',
        # )
