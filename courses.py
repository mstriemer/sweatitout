from models import Course


def google_map_embed_url(place):
    return ("https://www.google.com/maps/embed/v1/place"
            "?q={place}&"
            "key=AIzaSyAeHWzO8g1Cs7qWZu9Z1eNheQPazYk7zQY").format(place=place)

all_courses = []

all_courses.append(Course(
    slug="summer-bootcamp-2015",
    name="Summer Bootcamp",
    description="""
        Perfect for all fitness levels this dynamic class offers cardio,
        resistence training, circuits and plyometrics and is different each and
        every time. Our small class sizes ensure lots of individual attention
        from Jenna. Challenge yourself, get in shape and get sweaty!
    """,
    days=[
        ("Tuesdays", "7:00", "8:00pm"),
        ("Thursdays", "7:00", "8:00pm"),
    ],
    start_date="July 21st",
    end_date="August 27th, 2015",
    cost=110,
    has_space=True,
    location="Ron Duhamel Park",
    map_embed_url=google_map_embed_url(
        place="265 Sage Creek Boulevard, Winnipeg, MB, Canada"),
    allow_assessments=False,
))

all_courses.append(Course(
    slug="spring-bootcamp-2015",
    name="Spring Bootcamp",
    description="""
        Perfect for all fitness levels this dynamic class offers cardio,
        resistence training, circuits and plyometrics and is different each and
        every time. Our small class sizes ensure lots of individual attention
        from Nadine. Challenge yourself, get in shape and get sweaty!
    """,
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm"),
    ],
    start_date="April 6th",
    end_date="May 14th, 2015",
    cost=110,
    has_space=True,
    location="Revive Fitness St Vital",
    map_embed_url="https://www.google.com/maps/embed/v1/place?q=468%20St%20Anne's%20Rd%2C%20Winnipeg%2C%20MB%2C%20Canada&key=AIzaSyAeHWzO8g1Cs7qWZu9Z1eNheQPazYk7zQY",
    allow_assessments=False,
))

all_courses.append(Course(
    slug="end-of-winter-2015",
    name="End of Winter Bootcamp",
    description="""
        Perfect for all fitness levels this dynamic class offers cardio,
        resistence training, circuits and plyometrics and is different each and
        every time. Our small class sizes ensure lots of individual attention
        from Nadine. Challenge yourself, get in shape and get sweaty!
    """,
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm"),
    ],
    start_date="February 23rd",
    end_date="April 2nd, 2015",
    cost=110,
    has_space=True,
    location="Revive Fitness St Vital",
    map_embed_url="https://www.google.com/maps/embed/v1/place?q=468%20St%20Anne's%20Rd%2C%20Winnipeg%2C%20MB%2C%20Canada&key=AIzaSyAeHWzO8g1Cs7qWZu9Z1eNheQPazYk7zQY",
    allow_assessments=False,
))

all_courses.append(Course(
    slug="new-year-bootcamp-2015",
    name="New Year's Resolution Bootcamp",
    description="""
        Perfect for all fitness levels this dynamic class offers cardio,
        resistence training, circuits and plyometrics and is different each and
        every time. Our small class sizes ensure lots of individual attention
        from our newest instructor Nadine. Challenge yourself, get in shape and
        get sweaty!
    """,
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm"),
    ],
    start_date="January 5th",
    end_date="February 12th, 2015",
    cost=110,
    has_space=True,
    location="Revive Fitness St Vital",
    map_embed_url="https://www.google.com/maps/embed/v1/place?q=468%20St%20Anne's%20Rd%2C%20Winnipeg%2C%20MB%2C%20Canada&key=AIzaSyAeHWzO8g1Cs7qWZu9Z1eNheQPazYk7zQY",
    allow_assessments=False,
))

