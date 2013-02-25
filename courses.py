from models import Course

fit_fix = Course(
        "spring-fitness-fix-2013",
        "Weekend Fitness Fix",
        "Does your hectic work week keep you from getting the workouts you want? Weekend Fitness Fix is our sweaty solution to your busy schedule. Join us Saturday and Sunday mornings for a fantastic group fitness workout that is fun and challenging for all fitness levels. Piano lessons and Taekwondo carpool duties won't keep you from your fitness goals any longer! Start your mornings off sweaty and feel great all week.",
        [["Saturdays", "8:15", "9:15am"], ["Sundays", "7:45", "8:45am"]],
        "March 9th",
        "April 14th, 2013",
        "Revive Fitness Sage Creek",
        110,
        None,
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
        None,
        True,
        "/static/images/revive-fitness-sage-creek.png",
        "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
        )

winter = Course(
        "second-chance-2013",
        "Second Chance New Year's Resolution Bootcamp",
        "Didn't start on Janurary 1st? Don't worry about it, start February 5th instead! Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson. Make 2013 your best year!",
        [["Tuesdays", "8:00", "9:00pm"], ["Thursdays", "7:00", "8:00pm"]],
        "February 5th",
        "March 14th, 2013",
        "Revive Fitness Polo Park",
        110,
        60,
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
        None,
        False,
        "/static/images/revive-fitness-sage-creek.png",
        "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
        )

current_courses = [fit_fix, winter_boot, winter]
old_courses = [boot_camp]
courses = current_courses + old_courses
