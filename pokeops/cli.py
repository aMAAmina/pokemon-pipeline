import argparse
from pokeops.pipeline import run_pipeline 

def main():
    parser = argparse.ArgumentParser(description="Run the Pokémon data pipeline.")
    parser.add_argument("--filter", help="Filter based on type; e.g., keep water type pokemon.")
    parser.add_argument("--count", help="Fetch the first N pokemons, e.g., 20.")
    args = parser.parse_args()

    run_pipeline(filter_type=args.filter, count=int(args.count) if args.count else None)

if __name__ == "__main__":
    main()