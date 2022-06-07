import numpy as np
import h5py
from depth_map_to_point_cloud import depth_map_to_point_cloud

class DepthMap():
    """ DepthMap class containing data of the DepthMap image.

    Attributes:
        data : numpy array of <f8 type containing distances (z) from the camera plane
        fov_data : horizontal and vertival FOV angles ( in degrees )
    """

    def __init__(self):
        self.fov_data = {'horizontal_fov_deg': np.NaN,
                         'vertical_fov_deg': np.NaN}
        self.data = np.zeros((), "<f8")

    @classmethod
    def from_file(cls, filename):
        """ Construct a DepthMap object from a hdf5 file and extract FOV data """
        obj = DepthMap()
        file = h5py.File(filename, 'r')
        depth_map = file['depth_map']
        obj.data = np.zeros(depth_map.shape, dtype=depth_map.dtype)
        depth_map.read_direct(obj.data)
        metadata = dict(file['depth_map'].attrs.items())
        obj.fov_data = {"horizontal_fov_deg": metadata["horizontal_fov_deg"],
                        "vertical_fov_deg": metadata["vertical_fov_deg"]}
        file.close()
        return obj
