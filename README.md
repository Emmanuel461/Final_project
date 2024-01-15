### Final work course Introduction to Python 
# **Project description**
###Introduction to python 

Emmanuel Jesús Céspedes Rivera

This project aims to provide a tool for customized and fast downloading of satellite images, eliminating waiting times. This aspect is especially crucial for images corrected at the top of the atmosphere (surface reflectance).

The sensors available for download are:

1. Landsat 8 and 9
2. Sentinel 2
3. Sentinel 1 (Synthetic Aperture Radar)

These data are based on the use of the Geemap and ee libraries, used for processing information in Google Earth Engine (GEE). GEE is a free, cloud-based repository that enables access to large volumes of satellite data at various processing levels.

Each image can be downloaded in the Upper Atmosphere, Lower Atmosphere, and, in the case of Sentinel-1, with the default pre-processing provided by Google Earth Engine, with data available at the Ground Range Detected (GRD) processing level. For more details, you can check: [link](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD).