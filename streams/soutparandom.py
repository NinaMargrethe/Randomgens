from random import randint
import webbrowser

show = "south-park"
seasonsdict = {1:13, 2:18, 3:17, 4:17, 5:14, 6:17, 7:15, 8:14, 9:14, 10:14, 11:14, 12:14, 13:14, 14:14, 15:14, 16:14, 17:10, 18:9}
s = randint(1, len(seasonsdict)+1)
e = randint(1, seasonsdict[s]+1)

url = "http://watchonlinefree.tv/tv/"+show+"/season"+str(s)+"/episode"+str(e)
webbrowser.open(url)
