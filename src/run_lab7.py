from database import check_connection, fetch_parcels_by_land_use

if check_connection():
    rows = fetch_parcels_by_land_use("Residential")

    print("Rows returned:", len(rows))

    if rows:
        print("First database row:", rows[0])
