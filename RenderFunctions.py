import numpy as np
import wx
class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ''
        wx.Frame.__init__(self, parent, title=title)
        pass

class OutputImage:
    edge_buffer_percentage = .05
    def __init__(self, monitor_height, monitor_width):
        self.img = np.zeros((monitor_height // 2, monitor_width // 2, 3), dtype=np.uint8)
        self.total_region_range_yx = np.array([0, self.img.shape[0], 0, self.img.shape[1]])
        edge_buffer_x, edge_buffer_y = int(self.total_region_range_yx[2] * self.edge_buffer_percentage), int(self.total_region_range_yx[3] * self.edge_buffer_percentage)
        self.total_region_range_yx[0:2] += edge_buffer_y, -edge_buffer_y
        self.total_region_range_yx[2:] += edge_buffer_x, -edge_buffer_x


def two_dimension_plot_render():
    pass