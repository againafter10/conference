#######################
# core methods
#######################

import sys


from constants import *
from checks import *



##################################
##################################

def get_talk_list(fname):
    """

    :param fname: filename which lists all the talk topics and their duration
    :return: list of talk topics and their respective talk duration

    create a list of talk topis and their corresponding talk time
    """

    assert (check_input_file(fname)), sys.exit()

    f=open(fname,'r')
    talks=[]
    duplicates=[]
    flag=False

    for i in f.read().split("\n"):
        time = i[-5:-3]
        title = i[:-5]

        if check_title_alphnumeric_null(title):
            continue

        if i[-3:] == min:
            try:
                assert (check_talk_time(int(time)))
            except AssertionError:
                continue


            if int(time) > min_talk_time and int(time) > max_talk_time:
                pass
            else:
                talks.append([title,int(time)])


        else:
            #lightning talk or duration not given so assume to be a 5 min talk
            # insert such to the beginning
            talks.insert(0,[i,5])


    return talks

#################################
#################################

def findStartTime(duration, last_end_time, afternoon=False):
    """
    :param duration: numeric
    :param last_end_time: string
    :param afternoon: True or False
    :return: string

    return the start time of the talk

    """
    if last_end_time == '' and afternoon == True:
        last_end_time=lunch[2]

    if last_end_time == '':
        last_end_time = start_time_morning

    s_time= last_end_time[-2:]
    last_end_time= last_end_time[:-2]
    time=last_end_time.split(delimiter)
    hours= int(time[0])
    mins=int(time[1])

    if (mins + duration) < 60:
        mins = mins + duration
    else:
        hours = hours + 1
        mins = (mins + duration) - 60


    if hours > 12:
        hours = hours - 12

    mins = str(mins)
    hours = str(hours)

    if len(mins) == 1:
        mins = lpad_zero + mins

    if len(hours) == 1:
        hours = lpad_zero + hours

        
    s_time = str(hours) + delimiter + str(mins) + s_time
    return s_time


#################################
#################################


def new_track(talk,tracks):
    """
    :param talk: talk topic
    :param tracks: list of tracks for talk topics
    :return: list of tracks for talk topics
    create a new track topic with topic passed as the starting talk for the track
    """
    new_track_one = []
    last_end_time = findStartTime(talk[1], start_time_morning)
    talk.append(start_time_morning)
    tracks.append(
        [[talk],
         talk[1],
         0,
         last_end_time
         ]

    )

    return tracks


#################################
#################################


def track_topics(topic,track,time_limit):
    """

    :param topic: talk topic
    :param track: current track to be filled
    :param time_limit: duration of talk topic
    :return: True or False

    check if the talk topic can fit into the current track,if yes return True
    """

    if topic[1] + track > time_limit:
        return False
    else:
        return True


#################################
#################################


def fill_talk_tracks(talks,tracks):
    """

    :param talks: list of talk topics and their duration
    :param tracks: list of tracks into which the talk topics have to be ditributed
    :return: list of tracks containing corresponding talk topics

    create tracks with first fit is best fit strategy

    """
    total = len(talks)
    flag = False
    n_track=False
    m_track=True
    track_num = 0
    session_length=session_time[0]

    while len(talks) > 0:
        for i in talks:

            if len(tracks) == 0:
                tracks = new_track(i,tracks)
                talks.remove(i)
                continue

            if m_track:
                # determine  morning/afternoon session
                if tracks[track_num][1] + i[1] > session_length:

                    m_track = False
                    tracks[track_num][0].append([known_events[0], lunch_duration, lunch[2]])
                    session_length=session_time[1]
                    s_time = findStartTime(i[1], start_time_afternoon, True)
                    i.append(start_time_afternoon)
                    tracks[track_num][0].append(i)
                    tracks[track_num][2] = tracks[track_num][2] + i[1]
                    tracks[track_num][3] = s_time
                    talks.remove(i)
                    continue


            else:
                # fill new session
                if tracks[track_num][2] + i[1] > session_length:
                    tracks[track_num][0].append([known_events[1], time, tracks[track_num][3]])
                    n_track = True
                    tracks = new_track(i, tracks)
                    talks.remove(i)
                    track_num += 1
                    total = len(talks)
                    m_track=True
                    session_length = session_time[0]
                    continue

            flag = track_topics(i, tracks[track_num], session_length)

            if flag:

                s_time = findStartTime(i[1], tracks[track_num][3], True)
                i.append(tracks[track_num][3])
                tracks[track_num][0].append(i)
                if m_track:
                    tracks[track_num][1] = tracks[track_num][1] + i[1]
                else:
                    tracks[track_num][2] = tracks[track_num][2] + i[1]
                tracks[track_num][3] = s_time
                talks.remove(i)
                flag = False
                continue
            else:
                continue

    s_time = findStartTime(i[1], tracks[track_num][3], True)
    if s_time[-2:] == 'AM':
        tracks[track_num][0].append([known_events[0], '', lunch[2]])
        tracks[track_num][0].append([known_events[1], '', afternoon[2]])
    else:
        tracks[track_num][0].append([known_events[1], '', s_time])

    return tracks



##################################
##################################

def printTracks(tracks):
    """

    :param tracks: list of tracks containing talk topics
    :return: None
    print all the list of tracks
    """
    count = 1
    duration=""
    flag = True

    for i in tracks:
        print track_title + space +  str(count) + delimiter
        topic=""
        count += 1
        last = i[0][-1][2]
        for j in i[0]:

            duration=str(j[1])
            if flag:
                start_time = start_time_morning
                flag=False
                topic = start_time + space + j[0] + space + duration + min
                #print topic
            else:
                start_time = j[2]
                if j[2] == lunch[2] or j[2] == last:
                    topic = start_time + space + j[0]
                else:
                    topic = start_time + space + j[0] + space + duration + min
            print topic
        print



##################################
##################################

def track_topics(topic,track,time_limit):
    """

    :param topic: talk topic
    :param track: track where insertion of topic is to be determined
    :param time_limit: session time duration (morning or afternoon)
    :return: True or False
    """

    if topic[1] + topic[1] > time_limit:
        return False
    else:
        return True




