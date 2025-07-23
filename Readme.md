#### Description
This a one day hackathon project with Arkx, basically a pipline that fetchs data from the API `https://pokeapi.co/api/v2/pokemon` and goes through ingestion and transformation to eventually generate cleaned data in a CSV format.
The pipeline gives a detailed report at the end of the process.

#### Technologies Used
- Python
- Pandas
- Requests
- JSON  

#### Columns in the CSV
By eye inspection, these columns were found to be meaningful and included in the final CSV output:
- pokemon_id
- pokemon_name
- pokemon_weight
- pokemon_height
- pokemon_types[]

#### How to Run
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the script using `python pipeline.py`.
4. The output will be saved in `data/raw` and `data/processed`.