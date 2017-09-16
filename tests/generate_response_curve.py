import astropy.io.fits
import numpy as np
import matplotlib.pyplot as plt

# Create an empty numpy array. 2D; spectra with 4 data elements.
filtered = np.zeros((2040,4))

combined_extracted_1d_spectra_ = astropy.io.fits.open("xtfbrsnN20160705S0025.fits")
exptime = float(combined_extracted_1d_spectra_[0].header['EXPTIME'])

wstart = combined_extracted_1d_spectra_[1].header['CRVAL1']
wdelt = combined_extracted_1d_spectra_[1].header['CD1_1']

for i in range(len(filtered)):
	filtered[i][0] = wstart + (i*wdelt)

print "Wavelength array: \n", filtered

f = open("hk.txt")
lines = f.readlines()
f.close()
lines = [lines[i].strip().split() for i in range(len(lines))]
for i in range(len(lines)):
	lines[i][0] = float(lines[i][0])*10**4

for i in range(len(filtered)):
	mindif = min(lines, key=lambda x:abs(x[0]-filtered[i][0]))
	filtered[i][1] = mindif[2]

calibspec = np.load("calibspec.npy")

"""
effspec = np.load("effspec.npy")

print "Effspec:\n", effspec


calibspec = np.zeros((2040))


for i in range(len(effspec)):
	if effspec[i] != 0:
		calibspec[i] = combined_extracted_1d_spectra_[1].data[i]/exptime/effspec[i]
	else:
		calibspec[i] = 0
"""

filter_weighted_flux = []
temp_percentages = []
for i in range(len(calibspec)):
	filtered[i][2] = calibspec[i]
	filtered[i][3] = filtered[i][1] * filtered[i][2] * 0.01
	filter_weighted_flux.append(filtered[i][3])
	temp_percentages.append(filtered[i][1]*0.01)

print "\nIntegral of filter_weighted_flux:" 
print np.trapz(filter_weighted_flux)
print "\nIntegral of percentages:"
print np.trapz(temp_percentages)
print "Integral of filter_weighted_flux divided by integral of percentages:"
print np.trapz(filter_weighted_flux)/np.trapz(temp_percentages)
plt.figure(1)
plt.plot(calibspec)
plt.plot(filter_weighted_flux, "r--")
plt.figure(2)
plt.plot(temp_percentages)
plt.show()
