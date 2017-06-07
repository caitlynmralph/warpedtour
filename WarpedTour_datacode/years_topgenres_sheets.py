# create spreadsheet for five top genres based on each year

import os
import numpy as np

os.chdir('/Applications/MAMP/htdocs/project_1/WarpedTour_spreadsheets')

csv = np.genfromtxt('WarpedTour_top6genres.csv', delimiter=",", dtype=object, skiprows=0)
topgenres = csv[:]

csv = np.genfromtxt('WarpedTour_yearsgenres_totals.csv', delimiter=",", dtype=object, skiprows=0)
yearsgenres = csv[:]

csv = np.genfromtxt('WarpedTour_genretotalsperyear.csv', delimiter=",", dtype=object, skiprows=1)
totals = csv[:]

years_genres_top = np.zeros([1,1])

for i in range(0,len(topgenres)):
     years_genres_top = np.append(years_genres_top, np.reshape([topgenres[i]],[1,1]), axis = 1)

years_genres_top = np.delete(years_genres_top,0)
years_genres_top = np.reshape(years_genres_top,[6,1])

for i in range(1,24):
    year_topgenres = np.zeros([1, 1])
    for j in range(1,407):
        if yearsgenres[0:1,j:j+1] in topgenres:
            a = yearsgenres[i:i + 1, j:j + 1][0][0]
            b = totals[i-1:i, 1:2][0][0]
            n = float(a)/float(b)
            year_topgenres = np.append(year_topgenres, n)
    year_topgenres = np.delete(year_topgenres,0)
    year_topgenres = np.reshape(year_topgenres, [6,1])
    years_genres_top = np.append(years_genres_top,year_topgenres, axis=1)

years = np.empty([1,1])

year_labels = ["year", "1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

for i in range(0, len(year_labels)):
    years = np.append(years, year_labels[i:i+1])

years = np.delete(years, 0)
years = np.reshape(years, [1,24])

years_genres_top = np.append(years, years_genres_top,axis=0)

print years_genres_top

np.savetxt("WarpedTour_yearstop6genres.csv", years_genres_top, delimiter=",", fmt="%s")