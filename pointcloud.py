import numpy as np
from depth_map_to_point_cloud import depth_map_to_point_cloud

class PointCloud():
    """ PointCloud class containing data of the PointCloud image.

    Attributes:
        data : numpy array of <f8 type containing (x, y, z) coordinates of points
        fov_data : horizontal and vertival FOV angles ( in degrees )
    """

    def __init__(self):
        self.data = np.zeros((), "<f8")
        self.fov_data = {"horizontal_fov_deg": np.NaN,
                         "vertical_fov_deg": np.NaN}

    def filter_by_z(self, z_min, z_max):
        self.data = self.data[(self.data[:, 2] > z_min)
                              & (self.data[:, 2] < z_max)]

    @classmethod
    def from_depth_map(cls, map):
        """ Constructs a PointCloud object from DepthMap """
        obj = PointCloud()
        obj.data = depth_map_to_point_cloud(
            map.data, map.fov_data['horizontal_fov_deg'], map.fov_data["vertical_fov_deg"])
        return obj

    @classmethod
    def from_file(cls, filename):
        """ Constructs a PointCloud object from CSV file """
        obj = PointCloud()
        obj.data = np.genfromtxt(filename, delimiter=',', dtype="<f8", usecols=(
            0, 1, 2), loose=False, skip_header=1)
        obj.fov_data = {"horizontal_fov_deg": np.NaN,
                        "vertical_fov_deg": np.NaN}
        return obj