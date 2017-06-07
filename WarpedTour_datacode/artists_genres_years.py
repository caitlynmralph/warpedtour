# make a spreadsheet of artists, their genres, and the year(s) they were on Warped

import numpy as np
import os

os.chdir('/Applications/MAMP/htdocs/project_1/WarpedTour_spreadsheets')

csv = np.loadtxt('WarpedTour_artistsgenres_updated.tsv', delimiter="\t", dtype=object, skiprows=1)
artists_genres = csv[:]

years = np.empty([1000,1])

artists_genres = np.reshape(artists_genres, [1000,2])
artisst_genres = np.concatenate([artists_genres, years], axis = 1)

csv = np.genfromtxt('WarpedTour_lineupsbyyear.tsv', delimiter="\t", dtype=object)
lineupsbyyear = csv[:]

for i in range(1,1000):
    year = []
    for j in range(1,24):
        if lineupsbyyear[i:i+1,j:j+1][0][0] == '1':
            year = np.append(year, lineupsbyyear[0:1,j:j+1][0][0])
    print lineupsbyyear[i:i + 1, 0:1][0][0]
    print year
    artists_genres[i-1:i,2:3] = str(year)

np.savetxt("WarpedTour_artistsgenresyears.csv", artists_genres, delimiter="#", fmt="%s")
