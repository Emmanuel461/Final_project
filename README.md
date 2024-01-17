# **Project description (https://emmanuel461.github.io/Final_project/)**

**University of Lisbon**


Instituto Superior de Agronomia (ISA)

Introduction to python 

This project aims to provide a tool for customized and fast downloading of satellite images, eliminating waiting times. This aspect is especially crucial for images corrected at the top of the atmosphere (surface reflectance).

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



1. **Run the Pre-execution Code:** Ensure that the pre-execution code is run before using the tool.
2. **Input Dates and Point:** Provide start and end dates, and point of interest. (In case of choosing to crop the image using the GeoJson file available in this GitHub repository, it is recommended to use the coordinates X: -84.45 and Y: 9.34).
3. **Select Sensor and Preprocessing:** Choose a sensor and the desired preprocessing type (TOA, BOA, or SAR).
4. **Clip Option:** Decide whether to clip the image based on a region. Users can provide a GeoJSON file for custom regions.
5. **Download Images:** Specify a local folder for downloading the images, and the tool will handle the download process.

**Note:** The tool supports sensors like Landsat 8/9, Sentinel 1 (SAR), and Sentinel 2, offering flexibility and convenience for satellite image retrieval.

For further details on the Sentinel-1 data processing level, refer to the [Google Earth Engine documentation](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD).

*By Emmanuel Jesús Céspedes Rivera*

