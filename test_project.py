# Import the functions and classes you want to test
from project import DateFilter, aoi_clip
from unittest.mock import patch
import ee
import pytest
#_______________________________________________________________________________________________________
# Note: pytest should be called using this code: pytest -s test_project.py 
# The -s allows the capture of inputs in the console
#_______________________________________________________________________________________________________

ee.Initialize()

@pytest.fixture
def date_filter_instance():
    start_date = '2022-01-01'
    end_date = '2022-01-10'
    user_point = ee.Geometry.Point([1.0, 2.0])
    instance = DateFilter(start_date, end_date, user_point)
    return instance

def test_date_filter():
    # Create an instance of DateFilter with predefined dates and point
    start_date1 = '2022-01-01'
    end_date1 = '2022-01-10'
    user_point = ee.Geometry.Point([1.0, 2.0])
    date_filter_instance = DateFilter(start_date1, end_date1, user_point)

    # Verify that the dates are set correctly
    assert date_filter_instance.start_date == start_date1
    assert date_filter_instance.end_date == end_date1
    # Verify that the filtered collection is not None
    assert date_filter_instance.collection_filtered is not None


def test_surface_reflectance():
    # Create an instance of DateFilter with predefined dates and point
    start_date = '2022-01-01'
    end_date = '2022-01-10'
    user_point = ee.Geometry.Point([1.0, 2.0])
    date_filter_instance = DateFilter(start_date, end_date, user_point)

    # Define the value that should be entered by the user
    user_input_value = 'TOA'

    # Use patch to simulate user input
    with patch('builtins.input', return_value=user_input_value):
        # Call the surface_reflectance() function directly
        result = date_filter_instance.surface_reflectance()

    # Verify that the result is the simulated value
    assert result == user_input_value


def test_aoi_clip_user_provided_geojson_from_pc():
    ##### BE CAREFULL HERE -------------------------------------------- -j-
    # If you want to test this, use your local direcction of the ubication file
    user_geojson_path = 'C:/Users/cespe/Documents/Documents/Introductionpython/Final_project_2/AOI.geojson' 

    # Simulate user input by selecting option 1 and providing the GeoJSON file path
    with patch('builtins.input', side_effect=[user_geojson_path]):
        # Simulate the existence of the file
        with patch('os.path.exists', return_value=True):
            result = aoi_clip(1)
    # Verify that the result is not None (indicating a valid GeoJSON file location)
    assert result is not None
    # Verify that the result is an instance of the ee.Geometry class
    assert isinstance(result, ee.Geometry)

#_____________________________________________ END CODE __________________________________________________________




