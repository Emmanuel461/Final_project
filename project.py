#_______________________________________________________________________________________________________
# Code for Introduction to python final project 
# By Emmanuel Jesús Céspedes Rivera
# Please run the Pre-execution code first.

import geemap
import ee
import re
import json
import os


# In this classe we try to add all the things related with the filter of the image collection
class DateFilter:
    def __init__(self, start_date, end_date, point):
        # Initialization of the DateFilter class with start and end dates, point, and filtered collection
        self.start_date = start_date
        self.end_date = end_date
        self.collection, self.scale = self.get_sensor_info()
        self.point = self.get_point(point)
        self.collection_filtered = self.filter_collection()

    def get_sensor_info(self):
        while True:
            try:
                # Obtain sensor information (collection and scale) based on user's choice
                sensor_name = input('Write the name of the Sensor (Landsat 8/9, Sentinel 1(SAR), or 2): ').strip().upper().replace(" ", "")
                preprocess = self.surface_reflectance()
                landsat_toa_collections = {'LANDSAT8': 'LANDSAT/LC08/C02/T1_TOA', 'LANDSAT9': 'LANDSAT/LC09/C02/T1_TOA'}
                landsat_boa_collections = {'LANDSAT8': 'LANDSAT/LC08/C02/T1_L2', 'LANDSAT9': 'LANDSAT/LC09/C02/T1_L2'}
                
                # Define the collection and scale based on the sensor and preprocessing type
                if preprocess == 'TOA' and sensor_name in landsat_toa_collections:
                    collection = ee.ImageCollection(landsat_toa_collections[sensor_name])
                    scale = 30
                elif preprocess == 'BOA' and sensor_name in landsat_boa_collections:
                    collection = ee.ImageCollection(landsat_boa_collections[sensor_name])
                    scale = 30
                elif preprocess == 'SAR' and sensor_name == 'SENTINEL1':
                    collection = ee.ImageCollection('COPERNICUS/S1_GRD')
                    scale = 10
                elif preprocess == 'TOA' and sensor_name == 'SENTINEL2':
                    collection = ee.ImageCollection('COPERNICUS/S2')
                    scale = 10
                elif preprocess == 'BOA' and sensor_name == 'SENTINEL2':
                    collection = ee.ImageCollection('COPERNICUS/S2_SR')
                    scale = 10
                else:
                    raise ValueError('Insert a valid sensor.')
                return collection, scale
            except ValueError as ve:
                print(f"Error: {ve}")
                pass
    
    # Here the function is for filter the pre-process level
    def surface_reflectance(self):
        while True:
            try:
                # Obtain the desired preprocessing type (TOA, BOA, or SAR)
                choice = input("Do you want the image in TOA, BOA, or SAR (if you want data of Sentinel-1)?: ").upper()
                if choice in ["TOA", "BOA", "SAR"]:
                    return choice
                else:
                    print("Insert a right value (TOA, BOA, or SAR)")          
            except ValueError as ve:
                print(f"Error: {ve}")
                pass
    # Here we need to obtain a point for the filter bounds of the image collection
    def get_point(self, user_point):
        while True:
            try:
                # Obtain coordinates of the point of interest
                if user_point is not None:
                    return user_point
                x = float(input("Insert an X coordinate (for filter tile and bounds of the collection): "))
                y = float(input("Insert a Y coordinate (for filter tile and bounds of the collection): "))
                geometry = ee.Geometry.Point([x, y])
                return geometry
            except ValueError as ve:
                print(f"Error: {ve}")

    def filter_collection(self):
        # Filter the collection based on dates and the point of interest
        return self.collection.filterDate(self.start_date, self.end_date).filterBounds(self.point)
    
    # Create a property for managment of the start_date
    @property
    def start_date(self):
            return self._start_date
    
    # Management of the values of end date
    @start_date.setter
    def start_date(self, start_date):
        if not re.search(r'^\d{4}[-/]\d{2}[-/]\d{2}$', start_date):
            raise ValueError("Insert a valid start date (YYYY-MM-DD)")
        self._start_date = start_date
        
    # Create a property for managment of the end_date        
    @property
    def end_date(self):
        return self._end_date
    
    # Management of the values of start_date
    @end_date.setter
    def end_date(self, end_date):
        if not re.search(r'^\d{4}[-/]\d{2}[-/]\d{2}$', end_date):
            raise ValueError("Insert a valid end date (YYYY-MM-DD)")
        self._end_date = end_date


def clip(image, region):
    # Clip the image based on the specified region
    return image.clip(region)

# For clip the image (if we want) we need to use a file, in this case a geojson file in a directory in our computer or github
# GEE need this file in specific format so we upload the file and convert to format of GEE
def aoi_clip(clip_option):
    if clip_option == 1:
        geojson_path = input("Insert path to JSON file containing polygon information: ")
        if not os.path.exists(geojson_path):
            print(f"The file {geojson_path} does not exist.")
            return None
        else:
            with open(geojson_path) as f:
                geojson_data = json.load(f)
                try:
                    # Convert GeoJSON to Earth Engine geometry
                    geometry_clip = geemap.geojson_to_ee(geojson_data)
                    # Extract the first feature from the FeatureCollection
                    geometry_clip = ee.FeatureCollection(geometry_clip).geometry()
                    return geometry_clip
                except Exception as e:
                    print(f"Error converting GeoJSON to EE geometry: {e}")
                    
    else:
        return None

# Function for download without clip
def download_collection_region(collection, folder_name, scale, region):
    try:
        if region is None:
            print("Region is not defined. Downloading without clipping.")
        else:
            # Download the clipped collection based on the specified region
            geemap.download_ee_image_collection(
                collection,
                folder_name,
                scale=scale,
                region=region)
            print(f'The image was downloaded successfully in {folder_name}')
    except ValueError as e:
        print(f'Error downloading collection region: {e}')

# Function for download with clip
def download_collection(collection, folder_name, scale, region):
    try:
        # Download the collection based on the specified region (or without clipping if the region is not defined)
        geemap.download_ee_image_collection(
            collection,
            folder_name,
            scale=scale,
            region=region)
        print(f'The image was clipped and downloaded successfully in {folder_name}')
    except ValueError as e:
        print(f'Error downloading collection: {e}')


def main():
    ee.Initialize()
    try:
        # Get user input for dates and point of interest
        start_date = input("Insert start date (YYYY-MM-DD): ")
        end_date = input("Insert end date (YYYY-MM-DD): ")
        user_point = None
        # Create an instance of DateFilter
        date_filter_instance = DateFilter(start_date, end_date, user_point)
        # Ask the user if they want to clip the image
        clip_question = int(input("Do you want to clip the image? (0: No - 1: Yes): "))
        # Get the region only if the clip option is selected
        region = aoi_clip(clip_question) if clip_question == 1 else None  
        if clip_question == 0:
            if date_filter_instance.collection_filtered is not None and date_filter_instance.scale is not None:
                # Download the collection without clipping if the region is not defined
                folder_name = input("The image will be downloaded to your local folder, define the folder name: ")
                download_collection(
                    date_filter_instance.collection_filtered, folder_name, date_filter_instance.scale, region)
        elif clip_question == 1:
            if date_filter_instance.collection_filtered is not None and date_filter_instance.scale is not None:
                # Download the clipped collection if the region is defined
                folder_name = input("The image will be downloaded to your local folder, define the folder name: ")
                download_collection_region(
                    date_filter_instance.collection_filtered, folder_name, date_filter_instance.scale, region)
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()


#_____________________________________________ END CODE __________________________________________________________
