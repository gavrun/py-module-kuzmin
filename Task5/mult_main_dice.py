from mult_mod_dice import get_players, play_game, find_winner

p1, p2 = get_players()
s1, s2 = play_game(p1, p2)
find_winner(p1, p2, s1, s2)
