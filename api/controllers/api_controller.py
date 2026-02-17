import os
import pandas as pd # type: ignore
from sodapy import Socrata # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

def get_dates(api_limit, state):
    api_url = os.getenv("API_BASE_URL")
    api_source = os.getenv("API_RESOURCE")
    api_token = os.getenv("APP_TOKEN")

    client = Socrata(api_url, api_token, timeout = 15);

    results = client.get(api_source, limit = api_limit, where = f"departamento_nom='{state}'")

    results_df = pd.DataFrame.from_records(results)
    df_subset = results_df[["ciudad_municipio_nom", "departamento_nom", "edad", "sexo", "estado"]]
    
    return df_subset