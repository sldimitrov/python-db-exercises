import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ChessPlayer


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gt=2400).update(title="GM")


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title="IM")


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2299, 2200)).update(title="FM")


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(2199, 0)).update(title="regular player")


# Test
player1 = ChessPlayer(
    username='Player1',
    title='no title',
    rating=2200,
    games_played=50,
    games_won=20,
    games_lost=25,
    games_drawn=5,
)

player2 = ChessPlayer(username='Player2', title='IM', rating=2350, games_played=80, games_won=40, games_lost=25,
                      games_drawn=15, )
bulk_create_chess_players([player1, player2])

delete_chess_players()

print("Number of Chess Players after deletion:", ChessPlayer.objects.count())
