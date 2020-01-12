
syllabus = {
  'Scratch': [
    {
      'title':    "Scratch",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "Computer Setup",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    }
  ],
  'Basics': [
    {
      'title':    "The Basics: 1/2",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "The Basics: 2/2",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    }
  ],
  'C': [
    {
      'title':    "The Command Line",
      'desc':     "hello",
      'ppt_code': "2PACX-1vRxFfZxGMOTJvX4JB1ervJovwUa9mrcVyF65Kgj0t1ZexcdmeqZPUiVIZ7p5SsFVYWqBNiNv2oL-qX7",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "C: Variables, Datatypes & Operators",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "C: Conditionals, Arrays & Loops",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "C: Functions & Variables Scope",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "C: Command Line Arguments & Complexity Analysis",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "C: Magic Numbers & Structs",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "Algorithms: Search",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "Algorithms: Sorting",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "Memory Management",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "C: Data Structures (Linked Lists, Queues, Stacks ... )",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    }
  ],
  'Midterm': [
    {},
    {}
  ],
  'Python': [
    {
      'title':    "",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
  ],
  'MVC1': [
    {
      'title':    "MVC: Flask",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "MVC: Jinja2",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    }
  ],
  'Front-End': [
    {
      'title':    "HTML",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "CSS",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    }
  ],
  'MVC2': [
    {
      'title':    "MVC: SQL",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    },
    {
      'title':    "MVC: Flask Alquemy",
      'desc':     "hello",
      'ppt_code': "",
      'videos':   {},
      'resources':{}
    }
  ],
  'Final': [
    {},
    {}
  ],
  'Javascript': [
    {},
    {}
  ],
  'Bootstrap': [
    {},
    {}
  ],
  'Github': [
    {},
    {}
  ]
}

lectures, i = {}, 0

for (topic, courses) in syllabus.items():
  for course in courses:
    lectures[str(i)] = course
    i += 1

weeks  = {
  '0':{
    'lectures': [ lectures["0"], lectures["1"] ]
  },
  '1':{
    'lectures': [ lectures["2"], lectures["3"] ]
  },
  '2':{
    'lectures': [ lectures["4"], lectures["5"] ]
  },
  '3':{
    'lectures': [ lectures["6"], lectures["7"] ]
  },
  '4':{
    'lectures': [ lectures["8"], lectures["9"] ]
  },
  '5':{
    'lectures': [ lectures["10"], lectures["11"] ]
  },
  '6':{
    'lectures': [ lectures["12"], lectures["13"] ]
  },
  '7':{
    'lectures': [ lectures["14"], lectures["15"] ]
  },
  '8':{
    'lectures': [ lectures["16"], lectures["17"] ]
  },
  '9':{
    'lectures': [ lectures["18"], lectures["19"] ]
  },
  '10':{
    'lectures': [ lectures["20"], lectures["21"] ]
  },
  '11':{
    'lectures': [ lectures["22"], lectures["23"] ]
  },
  '12':{
    'lectures': [ lectures["24"], lectures["25"] ]
  },
  '13':{
    'lectures': [ lectures["26"], lectures["27"] ]
  },
  '14':{
    'lectures': [ lectures["28"], lectures["29"] ]
  },
  '15':{
    'lectures': [ lectures["30"], lectures["31"] ]
  },
  '16':{
    'lectures': [ lectures["32"], lectures["33"] ]
  },
  '17':{
    'lectures': [ lectures["34"], lectures["35"] ]
  }
}