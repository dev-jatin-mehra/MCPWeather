import sqlite3
from config import DATABASE_FILE

def query_weather_cache():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        print("Available tables:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(f"- {table[0]}")

        if 'weather_data' in [table[0] for table in tables]:
            print("\nQuerying the 'weather_data' table:")

            # Select all rows and columns from the weather_data table
            cursor.execute("SELECT * FROM weather_data")
            rows = cursor.fetchall()

            if rows:
                # Get column names for better readability
                cursor.execute("PRAGMA table_info(weather_data)")
                columns_info = cursor.fetchall()
                column_names = [info[1] for info in columns_info]
                print(f"{' | '.join(column_names)}")
                print("-" * (sum(len(name) + 3 for name in column_names) - 3)) # Separator

                for row in rows:
                    print(f"{' | '.join(str(item) for item in row)}")
            else:
                print("The 'weather_data' table is empty.")
        else:
            print("\nThe 'weather_data' table does not exist.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    query_weather_cache()