import numpy as np
import matplotlib.pyplot as plt
import csv

def gauss(x, A, x0, sigma):
    return A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

energy = []
counts = []

with open('Field_emission_distribution.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row == []:
                continue
            else:
                energy.append(float(row[0]))
                counts.append(float(row[1]))    
    csvfile.close()

energy = np.array(energy)
counts = np.array(counts)

A = 161.9
x0 = 0.06033
c = 0.2734
sigma = c/np.sqrt(2)

FWHM = 2*np.sqrt(2*np.log(2)) * sigma

energyticks = np.linspace(energy[0], energy[-1], 100)

########## Plotting the curve ############
plt.scatter(energy, counts, s=5, c='k')
plt.plot(energy, gauss(energy, A, x0, sigma), 'r', label='Gaussian fit')

plt.xlim(-1.3, 1.8)
# naming the x axis
plt.xlabel('Energy (eV)')
# naming the y axis
plt.ylabel('Counts ($\\times 10^{4}$)')
# giving a title to my graph
plt.title('Field emission distribution')
plt.legend()

plt.show()

print('Full width half maximum: ' +  str(round(FWHM, 5)) + ' eV, corresponding to sigma = ' + str(round(sigma, 5)))
print('Norminal energy: ' + str(round(x0, 5)) + ' eV')