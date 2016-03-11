from random import randint
import webbrowser

show = "the-simpsons"
seasonsdict = {1:14, 2:22, 3:24, 4:22, 5:22, 6:25, 7:25, 8:25, 9:25, 10:23, 11:22, 12:21, 13:22, 14:22, 15:22, 16:21, 17:22, 18:22, 19:20, 20:21, 21:23, 22:22, 23:22, 24:22, 25:22, 26:22, 27:7}
s = randint(1, len(seasonsdict)+1)
e = randint(1, seasonsdict[s]+1)

url = "http://watch8now.me/stream/"+show+"-s"+str(s)+"e"+str(e)
webbrowser.open(url)
