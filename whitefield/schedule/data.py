"""
Encode a string date to a (day code, modifier) pair, either of which
may be empty.
"""

day_code_ay2011_2012 = {
    '2011-08-16': ('', 'Late ALL'),
    '2011-10-03': ('C', ''),
    '2011-11-18': ('G', ''),
    '2012-01-05': ('C', 'Chapel'),
    '2012-02-22': ('F', 'Late'),
    '2012-04-10': ('D', ''),
    '2011-08-17': ('A', 'Late'),
    '2011-10-04': ('D', ''),
    '2011-11-21': ('A', ''),
    '2012-01-06': ('D', ''),
    '2012-02-23': ('G', 'Chapel'),
    '2012-04-11': ('E', 'Late'),
    '2011-08-18': ('B', 'Chapel'),
    '2011-10-05': ('E', 'Late'),
    '2011-11-22': ('B', ''),
    '2012-01-09': ('E', ''),
    '2012-02-24': ('A', ''),
    '2012-04-12': ('F', 'Chapel'),
    '2011-08-19': ('C', ''),
    '2011-10-06': ('F', 'Chapel'),
    '2011-11-23': ('', 'No School'),
    '2012-01-10': ('F', ''),
    '2012-02-27': ('B', ''),
    '2012-04-13': ('G', ''),
    '2011-08-22': ('', 'MS&US FT'),
    '2011-10-07': ('G', ''),
    '2011-11-24': ('', 'No School'),
    '2012-01-11': ('G', 'Late'),
    '2012-02-28': ('C', ''),
    '2012-04-16': ('A', ''),
    '2011-08-23': ('', 'LateMS/USServ'),
    '2011-10-10': ('', 'No School'),
    '2011-11-25': ('', 'No School'),
    '2012-01-12': ('A', 'Chapel'),
    '2012-02-29': ('D', 'Late'),
    '2012-04-17': ('B', ''),
    '2011-08-24': ('D', 'Late'),
    '2011-10-11': ('A', ''),
    '2011-11-28': ('C', ''),
    '2012-01-13': ('B', ''),
    '2012-03-01': ('E', 'Chapel'),
    '2012-04-18': ('C', 'Late'),
    '2011-08-25': ('E', 'Chapel'),
    '2011-10-12': ('', 'US PSAT,MS Conf'),
    '2011-11-29': ('D', ''),
    '2012-01-16': ('', 'No School'),
    '2012-03-02': ('F', ''),
    '2012-04-19': ('D', 'Chapel'),
    '2011-08-26': ('F', 'Pep'),
    '2011-10-13': ('B', 'Chapel'),
    '2011-11-30': ('E', 'Late'),
    '2012-01-17': ('C', ''),
    '2012-03-05': ('', 'No School'),
    '2012-04-20': ('E', ''),
    '2011-08-29': ('G', ''),
    '2011-10-14': ('C', ''),
    '2011-12-01': ('F', ''),
    '2012-01-18': ('D', 'Late'),
    '2012-03-06': ('', 'No School'),
    '2012-04-23': ('F', ''),
    '2011-08-30': ('A', ''),
    '2011-10-17': ('D', ''),
    '2011-12-02': ('G', 'Chapel'),
    '2012-01-19': ('E', 'Chapel'),
    '2012-03-07': ('', 'No School'),
    '2012-04-24': ('G', ''),
    '2011-08-31': ('B', 'Late'),
    '2011-10-18': ('E', ''),
    '2011-12-05': ('', 'ALL'),
    '2012-01-20': ('F', ''),
    '2012-03-08': ('', 'No School'),
    '2012-04-25': ('A', 'Late'),
    '2011-09-01': ('C', ''),
    '2011-10-19': ('F', 'Late'),
    '2011-12-06': ('', 'ALL'),
    '2012-01-23': ('G', ''),
    '2012-03-09': ('', 'No School'),
    '2012-04-26': ('B', 'Chapel'),
    '2011-09-02': ('D', 'Chapel'),
    '2011-10-20': ('G', 'Chapel'),
    '2011-12-07': ('', 'Late ALL'),
    '2012-01-24': ('A', ''),
    '2012-03-12': ('G', ''),
    '2012-04-27': ('C', ''),
    '2011-09-05': ('', 'No School'),
    '2011-10-21': ('A', ''),
    '2011-12-08': ('', 'Chap ALL'),
    '2012-01-25': ('B', 'Late'),
    '2012-03-13': ('A', ''),
    '2012-04-30': ('D', ''),
    '2011-09-06': ('E', ''),
    '2011-10-24': ('B', ''),
    '2011-12-09': ('', 'ALL'),
    '2012-01-26': ('C', 'Chapel'),
    '2012-03-14': ('B', 'Late'),
    '2012-05-01': ('E', ''),
    '2011-09-07': ('F', 'Late'),
    '2011-10-25': ('C', ''),
    '2011-12-12': ('', 'EXAMS'),
    '2012-01-27': ('D', ''),
    '2012-03-15': ('C', 'Chapel'),
    '2012-05-02': ('F', 'Late'),
    '2011-09-08': ('G', 'Chapel'),
    '2011-10-26': ('D', 'Late'),
    '2011-12-13': ('', 'EXAMS'),
    '2012-01-30': ('E', ''),
    '2012-03-16': ('D', ''),
    '2012-05-03': ('G', 'Chapel'),
    '2011-09-09': ('A', ''),
    '2011-10-27': ('E', 'Chapel'),
    '2011-12-14': ('', 'EXAMS'),
    '2012-01-31': ('F', ''),
    '2012-03-19': ('E', ''),
    '2012-05-04': ('', 'FIELD'),
    '2011-09-12': ('B', ''),
    '2011-10-28': ('F', ''),
    '2011-12-15': ('', 'EXAMS'),
    '2012-02-01': ('G', 'Late'),
    '2012-03-20': ('F', ''),
    '2012-05-07': ('A', ''),
    '2011-09-13': ('C', ''),
    '2011-10-31': ('G', ''),
    '2011-12-16': ('', 'EXAMS'),
    '2012-02-02': ('A', 'Chapel'),
    '2012-03-21': ('G', 'Late'),
    '2012-05-08': ('B', ''),
    '2011-09-14': ('D', 'Late'),
    '2011-11-01': ('A', ''),
    '2011-12-19': ('', 'No School'),
    '2012-02-03': ('B', ''),
    '2012-03-22': ('A', 'Chapel'),
    '2012-05-09': ('C', 'Late'),
    '2011-09-15': ('E', 'Chapel'),
    '2011-11-02': ('B', 'Late'),
    '2011-12-20': ('', 'No School'),
    '2012-02-06': ('C', ''),
    '2012-03-23': ('B', ''),
    '2012-05-10': ('D', 'Chapel'),
    '2011-09-16': ('F', 'Pep'),
    '2011-11-03': ('C', 'Chapel'),
    '2011-12-21': ('', 'No School'),
    '2012-02-07': ('D', ''),
    '2012-03-26': ('C', ''),
    '2012-05-11': ('E', 'Pep'),
    '2011-09-19': ('G', ''),
    '2011-11-04': ('D', ''),
    '2011-12-22': ('', 'No School'),
    '2012-02-08': ('E', 'Late'),
    '2012-03-27': ('D', ''),
    '2012-05-14': ('F', ''),
    '2011-09-20': ('A', ''),
    '2011-11-07': ('E', ''),
    '2011-12-23': ('', 'No School'),
    '2012-02-09': ('F', 'Chapel'),
    '2012-03-28': ('E', 'Late'),
    '2012-05-15': ('G', ''),
    '2011-09-21': ('B', 'Late'),
    '2011-11-08': ('F', ''),
    '2011-12-26': ('', 'No School'),
    '2012-02-10': ('G', 'Pep'),
    '2012-03-29': ('', 'ARTS'),
    '2012-05-16': ('', 'Late ALL'),
    '2011-09-22': ('C', 'Chapel'),
    '2011-11-09': ('G', 'Late'),
    '2011-12-27': ('', 'No School'),
    '2012-02-13': ('A', ''),
    '2012-03-30': ('F', ''),
    '2012-05-17': ('', 'Chap ALL'),
    '2011-09-23': ('D', ''),
    '2011-11-10': ('A', ''),
    '2011-12-28': ('', 'No School'),
    '2012-02-14': ('B', ''),
    '2012-04-02': ('G', ''),
    '2012-05-18': ('', 'ALL'),
    '2011-09-26': ('E', ''),
    '2011-11-11': ('B', 'Chapel'),
    '2011-12-29': ('', 'No School'),
    '2012-02-15': ('C', 'Late'),
    '2012-04-03': ('A', ''),
    '2012-05-21': ('', 'EXAMS'),
    '2011-09-27': ('F', ''),
    '2011-11-14': ('C', ''),
    '2011-12-30': ('', 'No School'),
    '2012-02-16': ('D', 'Chapel'),
    '2012-04-04': ('B', 'Late'),
    '2012-05-22': ('', 'EXAMS'),
    '2011-09-28': ('G', 'Late'),
    '2011-11-15': ('D', ''),
    '2012-01-02': ('', 'In-Service'),
    '2012-02-17': ('E', ''),
    '2012-04-05': ('C', 'Chapel'),
    '2012-05-23': ('', 'EXAMS'),
    '2011-09-29': ('A', 'Chapel'),
    '2011-11-16': ('E', 'Late'),
    '2012-01-03': ('A', ''),
    '2012-02-20': ('', 'No School'),
    '2012-04-06': ('', 'No School'),
    '2012-05-24': ('', 'EXAMS'),
    '2011-09-30': ('B', ''),
    '2011-11-17': ('F', 'Chapel'),
    '2012-01-04': ('B', 'Late'),
    '2012-02-21': ('', 'In-Service'),
    '2012-04-09': ('', 'No School'),
    '2012-05-25': ('', 'EXAMS')
}

