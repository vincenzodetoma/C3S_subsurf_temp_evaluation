import xarray as xr
import xarray.ufuncs as xu
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
var = ds[variable]
idx = len(depthvar.sel(depth=slice(0, float(depth))))
dz = dm['e3t_1d'].isel(depth=slice(0, idx))
if (depth == "1"):
  print("depth=1")
  vert_mean_15m = var.isel(depth=0)
else:
  print("depth different from 1")
  vert_mean_15m = var.isel(depth=slice(0,idx)).weighted(dz).mean('depth')

vert_mean_15m = vert_mean_15m.rename(variable+depth)
vert_mean_15m.to_netcdf(dest_path+'tmp/'+year+'/'+variable+'_'+depth+'m_ORCA-0.25x0.25_regular_'+year+month+'.nc')

ds.close()
dm.close()


