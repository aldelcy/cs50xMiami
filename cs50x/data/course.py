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
    'dates': [date(2020, 1, 21), date(2020, 1, 23) ],
    'topic': lectures["0"]['topic'].lower(),
    'lectures': [ lectures["0"], lectures["1"] ]
  },
  '1':{
    'dates': [date(2020, 1, 28), date(2020, 1, 30) ],
    'topic': lectures["2"]['topic'].lower(),
    'lectures': [ lectures["2"], lectures["3"] ],
    'pset' : psets[0]
  },
  '2':{
    'dates': [date(2020, 2, 4), date(2020, 2, 6) ],
    'topic': lectures["4"]['topic'].lower(),
    'lectures': [ lectures["4"], lectures["5"] ],
    'pset' : psets[1]
  },
  '3':{
    'dates': [date(2020, 2, 11), date(2020, 2, 13) ],
    'topic': lectures["6"]['topic'].lower(),
    'lectures': [ lectures["6"], lectures["7"] ]
  },
  '4':{
    'dates': [date(2020, 2, 18), date(2020, 2, 20) ],
    'topic': lectures["8"]['topic'].lower(),
    'lectures': [ lectures["8"], lectures["9"] ],
    'pset' : psets[2]
  },
  '5':{
    'dates': [date(2020, 2, 25), date(2020, 2, 27) ],
    'topic': lectures["10"]['topic'].lower(),
    'lectures': [ lectures["10"], lectures["11"] ]
  },
  '6':{
    'dates': [date(2020, 3, 3), date(2020, 3, 5) ],
    'topic': lectures["12"]['topic'].lower(),
    'lectures': [ lectures["12"], lectures["13"] ],
    'pset' : psets[3]
  },
  '7':{
    'dates': [date(2020, 3, 10), date(2020, 3, 12) ],
    'topic': lectures["14"]['topic'].lower(),
    'lectures': [ lectures["14"], lectures["15"] ]
  },
  '8':{
    'dates': [date(2020, 3, 17), date(2020, 3, 19) ],
    'topic': lectures["16"]['topic'].lower(),
    'lectures': [ lectures["16"], lectures["17"] ],
    'pset' : psets[4]
  },
  '9':{
    'dates': [date(2020, 3, 24), date(2020, 3, 26) ],
    'topic': lectures["18"]['topic'].lower(),
    'lectures': [ lectures["18"], lectures["19"] ]
  },
  '10':{
    'dates': [date(2020, 3, 31), date(2020, 4, 2) ],
    'topic': lectures["20"]['topic'].lower(),
    'lectures': [ lectures["20"], lectures["21"] ],
    'pset' : psets[5]
  },
  '11':{
    'dates': [date(2020, 4, 7), date(2020, 4, 9) ],
    'topic': lectures["22"]['topic'].lower(),
    'lectures': [ lectures["22"], lectures["23"] ]
  },
  '12':{
    'dates': [date(2020, 4, 14), date(2020, 4, 16) ],
    'topic': lectures["24"]['topic'].lower(),
    'lectures': [ lectures["24"], lectures["25"] ],
    'pset' : psets[6]
  },
  '13':{
    'dates': [date(2020, 4, 21), date(2020, 4, 23) ],
    'topic': lectures["26"]['topic'].lower(),
    'lectures': [ lectures["26"], lectures["27"] ]
  },
  '14':{
    'dates': [date(2020, 4, 28), date(2020, 4, 30) ],
    'topic': lectures["28"]['topic'].lower(),
    'lectures': [ lectures["28"], lectures["29"] ],
    'pset' : psets[7]
  },
  '15':{
    'dates': [date(2020, 5, 5), date(2020, 5, 7) ],
    'topic': lectures["30"]['topic'].lower(),
    'lectures': [ lectures["30"], lectures["31"] ]
  },
  '16':{
    'dates': [date(2020, 5, 12), date(2020, 5, 14) ],
    'topic': lectures["32"]['topic'].lower(),
    'lectures': [ lectures["32"], lectures["33"] ],
    'pset' : psets[8]
  },
  '17':{
    'dates': [date(2020, 5, 19), date(2020, 5, 21) ],
    'topic': lectures["34"]['topic'].lower(),
    'lectures': [ lectures["34"], lectures["35"] ]
  },
  '18':{
    'dates': [date(2020, 5, 26), date(2020, 5, 28) ],
    'topic': lectures["36"]['topic'].lower(),
    'lectures': [ lectures["36"], lectures["37"] ]
  },
  '19':{
    'dates': [date(2020, 6, 2), date(2020, 6, 24) ],
    'topic': lectures["38"]['topic'].lower(),
    'lectures': [ lectures["38"], lectures["39"] ]
  }
}
