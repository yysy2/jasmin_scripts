import numpy as np
import iris
import matplotlib.pyplot as plt
import iris.plot as iplt
import iris.quickplot as qplt

root = '/group_workspaces/jasmin2/ukca/ptg21/xlpzb/xlpzba.pm'
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
years = ['2000']

sec34_stashes = {
    101:'nuc_mode_sol number',
    102:"nuc mode",
    103:"Ait mode number",
    104:"Ait mode h2so4",
    105:"Ait mode bc",
    106:"Ait mode oc",
    107:"Acc mode sol number",
    108:"Acc mode h2so4",
    109:"Acc mode bc",
    110:"Acc mode oc",
    111:"Acc mode ss",
    113:"Crs mode sol number",
    114:"Crs mode h2so4",
    115:"Crs mode bc",
    116:"Crs mode oc",
    117:"Crs mode ss",
    119:"Ait mode insol number",
    120:"Ait mode insol BC",
    121:"Ait mode insol OC",
    126:"Nuc mode sol OC",
    126:"Ait mode sol SS",
    157:"Aerosol surface area",
    159:"O3 column",
    160:"N2O5 het rate",
    161:"HO2 self het rate",
    001:"O3 MMR"
    }
sec35_stashes = {001:'o3 on p levels'}

filenames = []
for yvar in range (0, len(years)):
  for ivar in range(0,len(months)):
    filenames = np.append(filenames, iris.sample_data_path(root + years[yvar] + months[ivar] + '.pp'))

stash_index=157
aerosol_sa=iris.load(filenames, iris.AttributeConstraint(STASH = 'm01'+'s34i'+str(stash_index))
iris.fileformats.netcdf.save(aerosol_sa, 'test_sa.nc')


