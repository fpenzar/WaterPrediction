import sqlite3


with open("site_coordinates.csv", "w") as file:
    conn = sqlite3.connect("database/old_database_geolux.db")
    sites = conn.execute("""select distinct(si.site_id), latitude, longitude from site si 
                            join sensor se on si.site_id=se.site_id
                            join sensor_measurement_type smt on smt.sensor_type_id=se.sensor_type
                            where measurement_type_id=4 or measurement_type_id=5 or measurement_type_id=6 or measurement_type_id=7 or measurement_type_id=20
                            """).fetchall()
    file.write("site_id,latitude,longitude\n")
    for site in sites:
        row = str(site[0]) + ',' + str(site[1]) + ',' + str(site[2]) + '\n'
        file.write(row)
 