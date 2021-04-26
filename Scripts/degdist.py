import numpy as np
import matplotlib.pyplot as plt

k = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,19,20,23,24,25,101]
pk = [53,41,24,8,11,2,8,5,2,4,2,2,2,2,1,2,1,2,1,1,1,1]
noShaka_k =  k[:-1]
noShaka_pk = pk[:-1]
cumulative_k = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,19,20,23,24,25,101]
cumulative_pk = [176,123,82,58,50,39,37,29,24,22,18,16,14,12,10,9,7,6,4,3,2,1]
noShaka_cumulative_k = cumulative_k[:-1]
noShaka_cumulative_pk = [175,122,81,57,49,38,36,28,23,21,17,15,13,11,9,8,6,5,3,2,1]

log_k = np.log(k)
log_pk = np.log(pk)
log_noShaka_k = np.log(noShaka_k)
log_noShaka_pk = np.log(noShaka_pk)
log_cumulative_k = np.log(cumulative_k)
log_cumulative_pk = np.log(cumulative_pk)
log_noShaka_cumulative_k = np.log(noShaka_cumulative_k)
log_noShaka_cumulative_pk = np.log(noShaka_cumulative_pk)


def k_fitted(x):
    return(43.5*(x**-1.122))

def noShaka_fitted(x):
    return(67.4*(x**-1.35))

def cumulative_fitted(x):
    return(330*(x**-1.299))

def cumulative_noShaka_fitted(x):
    return(405.85*(x**-1.451))

def log_fitted(x):
    return((-1.122*x)+3.77)

def log_noShaka_fitted(x):
    return((-1.35*x)+4.21)

def log_cumulative_fitted(x):
    return((-1.299*x)+5.799)

def log_cumulative_noShaka_fitted(x):
    return((-1.451*x)+6.006)

xData = [k, noShaka_k, log_k, log_noShaka_k, cumulative_k, log_cumulative_k, noShaka_cumulative_k, log_noShaka_cumulative_k]
yData = [pk, noShaka_pk, log_pk, log_noShaka_pk, cumulative_pk, log_cumulative_pk, noShaka_cumulative_pk, log_noShaka_cumulative_pk]
xLabels = ["$k$", "$k_{noShaka}$", "$log(k)$", "$log(k_{noShaka})$", "Cumulative $k$", "$log($cumulative $k)$", "Cumulative $k$ without Shaka", "$log($cumulative $k)$ without Shaka"]
yLabels = ["$p(k)$", "$p(k_{noShaka})$", "$log(p(k))$", "$log(p(k_{noShaka}))$", "$p($cumulative $k)$", "$log(p($cumulative $k))$", "$p($cumulative $k)$ without Shaka", "$log(p($cumulative $k))$ without Shaka"]
graphTitles = [
    "degree $k$ vs proportion $p(k)$,\nwith fitted curve $p(k)=43.5k^{-1.122}$",
    "degree $k_{noShaka}$ vs proportion $p(k_{noShaka})$,\nwith fitted curve $p(k_{noShaka})=67.4k^{-1.35}$",
    "log of degree $log(k)$ vs log of proportion $log(p(k))$,\nwith the fitted curve $log(p(k))=-1.122k+3.77$",
    "log of degree $log(k_{noShaka})$ vs log of proportion $log(p(k_{noShaka}))$,\nwith the fitted curve $log(p(k_{noShaka}))=-1.35k+4.21$",
    "cumulative degree $k$ vs proportion $p(k)$,\nwith the fitted curve $p(k)=330x^{-1.451}$",
    "log of degree $log(k)$ vs log of proportion $log(p(k))$,\nwith the fitted curve $log(p(k))=-1.299k+5.799$",
    "cumulative degree $k$ vs proportion $p(k)$ without Shaka,\nwith the fitted curve $p(k)=405.85x^{-1.299}$",
    "log of degree $log(k)$ vs log of proportion $log(p(k))$ without Shaka,\nwith the fitted curve $log(p(k))=-1.451k+6$"
]
xLowerLims = [0.8,0.8,0,0,1.25,0,1.25,0]
xUpperLims = [120,30,5,3.5,100,5,26,3.5]
fittedCurves = [k_fitted, noShaka_fitted, log_fitted, log_noShaka_fitted, cumulative_fitted, log_cumulative_fitted, cumulative_noShaka_fitted, log_cumulative_noShaka_fitted]
plotTitles = ["degdist.pdf", "degdist_noShaka.pdf", "logdegdist.pdf", "logdegdist_noShaka.pdf", "degdist_cumulative.pdf", "logdegdist_cumulative.pdf", "degdist_cumulative_noShaka.pdf", "logdegdist_cumulative_noShaka.pdf"]


def plot(xData, yData, xLabel, yLabel, title, xLowerLims, xUpperLims, fittedCurve, figTitle):
    plt.plot(xData, yData, 'ro')
    plt.grid()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    x = np.linspace(xLowerLims,xUpperLims,100)
    y = fittedCurve(x)
    plt.plot(x,y, 'b')
    plt.savefig(figTitle)
    plt.clf()

for i in range(len(xData)):
    plot(xData[i], yData[i], xLabels[i], yLabels[i], graphTitles[i], xLowerLims[i], xUpperLims[i], fittedCurves[i], plotTitles[i])