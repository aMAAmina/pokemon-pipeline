#### Description
Refactor pokemon pipeline into a python package named `pokeops`. 

#### Objectives
1. pokeops/ingest.py
2. pokeops/transform.py
3. pokeops/pipeline.py

#### instructions
1. Create a CLI entry point named pokeops that launches the end-to-end pipeline using argparse
2. Set up a virtual environment, and make it reproducible using requirements.txt and/or pyproject.toml
3. Write at least 3 unit tests using pytest, one per module
4. Package it using setup.py or pyproject.toml for installation
5. Add CI with GitHub Actions to run the tests on each push

#### Example CLI command
Run from the root of the project(where `setup.py` is located): 
`pip install -e .` to make sure the package is installed in editable mode.

Then, you can run the pipeline with the following command:
```bash
python -m pokeops.cli --filter "water" --count 20
```
OR
```bash
pokeops --filter "water" --count 20