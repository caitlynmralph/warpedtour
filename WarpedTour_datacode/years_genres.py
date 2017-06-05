# make a spreadsheet of years and genre counts

import numpy as np
import os

os.chdir('/Users/caitlynralph/Downloads/project_1/WarpedTour_spreadsheets')

csv = np.genfromtxt('WarpedTour_artistsgenresyears.tsv', delimiter="\t", dtype=object, skiprows=0)
artists_genres_years = csv[:]

years = ["1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

genres = artists_genres_years[:, 1:2]

genres_norepeats = np.empty([1,1])

for i in range(1,len(genres)):
    for x in genres[i][0].split(','):
        x = x.strip()
        x = str(x)
        x = x.replace('"','')
        x = x.lower()
        if x not in genres_norepeats:
            genres_norepeats = np.append(genres_norepeats, x)

genres_norepeats = np.delete(genres_norepeats, 0, 0)

for i in range(0,len(genres_norepeats)):
    genres_norepeats[i] = genres_norepeats[i].replace('"','')
    print genres_norepeats[i]

# np.savetxt("WarpedTour_genres.csv", genres_norepeats, delimiter="#", fmt="%s")

years_genres = np.zeros([23,408])

for i in range(1, len(artists_genres_years)):
    y = artists_genres_years[i:i+1,2:3]
    g = artists_genres_years[i:i+1,1:2]
    for x in g[0][0].split(','):
        for j in range(0, len(genres_norepeats)):
            if x.strip().lower().replace('"','') == genres_norepeats[j].lower():
                for k in y[0][0].replace('"','').replace("[","").replace("]","").replace("'","").split(" "):
                    if k.strip() == "1995":
                        years_genres[0:1,j:j+1] += 1
                    elif k.strip() == "1996":
                        years_genres[1:2, j:j + 1] += 1
                    elif k.strip() == "1997":
                        years_genres[2:3, j:j + 1] += 1
                    elif k.strip() == "1998":
                        years_genres[3:4, j:j + 1] += 1
                    elif k.strip() == "1999":
                        years_genres[4:5, j:j + 1] += 1
                    elif k.strip() == "2000":
                        years_genres[5:6, j:j + 1] += 1
                    elif k.strip() == "2001":
                        years_genres[6:7, j:j + 1] += 1
                    elif k.strip() == "2002":
                        years_genres[7:8, j:j + 1] += 1
                    elif k.strip() == "2003":
                        years_genres[8:9, j:j + 1] += 1
                    elif k.strip() == "2004":
                        years_genres[9:10, j:j + 1] += 1
                    elif k.strip() == "2005":
                        years_genres[10:11, j:j + 1] += 1
                    elif k.strip() == "2006":
                        years_genres[11:12, j:j + 1] += 1
                    elif k.strip() == "2007":
                        years_genres[12:13, j:j + 1] += 1
                    elif k.strip() == "2008":
                        years_genres[13:14, j:j + 1] += 1
                    elif k.strip() == "2009":
                        years_genres[14:15, j:j + 1] += 1
                    elif k.strip() == "2010":
                        years_genres[15:16, j:j + 1] += 1
                    elif k.strip() == "2011":
                        years_genres[16:17, j:j + 1] += 1
                    elif k.strip() == "2012":
                        years_genres[17:18, j:j + 1] += 1
                    elif k.strip() == "2013":
                        years_genres[18:19, j:j + 1] += 1
                    elif k.strip() == "2014":
                        years_genres[19:20, j:j + 1] += 1
                    elif k.strip() == "2015":
                        years_genres[20:21, j:j + 1] += 1
                    elif k.strip() == "2016":
                        years_genres[21:22, j:j + 1] += 1
                    else:
                        years_genres[22:23, j:j + 1] += 1

genres_norepeats = np.reshape(genres_norepeats, [1,len(genres_norepeats)])

years_genres = np.concatenate([genres_norepeats, years_genres], axis=0)

print years_genres

np.savetxt("WarpedTour_yearsgenres.csv", years_genres, delimiter=",", fmt="%s")