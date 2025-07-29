import argparse
from pokeops.ingest import ingest
from pokeops.transform import transform

def run_pipeline(filter_type=None, count=None):
    import time

    print("start pipeline ...")

    # Step 1: Ingest data
    ingest_exec_time = time.perf_counter()
    fetched_pok = ingest(count=count)
    ingest_exec_time = time.perf_counter() - ingest_exec_time
    ingest_status = "success" if fetched_pok else "failed or skipped"
    if not fetched_pok:
        ingest_exec_time = 0.0

    # Step 2: Transform data
    trans_exec_time = time.perf_counter()
    processed_pok = transform(filter_type=filter_type)
    trans_exec_time = time.perf_counter() - trans_exec_time
    trans_status = "success" if trans_exec_time > 0 else "failed"

    # Generate report
    report_lines = [
        "final report",
        f"-ingestion: {ingest_status}",
        f"-execution time of ingestion: {ingest_exec_time}",
        f"-transformation and validation: {trans_status}",
        f"-execution time transformation and validation: {trans_exec_time}",
        f"-number of fetched pokemons: {fetched_pok}",
        f"-numbers of pokemons processed: {processed_pok}" 
    ]

    for line in report_lines:
        print(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="run data pipeline")
    parser.add_argument('--filter', help='Filter based on type; e.g., keep water type pokemon')
    parser.add_argument('--count', help='Fetch the first N pokemons, e.g., 20')
    args = parser.parse_args()

    run_pipeline(filter_type=args.filter, count=int(args.count) if args.count else None)
