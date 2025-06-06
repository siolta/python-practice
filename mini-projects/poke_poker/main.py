import requests
import random


# Get 2 random pokemon
# fetch list of those pokemons moves and HP
# Cache the data locally
# for each move, get it's attack power and add it to the cache
# pick a pokemon to start
# take turns using random moves until one faints


def get_all_pokemon():
    print("Fetching all pokemon")
    url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
    data = requests.get(url).json()
    poke_list = [name["name"] for name in data["results"]]
    parsed_data = {"count": len(poke_list), "pokemon": poke_list}
    return parsed_data


def parse_pokemon_stats(pokemon_data: dict):
    """fetch given pokemons hp and moves"""
    stat_data = {
        "hp": pokemon_data["stats"][0]["base_stat"],
    }

    return stat_data


def parse_pokemon_moves(pokemon_data: str):
    move_data = []
    for move in pokemon_data["moves"]:
        move_name = move["move"]["name"]
        move_url = move["move"]["url"]
        move_data.append((move_name, move_url))

    return move_data


def construct_pokemon_cache(poke_dex):
    rand_id = random.randint(0, poke_dex["count"])
    pokemon = poke_dex["pokemon"][rand_id]
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    data = requests.get(url).json()
    pokemon_struct = {
        "name": pokemon.capitalize(),
        "stats": parse_pokemon_stats(data),
        "moves": parse_pokemon_moves(data),
    }

    return pokemon_struct


def pokemon_attack(attacker, defender, move: tuple):
    attk_pwr = requests.get(move[1]).json()["power"]
    print(f"{attacker['name']} uses {move[0]}!")
    if attk_pwr:
        print(f"{move[0]} does {attk_pwr // 2} damage!")
        defender["stats"]["hp"] -= attk_pwr // 2
    else:
        print(f"{move[0]} has no power!")
    print(f"{defender['name']} HP is now: {defender['stats']['hp']}\n")


def battle(poke_a, poke_b):
    poke_a_moves = len(poke_a["moves"])
    poke_b_moves = len(poke_b["moves"])
    while poke_a["stats"]["hp"] > 0 or poke_b["stats"]["hp"] > 0:
        # a attacks, b attacks
        a_move = poke_a["moves"][random.randint(0, poke_a_moves)]
        b_move = poke_b["moves"][random.randint(0, poke_b_moves)]
        print(f"{poke_a['name']} attacks!")
        pokemon_attack(poke_a, poke_b, a_move)
        if poke_b["stats"]["hp"] <= 0:
            print(f"{poke_b['name']} fainted!")
            break
        print(f"{poke_b['name']} attacks!")
        pokemon_attack(poke_b, poke_a, b_move)
        if poke_a["stats"]["hp"] <= 0:
            print(f"{poke_a['name']} fainted!")
            break


def print_start(a, b):
    print("3... 2... 1...\n")
    print("Two pokemon are about to battle!")
    print(f"It's: {a['name']}, with {a['stats']['hp']}")
    print("vs")
    print(f"{b['name']}, with {b['stats']['hp']}\n")


def main():
    pokemon_dict = get_all_pokemon()
    print("Choosing two random pokemon...")
    pokemon_a = construct_pokemon_cache(pokemon_dict)
    pokemon_b = construct_pokemon_cache(pokemon_dict)
    print_start(pokemon_a, pokemon_b)
    battle(pokemon_a, pokemon_b)


if __name__ == "__main__":
    main()