day_code_ay2010_2011 = {
    "2010-08-17": ("", "LATE ALL"),
    "2010-08-18": ("A", "Late"),
    "2010-08-19": ("B", "Chapel"),
    "2010-08-20": ("C", ""),
    "2010-08-23": ("", "MS/US Field Trips"),
    "2010-08-24": ("", "MS/US Field Trips"),
    "2010-08-25": ("D", "Late"),
    "2010-08-26": ("E", "Chapel"),
    "2010-08-27": ("F", "Pep"),
    "2010-08-30": ("G", ""),
    "2010-08-31": ("A", ""),
    "2010-09-01": ("B", "Late"),
    "2010-09-02": ("C", ""),
    "2010-09-03": ("D", "Chapel"),
    "2010-09-06": ("", "No School"),
    "2010-09-07": ("", "In-Service"),
    "2010-09-08": ("E", "Late"),
    "2010-09-09": ("F", "Chapel"),
    "2010-09-10": ("G", ""),
    "2010-09-13": ("A", ""),
    "2010-09-14": ("B", ""),
    "2010-09-15": ("C", "Late"),
    "2010-09-16": ("D", "Chapel"),
    "2010-09-17": ("E", ""),
    "2010-09-20": ("F", ""),
    "2010-09-21": ("G", ""),
    "2010-09-22": ("A", "Late"),
    "2010-09-23": ("B", "Chapel"),
    "2010-09-24": ("C", "Pep"),
    "2010-09-27": ("D", ""),
    "2010-09-28": ("E", ""),
    "2010-09-29": ("F", "Late"),
    "2010-09-30": ("G", "Chapel"),
    "2010-10-01": ("A", ""),
    "2010-10-04": ("B", ""),
    "2010-10-05": ("C", ""),
    "2010-10-06": ("D", "Late"),
    "2010-10-07": ("E", "Chapel"),
    "2010-10-08": ("F", ""),
    "2010-10-11": ("", "No School"),
    "2010-10-12": ("G", ""),
    "2010-10-13": ("", "US PSAT, MS Conf"),
    "2010-10-14": ("A", "Chapel"),
    "2010-10-15": ("B", ""),
    "2010-10-18": ("C", ""),
    "2010-10-19": ("D", ""),
    "2010-10-20": ("E", "Late"),
    "2010-10-21": ("F", "Chapel"),
    "2010-10-22": ("G", ""),
    "2010-10-25": ("A", ""),
    "2010-10-26": ("B", ""),
    "2010-10-27": ("C", "Late"),
    "2010-10-28": ("D", "Chapel"),
    "2010-10-29": ("E", ""),
    "2010-11-01": ("F", ""),
    "2010-11-02": ("G", ""),
    "2010-11-03": ("A", "Late"),
    "2010-11-04": ("B", "Chapel"),
    "2010-11-05": ("C", ""),
    "2010-11-08": ("D", ""),
    "2010-11-09": ("E", ""),
    "2010-11-10": ("F", "Late"),
    "2010-11-11": ("G", "Chapel"),
    "2010-11-12": ("A", ""),
    "2010-11-15": ("B", ""),
    "2010-11-16": ("C", ""),
    "2010-11-17": ("D", "Late"),
    "2010-11-18": ("E", "Chapel"),
    "2010-11-19": ("F", ""),
    "2010-11-22": ("G", ""),
    "2010-11-23": ("A", ""),
    "2010-11-24": ("", "No School"),
    "2010-11-25": ("", "No School"),
    "2010-11-26": ("", "No School"),
    "2010-11-29": ("B", ""),
    "2010-11-30": ("C", ""),
    "2010-12-01": ("D", "Late"),
    "2010-12-02": ("E", "Chapel"),
    "2010-12-03": ("F", ""),
    "2010-12-06": ("G", ""),
    "2010-12-07": ("", "ALL"),
    "2010-12-08": ("", "Late ALL"),
    "2010-12-09": ("", "Chapel ALL"),
    "2010-12-10": ("", "ALL"),
    "2010-12-13": ("", "EXAMS"),
    "2010-12-14": ("", "EXAMS"),
    "2010-12-15": ("", "EXAMS"),
    "2010-12-16": ("", "EXAMS"),
    "2010-12-17": ("", "EXAMS"),
    "2010-12-20": ("", "No School"),
    "2010-12-21": ("", "No School"),
    "2010-12-22": ("", "No School"),
    "2010-12-23": ("", "No School"),
    "2010-12-24": ("", "No School"),
    "2010-12-27": ("", "No School"),
    "2010-12-28": ("", "No School"),
    "2010-12-29": ("", "No School"),
    "2010-12-30": ("", "No School"),
    "2010-12-31": ("", "No School"),
    "2011-01-03": ("", "In-Service"),
    "2011-01-04": ("A", ""),
    "2011-01-05": ("B", "Late"),
    "2011-01-06": ("C", "Chapel"),
    "2011-01-07": ("D", ""),
    "2011-01-10": ("E", ""),
    "2011-01-11": ("F", ""),
    "2011-01-12": ("G", "Late"),
    "2011-01-13": ("A", "Chapel"),
    "2011-01-14": ("B", ""),
    "2011-01-17": ("", "No School"),
    "2011-01-18": ("C", ""),
    "2011-01-19": ("D", "Late"),
    "2011-01-20": ("E", "Chapel"),
    "2011-01-21": ("F", ""),
    "2011-01-24": ("G", ""),
    "2011-01-25": ("A", ""),
    "2011-01-26": ("B", "Late"),
    "2011-01-27": ("C", "Chapel"),
    "2011-01-28": ("D", ""),
    "2011-01-31": ("E", ""),
    "2011-02-01": ("F", ""),
    "2011-02-02": ("G", "Late"),
    "2011-02-03": ("A", "Chapel"),
    "2011-02-04": ("B", "Pep"),
    "2011-02-07": ("C", ""),
    "2011-02-08": ("D", ""),
    "2011-02-09": ("E", "Late"),
    "2011-02-10": ("F", "Chapel"),
    "2011-02-11": ("G", ""),
    "2011-02-14": ("A", ""),
    "2011-02-15": ("B", ""),
    "2011-02-16": ("C", "Late"),
    "2011-02-17": ("D", "Chapel"),
    "2011-02-18": ("E", ""),
    "2011-02-21": ("", "No School"),
    "2011-02-22": ("", "In-Service"),
    "2011-02-23": ("F", "Late"),
    "2011-02-24": ("G", "Chapel"),
    "2011-02-25": ("A", ""),
    "2011-02-28": ("B", ""),
    "2011-03-01": ("C", ""),
    "2011-03-02": ("D", "Late"),
    "2011-03-03": ("E", "Chapel"),
    "2011-03-04": ("F", ""),
    "2011-03-07": ("", "No School"),
    "2011-03-08": ("", "No School"),
    "2011-03-09": ("", "No School"),
    "2011-03-10": ("", "No School"),
    "2011-03-11": ("", "No School"),
    "2011-03-14": ("G", ""),
    "2011-03-15": ("A", ""),
    "2011-03-16": ("B", "Late"),
    "2011-03-17": ("C", "Chapel"),
    "2011-03-18": ("D", ""),
    "2011-03-21": ("E", ""),
    "2011-03-22": ("F", ""),
    "2011-03-23": ("G", "Late"),
    "2011-03-24": ("A", "Chapel"),
    "2011-03-25": ("B", ""),
    "2011-03-28": ("C", ""),
    "2011-03-29": ("D", ""),
    "2011-03-30": ("E", "Late"),
    "2011-03-31": ("F", "Chapel"),
    "2011-04-01": ("G", ""),
    "2011-04-04": ("A", ""),
    "2011-04-05": ("B", ""),
    "2011-04-06": ("C", "Late"),
    "2011-04-07": ("D", "Chapel"),
    "2011-04-08": ("", "ARTS"),
    "2011-04-11": ("E", ""),
    "2011-04-12": ("F", ""),
    "2011-04-13": ("G", "Late"),
    "2011-04-14": ("A", "Chapel"),
    "2011-04-15": ("B", ""),
    "2011-04-18": ("C", ""),
    "2011-04-19": ("D", ""),
    "2011-04-20": ("E", "Late"),
    "2011-04-21": ("F", "Chapel"),
    "2011-04-22": ("", "No School"),
    "2011-04-25": ("", "No School"),
    "2011-04-26": ("G", ""),
    "2011-04-27": ("A", "Late"),
    "2011-04-28": ("B", "Chapel"),
    "2011-04-29": ("", "FIELD"),
    "2011-05-02": ("C", ""),
    "2011-05-03": ("D", ""),
    "2011-05-04": ("E", "Late"),
    "2011-05-05": ("F", "Chapel"),
    "2011-05-06": ("G", ""),
    "2011-05-09": ("A", ""),
    "2011-05-10": ("B", ""),
    "2011-05-11": ("C", "Late"),
    "2011-05-12": ("D", "Chapel"),
    "2011-05-13": ("E", ""),
    "2011-05-16": ("F", "Pep"),
    "2011-05-17": ("G", ""),
    "2011-05-18": ("", "Late,MSALL,USREV"),
    "2011-05-19": ("", "Chapel,MSALL,USREV"),
    "2011-05-20": ("", "EXAMS"),
    "2011-05-23": ("", "EXAMS"),
    "2011-05-24": ("", "EXAMS"),
    "2011-05-25": ("", "EXAMS"),
    "2011-05-26": ("", "EXAMS"),
}

