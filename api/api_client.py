import json

import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all(self) -> json:
        url = self.base_url
        response = requests.get(f"{url}/type")
        return response

    def get_pokemon_type_url(self, _type: str) -> str:
        response = self.get_all()
        parsed_response = response.json()
        url = next((item['url'] for item in parsed_response['results'] if item['name'] == _type), None)
        if url is not None:
            return url
        else:
            raise ValueError(f"No URL found for '{_type}' pokemons in the response.")

    def get_pokemon_type_data(self, _type: str) -> json:
        response = requests.get(self.get_pokemon_type_url(_type=_type))
        return response.json()

    def get_pokemon_type_id(self, _type: str) -> int:
        response = self.get_pokemon_type_data(_type=_type)
        id = response['id']
        return id

    def get_pokemon_names_by_type(self, _type: str) -> list:
        response = self.get_pokemon_type_data(_type=_type)
        pokemon_names = [item['pokemon']['name'] for item in response['pokemon']]
        return pokemon_names

    def pokemon_weights(self, _type: str):
        pokemon_weights_dict = {}
        response = self.get_pokemon_type_data(_type=_type)
        for pokemon in response['pokemon']:
            # I extract from each pokemon dict its name and the url to its personal details
            pokemon_name = pokemon['pokemon']['name']
            pokemon_url = pokemon['pokemon']['url']
            # Performs a GET request for each of the Pokemon
            # If successful, I extract his weight from the answer
            iter_resp = requests.get(pokemon_url)
            if iter_resp.status_code == 200:
                weight = iter_resp.json()["weight"]
                # Creates a new dictionary with the name and weight of each Pokemon
                pokemon_weights_dict[pokemon_name] = weight
        return pokemon_weights_dict

    @staticmethod
    def get_five_heaviest_pokemons(pokemon_weight_dict: dict):
        sorted_pokemons = sorted(pokemon_weight_dict.items(), key=lambda x: x[1], reverse=True)
        five_heaviest_pokemons = sorted_pokemons[:5]
        return five_heaviest_pokemons
