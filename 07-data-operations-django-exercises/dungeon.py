import os
import django
from django.db.models import Model
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import *


def update_characters():
    characters = Character.objects.all()

    for character in characters:
        if character.class_name == "Mage":
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == "Warrior":
            character.hit_points /= 2
            character.dexterity *= 4
        elif character.class_name == "Assassin" or character.class_name == "Scout":
            character.inventory = "The inventory is empty"


def fuse_characters(character: Character, second_character: Character):
    # Create a brand new characters and drop fusion ones
    name = f"{character.name} {second_character.name}"
    class_name = "Fusion"
    level = (character.level + second_character.level) // 2
    strength = (character.strength + second_character.strength) * 1.2
    dexterity = (character.dexterity + second_character.dexterity) * 1.5
    intelligence = (character.intelligence + second_character.intelligence) * 1.5
    hit_points = character.hit_points + second_character.hit_points
    inventory = \
        "Bow of the Elven Lords, Amulet of Eternal" if character.class_name in ["Mage",
                                                                                "Scout"] else "Dragon Scale Armor, Excalibur"

    # Create fusion character
    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory,
    )

    # Delete old chars
    character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence=40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    characters_to_delete = Character.objects.filter(inventory="The inventory is empty").delete()


if __name__ == "__main__":
    character1 = Character.objects.create(
        name='Gandalf',
        class_name='Mage',
        level=10,
        strength=15,
        dexterity=20,
        intelligence=25,
        hit_points=100,
        inventory='Staff of Magic, Spellbook',
    )

    character2 = Character.objects.create(
        name='Hector',
        class_name='Warrior',
        level=12,
        strength=30,
        dexterity=15,
        intelligence=10,
        hit_points=150,
        inventory='Sword of Troy, Shield of Protection',
    )

    fuse_characters(character1, character2)
    fusion = Character.objects.filter(class_name='Fusion').get()

    print(fusion.name)
    print(fusion.class_name)
    print(fusion.level)
    print(fusion.intelligence)
    print(fusion.inventory)