day_code_ay2009_2010 = {
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
    "9/2/2009": ("C", "Late"),
    "9/3/2009": ("D", ""),
    "9/4/2009": ("E", "Chapel"),
    "9/7/2009": ("", "Labor"),
    "9/8/2009": ("F", ""),
    "9/9/2009": ("G", "Late"),
    "9/10/2009": ("A", "Chapel"),
    "9/11/2009": ("B", ""),
    "9/14/2009": ("C", ""),
    "9/15/2009": ("D", ""),
    "9/16/2009": ("E", "Late"),
    "9/17/2009": ("F", "Chapel"),
    "9/18/2009": ("G", ""),
    "9/21/2009": ("A", ""),
    "9/22/2009": ("B", ""),
    "9/23/2009": ("C", "Late"),
    "9/24/2009": ("D", "Chapel"),
    "9/25/2009": ("E", "Pep"),
    "9/28/2009": ("F", ""),
    "9/29/2009": ("G", ""),
    "9/30/2009": ("A", "Late"),
    "10/1/2009": ("B", "Chapel"),
    "10/2/2009": ("C", ""),
    "10/5/2009": ("D", ""),
    "10/6/2009": ("E", ""),
    "10/7/2009": ("F", "Late"),
    "10/8/2009": ("G", "Chapel"),
    "10/9/2009": ("", "Half"),
    "10/12/2009": ("", "Off"),
    "10/13/2009": ("A", ""),
    "10/14/2009": ("", "PSAT/MSConf"),
    "10/15/2009": ("B", "Chapel"),
    "10/16/2009": ("C", ""),
    "10/19/2009": ("D", ""),
    "10/20/2009": ("E", ""),
    "10/21/2009": ("F", "Late"),
    "10/22/2009": ("G", "Chapel"),
    "10/23/2009": ("A", ""),
    "10/26/2009": ("B", ""),
    "10/27/2009": ("C", ""),
    "10/28/2009": ("D", "Late"),
    "10/29/2009": ("E", "Chapel"),
    "10/30/2009": ("F", ""),
    "11/2/2009": ("G", ""),
    "11/3/2009": ("A", ""),
    "11/4/2009": ("B", "Late"),
    "11/5/2009": ("C", "Chapel"),
    "11/6/2009": ("D", ""),
    "11/9/2009": ("E", ""),
    "11/10/2009": ("F", ""),
    "11/11/2009": ("G", "Late"),
    "11/12/2009": ("A", "Chapel"),
    "11/13/2009": ("B", ""),
    "11/16/2009": ("C", ""),
    "11/17/2009": ("D", ""),
    "11/18/2009": ("E", "Late"),
    "11/19/2009": ("F", "Chapel"),
    "11/20/2009": ("G", ""),
    "11/23/2009": ("A", ""),
    "11/24/2009": ("B", ""),
    "11/25/2009": ("", "Off"),
    "11/26/2009": ("", "Off"),
    "11/27/2009": ("", "Off"),
    "11/30/2009": ("C", ""),
    "12/1/2009": ("D", ""),
    "12/2/2009": ("E", "Late"),
    "12/3/2009": ("F", "Chapel"),
    "12/4/2009": ("G", ""),
    "12/7/2009": ("A", ""),
    "12/8/2009": ("B", ""),
    "12/9/2009": ("C", "Late"),
    "12/10/2009": ("D", "Chapel"),
    "12/11/2009": ("E", ""),
    "12/14/2009": ("", "EXAMS"),
    "12/15/2009": ("", "EXAMS"),
    "12/16/2009": ("", "EXAMS"),
    "12/17/2009": ("", "EXAMS"),
    "12/18/2009": ("", "EXAMS"),
    "12/21/2009": ("", "Off"),
    "12/22/2009": ("", "Off"),
    "12/23/2009": ("", "Off"),
    "12/24/2009": ("", "Off"),
    "12/25/2009": ("", "Off"),
    "12/28/2009": ("", "Off"),
    "12/29/2009": ("", "Off"),
    "12/30/2009": ("", "Off"),
    "12/31/2009": ("", "Off"),
    "1/1/2010": ("", "Off"),
    "1/4/2010": ("", "Tchr"),
    "1/5/2010": ("F", ""),
    "1/6/2010": ("G", "Late"),
    "1/7/2010": ("A", "Chapel"),
    "1/8/2010": ("B", ""),
    "1/11/2010": ("C", ""),
    "1/12/2010": ("D", ""),
    "1/13/2010": ("E", "Late"),
    "1/14/2010": ("F", "Chapel"),
    "1/15/2010": ("G", ""),
    "1/18/2010": ("", "Off"),
    "1/19/2010": ("A", ""),
    "1/20/2010": ("B", "Late"),
    "1/21/2010": ("C", "Chapel"),
    "1/22/2010": ("D", ""),
    "1/25/2010": ("E", ""),
    "1/26/2010": ("F", ""),
    "1/27/2010": ("G", "Late"),
    "1/28/2010": ("A", "Chapel"),
    "1/29/2010": ("B", ""),
    "2/1/2010": ("C", ""),
    "2/2/2010": ("D", ""),
    "2/3/2010": ("E", "Late"),
    "2/4/2010": ("F", "Chapel"),
    "2/5/2010": ("G", ""),
    "2/8/2010": ("A", ""),
    "2/9/2010": ("B", ""),
    "2/10/2010": ("C", "Late"),
    "2/11/2010": ("D", "Chapel"),
    "2/12/2010": ("", "Tchr"),
    "2/15/2010": ("", "Off"),
    "2/16/2010": ("E", ""),
    "2/17/2010": ("F", "Late"),
    "2/18/2010": ("G", "Chapel"),
    "2/19/2010": ("A", ""),
    "2/22/2010": ("B", ""),
    "2/23/2010": ("C", ""),
    "2/24/2010": ("D", "Late"),
    "2/25/2010": ("E", "Chapel"),
    "2/26/2010": ("F", ""),
    "3/1/2010": ("G", ""),
    "3/2/2010": ("A", ""),
    "3/3/2010": ("B", "Late"),
    "3/4/2010": ("C", "Chapel"),
    "3/5/2010": ("D", ""),
    "3/8/2010": ("", "Off"),
    "3/9/2010": ("", "Off"),
    "3/10/2010": ("", "Off"),
    "3/11/2010": ("", "Off"),
    "3/12/2010": ("", "Off"),
    "3/15/2010": ("E", ""),
    "3/16/2010": ("F", ""),
    "3/17/2010": ("G", "Late"),
    "3/18/2010": ("A", "Chapel"),
    "3/19/2010": ("B", ""),
    "3/22/2010": ("C", ""),
    "3/23/2010": ("D", ""),
    "3/24/2010": ("E", "Late"),
    "3/25/2010": ("F", "Chapel"),
    "3/26/2010": ("G", ""),
    "3/29/2010": ("A", ""),
    "3/30/2010": ("B", ""),
    "3/31/2010": ("C", "Late"),
    "4/1/2010": ("D", "Chapel"),
    "4/2/2010": ("", "Off"),
    "4/5/2010": ("", "Off"),
    "4/6/2010": ("E", ""),
    "4/7/2010": ("F", "Late"),
    "4/8/2010": ("G", "Chapel"),
    "4/9/2010": ("", "ARTS"),
    "4/12/2010": ("A", ""),
    "4/13/2010": ("B", ""),
    "4/14/2010": ("C", "Late"),
    "4/15/2010": ("D", "Chapel"),
    "4/16/2010": ("E", ""),
    "4/19/2010": ("F", ""),
    "4/20/2010": ("G", ""),
    "4/21/2010": ("A", "Late"),
    "4/22/2010": ("B", "Chapel"),
    "4/23/2010": ("C", ""),
    "4/26/2010": ("D", ""),
    "4/27/2010": ("E", ""),
    "4/28/2010": ("F", "Late"),
    "4/29/2010": ("G", "Chapel"),
    "4/30/2010": ("", "FIELD"),
    "5/3/2010": ("A", ""),
    "5/4/2010": ("B", ""),
    "5/5/2010": ("C", "Late"),
    "5/6/2010": ("D", "Chapel"),
    "5/7/2010": ("E", ""),
    "5/10/2010": ("F", ""),
    "5/11/2010": ("G", ""),
    "5/12/2010": ("A", "Late"),
    "5/13/2010": ("B", "Chapel"),
    "5/14/2010": ("C", ""),
    "5/17/2010": ("D", ""),
    "5/18/2010": ("E", ""),
    "5/19/2010": ("F", "Late"),
    "5/20/2010": ("G", "Chapel"),
    "5/21/2010": ("", "Exams"),
    "5/24/2010": ("", "Exams"),
    "5/25/2010": ("", "Exams"),
    "5/26/2010": ("", "Exams"),
    "5/27/2010": ("", "Exams"),
}

