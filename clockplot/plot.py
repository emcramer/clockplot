# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:52:16 2019

@author: ecramer <eric.cramer@curie.fr>
"""
# imports
from matplotlib import pyplot
import collections, tqdm
from utils import calcCentroid, cartToPolar, adjustColor

## Plotting the center of mass on a polar graph
# treat each row of the pop_counts_p as radii, and each timepoint equally spaced as an angle measure
centroids = []
for i in tqdm.tqdm(range(pop_counts_p.shape[0])):
    # get the radii in ctl, ets, lts order
    radii = [pop_counts_p['Control'].values[i],
             pop_counts_p['10day'].values[i],
             pop_counts_p['20day'].values[i]]
    angles = np.deg2rad(np.asarray([0, 120, 240]))
    centroids.append(calcCentroid(radii, angles))

# create a list with the centroids as polar coordinates
centroids_polar = np.asarray([cartToPolar(a[0], a[1]) for a in centroids])

# set up the plot aesthetics
# point positions
theta = [a[1] for a in centroids_polar]
r = [a[0] for a in centroids_polar]

# point sizes
pop_freqs = collections.Counter(pooled_data['Population'])
pop_sizes = sorted([(key, pop_freqs[key]) for key in pop_freqs.keys()], key=lambda x: x[0])
pop_sizes = np.asarray([a[1] for a in pop_sizes])
pop_sizes = 2**abs(np.log(10000*pop_sizes/pop_sizes.max()))

# point colors
cmap = plt.get_cmap('brg')
colors = cmap(range(64))
colors = [adjust_color(c[:-1], 2) for c in colors]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
sc = [None]*len(theta)
# iteratively plot each of the points
for i in tqdm.tqdm(range(len(theta))):
    sc[i] = ax.scatter(theta[i], 3*r[i], cmap=colors[i], label=i+1, alpha=(100-i)/100, s=pop_sizes[i], edgecolor='black')

#sc.append(ax.scatter(theta[48], r[48], color='red', label='40r', s=pop_sizes[48])) #to show specific pops

#ax.set_rgrids(radii= np.round(np.linspace(0, 1, 11), 1), angle=90)
ax.set_xticklabels(['Control', 'ETS', 'LTS'], fontweight='bold')
ax.set_xticks(np.deg2rad(np.asarray([0, 120, 240])))
# ax.set_thetamin(0)
# ax.set_thetamax(180)
plt.title('Population Center of Mass')    
plt.legend(sc, np.arange(1, 65), title='Population', ncol=8, loc='center', bbox_to_anchor=(0.5, -0.2))

# Show polar plot
plt.show()