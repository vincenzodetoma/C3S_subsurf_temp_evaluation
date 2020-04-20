def slice_trend(masked_array1d,data_1d,lon,half_frequency,year_length,indexes,frequency,fill_value,k):
    print('loop: ',k)
    import numpy as np
    from statsmodels.tsa.seasonal import seasonal_decompose
    from mk_test import mk_test
    
    masked_array1d=np.squeeze(masked_array1d)
    data_1d=np.squeeze(data_1d)
    
    trend_matrix=np.zeros(lon.shape)
    trend_pvalue=np.zeros(lon.shape)
    trend_significance=np.zeros(lon.shape)
    
    
    for j in range(len(lon)):
        if np.isnan(masked_array1d[:,j]).all() == False:
            
            pixel_array = data_1d[:,j]       
            result = seasonal_decompose(pixel_array, model='additive', filt=None, freq=frequency, two_sided=True, extrapolate_trend=0)  
            monthly_trend_component = result.trend[half_frequency:-half_frequency]
            n_years_trend_component = np.int(year_length-frequency/12)
            yearly_trend_component = [np.average(monthly_trend_component[indexes[t]]) for t in range(n_years_trend_component)]
            trend,h,p,z,slope,std_conf = mk_test(yearly_trend_component, np.linspace(1,n_years_trend_component,n_years_trend_component), False, 1.5)
            
            if trend == 'no trend':
                trend_matrix[j] = np.nan
            else:
                trend_matrix[j] = slope
            trend_pvalue[j] = (1.-p)*100.
            trend_significance[j] = h
        else:
            trend_matrix[j] = np.nan
            trend_pvalue[j] = np.nan
            trend_significance[j] = np.nan
            
    return(trend_matrix,trend_pvalue,trend_significance)