"""
Define the periods for a given day code.
"""
day_periods = {
    "us": {
        "A": [1, 2, 3, 4, "Lunch", 5, 6],
        "B": [1, 7, 2, 3, "Lunch", 4, 5],
        "C": [1, 6, 7, 2, "Lunch", 3, 4],
        "D": [1, 5, 6, 7, "Lunch", 2, 3],
        "E": [1, 4, 5, 6, "Lunch", 7, 2],
        "F": [1, 3, 4, 5, "Lunch", 6, 7],
        "G": [2, 3, 4, 5, "Lunch", 6, 7],
    },

    "ms": {
        "A": [1, 2, 3, "Lunch", 4, 5, 6],
        "B": [1, 7, 2, "Lunch", 3, 4, 5],
        "C": [1, 6, 7, "Lunch", 2, 3, 4],
        "D": [1, 5, 6, "Lunch", 7, 2, 3],
        "E": [1, 4, 5, "Lunch", 6, 7, 2],
        "F": [1, 3, 4, "Lunch", 5, 6, 7],
        "G": [2, 3, 4, "Lunch", 5, 6, 7],
    },
}

"""
Define the schedule for a given modifier.
"""
schedule = {}
schedule["us"] = {
    "": [("7:45-8:10", "Extra Help"),
         ("8:10-8:25", "Advisee"),
         ("8:30-9:25", 0),
         ("9:30-10:25", 1),
         ("10:30-11:25", 2),
         ("11:30-12:25", 3),
         ("12:30-1:00", 4),
         ("1:05-2:00", 5),
         ("2:05-3:00", 6),
         ],
    "Late": [("8:45-9:10", "Extra Help"),
         ("9:10-9:25", "Advisee"),
         ("9:30-10:15", 0),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:45", 3),
         ("12:50-1:20", 4),
         ("1:25-2:10", 5),
         ("2:15-3:00", 6),
         ],
    "Chapel": [("7:45-8:10", "Extra Help"),
         ("8:10-8:55", 0),
         ("9:00-10:15", "Chapel/Advisee"),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:45", 3),
         ("12:50-1:20", 4),
         ("1:25-2:10", 5),
         ("2:15-3:00", 6),
         ],
    "Pep": [("", "Extra Help"),
         ("", "Advisee"),
         ("", 0),
         ("", 1),
         ("", 2),
         ("", 3),
         ("", 4),
         ("", 5),
         ("", 6),
         ],
}
schedule["ms"] = {
    "": [("7:45-8:10", "Extra Help"),
         ("8:10-8:25", "Advisee"),
         ("8:30-9:25", 0),
         ("9:30-10:25", 1),
         ("10:30-11:25", 2),
         ("11:30-12:00", 3),
         ("12:05-1:00", 4),
         ("1:05-2:00", 5),
         ("2:05-3:00", 6),
         ],
    "Late": [("8:45-9:10", "Clubs"),
         ("9:10-9:25", "Advisee"),
         ("9:30-10:15", 0),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:30", 3),
         ("12:35-1:20", 4),
         ("1:25-2:10", 5),
         ("2:15-3:00", 6),
         ],
    "Chapel": [("7:45-8:10", "Extra Help"),
         ("8:10-8:55", 0),
         ("9:00-10:15", "Chapel/Advisee"),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:30", 3),
         ("12:35-1:20", 4),
         ("1:25-2:10", 5),
         ("2:15-3:00", 6),
         ],
    "Pep": [("", "Extra Help"),
         ("", "Advisee"),
         ("", 0),
         ("", 1),
         ("", 2),
         ("", 3),
         ("", 4),
         ("", 5),
         ("", 6),
         ],
}

