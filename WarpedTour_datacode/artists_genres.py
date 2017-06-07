# use spotify api to get genre for each warped tour artist
# create spreadsheet with artist and accompanying genres

import spotipy
import numpy as np
import os

os.chdir('/Applications/MAMP/htdocs/project_1/WarpedTour_spreadsheets')

csv = np.genfromtxt('WarpedTour_artists.csv', delimiter="\n", dtype=object)
artists = csv[:]
zeros = np.zeros([1014,1])
artists = np.reshape(artists, [1014,1])
artists = np.append(artists, zeros,  axis=1)

token = 'BQBf6lPb5GuP_JHtNOcUiA9MzHLETefFVVOBF2AEUiLp-DsQpxsV0VhBIpjJ0ql_x_HKYIHc6aw-3-zqEJrKpGRHnycp-xFkpQvFsHjhRzA8LKA4qGxQ0hdrYhy7komcX9F2yF4U5vBTsGjixj77nO7n82oj973gxofd6ULAjMqgO4vcdDolu2e7Wd7krz2kkO_K9SQ5A4KYGDi2JH8gCCngfgk9hpQmDnG1cncgx86zQSwGwb_Q06_jyYOn9PyfcdEE0lrnXiv7bpWXa2SyWgTwkVjbOjzYgTQy9HJipFulKOd9Z6gV8WLRTrbtApH15XoGpIIVwYo_'

spotify = spotipy.Spotify(auth=token)

for i in range(0, 1014):
    print artists[i:i+1,0:1][0][0]
    results = spotify.search(q='artist:' + artists[i:i+1,0:1][0][0], type='artist')
    artistinfo = results.values()[0].values()[0]
    if artistinfo == []:
        artists[i:i + 1, 1:2] = "No artist data"
        continue
    genres = artistinfo[0].values()[0]
    if np.shape(genres) == (0,):
        artists[i:i + 1, 1:2] = "No genre data"
    else:
        genres = str(genres)
        genres = genres.replace("u'", '')
        genres = genres.replace("'", '')
        genres = genres.replace("[", '')
        genres = genres.replace("]", '')
        genres = genres.replace('"', '')
        artists[i:i+1, 1:2] = genres

nogenredata = np.empty([1, 1])

for i in range(0, len(artists)):
    if artists[i:i + 1, 1:2] == "No genre data" or artists[i:i + 1, 1:2] == "No artist data":
        nogenredata = np.append(nogenredata, artists[i:i + 1, 0:1], axis=0)

nogenredata = np.delete(nogenredata, 0, 0)

print nogenredata

np.savetxt("WarpedTour_nogenredata.csv", nogenredata, delimiter="#", fmt="%s")

np.savetxt("WarpedTour_artistsgenres.csv", artists, delimiter="#", fmt="%s")