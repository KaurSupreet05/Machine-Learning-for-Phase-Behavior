# Machine-Learning-for-Phase-Behavior
Principal component analysis and t-stochastic neighbor embedding methods implemented on three dimensional off lattice systems to predict critical behavior
# Required packages 
* Numpy
* Matplotlib
* Scikit-learn (this requires:Python (>= 2.6 or >= 3.3),NumPy (>= 1.6.1) and SciPy (>= 0.9))

# Protocol ( Here Widom-Rowlinson Mixture is taken as an example model system)
* After obtaining MD/MS simulation trajectory, calculate the feature vector using run.sh
* .dat files obtained for each density point are fed to the pca_tsne.py to obtain transformed data
* plotting the principal components in 2D plot using plot.py
