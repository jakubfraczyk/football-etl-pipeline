import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def load_to_db(df, table_name="standings"):
    """Load cleaned dataFrame into PostgreSQL database"""
    try:
        engine = create_engine(DATABASE_URL)
        df.to_sql(name = table_name,con = engine, index=False, if_exists="replace")

        print(f"Successfully loaded {len(df)} rows into '{table_name}' table")

    except Exception as e:
        print(e)
if __name__ == "__main__":
    from extract import get_standings
    from transform import transform_standings

    raw = get_standings("PL")
    df = transform_standings(raw)
    load_to_db(df)