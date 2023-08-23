from sqlalchemy import create_engine, text
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class DBHandler:
    def __init__(self, url):
        self.engine = create_engine(url)

    def run_query(self, query):
        try:
            with self.engine.connect() as conn:
                conn.execute(text(query))
                conn.commit()
                logging.info("Sikeres művelet")
        except Exception as e:
            conn.rollback()
            logging.error(f"A Hiba: {str(e)}")
            raise

    def fetch_data(self, query):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                conn.commit()
                logging.info("Sikeres lekérés")
                return result.fetchall()

        except Exception as e:
            conn.rollback()
            logging.error(f"A Hiba: {str(e)}")
            raise

    def insert_data(self, query, data):
        try:
            with self.engine.connect() as conn:
                conn.execute(text(query), data)
                conn.commit()
            logging.info("Sikeres adat hozzáadás")
        except Exception as e:
            conn.rollback()
            logging.error(f"A Hiba: {str(e)}")
            raise

    def delete(self, query):
        try:
            with self.engine.connect() as conn:
                conn.execute(text(query))
                conn.commit()
            logging.info("Sikeres törlés")
        except Exception as e:
            conn.rollback()
            logging.error(f"A Hiba: {str(e)}")
            raise
