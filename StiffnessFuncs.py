import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn as skl
from sklearn.metrics import r2_score

import bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import gridplot, row, column
from bokeh.models import Slope
output_notebook()
# poop

##------------------------------------------------------------------------------------------------------------------------
# Use Bokeh to Pick the index you want for th following sections:
    # DDS_Area is in mm
    # Dat is the data set you want

def convert_units (dat, DDS_Area):

    DDS_Area = DDS_Area # Area in meters of the surface

    p = figure(tools='pan,box_zoom, xzoom_in, yzoom_in, reset,save,box_select,hover',
          title = 'Slow-Slip Experiment')
    p.line((dat[2,:]/1e6),(dat[3,:] * 1e6 * DDS_Area))
    p.xaxis.axis_label = 'Vertical Displacement [m]'
    p.yaxis.axis_label = 'Vertical Force [N]'
    show(p, ncols=1, plot_width=1200, plot_height=400)

    return

    # dat[2,:] = dat[2,:]/1e6 # Displacment [m]
    # dat[3,:] = dat[3,:]*1e6 * DDS_Area # Force [N]
    # df['Vert DCDT [m]'] = df['Vert DCDT']/1e6 # Displacment [m]
    # df['Vert Force [N]'] = (df['Vert LOAD']*1e6) * DDS_Area # Force [N]


##-----------------------------------------------------------------------------------------------------------------------
    # x and y are the numpy array columns
    # idx are the index points from the run.

def k_section (dat, x, y, idx1, idx2):
    Disp = dat[x,idx1:idx2]
    Force = dat[y,idx1:idx2]

    return Disp, Force

##----------------------------------------------------------------------------------------------------------------------
# Fit the unload or reload section of the curve with a slope:
    # x and y are you displacement and force values from k_section

def k_slope(x,y):

    m[0] = np.polyfit(x,y, 1)
    fit = np.polyval(m[0], x)
    r2 = r2_score(y, fit)

    return m[0], fit, r2

##-----------------------------------------------------------------------------------------------------------------------
# Plot the Stiffness and Data:
    # x1, y1 are the raw data range for first unload/reload
    # x2, y2 are the raw data range for the second unload/reload.



def k_graph(x1, y1, x2, y2, unload1, reload1, unload2, reload2, expnum):

    fig = plt.figure(figsize=(12, 6), dpi=100)

    ax1, ax2 = fig.subplots(1,2, sharey=True)

    ax1.plot(x1, y1, color = 'black')
    ax1.plot(unload1[0], unload1[1], color = 'r', label = 'Unload Linear Fit')
    ax1.plot(reload1[0], reload1[1], color = 'b', label = 'Reload Linear Fit')
    ax1.set_title('expnum first', fontsize=12)
    ax1.legend()

    ax2.plot(x2, y2, color = 'black')
    ax2.plot(unload2[0], unload2[1], color = 'r', label = 'Unload Fit, r^2 = ')
    ax2.plot(reload2[0], reload2[1], color = 'b', label = 'Reload Linear Fit')
    ax2.set_title('expnum second', fontsize=12)
    ax2.legend()

    plt.show()


    ##----------------------------------------------------------------------------------------------------------------------
