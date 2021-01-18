current_cohort = "13"

staff = {
    "1" : {
        "fname": "Al",
        "lname": "Delcy",
        "role" : "Lead Instructor",
        "short_desc" : "Al was previously employed at Launch Code. He worked with an incredible teaching staff and restructured the material overtime to adapt to the student's pace and learning styles.",
        "desc" : " \
            <p>Al was previously employed at Launch Code. He worked with an incredible teaching staff and restructured the material overtime to adapt to the student's pace and learning styles.</p>  \
            <ul> \
                <li>M.B.A&nbsp;Business Management&nbsp;- Florida International University.</li> \
                <li>IronHack bootcamp full-stack development (teaching and learning).</li> \
                <li>5+ years involved in education with a focus on computer programming and web development.</li> \
                <li>CS50x Miami&nbsp;Instructor, EcoTech, EdTech (Digital Consultant).</li> \
                <li>Experience with well over a dozen programming languages.</li> \
                <li>Other areas of interest: Photography, Web Development, and Gaming.</li> \
            </ul>",
        "contact": {
            "phone": "",
            "email": "al@mdc.edu"
        },
        "social" : {
            "linkedin" : "https://www.linkedin.com/in/aldelcy/",
            "instagram" : "https://www.instagram.com/aldelcy/",
            "website" : "http://www.aldelcy.com",
        }
    },
    "2" : {
        "fname": "Urbano",
        "lname": "Baz",
        "role" : "Program Coordinator - Co-Instructor",
        "desc" : "",
        "contact": {
            "phone": "305-237-7822",
            "email": "ubaz@mdc.edu"
        },
        "social" : {
            "linkedin" : "https://www.linkedin.com/in/urbanobaz",
            "twitter" : "https://www.twitter.com/ubaz_3"
        }
    },
    # "3" : {
    #     "fname": "Gloria",
    #     "lname": "Jimenez",
    #     "role" : "Teaching Fellow",
    #     "short_desc" : "Gloria a Computer Science teacher and a student in Udacity's Nanodegree Android Basics by Google.",
    #     "desc" : "<p>\
    #             Gloria a Computer Science teacher and a student in Udacity's Nanodegree Android Basics by Google.\
    #             As an educator and program coordinator she has worked in inner city communities as well as internationally\
    #             with youth populations and everyday people fighting for justice.</p>\
    #             <p>Her tech experience includes knowledge of both front end and back end technologies. She has experience\
    #             teaching computer programming to both youth and adult learners.</p>\
    #         ",
    #     "contact": {
    #         "phone": "",
    #         "email": "gjimena@mdc.edu"
    #     },
    #     "social" : {
    #         "linkedin" : "https://www.linkedin.com/in/gloriajimenez/",
    #         "instagram" : "",
    #         "website" : "",
    #     }
    # }
}

theStaff = staff.items()
for (i, person) in theStaff:
        person['fullname'] = person['fname'] + " " + person['lname']