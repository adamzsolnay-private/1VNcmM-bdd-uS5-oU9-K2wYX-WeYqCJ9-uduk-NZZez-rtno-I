import sqlite3

def create_db():
    with sqlite3.connect("weather.db") as conn:
        cursor = conn.cursor()

        create_table_query = r'''
        CREATE TABLE IF NOT EXISTS Metrics (
            sensor_id INTEGER,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            wind_speed REAL NOT NULL
        );
        '''

        cursor.execute(create_table_query)
        conn.commit()
        print('DB is created and initialized...')


def insert_values(sensor_id, timestamp, temperature, humidity, wind_speed):
    try:
        sqliteConnection = sqlite3.connect("weather.db")
        cursor = sqliteConnection.cursor()

        sqlite_insert = """INSERT INTO Metrics
                              (sensor_id, timestamp, temperature, humidity, wind_speed)
                              VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (sensor_id, timestamp, temperature, humidity, wind_speed)
        cursor.execute(sqlite_insert, data_tuple)
        sqliteConnection.commit()
        print("Success: new records are inserted into the DB.")
        cursor.close()
        return "201"

    except sqlite3.Error as error:
        err_msg = "Failed to insert new values into the DB"
        print(err_msg, error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
          