all_courses.append(Course(
    slug="pre-holiday-bootcamp",
    name="Pre-Holiday Bootcamp",
    description="""
        Perfect for all fitness levels this dynamic class offers cardio,
        resistence training, circuits and plyometrics and is different each and
        every time. Our small class sizes ensure lots of individual attention
        from our newest instructor Nadine. Challenge yourself, get in shape and
        get sweaty!
    """,
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm"),
    ],
    start_date="November 3rd",
    end_date="December 11th, 2014",
    cost=110,
    has_space=True,
    location="Revive Fitness St Vital",
    map_embed_url="https://www.google.com/maps/embed/v1/place?q=468%20St%20Anne's%20Rd%2C%20Winnipeg%2C%20MB%2C%20Canada&key=AIzaSyAeHWzO8g1Cs7qWZu9Z1eNheQPazYk7zQY",
    allow_assessments=False,
))

all_courses.append(Course(
    slug="fall-back-bootcamp",
    name="Fall Back to Fitness Bootcamp",
    description="""
        Perfect for all fitness levels this dynamic class offers cardio,
        resistence training, circuits and plyometrics and is different each and
        every time. Our small class sizes ensure lots of individual attention
        from our newest instructor Nadine. Challenge yourself, get in shape and
        get sweaty!
    """,
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm"),
    ],
    start_date="September 22nd",
    end_date="October 30th, 2014",
    cost=110,
    has_space=True,
    location="Revive Fitness Sage Creek",
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    allow_assessments=True,
    note="Classes will move to the new Revive Fitness St. Anne's at 468 St. Anne's Road in mid-October.",
))

all_courses.append(Course(
    slug="saturday-bootcamp-2014-1",
    name="Saturday Outdoor Bootcamp",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Personal Trainer Specialist Emily Striemer and Certified Personal Trainer Jenna Hobson. Challenge yourself, get in shape and get sweaty!",
    days=[
        ("Saturdays", "9:00", "10:00am"),
    ],
    start_date="June 7th",
    end_date="July 5th, 2014",
    cost=50,
    has_space=True,
    location="Blue Lake Park",
    map_image="/static/images/blue-lake-park.jpg",
    map_url="http://maps.google.ca/maps?ie=UTF8&q=blue+lake+park+winnipeg&fb=1&gl=ca&hq=blue+lake+park+winnipeg&hnear=blue+lake+park+winnipeg&cid=8741893315126836065&ll=49.813398,-97.159352&spn=0.00972,0.022702&t=m&z=16&vpsrc=0&iwloc=A",
    note="Save $10 if you also sign up for Tuesdays and Thursdays!",
))

all_courses.append(Course(
    slug="outdoor-bootcamp-2014",
    name="Outdoor Spring Bootcamp",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Personal Trainer Specialist Emily Striemer and Certified Personal Trainer Jenna Hobson. Challenge yourself, get in shape and get sweaty!",
    days=[
        ("Tuesdays", "7:30", "8:30pm"),
        ("Thursdays", "7:30", "8:30pm"),
    ],
    start_date="June 3rd",
    end_date="July 10th, 2014",
    cost=110,
    has_space=True,
    location="Edgewood Park",
    map_image="/static/images/edgewood-park.jpg",
    map_url="http://maps.google.ca/maps?f=q&source=s_q&hl=en&geocode=&q=49.844691,+-97.068383&aq=&sll=49.853822,-97.152225&sspn=0.621562,1.452942&vpsrc=0&ie=UTF8&t=m&z=16&iwloc=A",
))

all_courses.append(Course(
    slug="spring-bootcamp-2014-2",
    name="Spring Bootcamp #2",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Personal Trainer Specialist Emily Striemer and Certified Personal Trainer Jenna Hobson. Challenge yourself, get in shape and get sweaty!",
    days=[
        ("Tuesdays", "8:45", "9:45pm"),
        ("Wednesdays", "8:45", "9:45pm")
    ],
    start_date="April 22nd",
    end_date="May 28th, 2014",
    location="Revive Fitness Sage Creek",
    cost=110,
    has_space=True,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    partial_attendance=False,
    allow_assessments=True,
    note="Please note: classes on April 29th and 30th will be taught by guest instructor, Kinesiology Masters student Travis Hrubeniuk (BKin).",
))

