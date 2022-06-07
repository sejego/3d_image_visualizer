from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
import numpy as np
from pathlib import Path
import copy
import yaml

from pointcloud import PointCloud
from depthmap import DepthMap
from validate_yaml import validate_yaml
from popups import show_err, show_info

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    """ Main business logic for the visualization app """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # Initialize None objects (placeholders for actual data)
        self.depth_map = None
        self.loaded_point_cloud = None
        self.used_point_cloud = None
        self.config = {"z_min": 0.0, "z_max": 0.0}

        # Signals from buttons
        self.PCImportBtn.clicked.connect(self.import_point_cloud)
        self.DMImportBtn.clicked.connect(self.import_depth)
        self.ConfigImportBtn.clicked.connect(self.import_config)
        self.PCExportBtn.clicked.connect(self.export_point_cloud)
        self.ConfigApplyBtn.clicked.connect(self.apply_configuration)
        self.ConfigResetBtn.clicked.connect(self.reset_point_cloud)
        self.ConfigExportBtn.clicked.connect(self.export_config)

        # Initialize plots
        self.init_plots()

    """
    Gets a file based on its filters. If file is chosen, returns its name,
    otherwise - None. 
    """
    def import_file(self, filters):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Import file', str(Path.home()), filters)
        if filename[0] != '':
            return filename[0]
        else:
            return None

    def export_file(self, filters):
        filename = QtWidgets.QFileDialog.getSaveFileName(
            None, 'Import file', str(Path.home()), filters)
        if filename[0] != '':
            return filename[0]
        else:
            return None

    """ 
    Initializes MatPlotLibs in PyQT 
    """
    def init_plots(self):
        self.axis = self.figDepth.add_subplot(111)  # for DepthMap
        self.axes = self.figPointCloud.add_subplot(111, projection='3d')    # For PointCloud
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Z')
        self.axes.set_zlabel('Y')
        self.canvasPointCloid.draw()
        self.canvasDepth.draw()

    """ 
    Plots 3D MatPlotLib PointCloud data. Places a camera vertex at (0, 0, 0).
    """
    def draw_point_cloud(self, point_cloud):
        self.axes.clear()
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Z')
        self.axes.set_zlabel('Y')
        x = point_cloud.data[:, 0]
        y = point_cloud.data[:, 1]
        z = point_cloud.data[:, 2]
        self.axes.scatter(x, z, y, s=0.5, marker=',', c='red')
        # FOV center point (e.g. centerpoint of camera lens)
        self.axes.scatter(0.0, 0.0, 0.0, s=1, marker='d', c='m')
        self.canvasPointCloid.draw()

    """
    Plots a pseudocolor 2D plot of the DepthMap.
    """
    def draw_depth_map(self, depth_map):
        self.axis.clear()
        self.axis.pcolor(depth_map.data, cmap="gray")
        self.canvasDepth.draw()

    """
    Resets the PointCloud to the one that was initially loades and
    resets the plot to this PointCloud.
    """
    def reset_point_cloud(self):
        try:
            if self.loaded_point_cloud is None:
                show_err("Error resetting the plot - PointCloud is empty")
            else:
                self.used_point_cloud = copy.copy(self.loaded_point_cloud)
                self.draw_point_cloud(self.loaded_point_cloud)
        except Exception as e:
            show_err("Error resetting the plot" + str(e))

    """
    Exports the PointCloud that is currently displayes in the app
    as .csv file.
    """
    def export_point_cloud(self):
        if self.used_point_cloud is not None:
            filename = self.export_file("CSV files (*.csv)")
            if filename is not None:
                try:
                    with open(filename, 'w') as f:
                        np.savetxt(f, self.used_point_cloud.data,
                                   delimiter=",", fmt="%f", header="x,y,z")
                except:
                    show_err('Error exporting PointCloud to CSV')
                show_info('Exported successfully')
        else:
            show_err("Nothing to export (PointCloud is empty)")
    
    """
    Exports the configuration from YAML based on the numbers inserted in the 
    configuration fields.
    """
    def export_config(self):
        try:
            self.update_config_params()
            filename = self.export_file("YAML files (*.yaml)")
            if filename is not None:
                with open(filename, 'w') as f:
                    yaml.dump(self.config, f)
                show_info('Exported successfully')
        except Exception as e:
            show_err('Error exporting Configuration to YAML. ' + str(e))
    
    def import_depth(self):
        filename = self.import_file("HDF document (*.hdf5)")
        if filename is not None:
            try:
                self.depth_map = DepthMap.from_file(filename)
                self.draw_depth_map(self.depth_map)

                # Automatically convert to PointCloud and display
                self.loaded_point_cloud = PointCloud.from_depth_map(self.depth_map)
                self.used_point_cloud = copy.deepcopy(self.loaded_point_cloud)
                self.draw_point_cloud(self.loaded_point_cloud)
            except Exception as e:
                show_err("DepthMap import failed. " + str(e))
    
    def import_point_cloud(self):
        filename = self.import_file("CSV files (*.csv)")
        if filename is not None:
            try:
                self.loaded_point_cloud = PointCloud.from_file(filename)
                self.used_point_cloud = copy.deepcopy(self.loaded_point_cloud)
                self.draw_point_cloud(self.loaded_point_cloud)
            except Exception as e:
                show_err("PointCloud import failed. " + str(e))
    
    def import_config(self):
        filename = self.import_file("YAML files (*.yaml)")
        if filename is not None:
            try:
                with open(filename, "r") as f:
                    self.config = yaml.safe_load(f)
                    validate_yaml(self.config)
                    self.RangeBeginInput.setText(str(self.config["z_min"]))
                    self.RangeEndInput.setText(str(self.config["z_max"]))
                    self.apply_configuration()
            except Exception as e:
                show_err("Config import failed. " + str(e))

    """
    Modify the PointCloud based on the configuration and redraw the graph
    """
    def apply_configuration(self):
        try:
            self.update_config_params()
            if self.used_point_cloud is None:
                raise Exception("PointCloud is not loaded.")
            self.used_point_cloud.filter_by_z(self.config["z_min"], self.config["z_max"])
            self.draw_point_cloud(self.used_point_cloud)
        except Exception as e:
            show_err("Could not modify PointCloud. " + str(e))

    """
    Reads the numbers from the configuration fields and 
    set them to instance variable.
    """
    def update_config_params(self):
        Z_min = self.RangeBeginInput.text()
        Z_max = self.RangeEndInput.text()
        if(Z_min != '' and Z_max != ''):
            self.config['z_min'] = float(Z_min)
            self.config['z_max'] = float(Z_max)
        else:
            raise Exception("Configuration parameters cannot be empty.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
