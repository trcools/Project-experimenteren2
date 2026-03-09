import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d

sheet = pd.read_excel("Data/Kalibratie magnetisch veld.xlsx", 0)

d = np.array(sheet['d(mm)'])
B = np.stack((sheet['Bx (µT)'], sheet['By (µT)'], sheet['Bz (µT)']), 1) * 10**-6
B_magnitude = (np.einsum('ij, ij -> i', B, B))**(1/2)

# We gaan er vanuit dat het veld in het midden van de spoelen perfect in de juiste richting is gericht
# Om het veld dan langs deze as te integreren moeten we de component van het veld langs deze as te bepalen
# We bepalen dus een eenheidsvector door de gemiddelde richting te bepalen van de middelste metingen
# en dan het puntproduct te nemen met onze data
mask = B[:, 1] > 10**-3
# We selecteren de metingen met een y-component groter dan 1 mT

eenheidsvector = np.sum(B[mask, :], 0)
eenheidsvector = eenheidsvector / (eenheidsvector @ eenheidsvector)**(1/2)

B_langs_as = B @ eenheidsvector


# =================================================================
# Is dat hier BIOPHYSICS
# =================================================================

B_data = B_langs_as * 10**3 # B_data in militesla

plt.plot(d, B_data)
plt.xlabel("d (mm)")
plt.ylabel("B langs as (mT)")

plt.title("Kalibratie van het magnetisch veld")
plt.grid()
plt.show()

# =================================================================
# Interpolatie van het veld
# =================================================================

interpolatie = interp1d(d, B_langs_as, kind='cubic')
d_interpolatie = np.linspace(d[0], d[-1], 100)
B_interpolatie = interpolatie(d_interpolatie)
plt.plot(d, B_langs_as, 'o', label='Data')
plt.plot(d_interpolatie, B_interpolatie, '-', label='Interpolatie')
plt.xlabel("d (mm)")
plt.ylabel("B langs as (T)")
plt.title("Interpolatie van het magnetisch veld")
plt.grid()
plt.legend()
plt.show()

# Het minimum van het veld in het midden tussen de 10 en 17 mm,
# het minimum die daar wordt bekomen is het gevolg van dat onze 2 spoelen tegen elkaar gelijmd zijn,
# en dat het dat het veld daar iets minder sterk is.

# Aan de hand van dat minimum kunnen we bepalen op welke afstand het midden van de spoelen ligt, 
# en op welke afstanden van de spoel de rest van het magnetisch veld is.

# -----------------------------------------------------------------------
# midden bepalen
# -----------------------------------------------------------------------

mask = (d > 10) & (d < 17)
d_midden = d[mask][np.argmin(B_langs_as[mask])]
print(f"Het midden van de spoelen ligt op {d_midden:.2f} mm")