all_courses.append(Course(
    slug="spring-bootcamp-2014-1",
    name="Spring Bootcamp #1",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Personal Trainer Specialist Emily Striemer and Certified Personal Trainer Jenna Hobson. Challenge yourself, get in shape and get sweaty!",
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm"),
    ],
    start_date="April 21st",
    end_date="May 29th, 2014",
    location="Revive Fitness Sage Creek",
    cost=110,
    has_space=False,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    partial_attendance=False,
    allow_assessments=True,
    note="Please note: classes on April 24th, 28th and May 1st will be taught by guest instructor, Kinesiology Masters student Travis Hrubeniuk (BKin).",
))

all_courses.append(Course(
    slug="rise-and-shine-2014",
    name="Rise and Shine Yoga",
    description="Greet the morning and wake your body and mind with Rise and Shine Yoga. <abbr title='Manitoba Fitness Council'>MFC</abbr> Certified yoga instructor Emily will take you through 60 minutes of Hatha yoga, incorporating breathing, stretching, muscle work and relaxation. Perfect for first timers and long timers alike, Rise and Shine Yoga will leave you with strength and zen to take on your weekend.",
    days=[
        ("Saturdays", "8:45", "9:45am"),
    ],
    start_date="April 5th",
    end_date="May 31st, 2014",
    note="Note: no classes on April 26th or May 3rd.",
    location="Revive Fitness Sage Creek",
    cost=75,
    drop_in_open=True,
    drop_in_fee=13,
    has_space=True,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    partial_attendance=False,
))

all_courses.append(Course(
    slug="almost-spring-2014",
    name="Almost Spring Bootcamp",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2014 off sweaty!",
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm")
    ],
    start_date="March 3rd",
    end_date="April 10th, 2014",
    location="Revive Fitness Sage Creek",
    cost=110,
    has_space=False,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    partial_attendance=False,
    allow_assessments=True,
))

all_courses.append(Course(
    slug="new-year-2014",
    name="New Year's Resolution Bootcamp",
    description="Kickstart your new year's resolution with Sweat It Out Fitness's bootcamp. Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Personal Trainer Specialist Emily Striemer and CanFit Pro Personal Trainer Megan Friedheim. Challenge yourself, get in shape and start 2014 off sweaty!",
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm")
    ],
    start_date="January 6th",
    end_date="February 13th, 2014",
    location="Revive Fitness Sage Creek",
    cost=110,
    has_space=True,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    partial_attendance=False,
    allow_assessments=True,
))

all_courses.append(Course(
    slug="year-end-yoga-2013",
    name="Year-End Yoga Session",
    description="Looking for a great workout that incorporates both body and mind? Sweat It Out Fitness is now offering Hatha/Fit Flow yoga. This class is suitable for beginner and intermediate Yoga participants of all fitness levels. Come stretch it out while you sweat it out with Hatha Yoga and Sweat It Out Fitness.",
    days=[["Thursdays", "7:30", "8:30pm"]],
    start_date="November 7th",
    end_date="December 19th, 2013",
    location="Revive Fitness Sage Creek",
    cost=84,
    has_space=True,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    drop_in_open=True,
    drop_in_fee=14,
    ))

all_courses.append(Course(
    slug="year-end-bootcamp-2013",
    name="Year-End Bootcamp Revive Fitness",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from our fully certified trainers. Challenge yourself, get in shape and start your fall routine off right with Sweat It Out Fitness!",
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm")
    ],
    start_date="November 11th",
    end_date="December 19th, 2013",
    location="Revive Fitness Sage Creek",
    cost=90,
    has_space=True,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    partial_attendance=False,
    allow_assessments=True,
))

