# -*- coding: utf-8 -*-
"""
Generates random data to be used for demoing purposes.
Created on Tue May 14 13:53:18 2019

@author: ecramer 
"""

import numpy as np
import pandas as pd

def genClusterData(n_obs, n_clusters):
    # calculate the probability of belonging to each cluster
    cluster_probs= [np.random.randint(1, 100, 1)[0] for i in range(n_clusters)]
    cluster_probs = [i/sum(cluster_probs) for i in cluster_probs]
    # generate the clusters given their probabilities
    clusters = np.random.choice(n_clusters, size=n_obs, replace=True, p=cluster_probs)
    return clusters, cluster_probs

def genStageData(n_obs, n_stages, cluster_data):
    # for each observation
    n_clusters = max(cluster_data)
    for obs in range(n_obs):
        # if the observation is 
    pass

def generateData(n_obs = 1000, n_stages = 5, n_clusters = 12):
    """
    Generates random data for demoing.
    
    Input:
        n_obs (int): the number of observations
        n_stages (int): the number of stages
        n_clusters (int): thenumber of clusters
    
    Output:
        a list with the clusters and stages randomly generated
    """
    # generate the stage and cluster data
    cluster_data, _ = genClusterData()
    stage_data = genStageData(n_obs, n_stages, cluster_data)
    stage_data = np.random.randint(0, high = n_stages, size = n_obs)
    cluster_data = np.random.randint(0, high = n_clusters, size = n_obs)
    # put the stage and cluster data into a dataframe, then pivot and set the sum of all rows=1
    data = pd.DataFrame({'cluster':cluster_data, 'stage':stage_data})
    pivoted = data.pivot_table(columns='stage', index=['cluster'], aggfunc={'stage':'count'})
    pivoted.reset_index(inplace=True)
    pivoted['sum'] = pivoted.drop('cluster', axis=1).sum(axis=1)
    pivoted2 = pivoted.loc[:, 'stage'].div(pivoted['sum'], axis=0)
    return pivoted2