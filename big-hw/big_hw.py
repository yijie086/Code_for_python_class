import numpy as np
np.set_printoptions(linewidth=1000000000000000000000)
R = 128
calR = 20
zoombeta=2;
sz=256*zoombeta;
dr=R/sz;
cfl=0.01;
dt=dr*cfl;
tnum=8000000;
tlength=tnum*dt;
Dim=2;
g=0.60;
A=1.0;
a=81;
sigma=90;
peroid=200;
pi=3.1415926535898;
numofrT=16;

def potenial(phi):
    return (0.5 * (phi * phi - phi * phi * phi * phi + g * phi * phi * phi * phi * phi * phi))


def pdpotenial(phi):
    return (1.0 * phi - 2.0 * phi * phi * phi + 3.0 * g * phi * phi * phi * phi * phi)


def myabs(i):
    if i>=0:
        return i
    else:
        return -i-1


def pdr(phi, i):
    if sz-i >= 2:
        return ((phi[myabs(i - 2)] - 8.0 * phi[myabs(i - 1)] + 8.0 * phi[myabs(i + 1)] - phi[myabs(i + 2)]) / (
                    12.0 * dr))
    else:
        return ((3.0 * phi[i - 4] - 16.0 * phi[i - 3] + 36.0 * phi[i - 2] - 48.0 * phi[i - 1] + 25.0 * phi[i]) / (
                    12.0 * dr))


def pd2r(phi, i ):
    if sz-i >=2:
        return ((-phi[myabs(i - 2)] + 16.0 * phi[myabs(i - 1)] - 30.0 * phi[myabs(i)] + 16.0 * phi[myabs(i + 1)] - phi[
            myabs(i + 2)]) / (12.0 * dr * dr))
    else:
        return ((-10 * phi[i - 5] + 61.0 * phi[i - 4] - 156.0 * phi[i - 3] + 214.0 * phi[i - 2] - 154.0 * phi[
            i - 1] + 45.0 * phi[i]) / (12.0 * dr * dr))


def outputphi(j, phi, peroid):
    if np.ceil(j/peroid) == j/peroid:
        f = open("phi.dat", mode='a', encoding="utf-8")
        f.write(str(j*dt) + ' ')
        for i in range(len(phi)):
            f.write(str(phi[i]) + ' ')
        f.write('\n')
        f.close()


def outputpdtphi(j, pdtphi, peroid):
    if np.ceil(j/peroid) == j/peroid:
        f = open("pdtphi.dat", mode='a', encoding="utf-8")
        f.write(str(j * dt) + ' ')
        for i in range(len(pdtphi)):
            f.write(str(pdtphi[i]) + ' ')
        f.write('\n')
        f.close()


def outputpdrphi(j, pdrphi, peroid):
    if np.ceil(j/peroid) == j/peroid:
        f = open("pdrphi.dat", mode='a', encoding="utf-8")
        f.write(str(j * dt) + ' ')
        for i in range(len(pdrphi)):
            f.write(str(pdrphi[i]) + ' ')
        f.write('\n')
        f.close()


def outputr(r):
    f = open("r.dat", mode='a', encoding="utf-8")
    for i in range(len(r)):
        f.write(str(r[i])+' ')
    f.write('\n')
    f.close()


def outputrT(rT):
    f = open("rT.dat", mode='a', encoding="utf-8")
    for i in range(len(rT)):
        f.write(str(rT[i]) + ' ')
    f.write('\n')
    f.close()


def formular(r, phi, pdtphi, pdrphi, pd2rphi, pdrtphi, i):
    if sz-i <= 2:
        return (-0.5*phi[i]-pdrtphi[i]-((Dim-1.0)/(2.0*r[i]))*pdtphi[i])
    else:
        return (pd2rphi[i]+((Dim-1.0)/(r[i]))*pdrphi[i]-pdpotenial(phi[i]))


def energycal(r, dr, phi, pdtphi, pdrphi):
    Energy = 0
    for i in range(sz+1):
        Energy = Energy + (
                    0.5 * pdrphi[i] * pdrphi[i] + 0.5 * pdtphi[i] * pdtphi[i] + 0.5 * phi[i] * phi[i] - 0.5 * phi[i] *
                    phi[i] * phi[i] * phi[i] + 0.5 * g * phi[i] * phi[i] * phi[i] * phi[i] * phi[i] * phi[i]) * 2 * pi * \
                 r[i] * dr
    return Energy


def energycallim(r, dr, phi, pdtphi, pdrphi):
    Energy = 0
    for i in range(int(np.ceil(calR/dr) + 1)):
        Energy = Energy + (
                0.5 * pdrphi[i] * pdrphi[i] + 0.5 * pdtphi[i] * pdtphi[i] + 0.5 * phi[i] * phi[i] - 0.5 * phi[i] *
                phi[i] * phi[i] * phi[i] + 0.5 * g * phi[i] * phi[i] * phi[i] * phi[i] * phi[i] * phi[i]) * 2 * pi * \
                 r[i] * dr
    return Energy


def outputenergy(j, energy, energylim, peroid):
    if np.ceil(j / peroid) == j / peroid:
        f = open("energy.dat", mode='a', encoding="utf-8")
        f.write(str(j * dt) + ' ')
        f.write(str(energy) + ' ')
        f.write('\n')
        f.close()

        f = open("energylim.dat", mode='a', encoding="utf-8")
        f.write(str(j * dt) + ' ')
        f.write(str(energylim) + ' ')
        f.write('\n')
        f.close()