all_courses.append(Course(
    slug="yoga-fall-2013",
    name="Fall Yoga Session",
    description="Looking for a great workout that incorporates both body and mind? Sweat It Out Fitness is now offering Hatha/Fit Flow yoga. This class is suitable for beginner and intermediate Yoga participants of all fitness levels. Come stretch it out while you sweat it out with Hatha Yoga and Sweat It Out Fitness.",
    days=[["Thursdays", "7:30", "8:30pm"]],
    start_date="October 3rd",
    end_date="October 24th, 2013",
    location="Revive Fitness Sage Creek",
    cost=30,
    has_space=True,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    drop_in_open=True,
    drop_in_fee=13,
    ))

all_courses.append(Course(
    slug="fall-bootcamp-2013",
    name="Fall Bootcamp Revive Fitness",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from our fully certified trainers. Challenge yourself, get in shape and start your fall routine off right with Sweat It Out Fitness!",
    days=[
        ("Mondays", "8:45", "9:45pm"),
        ("Thursdays", "8:45", "9:45pm")
    ],
    start_date="September 23rd",
    end_date="October 31st, 2013",
    location="Revive Fitness Sage Creek",
    cost=110,
    has_space=True,
    map_image="/static/images/revive-fitness-sage-creek.png",
    map_url="https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
    partial_attendance=False,
    allow_assessments=True,
))

all_courses.append(Course(
    slug="august-bootcamp-2013",
    name="August Edgewood Bootcamp",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from our fully certified trainers. Challenge yourself, get in shape and enjoy the beautiful Manitoba summer!",
    days=[
        ("Tuesdays", "8:00", "9:00pm", 45),
        ("Thursdays", "8:00", "9:00pm", 45)
    ],
    start_date="August 6th",
    end_date="August 29th, 2013",
    location="Edgewood Park",
    cost=80,
    has_space=True,
    map_image="/static/images/edgewood-park.jpg",
    map_url="http://maps.google.ca/maps?f=q&source=s_q&hl=en&geocode=&q=49.844691,+-97.068383&aq=&sll=49.853822,-97.152225&sspn=0.621562,1.452942&vpsrc=0&ie=UTF8&t=m&z=16&iwloc=A",
    partial_attendance=True,
))

all_courses.append(Course(
        slug="yoga-summer-2013",
        name="Summer Yoga Session",
        description="Looking for a great workout that incorporates both body and mind? Sweat It Out Fitness is now offering Hatha/Fit Flow yoga. This class is suitable for beginner and intermediate Yoga participants of all fitness levels. Come stretch it out while you sweat it out with Hatha Yoga and Sweat It Out Fitness.",
        days=[["Wednesdays", "7:00", "8:00pm"]],
        start_date="July 10th",
        end_date="August 28th, 2013",
        location="Southdale Community Centre",
        cost=75,
        has_space=True,
        map_image="/static/images/southdale-community-centre.png",
        map_url="https://maps.google.ca/maps?hl=en&ie=UTF8&q=Southdale+Community+Centre&fb=1&gl=ca&hq=Southdale+Community+Centre&cid=17007604877746385002&ll=49.846963,-97.076976&spn=0.009104,0.022724&t=m&z=16&vpsrc=0&iwloc=A",
        drop_in_open=True,
        drop_in_fee=13,
        ))

all_courses.append(Course(
    slug="edgewood-june-2013",
    name="Edgewood Bootcamp",
    description="Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from our fully certified trainers. Challenge yourself, get in shape and enjoy the beautiful Manitoba summer!",
    days=[("Tuesdays", "8:00", "9:00pm"), ("Thursdays", "8:00", "9:00pm")],
    start_date="June 25th",
    end_date="August 1st, 2013",
    location="Edgewood Park",
    cost=110,
    has_space=True,
    map_image="/static/images/edgewood-park.jpg",
    map_url="http://maps.google.ca/maps?f=q&source=s_q&hl=en&geocode=&q=49.844691,+-97.068383&aq=&sll=49.853822,-97.152225&sspn=0.621562,1.452942&vpsrc=0&ie=UTF8&t=m&z=16&iwloc=A",
))