"""
special days have an explicit schedule
"""
specials = {}
specials["us"] = {
    "2010-12-07": [("7:45-8:10", "Extra Help"),
                   ("8:10-8:25", "Advisee"),
                   ("8:30-9:15", "1st Period"),
                   ("9:20-10:05", "2nd Period"),
                   ("10:05-10:20", "Break"),
                   ("10:20-11:05", "3rd Period"),
                   ("11:10-11:55", "4th Period"),
                   ("12:00-12:45", "5th Period"),
                   ("12:50-1:20", "Lunch"),
                   ("1:25-2:10", "6th Period"),
                   ("2:15-3:00", "7th Period"),],
    "2010-12-08": [("8:45-9:10", "Extra Help"),
                   ("9:10-9:55", "1st Period"),
                   ("10:00-10:40", "2nd Period"),
                   ("10:45-11:25", "3rd Period"),
                   ("11:30-12:10", "4th Period"),
                   ("12:15-12:45", "Lunch"),
                   ("12:50-1:30", "5th Period"),
                   ("1:35-2:15", "6th Period"),
                   ("2:20-3:00", "7th Period"),],
    "2010-12-09": [("7:45-8:10", "Extra Help"),
                   ("8:10-8:55", "1st Period"),
                   ("9:00-9:55", "Chapel"),
                   ("10:00-10:40", "2nd Period"),
                   ("10:45-11:25", "3rd Period"),
                   ("11:30-12:10", "4th Period"),
                   ("12:15-12:45", "Lunch"),
                   ("12:50-1:30", "5th Period"),
                   ("1:35-2:15", "6th Period"),
                   ("2:20-3:00", "7th Period"),],
    "2010-12-10": [("7:45-8:10", "Extra Help"),
                   ("8:10-8:25", "Advisee"),
                   ("8:30-9:15", "1st Period"),
                   ("9:20-10:05", "2nd Period"),
                   ("10:05-10:20", "Break"),
                   ("10:20-11:05", "3rd Period"),
                   ("11:10-11:55", "4th Period"),
                   ("12:00-12:45", "5th Period"),
                   ("12:50-1:20", "Lunch"),
                   ("1:25-2:10", "6th Period"),
                   ("2:15-3:00", "7th Period"),]
}


from . import parse_date

day_code = day_code_ay2009_2010.copy()
day_code.update(day_code_ay2010_2011)
day_code.update(day_code_ay2011_2012)

# convert day code dates to date objects
day_code = dict(zip(map(parse_date, day_code.keys()), day_code.values()))

for school in specials.keys():
    specials[school] = dict(zip(map(parse_date, specials[school].keys()),
                                specials[school].values()))
