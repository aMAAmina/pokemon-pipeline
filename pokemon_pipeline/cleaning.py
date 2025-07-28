import pandas as pd

def extract_pokemon_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the 'types' column into a list of type names.

    Args:
        df (pd.DataFrame): A DataFrame containing a 'types' column with nested type data.

    Returns:
        pd.DataFrame: The modified DataFrame with a new 'pokemon_types' column.
    """
    if "types" not in df.columns:
        raise KeyError("The DataFrame does not contain a 'types' column.")

    df["pokemon_types"] = df["types"].apply(lambda types: [t["type"]["name"] for t in types])

    return df

def prepare_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Only relevant columns are kept and renamed

    Args:
        df (pd.DataFrame): A DataFrame containing all columns, and a new 'pokemon_types' column.

    Returns:
        pd.DataFrame: The modified DataFrame(only selceted columns, and renamed).
    """
    if "pokemon_types" not in df.columns:
        raise KeyError("The DataFrame does not contain 'pokemon_types'")
    
    df = df[["id", "name", "weight", "height", "pokemon_types"]]
    df.columns = ["pokemon_id", "pokemon_name", "pokemon_weight", "pokemon_height", "pokemon_types"]

    return df

def data_validation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Asserts there are no duplicate Pokemon

    Args:
        df (pd.DataFrame): A DataFrame containing a 'pokemon_id' column.

    Returns:
        pd.DataFrame: The same DataFrame if validation passes.

    Raises:
        ValueError: If duplicate Pokémon IDs are found.
    """
    if df["pokemon_id"].duplicated().any():
        raise ValueError("Duplicate user_ids found")
    return df
    
def filter_by_type(df: pd.DataFrame, filter_type: str) -> pd.DataFrame:
    """
    filters the pokemons by type.

    Args:
        df (pd.DataFrame): A cleaned data_frame.
        filter_type: the type to filter by the DataFrame
    
    returns:
        pd.DataFrame: all pokemons with the specific type 
    """
    df = df[df["pokemon_types"].apply(lambda types: filter_type in types)]
    return df