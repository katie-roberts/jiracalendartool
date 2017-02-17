import collections

team = collections.OrderedDict([
    ('Test', [
        ('testerName', 'emailAddress@bbc.co.uk'),
    ]),
    ('UX', [
        ('UXname', 'emailAddress@bbc.co.uk'),
        ('moreUXName', 'email@bbc.co.uk')
    ]),
    ('Dev', [
        ('devName', 'emailAddress@bbc.co.uk'),
    ]),
    ('Others', [
        ('name', 'emailAddress@bbc.co.uk'),
    ]),
    ('indiePartners', [
        ('name', 'address@email.co.uk'),
    ]),
    ('Editorial', [
        ('editorialName', 'emailAddress@bbc.co.uk'),
    ])
])

hot_shoes = [

]

events = [
    ('2017-03-24', 'Big last day'),
]


leave_missing_from_calendars = {
    'devName' : ['Friday'], # Doesn't work on Fridays
}


calendar_file = './cal.ics'
