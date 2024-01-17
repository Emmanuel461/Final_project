# **Project description**

**University of Lisbon**


Instituto Superior de Agronomia (ISA)

Introduction to python 

This project [Webpage]((https://emmanuel461.github.io/Final_project/)) aims to provide a tool for customized and fast downloading of satellite images, eliminating waiting times. This aspect is especially crucial for images corrected at the top of the atmosphere (surface reflectance).

The sensors available for download are:

1. Landsat 8 and 9
2. Sentinel 2
3. Sentinel 1 (Synthetic Aperture Radar)

These data are based on the use of the Geemap and ee libraries, used for processing information in Google Earth Engine (GEE). GEE is a free, cloud-based repository that enables access to large volumes of satellite data at various processing levels.

Each image can be downloaded in the Upper Atmosphere, Lower Atmosphere, and, in the case of Sentinel-1, with the default pre-processing provided by Google Earth Engine, with data available at the Ground Range Detected (GRD) processing level. For more details, you can check: [link](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD).



# Satellite Image Download Tool Steps

## DateFilter Class

The `DateFilter` class is designed to handle the filtering of image collections based on specified start and end dates, a chosen sensor, and a designated point of interest. It offers the following features:

- **Sensor Selection:** Users can choose from sensors such as Landsat 8/9, Sentinel 1 (SAR), and Sentinel 2.
- **Preprocessing Options:** TOA (Top of Atmosphere), BOA (Bottom of Atmosphere), or SAR (Synthetic Aperture Radar) preprocessing can be selected based on user preferences.
- **Filtering by Point:** Users should provide coordinates for filter the image collection. 

## Image Clipping

The tool allows users to clip downloaded images based on a specified region. Users have the option to define a region using a GeoJSON file, providing flexibility in tailoring the output to specific geographic areas.

## Usage Instructions
In this specific scenario, it becomes essential to have multiple inputs to efficiently filter satellite images. To address this type of use case, it is essential to have accurate information about the area of interest, the relevant dates, the specific sensor required and, crucially, the desired level of processing. To avoid high data downloads, the option to crop the satellite image, focusing on the region of interest provided, is offered. 

This aspect was meticulously taken into account, given that the code necessitates multiple inputs. Nonetheless, as indicated towards the end, such a requirement was deemed necessary in light of the application's inherent nature.

1. **Run the Pre-execution Code:** Ensure that the pre-execution code is run before using the tool.
(You need a GEE account for this section, if you don't have, can register here: [Register in GEE](https://code.earthengine.google.com/register)
2. **Input Dates and Point:** Provide start and end dates, and point of interest. (If you decide to crop the image using the provided GeoJSON file from this GitHub repository, it is recommended to use the coordinates X: -84.45 and Y: 9.34.).
3. **Select Sensor and Preprocessing:** Choose a sensor and the desired preprocessing type (TOA, BOA, or SAR).
4. **Clip Option:** Decide whether to clip the image based on a region. Users can provide a GeoJSON file for custom regions.
5. **Download Images:** Specify a local folder for downloading the images, and the tool will handle the download process.

**Note:** The tool supports sensors like Landsat 8/9, Sentinel 1 (SAR), and Sentinel 2, offering flexibility and convenience for satellite image retrieval.

For further details on the Sentinel-1 data processing level, refer to the [Google Earth Engine documentation](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD).

The repository comprises the following components:

1. A pre-execution code.
2. A file named `requirements.txt`, which contains the names of the libraries required to run the project (use `pip install -r requirements.txt` in your terminal to install the necessary libraries).
3. A GeoJSON file, available for use in the code execution as an example. This file is spatially located in Perez Zeledon, San Jose, Costa Rica.
4. The `README.md` file, containing current information about the project.
5. A `_config.yml` file, holding the configuration of the web page ([link](https://emmanuel461.github.io/Final_project/)).
6. The `project.py` file, containing the code for downloading satellite images.
7. The `test_project.py` file, designed for performing tests on some of the functions used in `project.py`.


*By Emmanuel Jesús Céspedes Rivera*

