import expected_data.expected_data


def test_pokemon_count_and_type(api_client):
    response = api_client.get_all()
    response_data = response.json()
    assert isinstance(response_data, dict)
    assert response_data["count"] == expected_data.expected_data.expected_pokemon_count


def test_question_two(api_client):
    fire_type_id = api_client.get_pokemon_type_id('fire')
    response = api_client.get_pokemon_type_data('fire')
    # Based on question 2 sections a and b, I assume that there is a list named 'Pokemon'
    pokemon_names = [pokemon['pokemon']['name'] for pokemon in response['pokemon']]
    assert fire_type_id == 10
    assert 'charmander' in pokemon_names
    assert 'bulbasaur' not in pokemon_names


def test_get_five_heaviest_pokemon_of_the_fire_type(api_client):
    response = api_client.get_five_heaviest_pokemons(pokemon_weight_dict=api_client.pokemon_weights('fire'))
    assert response == list(expected_data.expected_data.expected_heaviest_pokemons.items())
