import pylas
import laspy
import numpy as np




las = pylas.read("C:\\Users\\yuri7100\\Desktop\\lidar_raleigh_nc_spm_height_feet_las\\lidar_raleigh_nc_spm_height_feet.las")
print(las.header)
print(las.z.max())

