from random import randint
import webbrowser

show = "adventure-time"
seasonsdict = {1:26, 2:26, 3:26, 4:26, 5:52, 6:21}
s = randint(1,len(seasonsdict))
e = randint(1, seasonsdict[s])
                              
url = "http://watchonlinefree.tv/tv/"+show+"/season"+str(s)+"/episode"+str(e)
webbrowser.open(url)
