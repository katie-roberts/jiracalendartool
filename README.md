# Neil Vass's marvolous jira calendar tool

You will need to access the science_config.py and add the email addresses of the people in your team.  Once this is done:

* Install the libraries needed (a package manager like Homebrew finds them easily), 
* Go to your jira calendar, download the “Away” calendar as an ical file,
* Save it as “cal.ics” in the same folder as this script,
* Run python make_timetable.py – this outputs “teamtable.txt"
* Edit the clever Confluence page, delete the current planner, then insert markup and paste in the contents of “teamtable.txt”
* Bask in everyone’s admiration.

