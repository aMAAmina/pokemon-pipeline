from setuptools import setup, find_packages

setup(
    name="pokemon_pipeline",
    version="0.1",
    description="A pipeline for preprocessing Pokémon data.",
    author="Your Name",
     # Automatically includes `pokeops` and other sub-packages
    packages=find_packages(), 
    install_requires=[
        "pandas>=2.0.0", 
        "requests>=2.0.0"
    ],
    entry_points={
        "console_scripts": [
            # Adds `pokeops` as a CLI command
            "pokeops=pokeops.cli:main",  
        ],
    },
)