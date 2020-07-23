from datetime import date
from syllabus import *
from psets import *

lectures, i = {}, 0

for (topic, courses) in syllabus.items():
  for course in courses:
    lectures[str(i)] = {**course, **{'topic': topic, 'number': i}}
    i += 1

weeks  = {
  '0':{
    'dates': [date(2020, 7, 21), date(2020, 7, 23) ],
    'topic': lectures["0"]['topic'].lower(),
    'lectures': [ lectures["0"], lectures["1"] ]
  },
  '1':{
    'dates': [date(2020, 7, 28), date(2020, 7, 30) ],
    'topic': lectures["2"]['topic'].lower(),
    'lectures': [ lectures["2"], lectures["3"] ],
    'pset' : psets[0]
  },
  '2':{
    'dates': [date(2020, 8, 4), date(2020, 8, 6) ],
    'topic': lectures["4"]['topic'].lower(),
    'lectures': [ lectures["4"], lectures["5"] ]
  },
  '3':{
    'dates': [date(2020, 8, 11), date(2020, 8, 13) ],
    'topic': lectures["6"]['topic'].lower(),
    'lectures': [ lectures["6"], lectures["7"] ],
    'pset' : psets[1]
  },
  '4':{
    'dates': [date(2020, 8, 18), date(2020, 8, 20) ],
    'topic': lectures["8"]['topic'].lower(),
    'lectures': [ lectures["8"], lectures["9"] ],
    'pset' : psets[2]
  },
  '5':{
    'dates': [date(2020, 8, 25), date(2020, 8, 27) ],
    'topic': lectures["10"]['topic'].lower(),
    'lectures': [ lectures["10"], lectures["11"] ]
  },
  '6':{
    'dates': [date(2020, 9, 1), date(2020, 9, 3) ],
    'topic': lectures["12"]['topic'].lower(),
    'lectures': [ lectures["12"], lectures["13"] ],
    'pset' : psets[3]
  },
  '7':{
    'dates': [date(2020, 9, 8), date(2020, 9, 10) ],
    'topic': lectures["14"]['topic'].lower(),
    'lectures': [ lectures["14"], lectures["15"] ]
  },
  '8':{
    'dates': [date(2020, 9, 15), date(2020, 9, 17) ],
    'topic': lectures["16"]['topic'].lower(),
    'lectures': [ lectures["16"], lectures["17"] ],
    'pset' : psets[4]
  },
  '9':{
    'dates': [date(2020, 9, 22), date(2020, 9, 24) ],
    'topic': lectures["18"]['topic'].lower(),
    'lectures': [ lectures["18"], lectures["19"] ]
  },
  '10':{
    'dates': [date(2020, 9, 29), date(2020, 10, 1) ],
    'topic': lectures["20"]['topic'].lower(),
    'lectures': [ lectures["20"], lectures["21"] ],
    'pset' : psets[5]
  },
  '11':{
    'dates': [date(2020, 10, 6), date(2020, 10, 8) ],
    'topic': lectures["22"]['topic'].lower(),
    'lectures': [ lectures["22"], lectures["23"] ]
  },
  '12':{
    'dates': [date(2020, 10, 13), date(2020, 10, 15) ],
    'topic': lectures["24"]['topic'].lower(),
    'lectures': [ lectures["24"], lectures["25"] ],
    'pset' : psets[6]
  },
  '13':{
    'dates': [date(2020, 10, 20), date(2020, 10, 22) ],
    'topic': lectures["26"]['topic'].lower(),
    'lectures': [ lectures["26"], lectures["27"] ]
  },
  '14':{
    'dates': [date(2020, 5, 12), date(2020, 5, 14) ],
    'topic': lectures["28"]['topic'].lower(),
    'lectures': [ lectures["28"], lectures["29"] ],
    'pset' : psets[7]
  },
  '15':{
    'dates': [date(2020, 5, 19), date(2020, 5, 21) ],
    'topic': lectures["30"]['topic'].lower(),
    'lectures': [ lectures["30"], lectures["31"] ]
  },
  '16':{
    'dates': [date(2020, 5, 26), date(2020, 5, 28) ],
    'topic': lectures["32"]['topic'].lower(),
    'lectures': [ lectures["32"], lectures["33"] ],
    'pset' : psets[8]
  },
  '17':{
    'dates': [date(2020, 6, 2), date(2020, 6, 4) ],
    'topic': lectures["34"]['topic'].lower(),
    'lectures': [ lectures["34"], lectures["35"] ]
  },
  '18':{
    'dates': [date(2020, 6, 9), date(2020, 6, 11) ],
    'topic': lectures["36"]['topic'].lower(),
    'lectures': [ lectures["36"], lectures["37"] ]
  },
  '19':{
    'dates': [date(2020, 6, 16), date(2020, 6, 18) ],
    'topic': lectures["38"]['topic'].lower(),
    'lectures': [ lectures["38"], lectures["39"] ]
  }
}
