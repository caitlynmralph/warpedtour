# figure out the top genres

import os
import numpy as np

os.chdir('/Applications/MAMP/htdocs/project_1/WarpedTour_spreadsheets')

csv = np.genfromtxt('WarpedTour_yearsgenres_totals.csv', delimiter=",", dtype=object, skiprows=0)
years_genres_totals = csv[:]

genres = years_genres_totals[0:1,1:]
totals = years_genres_totals[24:25,1:]

genres_totals = np.concatenate([genres,totals],axis=0)

# np.savetxt("WarpedTour_genres_totals.csv", genres_totals, delimiter=",", fmt="%s")

genres = genres_totals[0:1,:][0]
totals = genres_totals[1:2,:][0]

totals_list = []

for i in range(0,408):
    totals_list = np.append(totals_list,float(totals[i]))

print np.median(np.array(totals_list))

new_totals = np.empty([1,1])

# adjust threshold to change number of genres

for i in range(0,408):
    if int(totals[i]) > 105 and genres[i:i+1] != "no data" and genres[i:i+1] != "punk christmas":
        print genres[i:i+1], totals[i]
        new_totals = np.append(new_totals, np.reshape(genres[i:i+1],[1,1]), axis = 0)

new_totals = np.delete(new_totals, 0, axis=0)

print np.shape(new_totals)

for i in range(0,len(new_totals)):
    print new_totals[i:i+1,:]

# change file name to reflect number of genres

np.savetxt("WarpedTour_top20genres.csv", new_totals, delimiter=",", fmt="%s")