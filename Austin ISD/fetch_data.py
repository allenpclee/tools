import geopandas as gpd
import os
import requests
import zipfile
import io

def download_and_extract_shapefile(url, target_dir):
    print(f"Downloading shapefile from {url}...")
    response = requests.get(url)
    print("Extracting...")
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall(target_dir)
    print("Extraction complete.")

target_dir = "shapefile_data"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 1. Process ISDs
isd_url = "https://www2.census.gov/geo/tiger/GENZ2022/shp/cb_2022_48_unsd_500k.zip"
isd_shp = os.path.join(target_dir, "cb_2022_48_unsd_500k.shp")
if not os.path.exists(isd_shp):
    download_and_extract_shapefile(isd_url, target_dir)

print("Loading ISD shapefile...")
gdf_isd = gpd.read_file(isd_shp)

target_isds = ["Eanes", "Dripping Springs", "Leander", "Lake Travis", "Liberty Hill", "Round Rock"]
gdf_isd_filtered = gdf_isd[gdf_isd['NAME'].str.contains('|'.join(target_isds), case=False, na=False)].copy()
gdf_isd_filtered = gdf_isd_filtered.to_crs(epsg=4326)
gdf_isd_filtered.to_file("isds.geojson", driver="GeoJSON")
print("Saved isds.geojson")

# 2. Process Cities (Places)
place_url = "https://www2.census.gov/geo/tiger/GENZ2022/shp/cb_2022_48_place_500k.zip"
place_shp = os.path.join(target_dir, "cb_2022_48_place_500k.shp")
if not os.path.exists(place_shp):
    download_and_extract_shapefile(place_url, target_dir)

print("Loading Places shapefile...")
gdf_place = gpd.read_file(place_shp)
gdf_place = gdf_place.to_crs(epsg=4326)

# Austin area bounding box approx:
# Longitude: -98.3 to -97.3
# Latitude: 30.0 to 30.8
minx, miny, maxx, maxy = -98.3, 30.0, -97.3, 30.8
# Use spatial index to filter
gdf_place_filtered = gdf_place.cx[minx:maxx, miny:maxy].copy()

# Filter out very small CDPs if we want, or just keep them all
gdf_place_filtered.to_file("cities.geojson", driver="GeoJSON")
print("Saved cities.geojson")
