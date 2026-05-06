import os

from django.conf import settings
from django.core.management.base import BaseCommand

from courses.models import Lecture, Practice, Resource


class Command(BaseCommand):
    help = "Create DB records for existing PDF files under the media folders."

    MAPPINGS = [
        ("lectures", Lecture, "Lecture"),
        ("practice", Practice, "Practice"),
        ("resources", Resource, "Resource"),
    ]

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT

        for folder, model, label in self.MAPPINGS:
            folder_path = os.path.join(media_root, folder)

            if not os.path.isdir(folder_path):
                self.stdout.write(self.style.WARNING(f"Media folder not found: {folder_path}"))
                continue

            pdf_files = sorted(
                filename for filename in os.listdir(folder_path)
                if filename.lower().endswith(".pdf")
            )

            if not pdf_files:
                self.stdout.write(self.style.NOTICE(f"No PDF files found in media/{folder}/"))
                continue

            for filename in pdf_files:
                relative_path = os.path.join(folder, filename).replace("\\", "/")

                if model.objects.filter(pdf=relative_path).exists():
                    self.stdout.write(f"Skipped existing {label}: {relative_path}")
                    continue

                title = os.path.splitext(filename)[0].replace("_", " ").replace("-", " ").title()
                instance = model(
                    title=title,
                    description=f"Imported from media/{folder}/",
                    pdf=relative_path,
                )
                instance.save()
                self.stdout.write(self.style.SUCCESS(f"Imported {label}: {relative_path}"))
