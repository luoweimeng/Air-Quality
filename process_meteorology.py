from netCDF4 import Dataset, num2date
import pandas as pd

pm25_data = pd.read_csv('pm25.csv', parse_dates=True, index_col=0, header=None)

nc_data = Dataset("test.nc", "r", format="NETCDF4")
times = num2date(nc_data.variables['time'][:], nc_data.variables['time'].units)

# lat:39.875, lon:116.375
t2m = pd.Series(nc_data.variables['t2m'][:, 9, 11], index=times)
t2m.shift(8, freq='H')
d2m = pd.Series(nc_data.variables['d2m'][:, 9, 11], index=times)
d2m.shift(8, freq='H')
u10 = pd.Series(nc_data.variables['u10'][:, 9, 11], index=times)
u10.shift(8, freq='H')
v10 = pd.Series(nc_data.variables['v10'][:, 9, 11], index=times)
v10.shift(8, freq='H')
print(pm25_data)
print(v10)
pd.concat([pm25_data, t2m, d2m, u10, v10])