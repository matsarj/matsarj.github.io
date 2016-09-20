
#  NFL Fourth Down Statistics
# 
#In this code, we will examine the play-by-play data from the 2015 NFL season,   
#focusing on the fourth down statistics.


import numpy as np # library for handling arrays
import pandas as pd #library for handling dataframes
import matplotlib.pyplot as plt #library for viewing graphs
from matplotlib.widgets import Slider #this method will allow us to add a slider to our graphs

#We first read in the 2015 NFL play-by-play data and grab: all fourth down plays,
#fourth down plays where the team went for it, and fourth down plays where the team
#converted.

data = pd.read_csv('/home/matt/Downloads/nfl.csv')
fourth = data[data['down'] == 4]
go_for_it = fourth[(fourth['PlayType'] == 'Run') | (fourth['PlayType'] == 'Pass')]
made_it = go_for_it[go_for_it['Yards.Gained'] > go_for_it['ydstogo']]
yds = 1

#Next we count the number of total/successful runs/passes

num_runs = go_for_it[go_for_it['PlayType'] == "Run"]['PlayType'].count()
num_passes = go_for_it[go_for_it['PlayType'] == "Pass"]['PlayType'].count()

num_succ_runs = made_it[made_it['PlayType'] == "Run"]['PlayType'].count()
num_succ_passes = made_it[made_it['PlayType'] == "Passes"]['PlayType'].count()

#Initialize the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom = .3)
index = np.arange(2)
ax.bar(index, np.array([num_runs, num_passes]), align = 'center', color = 'blue', label = "All Attempts")
ax.bar(index,np.array([num_succ_runs, num_succ_passes]), align = 'center', color = '#6666ff', width = .75, label = "Successful Attempts")
plt.legend(loc = 'best')
plt.title("Fourth Down Attempts")
plt.xticks(index, ['Run', 'Pass'])

#Draw the slider
axYTG = plt.axes([.2,.08, .65, .08], axisbg = 'white')
sYTG = Slider(axYTG, 'Yards To Go', 1, 32, valinit = 0, valfmt = '%0.0f', color = 'green')

#This is the function that refreshes the plot with the new slider values
def update(val):
	yds = int(round(val))
	ax.clear()

	num_run_yds = go_for_it[(go_for_it['PlayType'] == "Run") & (go_for_it['ydstogo'] == yds)]['PlayType'].count()	
	num_pass_yds = go_for_it[(go_for_it['PlayType'] == "Pass") & (go_for_it['ydstogo'] == yds)]['PlayType'].count()		

	ax.bar(index,np.array([num_run_yds, num_pass_yds]), align = 'center', color = 'blue', label = "All Attempts")
	
	num_succ_run_yds = made_it[(made_it['PlayType'] == "Run") & (made_it['ydstogo'] == yds)]['PlayType'].count()	
	num_succ_pass_yds = made_it[(made_it['PlayType'] == "Pass") & (made_it['ydstogo'] == yds)]['PlayType'].count()		
		
	ax.bar(index,np.array([num_succ_run_yds, num_succ_pass_yds]), align = 'center', color = '#6666ff', width = .75, label = "Successful Attempts")

	ax.legend(loc = 'best')
	ax.set_title("Fourth Down Attempts")
	labels = [item.get_text() for item in ax.get_xticklabels()]
	labels[2] = 'Run'
	labels[7] = 'Pass'
	ax.set_xticklabels(labels)	
	fig.canvas.draw()

sYTG.on_changed(update)
plt.show()
	



