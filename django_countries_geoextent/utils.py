import json

import geopandas as gpd


def read_gadm_countries(geopackage_path, out_file):
    gdf = gpd.read_file(geopackage_path, layer="ADM_0")

    countries = {}

    for index, row in gdf.iterrows():
        countries[row["GID_0"]] = {
            "name": row["COUNTRY"],
            "bbox": row["geometry"].bounds
        }

    with open(out_file, "w") as outfile:
        json.dump(countries, outfile)
