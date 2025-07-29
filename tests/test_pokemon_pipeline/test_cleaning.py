import pandas as pd
from pokemon_pipeline.cleaning import *

def test_extract_pokemon_types():
    # Sample input DataFrame
    input_data = pd.DataFrame({
        "types": [
            [{"type": {"name": "grass"}}, {"type": {"name": "poison"}}],
            [{"type": {"name": "fire"}}],
            [{"type": {"name": "water"}}, {"type": {"name": "flying"}}]
        ]
    })

    # Expected output DataFrame
    expected_data = pd.DataFrame({
        "types": [
            [{"type": {"name": "grass"}}, {"type": {"name": "poison"}}],
            [{"type": {"name": "fire"}}],
            [{"type": {"name": "water"}}, {"type": {"name": "flying"}}]
        ],
        "pokemon_types": [
            ["grass", "poison"],
            ["fire"],
            ["water", "flying"]
        ]
    })
    result = extract_pokemon_types(input_data)
    pd.testing.assert_frame_equal(result, expected_data)

def test_prepare_columns():
    # Sample input DataFrame
    input_data = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Bulbasaur", "Charmander", "Squirtle"],
        "weight": [69, 85, 90],
        "height": [7, 6, 5],
        "types": [
            [{"type": {"name": "grass"}}, {"type": {"name": "poison"}}],
            [{"type": {"name": "fire"}}],
            [{"type": {"name": "water"}}, {"type": {"name": "flying"}}]
        ],
        "pokemon_types": [
            ["grass", "poison"],
            ["fire"],
            ["water", "flying"]
        ]
    })
    # Expected output DataFrame
    expected_data = pd.DataFrame({
        "pokemon_id": [1, 2, 3],
        "pokemon_name": ["Bulbasaur", "Charmander", "Squirtle"],
        "pokemon_weight": [69, 85, 90],
        "pokemon_height": [7, 6, 5],
        "pokemon_types": [
            ["grass", "poison"],
            ["fire"],
            ["water", "flying"]
        ]
    })
    result =  prepare_columns(input_data)
    pd.testing.assert_frame_equal(result, expected_data)

def test_data_validation():
    # Sample input DataFrame
    input_data = pd.DataFrame({
        "pokemon_id": [
            1,
            12,
            148
        ]
    })
    # Expected output DataFrame same as input DataFrame
    result =  data_validation(input_data)
    pd.testing.assert_frame_equal(result, input_data)

def test_filter_by_type():
    # Sample input DataFrame
    input_data = pd.DataFrame({
        "pokemon_id": [
            1,
            12,
            148
        ],
        "types": [
            [{"type": {"name": "water"}}, {"type": {"name": "poison"}}],
            [{"type": {"name": "fire"}}],
            [{"type": {"name": "water"}}, {"type": {"name": "flying"}}]
        ],
        "pokemon_types": [
            ["water", "poison"],
            ["fire"],
            ["water", "flying"]
        ]
    })
    filter_type = "water"
    # Expected output DataFrame
    output_data = pd.DataFrame({
        "pokemon_id": [
            1,
            148
        ],
        "types": [
            [{"type": {"name": "water"}}, {"type": {"name": "poison"}}],
            [{"type": {"name": "water"}}, {"type": {"name": "flying"}}]
        ],
        "pokemon_types": [
            ["water", "poison"],
            ["water", "flying"]
        ]
    })
    result = filter_by_type(input_data, filter_type)
    pd.testing.assert_frame_equal(result, output_data)