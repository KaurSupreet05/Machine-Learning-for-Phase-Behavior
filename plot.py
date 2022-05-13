import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys


ndens = 51
nconfigs = 100

pca = np.loadtxt('2D_scatter_pca.dat')
tsne = np.loadtxt('tsne-scatter.dat')

# setting range of color bar for density data

scat_color = np.zeros(ndens*nconfigs)
sc_color = np.zeros(ndens)
for i in range(ndens):
    scat_color[i*nconfigs:(i+1)*nconfigs] = 0.50+0.01*i
    sc_color[i] = 0.50+0.01*i

plot_figsize = 22

cbar_border_width = 3.7
plot_border_width = 3.7

cbar_tick_width = 3.7
plot_tick_width = 3.7

cbar_tick_length = 10
plot_tick_length = 10

cbar_tick_label_size = 50
plot_tick_label_size = 50
cbar_label_size = 60
plot_label_size = 60


fig1 = plt.figure(figsize=(plot_figsize,plot_figsize))
ax1 = fig1.add_subplot(111)
pcm1 = plt.scatter(pca[:,0],pca[:,1],s=290,c=scat_color,cmap='rainbow')
cbar1 = fig1.colorbar(pcm1)
cbar1.set_label('Density',fontsize=cbar_label_size)
cbar1.outline.set_linewidth(cbar_border_width)
cbar1.ax.tick_params(labelsize=cbar_tick_label_size,length=cbar_tick_length,width=cbar_tick_width) 
plt.xlabel(r'$S_1$',fontsize=plot_label_size)
plt.ylabel(r'$S_2$',fontsize=plot_label_size)
plt.xticks(fontsize=plot_tick_label_size)
plt.yticks(fontsize=plot_tick_label_size)
for axis in ['top', 'bottom', 'left', 'right']:
    ax1.spines[axis].set_linewidth(plot_border_width)  # change width
ax1.tick_params(length=plot_tick_length,width=plot_tick_width)
fig1.savefig("pca-wr.png")

fig2 = plt.figure(figsize=(plot_figsize,plot_figsize))
ax2 = fig2.add_subplot(111)
pcm2 = plt.scatter(tsne[0,:],tsne[1,:],s=290,c=scat_color,cmap='rainbow')
cbar2 = fig2.colorbar(pcm2)
cbar2.set_label('Density',fontsize=cbar_label_size)
cbar2.outline.set_linewidth(cbar_border_width)
cbar2.ax.tick_params(labelsize=cbar_tick_label_size,length=cbar_tick_length,width=cbar_tick_width)
plt.xlabel(r'$S_1$',fontsize=plot_label_size)
plt.ylabel(r'$S_2$',fontsize=plot_label_size)
plt.xticks(fontsize=plot_tick_label_size)
plt.yticks(fontsize=plot_tick_label_size)
for axis in ['top', 'bottom', 'left', 'right']:
    ax2.spines[axis].set_linewidth(plot_border_width)  # change width
ax2.tick_params(length=plot_tick_length,width=plot_tick_width)
fig2.savefig("tsne-wr.png")

plt.show()
