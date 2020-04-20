#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:43:22 2019

@author: Andrea.Pisano@artov.isac.cnr.it
"""
def trend_2d_parallel(data_2d, masked_array, lat, lon, time, fill_value, frequency, nsplit):
    
    import numpy as np
#    import netCDF4 as nc
    from slice_trend import slice_trend
    from joblib import Parallel, delayed
    
#    nsplit=16

    half_frequency = np.int(frequency/2)
    
    time_length = len(time)

    trend_matrix=np.zeros((len(lat),len(lon)))
    trend_pvalue = np.zeros((len(lat),len(lon)))
    trend_significance = np.zeros((len(lat),len(lon)))
#    time_vector = np.linspace(1,len(time),len(time))
    
    year_length = np.int(time_length/12)
    indexes=[np.array(range(i*12,(i+1)*12)).astype(int) for i in range(np.int(year_length))]
    
    #for i in range(len(lon)):
    #    print(i)
    #    result=slice_trend(masked_array[:,i,:],data_2d[:,i,:],lon,half_frequency,year_length,indexes,frequency,fill_value)
    result = Parallel(n_jobs=nsplit)(delayed(slice_trend)(masked_array[:,i,:],data_2d[:,i,:],lon,half_frequency,year_length,indexes,frequency,fill_value,i) for i in range(len(lat)))
    
    for i in range(len(lat)):
        print('lat: ',i)
        trend_matrix[i,:]=result[i][0]
        trend_pvalue[i,:]=result[i][1]
        trend_significance[i,:]=result[i][2]
    
   
    return trend_matrix, trend_pvalue, trend_significance


