
# -------------------------------------------------------------------------
#  DATE:  September 13, 2017
#
#  Problem : Conference Track Management
#
#  You are planning a big programming conference and have received many proposals which
#  have passed the initial screen process but you're having trouble fitting them into
#  the time constraints of the day -- there are so many possibilities!
#  So you write a program to do it for you.
#
#
#  -----------------------------------------------------------------
#  Software/Tools Used
#  -----------------------------------------------------------------
#  Operating System : Darwin 15.6.0 x86_64
#  Language : Python 2.7.13
#
#
#  -----------------------------------------------------------------
#  Constraints/Assumptions
#  -----------------------------------------------------------------
#  - The conference has multiple tracks each of which has a morning and afternoon session.
#  - Each session contains multiple talks.
#  - Morning sessions begin at 9am and must finish by 12 noon, for lunch.
#  - Afternoon sessions begin at 1pm and must finish in time for the networking event.
#  - The networking event can start no earlier than 4:00 and no later than 5:00.
#  - All talk times are either in minutes (not hours) or lightning (5 minutes).
#  - Length of each talk time should be suffixed by "min" (eg. 45min which implies 45 minutes).
#  - If talk time is not specified or is invalid, it is assumed to be 5 minutes.
#  - There needs to be no gap between any two talks.
#  - There can be a gap between the last morning session and lunch.
#  - There can be a gap between the last afternoon session and networking event.
#  - Duplicate titles are allowed in the talk list.
#  - Title cannot be blank.
#  - No talk title has numbers in it.
#  - List of Talk topics is stored in a regular text file and given as positional parameter to the program.
#
#
#  ----------------------------------------------
#  Strategy Used
#  ----------------------------------------------
#  The program uses first fit is the best fit algorithm
#
#
#  -----------------------------------------------
#  Usage Instructions
#  -----------------------------------------------
#
#  1. Change directory to folder "../tw_conference/files"
#
#  2. Please confirm that you execute permission for the files inside the folder "../tw_conference/files"
#
#  3. Execute the program giving a file which contains talk topics as a command line arguement
#       eg:
#         - [[files]] $python conference.py "../input/input_custom.txt"
#
#            or
#
#         - [[files]] $python conference.py "../input/input_custom.txt" > ../log/logfile
#
#
#  -----------------------------------------------
#  Folder/File Description
#  -----------------------------------------------
#
#     tw_conference
#         |
#         |__README.txt
#         |
#         |__log
#         |
#         |__problem_2_description.txt
#         |
#         |__files
#           |
#           |__checks.py
#           |
#           |__conference.py
#           |
#           |__constants.py
#           |
#           |__trackss.py
#
#
#  1. tw_conference - enclosing folder
#
#  2. README.txt - contains generic information about other files in the folder and usage of the programd.
#
#  3. log - log file directory,has program output for some usecases. 
#
#  4. problem_2_description.txt - problem description as given in the assignment
#
#  5. file - source code file
#     a) checks.py - file for common test cases/checks
#     a) conference.py - main driver file
#     a) constants.py - constants/values used in the program
#     a) tracks.py - core methods
#
