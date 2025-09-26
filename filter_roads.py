import geopandas as gpd

# === 1. Load your GeoJSON ===
input_file = "sabah_road.geojson"   # input file
output_file = "sabah_main_roads.geojson"  # output file

print("Loading data...")
gdf = gpd.read_file(input_file)

print(f"Original number of roads: {len(gdf)}")

# === 2. Filter only motorway, primary, secondary AND not null name ===
filtered = gdf[
    (gdf["fclass"].isin(["motorway", "primary", "secondary"])) &
    (gdf["name"].notnull())
]

print(f"Filtered number of roads: {len(filtered)}")

# === 3. Save the filtered result ===
filtered.to_file(output_file, driver="GeoJSON")

print(f"Filtered roads saved to: {output_file}")
