import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Meal


def set_new_chefs():
    meals = Meal.objects.all()

    for meal in meals:
        if meal.meal_type == "Breakfast":
            meal.chef = "Gordon Ramsay"
        elif meal.meal_type == "Lunch":
            meal.chef = "Julia Child"
        elif meal.meal_type == "Dinner":
            meal.chef = "Jamie Oliver"
        elif meal.meal_type == "Snack":
            meal.chef = "Thomas Keller"

    Meal.objects.bulk_update(meals, ["chef"])


def set_new_preparation_times():
    meals = Meal.objects.all()

    for meal in meals:
        if meal.meal_type == "Breakfast":
            meal.preparation_time = 10
        elif meal.meal_type == "Lunch":
            meal.preparation_time = 12
        elif meal.meal_type == "Dinner":
            meal.preparation_time = 15
        elif meal.meal_type == "Snack":
            meal.preparation_time = 5

    Meal.objects.bulk_update(meals, ["preparation_time"])


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=("Breakfast", "Dinner")).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).delete()


if __name__ == "__main__":
    meal1 = Meal.objects.create(

        name="Pancakes",

        meal_type="Breakfast",

        preparation_time="20 minutes",

        difficulty=3,

        calories=350,

        chef="Jane",

    )

    meal2 = Meal.objects.create(

        name="Spaghetti Bolognese",

        meal_type="Dinner",

        preparation_time="45 minutes",

        difficulty=4,

        calories=550,

        chef="Sarah",

    )

    # Test the set_new_chefs function

    set_new_chefs()

    # Test the set_new_preparation_times function

    set_new_preparation_times()

    # Refreshes the instances

    meal1.refresh_from_db()

    meal2.refresh_from_db()

    # Print the updated meal information

    print("Meal 1 Chef:", meal1.chef)

    print("Meal 1 Preparation Time:", meal1.preparation_time)

    print("Meal 2 Chef:", meal2.chef)

    print("Meal 2 Preparation Time:", meal2.preparation_time)
