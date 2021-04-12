import numpy as np
import matplotlib.pyplot as plt

k = [17,25,4,1,3,2,9,11,101,10,7,6,12,5,19,20,14,24,13,23,8,16]
pk = [2,1,8,53,24,41,2,2,1,4,8,2,2,11,1,2,2,1,2,1,5,1]
weighted_k = [19,59,4,1,3,2,12,21,252,17,10,9,6,29,33,5,53,41,67,24,22,62,7,8,15,13,25,16,20,11,14]
weighted_pk = [1,1,11,53,19,37,3,1,1,3,6,3,4,1,1,11,1,1,1,1,2,1,3,2,1,1,1,1,1,1,2]

log_k = np.log(k)
log_pk = np.log(pk)
log_weighted_k = np.log(weighted_k)
log_weighted_pk = np.log(weighted_pk)

# Plot k vs pk
plt.plot(k, pk, 'ro')
plt.grid()
plt.xlabel("$k$")
plt.ylabel("$p(k)$")
plt.title("degree $k$ vs proportion $p(k)$,\nwith fitted curve $p(k)=43.5k^{-1.122}$")
x = np.linspace(0.75,120,1000)
y = 43.5*(x**-1.122)
plt.plot(x,y, 'b')
plt.savefig("degdist.pdf")
plt.clf()

# Plot weighted k vs weighted pk
plt.plot(weighted_k, weighted_pk, 'ro')
plt.grid()
plt.xlabel("$k_{weighted}$")
plt.ylabel("$p(k_{weighted})$")
plt.title("weighted degree $k_{weighted}$ vs proportion $p(k_{weighted})$,\nwith fitted curve $p(k_{weighted})=23.4k^{-0.861}$")
x = np.linspace(0.5,275,1000)
y = 23.4*(x**-0.861)
plt.plot(x,y, 'b')
plt.savefig("degdist_weighted.pdf")
plt.clf()

# Plot log(k) vs log(pk)
plt.plot(log_k, log_pk, 'ro')
plt.grid()
plt.xlabel("$log(k)$")
plt.ylabel("$log(p(k))$")
plt.title("log of degree $log(k)$ vs log of proportion $log(p(k))$,\nwith the fitted curve $log(p(k))=-1.122k+3.77$")
x = np.linspace(0,5,100)
y = (-1.122*x)+3.77
plt.plot(x,y, 'b')
plt.savefig("logdegdist.pdf")
plt.clf()

# Plot log(weighted k) vs log(weighted pk)
plt.plot(log_weighted_k, log_weighted_pk, 'ro')
plt.grid()
plt.xlabel("$log(k_{weighted})$")
plt.ylabel("$log(p(k_{weighted}))$")
plt.title("log of weighted degree $log(k_{weighted})$ vs log of proportion $log(p(k_{weighted}))$,\nwith the fitted curve $log(p(k_{weighted}))=-0.86k+3.15$")
x = np.linspace(0,6,100)
y = (-0.86*x)+3.15
plt.plot(x,y, 'b')
plt.savefig("logdegdist_weighted.pdf")
plt.clf()