
from database import check_connection, fetch_parcels_by_land_use
from spatial import Parcel

# Step 1: Check database connection
if check_connection():

    # Step 2: Retrieve Residential parcels
    rows = fetch_parcels_by_land_use("Residential")

    print("Rows returned:", len(rows))

    if rows:
        print("First database row:", rows[0])

    # Step 3: Convert database rows into Parcel objects
    parcels = [
        Parcel.from_row(row)
        for row in rows
    ]

    print("Parcel objects created:", len(parcels))

    if parcels:
        first = parcels[0]
        print(
            "First Parcel object:",
            first.parcel_id,
            first.land_use,
        )
