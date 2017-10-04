"""
main driver file

"""

"""
Usage: conference.py <<filename>>
       python conference.py "input.txt"

"""

from tracks import *


try:
    fname = sys.argv[1]
except (ValueError,IndexError) as e:
    check_input_argument()


talks=[]
tracks = []

talks = get_talk_list(fname)
tracks = fill_talk_tracks(talks,tracks)
printTracks(tracks)
