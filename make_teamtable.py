import science_config as config
from datetime import date, timedelta
import dateutil.parser
import itertools
import icalendar
import operator
import collections

teamcalendar = []

def to_date(datestring):
    return dateutil.parser.parse(datestring).date()

def is_on_leave(person, email, current_date):
    if person in config.leave_missing_from_calendars:
        for booking in config.leave_missing_from_calendars[person]:
            if len(booking) == 2:
                start = to_date(booking[0])
                end = to_date(booking[1])
                if start <= current_date <= end:
                    return True
            elif booking == current_date.strftime('%A'):
                return True

    if not teamcalendar:
        with open(config.calendar_file, 'rb') as f:
            cal = icalendar.Calendar.from_ical(f.read())
            for event in cal.walk('VEVENT'):
                teamcalendar.append(
                    (event.get('summary').encode('utf-8'),
                    str(event.get('attendee')).lower(),
                    event.get('dtstart').dt,
                    event.get('dtend').dt - timedelta(days=1))
                ) #For some reason, events are listed as ending a day late.

    for what, who, start, end in teamcalendar:
        if email.lower() in who:
            if type(start) is date and type(end) is date:
                if start <= current_date <= end:
                    return True

    return False


def add_status(name, colour, on_leave):
    return '{status:colour='+colour+'|title='+name+'|subtle='+str(on_leave)+'} '

def do_hot_shoes_placements(team, current_date):
    # List of who's moving today. We'll find their email address in a minute.
    movers = [(name, role) for (name, role, day) in config.hot_shoes
                if day == current_date.strftime('%A')]

    mover_details = []

    updated_team = collections.OrderedDict()
    for role, people in team.iteritems():
        updated_team[role] = []
        for name, email in people:
            if name in (n for n,r in movers):
                mover_details.append((name, email))
            else:
                updated_team[role].append((name, email))

    for m in movers:
        mover = next((x for x in mover_details if x[0] == m[0]))
        updated_team[m[1]].append((mover))

    return updated_team


def teamtable_row(rw):
    current_date = date.today() + timedelta(rw)
    if current_date.weekday() == 6:
        return ''
    elif current_date.weekday() == 5:
        return '| |\n'
    else:
        # Check if anyone's changing roles today.
        current_team = do_hot_shoes_placements(config.team, current_date)

        row = '| ' + current_date.strftime('%a %d') + '| '
        colours = itertools.cycle(['Green','Yellow','Blue','Red'])
        for role in current_team:
            colour = next(colours)
            for person, email in current_team[role]:
                on_leave = is_on_leave(person, email, current_date)
                row += add_status(person, colour, on_leave)
            row += ' |'

        for datestring, eventname in config.events:
            if to_date(datestring) == current_date:
                row += eventname + '\n'
        row += ' |\n'
        return row



with open('./teamtable.txt', 'w') as f:
    f.write('|| ')
    for role in config.team:
        f.write('|| ' + role)
    f.write('|| Events ||\n')
    for rw in range(60):
        f.write(teamtable_row(rw))
