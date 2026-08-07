import os
import django
import random
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event_management.settings")
django.setup()

from faker import Faker
from events.models import Category, Participant, Event

fake = Faker()


def populate():

    # Clear old data
    Event.objects.all().delete()
    Participant.objects.all().delete()
    Category.objects.all().delete()

    # Categories
    categories = []

    category_names = [
        "Technology",
        "Business",
        "Sports",
        "Education",
        "Music",
        "Gaming",
        "Health"
    ]

    for category_name in category_names:
        category = Category.objects.create(
            name=category_name,
            description=fake.text(max_nb_chars=100)
        )
        categories.append(category)

    # Participants
    participants = []

    for _ in range(30):
        participant = Participant.objects.create(
            name=fake.name(),
            email=fake.unique.email()
        )
        participants.append(participant)

    # Events
    for _ in range(10):

        event = Event.objects.create(
            name=fake.catch_phrase(),
            description=fake.paragraph(nb_sentences=4),
            date=fake.date_between(start_date="today", end_date="+90d"),
            time=fake.time_object(),
            location=f"{fake.city()}, {fake.country()}",
            category=random.choice(categories),
            ticket=Decimal(random.randint(100, 5000))
        )

        event.participants.set(
            random.sample(
                participants,
                random.randint(3, 10)
            )
        )

    print("Successfully created fake data.")


if __name__ == "__main__":
    populate()