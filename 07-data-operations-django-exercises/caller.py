import decimal
import os
import django
from django.db.models import Model

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import *
import datetime

locations = [
    {
        "name": "Sofia",
        "region": "Sofia Region",
        "population": 1329000,
        "description": "The capital of Bulgaria and the largest city in the country",
        "is_capital": False
    },
    {
        "name": "Plovdiv",
        "region": "Plovdiv Region",
        "population": 346942,
        "description": "The second-largest city in Bulgaria with a rich historical heritage",
        "is_capital": False
    },
    {
        "name": "Varna",
        "region": "Varna Region",
        "population": 330486,
        "description": "A city known for its sea breeze and beautiful beaches on the Black Sea",
        "is_capital": False
    }
]


# Create queries within functions
def create_pet(name: str, species: str):
    pet = Pet.objects.create(name=name, species=species)
    pet.save()

    return f"{pet.name} is a very cute {pet.species}"


# Artifacts
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    artifact.save()

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name


def delete_all_artifacts():
    Artifact.objects.all().delete()


# Location
def add_locations():
    for location in locations:
        Location(**location).save()


def show_all_locations():
    locations = Location.objects.all()

    output = []

    for location in locations:
        output.append(f"{location.name} has a population of {location.population}!")

    return "\n".join(output)


def new_capital():
    first_location = Location.objects.first()

    first_location.is_capital = True
    first_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values_list("name", flat=True)


def delete_first_location():
    first_location = Location.objects.first()

    if first_location:
        first_location.delete()
        return "First location deleted successfully!"

    return "No locations found to delete."


# Car
cars = [
    {
        "model": "Mercedes C63 AMG",
        "year": 2019,
        "color": "white",
        "price": 120000.00
    },
    {
        "model": "Audi Q7 S line",
        "year": 2023,
        "color": "black",
        "price": 183900.00
    },
    {
        "model": "Chevrolet Corvette",
        "year": 2021,
        "color": "dark grey",
        "price": 199999.00
    }
]


def add_cars():
    for car in cars:
        Car.objects.create(**car)


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        discount = 0

        for digit in str(car.year):
            discount += int(digit)

        discount_price = car.price * decimal.Decimal(discount / 100)

        car.discount = discount
        car.price_with_discount = discount_price
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()


# Task Encoder
def show_unfinished_tasks():
    due_tasks = Task.objects.filter(due_date__lte=datetime.date.today())

    result = []

    for task in due_tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")


def complete_odd_tasks():
    odd_ids = [id for id in Task.objects.values_list("id", flat=True) if id % 2 == 1]

    Task.objects.filter(id__in=odd_ids).update(is_finished=True)


def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.filter(title=task_title)

    for task in tasks:
        updated_description = ""

        for letter in text:
            ascii_num = ord(letter)
            # Shift the position by 3
            ascii_num -= 3

            # Add character to the updated description
            updated_description += chr(ascii_num)

        # Update the description
        task.description = updated_description

    Task.objects.bulk_update(tasks, "description")


# Hotel Room
def get_deluxe_rooms():
    pass


def increase_room_capacity():
    pass


def increase_room_capacity():
    pass


def reserve_first_room():
    pass


def delete_last_room():
    pass


if __name__ == "__main__":
    pass
