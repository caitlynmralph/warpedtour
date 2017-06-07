# create spreadsheet for each year based on top 19 genres

import os
import numpy as np

os.chdir('/Applications/MAMP/htdocs/project_1/WarpedTour_spreadsheets')

csv = np.genfromtxt('WarpedTour_top19genres.csv', delimiter=",", dtype=object, skiprows=0)
topgenres = csv[:]

csv = np.genfromtxt('WarpedTour_yearsgenres_totals.csv', delimiter=",", dtype=object, skiprows=0)
yearsgenres = csv[:]

csv = np.genfromtxt('WarpedTour_genretotalsperyear.csv', delimiter=",", dtype=object, skiprows=1)
totals = csv[:]

year_labels = ["1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

for i in range(1,24):
    year_topgenres = np.zeros([1, 2])
    for j in range(1,409):
        if yearsgenres[0:1,j:j+1] in topgenres:
            year_topgenres = np.append(year_topgenres, [yearsgenres[0:1,j:j+1][0][0], (float(yearsgenres[i:i+1,j:j+1][0][0])/float(totals[i-1:i,1:2][0][0]))])
    year_topgenres = np.reshape(year_topgenres, [20,2])
    year_topgenres[0:1,0:1] = ["genre"]
    year_topgenres[0:1, 1:2] = ["count"]
    print year_topgenres
    np.savetxt("%s.csv" % (year_labels[i-1]), year_topgenres, delimiter=",", fmt="%s")