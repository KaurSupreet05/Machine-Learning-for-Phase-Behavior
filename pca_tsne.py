import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
#from itertools import combinations
#from itertools import permutations

ndens = 51 # number of density points chosen within the range of 0.5 to 1.0
nconfigs = 100 #number of snapshots for each density point
natom = 8192 # total number of particles (A+B)


 # Importing feature vector data calculated for all the density points
data = np.zeros((ndens*nconfigs,natom))

for i in range(ndens):
    data[nconfigs*i:nconfigs*(i+1)] = np.loadtxt('spin-total_'+str(i+1)+'.out').reshape(nconfigs,natom)


np.savetxt('data_total4',data,delimiter=',') #saving the importing data is not necessary if calculation is done on the fly


# PCA and t-SNE CALCULATION
n20 = PCA(n_components=20) # providing the number of principal components

pca = n20.fit_transform(data) # this transformatio function is a part of sklearn.decomposition package

tsne = np.transpose(TSNE(n_components = 2, perplexity=30).fit_transform(pca)) #here t-sne is performed on pca transformed data

 # calculating relative explained variance for knowing the dominant components  
eigenvalues = n20.explained_variance_ratio_
print(eigenvalues)

# ORDER PARAMETER CALCULATION (mean and standard deviation)

mean = np.zeros((ndens,2))
std = np.zeros((ndens,2))

for i in range(ndens):
    mean[i,0] = 0.5+0.01*i
    mean[i,1] = np.mean(pca[i*nconfigs:(i+1)*nconfigs,0])
    std[i,0] = 0.5+0.01*i
    std[i,1]  = np.sqrt(np.var(pca[i*nconfigs:(i+1)*nconfigs,0])+np.var(pca[i*nconfigs:(i+1)*nconfigs,1]))


np.savetxt('mean-pca.out',mean,delimiter=' ')
np.savetxt('std-dev-pca.out',std,delimiter=' ')


# PLOTTING THE SCATTER PLOTS AND ORDER PARAMETER
 # setting the range of color bar data 
scat_color = np.zeros(ndens*nconfigs)
sc_color = np.zeros(ndens)
for i in range(ndens):
    scat_color[i*nconfigs:(i+1)*nconfigs] = 0.5+0.01*i
    sc_color[i] = 0.5+0.01*i
 # plotting
fig,axs = plt.subplots(1,2,figsize=(30,15))
pcm1 = axs[0].scatter(pca[:,0],pca[:,1],c=scat_color,cmap='rainbow')
pcm2 = axs[1].scatter(tsne[0,:],tsne[1,:],c=scat_color,cmap='rainbow')
cbar1 = fig.colorbar(pcm1,ax=axs)
cbar1.set_label('Density',fontsize=30)

fig,axs = plt.subplots(1,2,figsize=(30,15))
pcm3 = axs[0].scatter(mean[:,0],mean[:,1],c=sc_color,cmap='rainbow')
pcm4 = axs[1].scatter(std[:,0],std[:,1],c=sc_color,cmap='rainbow')
cbar2 = fig.colorbar(pcm4,ax=axs)
cbar2.set_label('Density')
plt.show()
