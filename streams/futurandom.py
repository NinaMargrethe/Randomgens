from random import randint
import webbrowser

show = "futurama"
seasonsdict = {1:9, 2:20, 3:15, 4:12, 5:16, 6:26, 7:26}
s = randint(1, len(seasonsdict)+1)
e = randint(1, seasonsdict[s]+1)

url = "http://watchonlinefree.tv/tv/"+show+"/season"+str(s)+"/episode"+str(e)
webbrowser.open(url)
