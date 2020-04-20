import xarray as xr
import xarray.ufuncs as xu
import numpy as np
import sys
variable=sys.argv[1]
year=sys.argv[2]
month=sys.argv[3]
depth=sys.argv[4]
data_path='/DataArchive/C3S/ORAS5/REGULAR/opa0/'
weight_path = '/DataArchive/cyang/GLORYS_Atlantic/GRID/ORAS5'
dest_path = '/DataArchive/C3S/subsurf_temp/'
dm = xr.open_dataset(weight_path+'/'+'mesh_mask.nc').rename({'t': 'time', 'z': 'depth'})
ds = xr.open_dataset(data_path+variable+'/'+variable+'_ORCA-0.25x0.25_regular_'+year+month+'.nc')
lat = ds.lat
lon = ds.lon
Nlat = len(lat)
Nlon = len(lon)
depthvar = ds.depth
idx = len(depthvar.sel(depth=slice(0, float(depth))))
var = ds[variable].isel(depth=slice(0,idx))
dz = dm['e3t_1d'].isel(depth=slice(0, idx))
w = np.cos(lat*np.pi/180.)
h_av = var.weighted(w).mean(dim=['lat', 'lon'])
globmean = h_av.weighted(dz).mean(dim='depth')

globmean = globmean.rename(variable+depth)
globmean.to_netcdf(dest_path+'tmp/'+year+'/glob_'+variable+'_'+depth+'m_ORCA-0.25x0.25_regular_'+year+month+'.nc')

ds.close()
dm.close()

