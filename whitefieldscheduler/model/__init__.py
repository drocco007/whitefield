"""
Encode a string date to a (day code, modifier) pair, either of which
may be empty.
"""
day_code = {
    "8/18/2009": ("A", "Late"),
    "8/19/2009": ("B", "Late"),
    "8/20/2009": ("C", "Chapel"),
    "8/21/2009": ("D", ""),
    "8/24/2009": ("", "Trip"),
    "8/25/2009": ("", "Trip"),
    "8/26/2009": ("E", "Late"),
    "8/27/2009": ("F", "Chapel"),
    "8/28/2009": ("G", "Pep"),
    "8/31/2009": ("A", ""),
    "9/1/2009": ("B", ""),
    #...
}

"""
Define the periods for a given day code. 
"""
day_periods = {
    "A": [1, 2, 3, 4, 5, 6],
    "B": [1, 7, 2, 3, 4, 5],
    "C": [1, 6, 7, 2, 3, 4],
    "D": [1, 5, 6, 7, 2, 3],
    "E": [1, 4, 5, 6, 7, 2],
    "F": [1, 3, 4, 5, 6, 7],
    "G": [2, 3, 4, 5, 6, 7],
}

"""
Define the schedule for a given modifier. 
"""
schedule = {
    "": [("7:45-8:10", "Extra Help"), 
         ("8:10-8:25", "Advisee"),
         ("8:30-9:25", 0),
         ("9:30-10:25", 1),
         ("10:30-11:25", 2),
         ("11:30-12:25", 3),
         ("12:30-1:00", "Lunch"),
         ("1:05-2:00", 4),
         ("2:05-3:00", 5),
         ],
    "Late": [("8:45-9:10", "Extra Help"), 
         ("9:10-9:25", "Advisee"),
         ("9:30-10:15", 0),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:45", 3),
         ("12:50-1:20", "Lunch"),
         ("1:25-2:10", 4),
         ("2:15-3:00", 5),
         ],
    "Chapel": [("7:45-8:10", "Extra Help"), 
         ("8:10-8:55", 0),
         ("9:00-10:15", "Chapel/Advisee"),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:45", 3),
         ("12:50-1:20", "Lunch"),
         ("1:25-2:10", 4),
         ("2:15-3:00", 5),
         ],
}

from whitefieldscheduler.lib.date_parser import parse_date

# convert day code dates to date objects
day_code = dict(zip(map(parse_date, day_code.keys()), day_code.values()))