all_courses.append(Course(
    "outdoor-june-2013",
    "Outdoor Bootcamp",
    "It's summertime and that can only mean one thing: it's time to get sweaty outside!! Join Megan on Mondays for 60 minutes and Emily on Saturdays for 90 minutes of  sweaty cardio, resistance and core! Rain or shine, bring a water bottle, a yoga mat or towel and some good outdoor shoes to Blue Lake Park and prepare to Sweat It Out in the great outdoors!",
    [("Mondays", "7:00", "8:00pm", 60), ("Saturdays", "8:00", "9:30am", 75)],
    "June 17th",
    "July 27th, 2013",
    "Blue Lake Park",
    110,
    True,
    "/static/images/blue-lake-park.jpg",
    "http://maps.google.ca/maps?ie=UTF8&q=blue+lake+park+winnipeg&fb=1&gl=ca&hq=blue+lake+park+winnipeg&hnear=blue+lake+park+winnipeg&cid=8741893315126836065&ll=49.813398,-97.159352&spn=0.00972,0.022702&t=m&z=16&vpsrc=0&iwloc=A",
    partial_attendance=True,
))

all_courses.append(Course(
    "revive-late-spring-2013",
    "Bootcamp at Revive Fitness",
    "Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson and Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2013 off sweaty!",
    [["Tuesdays", "8:45", "9:45pm"], ["Thursdays", "8:45", "9:45pm"]],
    "May 14th",
    "June 20th, 2013",
    "Revive Fitness Sage Creek",
    110,
    True,
    "/static/images/revive-fitness-sage-creek.png",
    "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
))

all_courses.append(Course(
    "yoga-late-spring-2013",
    "Late Spring Yoga Session",
    "Looking for a great workout that incorporates both body and mind? Sweat It Out Fitness is now offering Hatha/Fit Flow yoga. This class is suitable for beginner and intermediate Yoga participants of all fitness levels. Come stretch it out while you sweat it out with Hatha Yoga and Sweat It Out Fitness.",
    [["Wednesdays", "7:00", "8:00pm"]],
    "May 8th",
    "June 26th, 2013",
    "Southdale Community Centre",
    67,
    True,
    "/static/images/southdale-community-centre.png",
    "https://maps.google.ca/maps?hl=en&ie=UTF8&q=Southdale+Community+Centre&fb=1&gl=ca&hq=Southdale+Community+Centre&cid=17007604877746385002&ll=49.846963,-97.076976&spn=0.009104,0.022724&t=m&z=16&vpsrc=0&iwloc=A",
    drop_in_open=True,
    drop_in_fee=13,
    note="Please note - no class Wednesday, May 15th.",
))

all_courses.append(Course(
    "revive-spring-2013",
    "Spring Bootcamp at Revive Fitness",
    "Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson and Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2013 off sweaty!",
    [["Mondays", "8:45", "9:45pm"], ["Thursdays", "8:45", "9:45pm"]],
    "April 1st",
    "May 9th, 2013",
    "Revive Fitness Sage Creek",
    110,
    True,
    "/static/images/revive-fitness-sage-creek.png",
    "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
))

all_courses.append(Course(
    "polo-park-spring-2013",
    "Spring Polo Park Bootcamp",
    "Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson.",
    [["Tuesdays", "7:00", "8:00pm"], ["Thursdays", "7:00", "8:00pm"], ["Saturdays", "10:00", "11:00am"]],
    "March 26th",
    "April 18th, 2013",
    "Revive Fitness Polo Park",
    100,
    True,
    "/static/images/revive-fitness-polo-park.png",
    "https://maps.google.ca/maps?q=1740+Ellice+Avenue+(Revive+Fitness+Polo+Park)&hl=en&sll=49.864325,-97.124977&sspn=0.155357,0.363579&hnear=1740+Ellice+Ave,+Winnipeg,+Manitoba+R3H+0B6&t=m&z=16&iwloc=A",
))

