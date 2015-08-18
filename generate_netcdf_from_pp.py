import numpy as np
import iris
import matplotlib.pyplot as plt
import iris.plot as iplt
import iris.quickplot as qplt

root = '/group_workspaces/jasmin2/ukca/ptg21/xlpzb/xlpzba.pm'
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
years = ['2000']

#filenames = np.empty(0)
filenames = []
for yvar in range (0, len(years)):
  for ivar in range(0,len(months)):
    filenames = np.append(filenames, iris.sample_data_path(root+years[yvar]+months[ivar]+'.pp'))


aerosol_sa=iris.load(filenames, iris.AttributeConstraint(STASH='m01s34i157'))
iris.fileformats.netcdf.save(aerosol_sa, 'test_sa.nc')


