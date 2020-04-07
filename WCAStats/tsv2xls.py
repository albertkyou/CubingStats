import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats as stats 
import pandas as pd 

df = pd.read_csv('D:\GitHub\CubingStats\WCAStats\WCA_export_Results.tsv','\t')

threespeed = df.loc[df.eventId=='333']

threespeed.to_excel('threespeed_results.xlsx')