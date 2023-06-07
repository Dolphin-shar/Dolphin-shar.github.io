## [Home](README.md) 
Michaelis-Menten kinetics is an analysis on enzymatic activity, which are usually consist of a *Initial reaction velocity* dependence and a *Substrate concentration* variable in the curve. By controling difference initial reaction concentration and measuring the corresponding reaction velocity, we can plot a M-M curve and give us more detailed prodiction on enzymatic activity. However, in order to plot such curve, multiple sets of experiment will be needed as different concentration would be tested, the analysis of data would be repetitive and thus, we can create a standardised way to analyse to improve our efficiency. Here is an example,
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit_function(x,m,c):
    return m*x + c

def half_area_OD(OD,background,bac_type):
    OD = (OD-background)*4
    print("OD is {} for {}".format(OD,bac_type))
    return OD

def averaging_function(function,xdata,paras1,paras2):
    paras1 = np.array(paras1)
    paras2 = np.array(paras2)
    average = np.mean([paras1,paras2],axis= 0)
    print("Average of fitted parameters are {}".format(average))
    y1 = function(xdata,*paras1)
    y2 = function(xdata,*paras2)
    avey = function(xdata,*average)
    plt.plot(xdata,y1,label = "line set")
    plt.plot(xdata,y2,label = "line dup")
    plt.plot(xdata,avey, label = "line average")
    plt.title("Averaged curve from fitted function")
    plt.legend()
    plt.show()


class michealis_menten_analysis:
    def __init__(self, time, intensity):
        self.time = time
        self.intensity = intensity

    
    def fitting(self,correction = 3, number_of_initial_points = 10,paras = None,starting_data_point = 0, title = "MM exp vs fitted data",Unit = None):
        for i in range(correction):
            paras, self.covar = curve_fit(fit_function,xdata = self.time[starting_data_point:number_of_initial_points+1],ydata = self.intensity[starting_data_point:number_of_initial_points+1],p0=paras)
        self.paras = paras
        print("Fitted parameters are {}".format(self.paras))
        plt.plot(self.time,self.intensity,"ro",label = "experimental data")
        plt.plot(self.time,fit_function(self.time,*self.paras),"-b",label = "fitted curve")
        plt.title(title)
        plt.legend()
        plt.xlabel("Time(s)")
        plt.ylabel("Intensity({})".format(Unit))
        plt.show()

```
<br>
This module takes in an array of time and intensity measured for each set of experiment, producing the corresponding time dependent reaction plot and produce the fitted parameter of initial raction velocity and intensity shift value.