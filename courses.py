from models import Course

yoga_summer = Course(
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
        )

edgewood_bootcamp = Course(
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
)

outdoor_june = Course(
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
        )

spring_boot_v2 = Course(
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
        )

yoga_v2 = Course(
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
        )

spring_boot = Course(
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
        )

polo_v2 = Course(
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
        )

yoga = Course(
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
        )

fit_fix = Course(
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
        )

winter_boot = Course(
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
        )

winter = Course(
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
        )

boot_camp = Course(
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
        )

current_courses = [edgewood_bootcamp, outdoor_june]
old_courses = [boot_camp]
courses = current_courses + old_courses