all_courses.append(Course(
    "yoga-spring-2013",
    "Spring Yoga Session",
    "Looking for a great workout that incorporates both body and mind? Sweat It Out Fitness is now offering Hatha/Fit Flow yoga. This class is suitable for beginner and intermediate Yoga participants of all fitness levels. Come stretch it out while you sweat it out with Hatha Yoga and Sweat It Out Fitness.",
    [["Wednesdays", "7:00", "8:00pm"]],
    "March 13th",
    "May 1st, 2013",
    "Southdale Community Centre",
    75,
    True,
    "/static/images/southdale-community-centre.png",
    "https://maps.google.ca/maps?hl=en&ie=UTF8&q=Southdale+Community+Centre&fb=1&gl=ca&hq=Southdale+Community+Centre&cid=17007604877746385002&ll=49.846963,-97.076976&spn=0.009104,0.022724&t=m&z=16&vpsrc=0&iwloc=A",
    drop_in_open=True,
    drop_in_fee=13,
))

all_courses.append(Course(
    "spring-fitness-fix-2013",
    "Weekend Fitness Fix",
    "Does your hectic work week keep you from getting the workouts you want? Weekend Fitness Fix is our sweaty solution to your busy schedule. Join us Saturday and Sunday mornings for a fantastic group fitness workout that is fun and challenging for all fitness levels. Piano lessons and Taekwondo carpool duties won't keep you from your fitness goals any longer! Start your mornings off sweaty and feel great all week.",
    [["Saturdays", "8:15", "9:15am"], ["Sundays", "7:45", "8:45am"]],
    "March 9th",
    "April 14th, 2013",
    "Revive Fitness Sage Creek",
    110,
    True,
    "/static/images/revive-fitness-sage-creek.png",
    "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
))

all_courses.append(Course(
    "winter-bootcamp-2013",
    "Bootcamp",
    "Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson and Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2013 off sweaty!",
    [["Mondays", "8:45", "9:45pm"], ["Thursdays", "8:45", "9:45pm"]],
    "February 18th",
    "March 28th, 2013",
    "Revive Fitness Sage Creek",
    110,
    False,
    "/static/images/revive-fitness-sage-creek.png",
    "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
))

all_courses.append(Course(
    "second-chance-2013",
    "Second Chance New Year's Resolution Bootcamp",
    "Didn't start on Janurary 1st? Don't worry about it, start February 5th instead! Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson. Make 2013 your best year!",
    [["Tuesdays", "8:00", "9:00pm", 60], ["Thursdays", "7:00", "8:00pm", 60]],
    "February 5th",
    "March 14th, 2013",
    "Revive Fitness Polo Park",
    110,
    True,
    "/static/images/revive-fitness-polo-park.png",
    "https://maps.google.ca/maps?q=1740+Ellice+Avenue+(Revive+Fitness+Polo+Park)&hl=en&sll=49.864325,-97.124977&sspn=0.155357,0.363579&hnear=1740+Ellice+Ave,+Winnipeg,+Manitoba+R3H+0B6&t=m&z=16&iwloc=A",
))

all_courses.append(Course(
    "new-year-2013",
    "New Year's Resolution Bootcamp",
    "Kickstart your new year's resolution with Sweat It Out Fitness's bootcamp. Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson and Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2013 off sweaty!",
    [["Mondays", "8:45", "9:45pm"], ["Thursdays", "8:45", "9:45pm"]],
    "January 7th",
    "February 14th, 2013",
    "Revive Fitness Sage Creek",
    110,
    False,
    "/static/images/revive-fitness-sage-creek.png",
    "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
))


class CurrentCourseIterator(object):

    def __init__(self, courses, predicate):
        self.courses = courses
        self.predicate = predicate

    def __iter__(self):
        return (course for course in self.courses if self.predicate(course))

current_courses = CurrentCourseIterator(all_courses,
                                        lambda c: not c.completed())
upcoming_courses = CurrentCourseIterator(
    list(reversed(sorted(all_courses, key=lambda c: c.has_space))),
    lambda c: c.upcoming())
active_courses = CurrentCourseIterator(
    all_courses, lambda c: not c.completed() and not c.upcoming())