def initialize(phi, pdtphi, r):
    for i in range(sz + 1):
        phi[i]=A*np.exp(-pow((r[i])*(r[i])-a,2.0)/(sigma*sigma))
        pdtphi[i] = 0
    return phi,pdtphi


def peroidcal(phi, tempTphi, j, tempT1, tempT2, T):
    for i in range(numofrT + 1):
        if ((phi[int(i*(sz/numofrT))]<=0) and (tempTphi[int(i*(sz/numofrT))]>=0)):
            tempT2[i] = j * dt
            T[i] = tempT2[i] - tempT1[i]
            tempT1[i] = tempT2[i]


def outputperoid(j, T, peroid):
    if np.ceil(j / peroid) == (j / peroid):
        f = open("T.dat", mode='a', encoding="utf-8")
        f.write(str(j * dt) + ' ')
        for i in range(len(T)):
            f.write(str(T[i]) + ' ')
        f.write('\n')
        f.close()


phi = np.zeros(sz+1)
r = np.zeros(sz+1)
pdrphi = np.zeros(sz+1)
pdtphi = np.zeros(sz+1)
pd2tphi = np.zeros(sz+1)
pd2rphi = np.zeros(sz+1)
pdrtphi = np.zeros(sz+1)
temphi1 = np.zeros(sz+1)
tempdtphi = np.zeros(sz+1)
tempdrphi = np.zeros(sz+1)
tempd2rphi = np.zeros(sz+1)
tempdrtphi = np.zeros(sz+1)
temphi2 = np.zeros(sz+1)
k1 = np.zeros(sz+1)
k2 = np.zeros(sz+1)
k3 = np.zeros(sz+1)
k4 = np.zeros(sz+1)
k1t = np.zeros(sz+1)
k2t = np.zeros(sz+1)
k3t = np.zeros(sz+1)
k4t = np.zeros(sz+1)
y1 = np.zeros(sz+1)
y2 = np.zeros(sz+1)
y3 = np.zeros(sz+1)
y1t = np.zeros(sz+1)
y2t = np.zeros(sz+1)
y3t = np.zeros(sz+1)

rT = np.zeros(numofrT+1)
tempT1 = np.zeros(numofrT+1)
tempT2 = np.zeros(numofrT+1)
T = np.zeros(numofrT+1)

for i in range(sz + 1):
    r[i] = (i + 0.5) * dr

for i in range(numofrT + 1):
    rT[i] = r[int(i*np.ceil(sz/numofrT))]


outputr(r)
outputrT(rT)

initialize(phi, pdtphi, r)

for j in range(tnum):
    for i in range(sz + 1):
        pdrphi[i] = pdr(phi, i)
        pd2rphi[i] = pd2r(phi, i)
        pdrtphi[i] = pdr(pdtphi, i)
        pd2tphi[i] = formular(r, phi, pdtphi, pdrphi, pd2rphi, pdrtphi, i)
        temphi1[i] = phi[i]
        tempdtphi[i] = pdtphi[i]
    outputphi(j, phi, peroid)
    outputphi(j, phi, peroid)
    outputpdtphi(j, pdtphi, peroid)
    outputpdrphi(j, pdrphi, peroid)
    outputenergy(j, energycal(r, dr, phi, pdtphi, pdrphi), energycallim(r, dr, phi, pdtphi, pdrphi), peroid)
    outputperoid(j, T, peroid)
    for i in range(sz + 1):
        k1[i] = dt * pdtphi[i]
        k1t[i] = dt * formular(r, phi, pdtphi, pdrphi, pd2rphi, pdrtphi, i)
        y1[i] = phi[i] + 0.5 * k1[i]
        y1t[i] = pdtphi[i] + 0.5 * k1t[i]
    for i in range(sz + 1):
        tempdrphi[i] = pdr(y1, i)
        tempd2rphi[i] = pd2r(y1, i)
        tempdrtphi[i] = pdr(y1t, i)
        k2[i] = dt * y1t[i]
        k2t[i] = dt * formular(r, y1, y1t, tempdrphi, tempd2rphi, tempdrtphi, i)
        y2[i] = phi[i] + 0.5 * k2[i]
        y2t[i] = pdtphi[i] + 0.5 * k2t[i]
    for i in range(sz + 1):
        tempdrphi[i] = pdr(y2, i)
        tempd2rphi[i] = pd2r(y2, i)
        tempdrtphi[i] = pdr(y2t, i)
        k3[i] = dt * y2t[i]
        k3t[i] = dt * formular(r, y2, y2t, tempdrphi, tempd2rphi, tempdrtphi, i)
        y3[i] = phi[i] + k3[i]
        y3t[i] = pdtphi[i] + k3t[i]
    for i in range(sz + 1):
        tempdrphi[i] = pdr(y3, i)
        tempd2rphi[i] = pd2r(y3, i)
        tempdrtphi[i] = pdr(y3t, i)
        k4[i] = dt * y3t[i]
        k4t[i] = dt * formular(r, y3, y3t, tempdrphi, tempd2rphi, tempdrtphi, i)
        phi[i] = phi[i] + (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) / 6.0
        pdtphi[i] = pdtphi[i] + (k1t[i] + 2.0 * k2t[i] + 2.0 * k3t[i] + k4t[i]) / 6.0
    peroidcal(phi, temphi1, j, tempT1, tempT2, T)
    if j/peroid == np.ceil(j/peroid):
        print("Time =",j*dt,'Beacon =',j/tnum,'Energy = ',energycallim(r, dr, phi, pdtphi, pdrphi))
