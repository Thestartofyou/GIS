import geopandas as gpd
import folium

# Assuming you have a shapefile or GeoJSON file containing the forest boundary
forest_boundary_file = 'path/to/forest_boundary.shp'
forest_boundary = gpd.read_file(forest_boundary_file)

# Assuming you have a shapefile or GeoJSON file containing the location of cut trees
cut_trees_file = 'path/to/cut_trees.shp'
cut_trees = gpd.read_file(cut_trees_file)

# Create a base map using Folium
map_center = [latitude_center, longitude_center]  # Center of the rainforest area
m = folium.Map(location=map_center, zoom_start=10)

# Add the forest boundary to the map
folium.GeoJson(forest_boundary).add_to(m)

# Add cut trees to the map as markers
for idx, tree in cut_trees.iterrows():
    folium.Marker([tree['latitude'], tree['longitude']], popup=f"Cut Tree {idx}").add_to(m)

# Save the map as an interactive HTML file
m.save('rainforest_trees_map.html')

