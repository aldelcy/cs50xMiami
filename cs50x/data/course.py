from datetime import date
from syllabus import *
from psets import *
import os

lectures, i = {}, 0

for (topic, courses) in syllabus.items():
  for course in courses:
    lectures[str(i)] = {**course, **{'topic': topic, 'number': i}}
    if 'desc' in lectures[str(i)]:
      if lectures[str(i)]['published']:
        file = lectures[str(i)]['desc']
        path = os.getcwd() + "/cs50x/lectures/" + file
        try:
          content = open( path, 'r')
          lectures[str(i)]['desc'] = "\n".join([line.strip() for line in content])
        except:
          lectures[str(i)]['desc'] = ""
        finally:
          content.close()
    i += 1

weeks  = {
  '0':{
    'dates': [date(2021, 2, 23), date(2021, 2, 25) ],
    'topic': lectures["0"]['topic'].lower(),
    'lectures': [ lectures["0"], lectures["1"] ]
  },
  '1':{
    'dates': [date(2021, 3, 2), date(2021, 3, 4) ],
    'topic': lectures["2"]['topic'].lower(),
    'lectures': [ lectures["2"], lectures["3"] ],
    'pset' : psets[0]
  },
  '2':{
    'dates': [date(2021, 3, 9), date(2021, 3, 11) ],
    'topic': lectures["4"]['topic'].lower(),
    'lectures': [ lectures["4"], lectures["5"] ]
  },
  '3':{
    'dates': [date(2021, 3, 16), date(2021, 3, 18) ],
    'topic': lectures["6"]['topic'].lower(),
    'lectures': [ lectures["6"], lectures["7"] ],
    'pset' : psets[1]
  },
  '4':{
    'dates': [date(2021, 3, 23), date(2021, 3, 25) ],
    'topic': lectures["8"]['topic'].lower(),
    'lectures': [ lectures["8"], lectures["9"] ],
    'pset' : psets[2]
  },
  '5':{
    'dates': [date(2021, 3, 30), date(2021, 4, 1) ],
    'topic': lectures["10"]['topic'].lower(),
    'lectures': [ lectures["10"], lectures["11"] ]
  },
  '6':{
    'dates': [date(2021, 4, 6), date(2021, 4, 8) ],
    'topic': lectures["12"]['topic'].lower(),
    'lectures': [ lectures["12"], lectures["13"] ],
    'pset' : psets[3]
  },
  '7':{
    'dates': [date(2021, 4, 13), date(2021, 4, 15) ],
    'topic': lectures["14"]['topic'].lower(),
    'lectures': [ lectures["14"], lectures["15"] ]
  },
  '8':{
    'dates': [date(2021, 4, 20), date(2021, 4, 22) ],
    'topic': lectures["16"]['topic'].lower(),
    'lectures': [ lectures["16"], lectures["17"] ],
    'pset' : psets[4]
  },
  '9':{
    'dates': [date(2021, 4, 27), date(2021, 4, 29) ],
    'topic': lectures["18"]['topic'].lower(),
    'lectures': [ lectures["18"], lectures["19"] ]
  },
  '10':{
    'dates': [date(2021, 5, 4), date(2021, 5, 6) ],
    'topic': lectures["20"]['topic'].lower(),
    'lectures': [ lectures["20"], lectures["21"] ],
    'pset' : psets[5]
  },
  '11':{
    'dates': [date(2021, 5, 11), date(2021, 5, 13) ],
    'topic': lectures["22"]['topic'].lower(),
    'lectures': [ lectures["22"], lectures["23"] ]
  },
  '12':{
    'dates': [date(2021, 5, 18), date(2021, 5, 20) ],
    'topic': lectures["24"]['topic'].lower(),
    'lectures': [ lectures["24"], lectures["25"] ],
    'pset' : psets[6]
  },
  '13':{
    'dates': [date(2021, 5, 25), date(2021, 5, 27) ],
    'topic': lectures["26"]['topic'].lower(),
    'lectures': [ lectures["26"], lectures["27"] ]
  },
  '14':{
    'dates': [date(2021, 6, 1), date(2021, 6, 3) ],
    'topic': lectures["28"]['topic'].lower(),
    'lectures': [ lectures["28"], lectures["29"] ],
    'pset' : psets[7]
  },
  '15':{
    'dates': [date(2021, 6, 8), date(2021, 5, 10) ],
    'topic': lectures["30"]['topic'].lower(),
    'lectures': [ lectures["30"], lectures["31"] ]
  }
  # '16':{
  #   'dates': [date(2021, 5, 26), date(2021, 5, 28) ],
  #   'topic': lectures["32"]['topic'].lower(),
  #   'lectures': [ lectures["32"], lectures["33"] ],
  #   'pset' : psets[8]
  # },
  # '17':{
  #   'dates': [date(2021, 6, 2), date(2021, 6, 4) ],
  #   'topic': lectures["34"]['topic'].lower(),
  #   'lectures': [ lectures["34"], lectures["35"] ]
  # },
  # '18':{
  #   'dates': [date(2021, 6, 9), date(2021, 6, 11) ],
  #   'topic': lectures["36"]['topic'].lower(),
  #   'lectures': [ lectures["36"], lectures["37"] ]
  # },
  # '19':{
  #   'dates': [date(2021, 6, 8), date(2021, 6, 10) ],
  #   'topic': lectures["38"]['topic'].lower(),
  #   'lectures': [ lectures["38"], lectures["39"] ]
  # }
}
