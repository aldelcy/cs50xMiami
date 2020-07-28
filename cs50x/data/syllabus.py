from activities import *

syllabus = {
  'Scratch' :   [
    {
      'title'       :   "Scratch",
      'desc'        :   "0_scratch.html",
      'ppts' : [
        {
          'title'   : "",
          'code'    :   "2PACX-1vTPbdgFdyj1a8So3XTxHOVgETZR5nQyExRAIqkclpdaij6wBTl09IqYfbegmNTIDXKFTxvmQxRydOLo",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [{
        'title' : 'Computational Thinking, Scratch',
        'id'    : "jjqgP9dpD1k",
        'time'  : [1940,3742]
      }],
      'recording'   :   "",
      'resources'   :   [
        {
          'type': 'link',
          'title': 'Scratch',
          'desc': 'Create stories, games and Animations',
          'url' : 'https://scratch.mit.edu/'
        },
        {
          'type': 'video',
          'title': 'Scratch Tutorial',
          'desc': 'Make your first program',
          'url' : 'https://www.youtube.com/watch?v=1E8opsBP_98'
        },
        {
          'type': 'link',
          'title': 'Scratch Game',
          'desc': 'Sample Mario Game',
          'url' : 'https://scratch.mit.edu/projects/357390177/'
        }
      ],
      'activities'  :   [activities['2a8a3r2c0']],
      'published'   :   True
    },
    {
      'title'       :   "Computer Basics & Binary",
      'desc'        :   "1_binary.html",
      'ppts' : [
        {
          'title'   : "",
          'code'    :   "2PACX-1vSs6x06eE_7kEtOX3-cuvXmibi7McMBuyRitFm9XryuFfM6jRMYNkcWGRHiMil_xmJSvuv0f6Y1ayHb",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [{
        'title' : 'Computational Thinking, Scratch',
        'id'    : "jjqgP9dpD1k",
        'time'  : [0,1297]
      }],
      'recording'      :   "o4159urnsrv82te/July%2023rd%202020",
      'resources'   :   [
        {
          'type'  : 'link',
          'title' : 'Ascii Codes',
          'desc'  : "Full list of ASCII Codes from 0 to 255",
          'url'   : 'https://www.ascii-code.com/'
        },
        {
          'type'  : 'video',
          'title' : 'Tutorial',
          'desc'  : "How to count in Binary",
          'url'   : 'https://www.youtube.com/watch?v=txoRI2t0boI'
        },
        {
          'type'  : 'video',
          'title' : 'Binary Math',
          'desc'  : "How to Find a number in Binary",
          'url'   : 'https://www.youtube.com/watch?v=jRSqhjMx0X0'
        },
        {
          'type'  : 'video',
          'title' : 'Binary Video',
          'desc'  : "Computer Science Basics: Binary",
          'url'   : 'https://www.youtube.com/watch?v=M41M9ATm49M'
        }
      ],
      'activities'  :   [activities['7g4k9c0o8']],
      'published'   :   True
    }
  ],
  'Basics'  :   [
    {
      'title':    "The Basics: 1/2",
      'desc':     "2_basics1.html",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQjn9S_W3FyTO2Q7ou5DUrrS0JOtt3cWGEo2i0TRnbI--FER06m5N9_YW_PGHRHMZJCxLNymE7uUZ2n",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [{
        'title' : 'PseudoCoding',
        'id'    : "jjqgP9dpD1k",
        'time'  : [1297,1940]
      }],
      'recording':   "",
      'resources':[
        {
          'type'  : 'link',
          'title' : 'Algorithm',
          'desc'  : "A guessing game",
          'url'   : 'https://www.khanacademy.org/computing/computer-science/algorithms/intro-to-algorithms/a/a-guessing-game'
        },
        {
          'type'  : 'video',
          'title' : 'Game',
          'desc'  : "What is an Algorithm",
          'url'   : 'https://www.youtube.com/watch?v=CvSOaYi89B4'
        }
      ],
      'published': True
    },
    {
      'title':    "The Basics: 2/2",
      'desc':     """
                  <h2 class="bold">Welcome to the Basics 2:</h2>

                  In this lecture we will cover the last 4 components of programming and how they will be useful for you as a programmer.<br><br>
                  These 4 components will allow you to group and organize your data in order to simplify your code. Mastering these 4 components will allow you to repeat the same line of code multiple times without having to type them over and over again.<br><br>

                  <br>
                  <h3 class="bold">CONDITIONALS</h3>
                  Conditionals help your program make decisions based on certain inputs or changes in the data you recieve.<br><br>
                  Just like in real life, you have to make decisions based on information you are given (inputs) and decide whether you want to do THIS action or ANOTHER action.<br>

                  <h4>EXAMPLE:</h4>

                  - You are deciding what to make for breakfast.<br>
                  - You check the fridge<br>
                  - IF there is Milk and Cereal<br>
                  - - Then you will eat milk and cereal<br>
                  - ELSE IF there is bread, peanut butter and jelly<br>
                  - - Then you will eat a PB&J instead<br>
                  - ELSE IF there is bread and cheese<br>
                  - - Then Grilled Cheese Sandwich it is.<br>
                  - ELSE if there is nothing<br>
                  - - Then Water it is.<br>
                  <p>
                      Notice in this example that you are making decisions based on whether a condition is true:<br><br>
                      FIRST:  “ there is Milk and Cereal ” ?<br><br>
                      If that’s True, then I make milk and cereal and move on with my morning. And ignore the rest.<br><br>
                      If that’s NOT True, then I check IF “ there is bread, peanut butter and jelly ” ?<br><br>
                      If that’s True, then I make a PB&J and move on with my morning. And ignore the rest.<br><br>
                      Ect…
                  </p>

                  ONLY if i don’t find anything else do I drink water.

                  <br><br>
                  <h3 class="bold">FUNCTIONS</h3>
                  <p>
                      Functions allow you to group pieces of code and give it a name.<br>
                      Whenever you need to run that block of code, you don’t need to write the whole thing over again, you just call it’s name.<br><br>
                  </p>
                  <h4>EXAMPLE:</h4>
                  <p>
                      Since we’re going with a morning theme… let’s keep doing that.<br><br>
                      Every Morning, you wake up and you have a morning routine.<br><br>

                      Let’s say it consists of:<br>
                      - Bathing<br>
                      - Brushing teeth<br>
                      - Getting dressed<br>
                      - Fixing hair<br>
                      - Eating breakfast<br>
                      - Reading the news<br><br>
                  </p>
                  <p>
                      Now imagine that every morning, you wake up and have to write these tasks again from scratch in order to do them. Each of those tasks are made of many steps, and guess what, you have to write all those too. Once you are done doing them… you throw it away and you forget them.<br><br>
                      That would get tiring real quick.<br>
                      SO… what’s the solution? You can write a list of steps that’s called “Morning Routine” in a notebook and then, every morning, all you have to do is pick up that notebook and do each task that was saved in there.<br>
                      NOW… you might want to change these steps based on the time you wake up.<br>
                      The “time” in this case is a parameter that you pass to your “Morning Routine” Function. Now, everytime you wake up, you HAVE to check the time, and if it’s less than 8AM, you have time to do all your tasks, if not, then you can skip some tasks and rush out.<br>
                  </p>

                  <br>
                  <h3 class="bold">LOOPS</h3>
                  <p>
                      Loops are used to repeat something or a piece of code multiple times.<br>
                      You can either repeat indefinitely based on whether something is true and only stop when it’s false, OR repeat a specific number of times.<br><br>
                  </p>

                  <h4>For EXAMPLE:</h4>
                  <p>
                      You could decide, this morning, you’re gonna do 30 pushups. In that case you have a specific number of pushups to do.<br>
                      You could also decide to keep on doing push ups until your phone rings, or you can put bread in your toaster and keep doing push ups until the bread pops up. In this case, the number of push ups might vary depending on how long it takes for you to stop.<br>
                  </p>
      """,
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vT2Dj1UmLwnip0L_FUncuwFNg0mDW7RhlmHxdkV1H62V0TsahZx6Lt88Sx4ZSpGdCMZNpgvYf16-PJk",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Loops',
          'desc'  : "Intro to Programming",
          'url'   : 'https://www.youtube.com/watch?v=wxds6MAtUQ0'
        },
        {
          'type'  : 'video',
          'title' : 'Proramming Structures',
          'desc'  : "Sequences, Selections, and Loops",
          'url'   : 'https://www.youtube.com/watch?v=eSYeHlwDCNA'
        },
        {
          'type'  : 'video',
          'title' : 'Programming Basics:',
          'desc'  : "Statements & Functions: Crash Course Computer Science",
          'url'   : 'https://www.youtube.com/watch?v=l26oaHV7D40'
        }
      ],
      'activities'  :   [activities['2n4n5f0s0']],
      'published': False
    }
  ],
  'Command Line' :   [
    {
      'title':    "The Command Line",
      'desc':     """
                  <h3 class="bold">The terminal</h3>
                  <p>
                  The terminal (or command prompt) is a very powerful tool.<br>
                  It allows you to navigate folders, create files and directories, delete, rename, move, copy and find files without ever having to touch the mouse. <br>
                  </p>
                  <p>
                  Most of you probably never touched a terminal before this class.<br>
                  After this class however, you 2 wil become inseparable.
                  </p>
                  <p>
                  In fact, almost all programmer in the field is very versed in Terminal commands and almost use them all the time.<br>
                  It allows you to do things fast, efficiently and in bulk.<br>
                  Things that would take you some time to do by clicking around a user interface.
                  </p>
                  <p>
                  For the beginning of this course, we will be using the <a href="https://ide.cs50.io/" target="_blank">CS50 IDE</a> and code online.<br>
                  That terminal is EXACTLY like the Mac Terminal, so you should use the Mac commands in there.<br><br>
                  But just in case you are curious. Here is how to find the terminals in your respective operating systems.
                  </p>
                  <h3 class="bold">How to open Terminal on Mac</h3>
                  <p>
                    <ul>
                      <li>Press the <code>Command</code> Key and the <code>Spacebar</code> Key right after the other</li>
                      <li>Type in the word <code>Terminal</code></li>
                      <li>Press <code>Enter</code></li>
                    </ul>
                    You may also have <code>iTerm2</code> as a terminal.
                  </p>
                  <h3 class="bold">How to open Terminal on Windows</h3>
                  <p>
                    <ul>
                      <li>Click on the <code>Start</code> menu icon on the bottom left of the screen</li>
                      <li>Type in the words <code>Command Prompt</code> or simply <code>CMD</code></li>
                      <li>Right click and choose <code>Run as aministrator</code></li>
                    </ul>
                    If you attended the Section last week and turned on the Ubunty Subsystem, you should use <code>hyperJS</code> as a terminal instead.
                  </p>
      """,
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQCULe-AyITdYYqgClUqjETevYea2mu6f36ZSyURpYCn7jVDY0CSLRMVv3HXtDoAk6u715Hd8JDgnAZ",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [{
        'title' : 'The Command Line',
        'id'    : "BnJ013X02b8",
        'time'  : [0,1070]
      }],
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Mac Terminal',
          'desc'  : "Basic Commands and Concepts",
          'url'   : 'https://www.youtube.com/watch?v=-Vl4rpZVA6I'
        },
        {
          'type'  : 'video',
          'title' : 'Mac Terminal',
          'desc'  : "Terminal Basics for Beginners",
          'url'   : 'https://www.youtube.com/watch?v=5XgBd6rjuDQ'
        },
        {
          'type'  : 'video',
          'title' : 'Windows Terminal',
          'desc'  : "Introduction to the Command Prompt",
          'url'   : 'https://www.youtube.com/watch?v=MBBWVgE0ewk'
        },
        {
          'type'  : 'video',
          'title' : 'Windows Terminal',
          'desc'  : "Listing Files and Directories",
          'url'   : 'https://www.youtube.com/watch?v=7ABkcHLdG_A'
        },
        {
          'type'  : 'link',
          'title' : 'Terminal Commands',
          'desc'  : "Ultimate Cheat Sheet",
          'url'   : 'https://github.com/0nn0/terminal-mac-cheatsheet/blob/master/README.markdown'
        }
      ],
      'activities'  :   [activities['7g8h0m8j2']],
      'published': False
    },
  ],
  'C'       :   [
    {
      'title':    "C: Variables, Datatypes, Operators & Conditionals",
      'desc':     "",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vRQzjjGDAj9dus0DxS4vkSCQjAXBovZ43fGy9mdATWKzAMWwbeYv-QIbqZAl2JJD2QWtkj2RUac6enL",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/1/',
      'harvard'     :   [{
        'title' : 'Lecture 1: Variables and Datatype',
        'id'    : "e9Eds2Rc_x8",
        'time'  : [0,2994]
      }],
      'recording':   "",
      'resources':[
        {
          'type'  : 'link',
          'title' : 'Tutorial Point',
          'desc'  : "Defining Variables",
          'url'   : 'https://www.tutorialspoint.com/cprogramming/c_variables.htm'
        },
        {
          'type'  : 'link',
          'title' : 'Geeks for Geeks',
          'desc'  : "C Datatypes",
          'url'   : 'https://www.geeksforgeeks.org/data-types-in-c/'
        },
        {
          'type'  : 'link',
          'title' : 'Geeks for Geeks',
          'desc'  : "C Operators",
          'url'   : 'https://www.geeksforgeeks.org/operators-c-c/'
        },
        {
          'type'  : 'link',
          'title' : 'Tutorial Point',
          'desc'  : "C Operators",
          'url'   : 'https://www.tutorialspoint.com/cprogramming/c_operators.htm'
        }
      ],
      'activities'  :   [activities['y48203j0']],
      'published': False
    },
    {
      'title':    "C: Arrays & Loops",
      'desc':     "",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vR_Mm-zwmbEwWvsCebYUDHbKZqTfJvPq82S1Jzm1eYXyfQbsZVsAvLyBmtx0W4j_QGFWzKO10-GGGzT",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard' : [
        {
          'title' : 'Lecture 2: Arrays in C',
          'id'    : "8PrOp9t0PyQ",
          'time'  : [0,3399]
        },
        {
          'title' : 'Lecture 1: Conditionals and Loops',
          'id'    : "e9Eds2Rc_x8",
          'time'  : [2696,6373]
        }
      ],
      'recording': "",
      'ppts': [
        {
          'title': 'How to compare 2 strings.',
          'url': 'https://www.loom.com/share/759870e2d548446d8e2a8f3683eddf18'
        }
      ],
      'resources':[],
      'activities'  :   [activities['6a82js91']],
      'published': False
    },
    {
      'title':    "C: Functions & Variables Scope",
      'desc':     """
                  <h2 class="bold">What are functions?</h2>
                  <p>
                      Functions help us group code into re-usable blocks.<br>
                      Imagine you are a cook and that you created this amazing but formula to calculate the perfect quantity of ingredients to buy for x number of guests. <br> <br>
                      Everytime you throw a party you have to open your notebook and you have to: <br>
                      - Remember the formula<br>
                      - Plug in the numbers<br>
                      - Calculate and hop you did not make any mistakes<br>
                      - Finally get the final number/output.<br><br>
                      Wouldn't be nice to be able to just write that formula once and everytime you need to use it, All you need to do is to just plug in the numbers and it gives you the answer?<br>
                      That's what functions do. They allow you to write an algorithm one time, and use that SAME algorithm everytime you need to use it.
                  </p>
                  <h2 class="bold">How to write functions?</h2>
                  <a>
                      In C we have a very specific way to write functions:<br><br>
                      1) First, just like a variable, we need to say the type of function we are declaring by putting the data type first.<br>
                      <code>char</code>, <code>int</code>, <code>float</code> <br>
                      OR <br>
                      <code>void</code><br><br>

                      2) Then, like a variable, you choose a name for the function. Remember to make it descriptive and follow the rules of <a href="/lecture/2">variable naming conventions</a><br> <br>
                      <code>int addNumbers</code><br>
                      <code>float taxCalculation</code><br><br>
                      3) Next, we open and close parenthesis right after the name, and we then open and close curly braces.</a><br>
                      <code>int addNumbers() {  };</code><br>
                      <code>float taxCalculation() {  };</code><br><br>
                      4) We need to decide if we will need input for the function to use in our algorithm OR if the function will just perform the algorithm with no input.</a><br>
                      Moving forward, we will refer to functions "Inputs" as "Parameters".<br><br>
                      ** Parameters are not obligatory, but if you want your function to be flexible and dynamic, they are a great way to put in different data and get differnt results based on the data you provided. <br> <br>
    <pre>
      // This is an example of a function WITH NO parameters.

      void sayHello() {
          printf( "Hello World" );
      };</pre> <br>
                      In the example above, the function just ran and printed the words <code>Hello World</code>. You did not pass it any input or data. <br> <br>

                      Now, let's see an example with parameters. <br> <br>
                      When asking for parameters, you must declare the data type of each parameters as well as the names you will use them as in your algorithm. <br>
                      Think of parameters as empty variables that you will use to hold data, and that only exist INSIDE the function. <br>
    <pre>
      // This is an example of a functions WITH parameters a and b.

      void addNumbers( int a, int b) {
          int result = a + b;
          printf( "%i", result );
      };</pre> <br>
                      In the example above, the function required that you give it 2 parameters <code>a</code> and <code>b</code> in order to do the math you wrote in the <code>result</code> variable.
                  </p> <br>

                  <h2 class="bold">2 Types of Functions?</h2>
                  <p>
                      Above, we saw that we made the distinction between: <br>
                      <code>char</code>, <code>int</code>, <code>float</code> <br>
                      AND <br>
                      <code>void</code><br><br>

                      There is a reason for that. <br><br>

                      char, int and float functions require you to <code>return</code> a result of the data type you declared.<br>
                      void does nor require you to return anything. <br> <br>

                      Let's see this example here:<br>
    <pre>
      void addNumbers( int a, int b) {
          int result = a + b;
          printf( "%i", result );
      };</pre>
                      This function is a <code>void</code> function and does not return any data, it performs the action and THAT's it, nothing else. You can't use the result of the operation.<br>
                      If we need to use the result of the operation we need to change it from a <code>void</code> function to an <code>int</code> function and <code>return</code> the result.
    <pre>
      int addNumbers( int a, int b) {
          int result = a + b;
          printf( "%i", result );
          return result;
      };</pre>
                      Here we are telling it to perform the operation, and return us the result as an <code>int</code> so we can use it later. <br>

                  </p>

                  <h2 class="bold">Using fucntions</h2>
                  <p>
                      You've created the functions, but they would be pretty useless if you can't use them right? <br> <br>
                      Lets put them to use. <br>  <br>

                      To call a function, all you need to do it call it's name like so:  <br>
                      <code>addNumbers();</code> <br>  <br>

                      But we are not done, If you look at the function declaration above, <code>addNumbers</code> is expecting you to pass it 2 parameters: <code>a</code> and <code>b</code>. <br>
                      Both of those parameters are <code>int</code>. <br> <br>
                      Ok, let's give those parameters to the function. <br> <br>
                      <code>addNumbers( 10, 45 );</code> <br> <br>

                      PERFECT... now we're cooking. <br> <br>
                      Normally this function should print out <code>55</code> and that's fine if that's all you want it to do. <br> <br>

                      But remember, we might want to use <code>55</code> as part of our code somewhere. Since we are <code>returning</code> the result as an output, we can go ahead an assign that to a vaiable. <br> <br>
                      for example: <br>
                      <code>int calculation = addNumbers( 10, 45 );</code> <br><br>
                      and BOOM, done!!! <br>
                      No we can use the variable <code>calculation</code> somewhere in our code, because it called the function <code>addNumbers</code> and passed it the parameters <code>10</code> and <code>45</code> and it returned us the result <code>55</code>.
                  </p>
      """,
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vS3rpYnX6KBElMdsCY3-xIpwY0DocufYGDh5wCozsfgSKaRD1o8QJzDqnoL-vBCdPAUyeMMpuH5-XSp",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard' : [
        {
          'title' : 'Lecture 2: Functions',
          'id'    : "8PrOp9t0PyQ",
          'time'  : [3399,5695]
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'video',
          'title' : 'C Functions',
          'desc'  : 'How to CREATE functions',
          'url'   : 'https://www.youtube.com/watch?v=DbR-0GfnQOs'
        },
        {
          'type'  : 'video',
          'title' : 'C Functions',
          'desc'  : 'How to USE / INVOKE functions',
          'url'   : 'https://www.youtube.com/watch?v=_0Lp3utEEcs'
        },
        {
          'type'  : 'video',
          'title' : 'C Functions',
          'desc'  : 'Void vs Return Functions',
          'url'   : 'https://www.youtube.com/watch?v=MZAF1R_KzgQ'
        }
      ],
      'activities'  :   [activities['5h23kw23']],
      'published': False
    },
    {
      'title':    "C: Command Line Arguments & Complexity Analysis",
      'desc':     """
        <h2 class="bold">Command Line Arguments</h2>

        <p>
            So far, you've been used to just starting your app with the command: <br>
            <code> make app.c </code> and <code> ./app </code>.
        </p>
        <p>
            In your <code>app.c</code> file, you may notice there is a function called <code>main</code> that is written like so: <br>

            <pre>int main (void) { ... }</pre>
        </p>

        <p>
            the <code>void</code> parameter in that function is placed there to avoid any information to be passed to the function while running the application. <br>

            BUT, just like any other function, you can use declare parameters to be passed to the <code>main</code> function. That's where we will be using the default parameters <code>int argc</code> and <code>char* argv[]</code>.
        </p>

        <p>
            <h4 class="bold">char* argv[ ]</h4>
            As you can notice, this is a parameter expecting to be passed an array of <code>char*</code> or <code>strings</code>. <br> <br>
            This will collect the arguments passed in the command line and pass them in as an array to the main function.

        </p>

        <p>
            <h4 class="bold">int argc</h4>
            Argc is an integer that is meant to represent the NUMBER of array items passed in <code> char* argv[] </code>. As you may have experienced, You can't calculate the size of an Array passed as a parameter, so you have to send in the size of the array as well.
        </p>


        <p>
            <h4 class="bold">Getting Argv Items</h4>
            Now you can get each item passed from the <code>char* argv[]</code> by indexing like so <code>argv[0]</code>, <code>argv[3]</code> ... ect. <br> <br>

            You can use a For Loop to interate over the array and see all the arguments passed, or you can use them in whatever algorithm you would like. <br><br>


            <code>PS:</code> The arguments passed in <code>char* argv[]</code> are all characters. Make sure to type cast as needed. <br> <br>
            for example: <br>
            <pre>char* x = "12";</pre>
            Type casting <code>x</code> into <code>int</code>:
            <pre> int y = (int) x; </pre>
            Type casting <code>x</code> into <code>int</code>:
            <pre> float z = (float) x; </pre>
            <a href="https://www.geeksforgeeks.org/type-conversion-c/"> How to typecast in C.</a>
        </p>


        <br> <br>

        <h2 class="bold">Complexity Analysis</h2>
        <p>
            Computers use resources (RAM - Ramdom Access Memory) in order to process information that you want it to process.
        </p>

        <h4 class="bold">For example</h4>
        <p>
            When you run a <b>FOR LOOP</b> to count up to 100, you run the same code 100 times them the for loop runs. This might seem insignificant, given that computers are super fast, but when you are dealing with hundreds of request per minute, it can get a bit excessive.
        </p>

        <p>
            <b>Complexity Analysis</b> is a way to measure the steps taken by an algorithm to excecute a program. <br>
        </p>

        <p>
            To measure the steps taken by our algorithm, we will use a methodology called the <b>BIG O Notation</b>. With Big O, we try to calculate the <b>Worst case scenario</b>, and assign a step level to each statement and loop in our algorithm. We can also use <b>BIG OMEGA Notation</b> to calculate the <b>Best case scenario.</b>
        </p>

        <p>
            In the case that BIG O and BIG OMEGA notation are the same complexity, we refer to that as <b>THETA Notation</b>.
        </p>

        <p>
            The Notations assignments are as follows: <br><br>
            ▪ Polynomial – <b>O(n^2)</b>: Runtime grows quicker than previous all based on n.<br>
            ▪ Superlinear – <b>O(n log(n))</b>: Runtime grows in proportion to n.<br>
            ▪ Linear – <b>O(n)</b>: Runtime grows directly in proportion to n.<br>
            ▪ Logarithmic – <b>O(log(n))</b>: Runtime grows logarithmically in proportion to n.<br>
            ▪ Exponential – <b>O(c^n)</b>: Runtime grows even faster than polynomial algorithm based on n.<br>
            ▪ Constant – <b>O(1)</b>: Runtime will always be in the same regardless of the size of the input data set.<br>
        </p>

        <p>
            Please watch the videos in the resources links to see how to assign a level to each step of your algorithm.
        </p>
        <p>
            After assigning a Notation to each step, we can compile them together and calculate the final BIG O notation of the algorithm as a whole.
        </p>
      """,
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vR9Prvp89ENtQRuBAAMDuBlsCEl1EbjlYoEjLGm-FXgLD0m5hnh3Dl7lTJ0pKdXvVEdiG31HGzVc3Yz",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':   [
        {
          'title' : 'Command Line Arguments',
          'id'    : "AI6Ccfno6Pk",
          'time'  : [0,470]
        },
        {
          'title' : 'Complexity Analysis',
          'id'    : "YoZPTyGL2IQ",
          'time'  : [0,754]
        }
      ],
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Command Line Arguments',
          'desc'  : '**Argv and Argc',
          'url'   : 'https://www.youtube.com/watch?v=6Dk8s0F2gow'
        },
        {
          'type'  : 'video',
          'title' : 'Big O Basics',
          'desc'  : 'Big O Notation in 5 minutes',
          'url'   : 'https://www.youtube.com/watch?v=__vX2sjlpXU'
        },
        {
          'type'  : 'video',
          'title' : 'Algorithm Complexity',
          'desc'  : 'Big O Notation',
          'url'   : 'https://www.youtube.com/watch?v=kS_gr2_-ws8'
        },
        {
          'type'  : 'video',
          'title' : 'Hacker Rank',
          'desc'  : 'Big O Notation',
          'url'   : 'https://www.youtube.com/watch?v=v4cd1O4zkGw'
        },
        {
          'type'  : 'link',
          'title' : 'Type casting',
          'desc'  : 'Type conversion of data in C',
          'url'   : 'https://www.w3schools.in/c-tutorial/type-casting/'
        }
      ],
      'activities'  :   [activities['6dj72j28']],
      'published': False
    },
    {
      'title':    "C: Libraries",
      'desc':     """
        <h2 class="bold">Libraries</h2>
        Libraries in any language are files or ONE compiled file that holds many functions that you can use in your program without having to write those functions yourself.<br>
        <br>
        <h3 class="bold">Why is that useful?</h3><br>
        Somethings will ALWAYS be the same, and never really change, like math properties, or how to find the length of a string. So instead of having to write all that logic yourself, you can use a library where another programmer already wrote those for you.<br>
        <br>
        <h3 class="bold">Why create personal libraries ( helpers )</h3><br>
        Just like external libraries, you may have a function that can be used multiple times in a project. when that happens, you may want to put that function in a library and include it at the top of your file whenever you need in it in that file.<br>
        <br>
        Think of them as helpers of functions or code you can group together and use without having your code bloated with too many functions.<br>
        <br>
        You can create your own library of math equations that you will use later.<br>
        Or a library of specific password scrambler and key generator… ect.<br>

      """,
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vTx26R7VRhz-2ozd7a2ygKQr6TVm7iSA94XNK-snT7Dc8BOs96bZ9Uh9GPYYYyGGXURqGr70mvWYVKf",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':  [
        {
          'title' : 'Getting Started with Github',
          'id'    : "MJUJ4wbFm_A",
          'time'  : [0,2304]
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Libraries',
          'desc'  : "Using Libraries in C",
          'url'   : 'https://www.youtube.com/watch?v=JSo85ORXKqQ'
        },
        {
          'type'  : 'link',
          'title' : 'Header Files',
          'desc'  : "Creating your own header file.",
          'url'   : 'https://www.geeksforgeeks.org/write-header-file-c/'
        },
        {
          'type'  : 'link',
          'title' : 'C Libraries',
          'desc'  : "List of Standard C Libraries and headers",
          'url'   : 'https://en.cppreference.com/w/c/header'
        },
        {
          'type'  : 'link',
          'title' : 'More C Libraries and Resources',
          'desc'  : "List of Standard C Libraries and headers",
          'url'   : 'https://www.programiz.com/c-programming/library-function'
        }
      ],
      'activities'  :   [activities['k232kn34']],
      'published': False
    },
    {
      'title':    "Algorithms: Searching",
      'desc':     """
      """,
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vS0bizVVMblWF6UC0PlNn3NJuLciHd6izNwf1QBpwRSf2LIxLTmffMsinFSrJsAccm6fJ_cbcS9g-LY",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [
        {
          'title' : 'Lecture 3 - Searching Algorithms',
          'id'    : "fykrlqbV9wM",
          'time'  : [0,2238]
        },
        {
          'title' : 'Linear Search',
          'id'    : "TwsgCHYmbbA",
          'time'  : [0,168]
        },
        {
          'title' : 'Binary Search',
          'id'    : "T98PIp4omUA",
          'time'  : [0,568]
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Algorithms: Binary Search',
          'desc'  : 'Learn the basics of binary search algorithm',
          'url'   : 'https://www.youtube.com/watch?v=P3YID7liBug'
        },
      ],
      'activities'  :   [activities['h5j30345']],
      'published': False
    },
    {
      'title':    "Algorithms: Sorting",
      'desc':     """
      """,
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vSj2krye8zTj46z7bsnUVu-rB2G2M7ZAX7o3C4wES2gMzD5wxETfPqYaeShDMVuH3fQ4aCMJqH843QG",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [
        {
          'title' : 'Lecture 3 - Sorting Algorithms',
          'id'    : "fykrlqbV9wM",
          'time'  : [2238,5337]
        },
        {
          'title' : 'Lecture 4 - Swapping Values',
          'id'    : "cF6YkH-8vFk",
          'time'  : [4121,4390]
        },
        {
          'title' : 'Selection Sort',
          'id'    : "3hH8kTHFw2A",
          'time'  : [0,239]
        },
        {
          'title' : 'Bubble Sort',
          'id'    : "RT-hUXUWQ2I",
          'time'  : [0,353]
        },
        {
          'title' : 'Insertion Sort',
          'id'    : "O0VbBkUvriI",
          'time'  : [0,284]
        },
        {
          'title' : 'Merge Sort',
          'id'    : "Ns7tGNbtvV4",
          'time'  : [0,626]
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Algorithms: Quick Sort',
          'desc'  : 'Learn the basics of quicksort',
          'url'   : 'https://www.youtube.com/watch?v=SLauY6PpjW4'
        },
      ],
      'activities'  :   [activities['344ij0i5']],
      'published': False
    },
    {
      'title':    "Memory, Pointers & Structs",
      'desc':     """""",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [
        {
          'title' : 'Lecture 4 - Memory',
          'id'    : "cF6YkH-8vFk",
          'time'  : [0,6474]
        },
        {
          'title' : 'Dynamic Memory Allocation',
          'id'    : "xa4ugmMDhiE",
          'time'  : [0,845]
        },
        {
          'title' : 'Memory Leaks, valgrind',
          'id'    : "z4QOYi6FXIo",
          'time'  : [0,128]
        },
        {
          'title' : 'Structures',
          'id'    : "N5pA7RvvQDg",
          'time'  : [0,479]
        }
      ],
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vS97UPH6ItPBfCA8dWqdIjsvMvMDVL0m2cKqZpKWf92OgbSaT1dUdlxn2rdW9DJDBGlJZme2qUQueFC",
        }
      ],
      'recording': "",
      'resources':[
        {
          'title': 'structs-0',
          'type': 'video',
          'desc': "",
          'url': 'https://www.youtube.com/watch?v=yMvRqKmbRm4'
        },
        {
          'title': 'structs-1',
          'type': 'video',
          'desc': "",
          'url': 'https://www.youtube.com/watch?v=hZ2Fy-J8DwQ'
        }
      ],
      'published': False
    },
    {
      'title':    "C: Data Structures (Linked Lists, Queues, Stacks ... )",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vTVlxBXJFQyppD1YY5KRKrmIwGZxOn5KyxV46ebMf8pLHX-FXMPrbM2uO05fM8obUVbjXkrgEImsaLZ",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [
        {
          'title' : 'Lecture 5 - Data Structures',
          'id'    : "4IrUAqYKjIA",
          'time'  : [0,6302]
        },
        {
          'title' : 'Pointers',
          'id'    : "XISnO2YhnsY",
          'time'  : [0,1747]
        },
        {
          'title' : 'Singly-Linked Lists',
          'id'    : "zQI3FyWm144",
          'time'  : [0,1392]
        },
        {
          'title' : 'Doubly-Linked Lists',
          'id'    : "FHMPswJDCvU",
          'time'  : [0,588]
        }
      ],
      'resources':{

      },
      'published': False
    }
  ],
  'Midterm' :   [
    {
      'title':    "Midterm Week",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vTg9GBTa1PUN0rayILyPkWkJNKAFCWKoZLgHVjP7NUyb5DRO-22tpvujJwdP_ZqLFTVKrbIS2lncC83",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'link',
          'title' : 'Review PDF',
          'desc'  : 'Review Document for Quiz 0',
          'url'   : '../static/data/review_0.pdf'
        }
      ],
      'published': False
    },
    {}
  ],
  'Python'  :   [
    {
      'title':    "Python: (Syntax Comparison to C) Data Types, Strings",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQnCUskqzx0vtxZAqF4-VqhdoEaokLb8Kimnic3ygZmWSO0db9JpajSugnFmyl1fX-IJx61D-Z7tsxf",
        }
      ],
      'recording':   "",
      'resources':[],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [
        {
          'title' : 'Lecture 6 - Python',
          'id'    : "fL308_-Kbt0",
          'time'  : [0,2149]
        }
      ],
      'published': False
    },
    {
      'title':    "Python: Lists, Dictionaries and Tuples",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQfgJQOngawB8tQcs-CMQrLAw7PBZVYWl2RJyiEdFOQb7cVpax9gWvTMiqiRJcBn0tRGVVGHk98ulBr",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [
        {
          'title' : 'Lecture 6 - Python',
          'id'    : "fL308_-Kbt0",
          'time'  : [4390,5120]
        }
      ],
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Lists, Dictionaries, tuples',
          'desc'  : 'Basic Overview',
          'url'   : 'https://www.youtube.com/watch?v=R-HLU9Fl5ug'
        },
        {
          'type'  : 'video',
          'title' : 'Lists, Dictionaries, Tuples',
          'desc'  : 'Python for Beginners',
          'url'   : 'https://www.youtube.com/watch?v=W8KRzm-HUcc'
        }
      ],
      'published': False
    },
    {
      'title':    "Python: Methods and Functions",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vSIIv8iozJ1VDSEow1tzFDf7xtWVnvJf22w3abE9nO9XKOHlxfh_LTly2m8xOWFFP91gM4oPxZ9ATt9",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'video',
          'title' : 'Functions',
          'desc'  : 'How to build python functions',
          'url'   : 'https://www.youtube.com/watch?v=9Os0o3wzS_I'
        },
        {
          'type'  : 'video',
          'title' : 'Built in Functions',
          'desc'  : 'How to use Python Functions',
          'url'   : 'https://www.youtube.com/watch?v=7rjJrQy9gi4'
        },
        {
          'type'  : 'video',
          'title' : 'Built in Methods',
          'desc'  : 'How to use Python Methods',
          'url'   : 'https://www.youtube.com/watch?v=fbaSAS9DWZw'
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'  : [
        {
          'title' : 'Lecture 6 - Python',
          'id'    : "fL308_-Kbt0",
          'time'  : [2149,4390]
        }
      ],
      'published': False
    },
    {
      'title':    "Python: Operators, Main and Libraries",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vSihCXcXk-P1BOC28ViIoZRPsle5hczmaX39ndifOArriP934wVBM4GuRRvX2Rg8qWfEEq1F_wLt_p8",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type'  : 'link',
          'title' : 'Python Coding challlenges',
          'desc'  : 'Practice, Practice, Practice',
          'url'   : 'https://codingbat.com/python'
        },
        {
          'type'  : 'Video',
          'title' : '__name__ == __main__',
          'desc'  : 'Python Tutorial: if __name__ == "__main__"',
          'url'   : 'https://www.youtube.com/watch?v=sugvnHA7ElY'
        },
        {
          'type'  : 'video',
          'title' : 'Python TURTLE',
          'desc'  : 'Draw Graphics with the python library turtle',
          'url'   : 'https://www.youtube.com/watch?v=pxKu2pQ7ILo'
        },
        {
          'type'  : 'link',
          'title' : 'Python TURTLE',
          'desc'  : 'Turtle challenges',
          'url'   : 'https://docs.google.com/presentation/d/e/2PACX-1vTzHY5E1FigTXmyd-U-KUR2Zxyj16uZ4ggNzOINcwF5gW9U6OqlBvoE1CoWSZgFrH_UarSV43YIt278/embed'
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard'     :   [
        {
          'title' : 'Lecture 6 - Python',
          'id'    : "fL308_-Kbt0",
          'time'  : [5120,6489]
        }
      ],
      'published': False
    },
    {
      'title':    "Python: Classes, Objects",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQp2rh9JgwUEvWoiqY7TmpEyuM2C2T4XzUvjQ1SR4sgkxLojus6NxP9UZBBPa8RbSI5MQZprzqGk57v",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'title' : 'Python Classes and Obects',
          'desc'  : 'Python OOP Tutorial 1: Classes and Instances',
          'url'   : 'https://www.youtube.com/watch?v=ZDa-Z5JzLYM'
        },
        {
          'title' : 'Python Classes 2',
          'desc'  : 'Python OOP Tutorial: Class Variables',
          'url'   : 'https://www.youtube.com/watch?v=BJ-VvGyQxho'
        },
        {
          'title' : 'Python Classes',
          'desc'  : 'OBJECT-ORIENTED PROGRAMMING IN PYTHON',
          'url'   : 'https://www.youtube.com/watch?v=ECMSnU9ilbQ'
        }
      ],
      'published': False
    },
    {
      'title':    "Python: Inheritance, Abstractions",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vTlnFQf0YGvwoD1srBETTQyGrw6eZUlBwcW9U39NxTHwBPmLmC5dhWredWmEYbL9lnPWfOfVBegXTC8",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'title' : 'Python Class Inheritance',
          'desc'  : 'Python OOP Tutorial: Inheritance - Creating Subclasses',
          'url'   : 'https://www.youtube.com/watch?v=RSl87lqOXDE'
        }
      ],
      'published': False
    },
  ],
  'Front_end':  [
    {
      'title':    "Front End: HTML / Github",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vThWQwKcNvvcwos52xtb8kFwUf3J5zABoXzzeBbZu8iYwOQKz0oFmqdrJfHQhz3yNCw989NekHDUJkn",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':   [
        {
          'title' : 'HTML',
          'id'    : "uEmF74eHRO8",
          'time'  : [1802,3630]
        },
        {
          'title' : '**GITHUB',
          'id'    : "eulnSXkhE7I",
          'time'  : [0,3939]
        }
      ],
      'resources':[
        {
          'type': 'video',
          'title': 'What is GITHUB?',
          'desc': "Let's see how Eddie and his team use GitHub.",
          'url': 'https://www.youtube.com/watch?v=w3jLJU7DT5E'
        },
        {
          'type': 'video',
          'title': 'Learn GITHUB in 20mns',
          'desc': 'Learn how to use Git & Github to share code and collaborate with other developers.',
          'url': 'https://www.youtube.com/watch?v=nhNq2kIvi9s'
        },
        {
          'type': 'link',
          'title': 'GITHUB Steps',
          'desc': 'Steps to use and pushing to Github',
          'url': 'https://docs.google.com/presentation/d/e/2PACX-1vQC0X7Ti8Y6TvZFpIy9lwtZxpeD3h9AFScVBdMUB8htHbdGw9ouYaEGz0HwGe3x3WAcY-xfmE7JHO0S/pub?start=false&loop=false&delayms=3000'
        }
      ],
      'published': False
    },
    {
      'title':    "Front End: CSS",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vSo6WpKlhGX0bbA9EhC6KX-WzHhYvVswo93ePFgp2IisPiVgdOPhPm73W4byYCOu5LpagfTqHP563Ke",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':   [
        {
          'title' : 'HTML',
          'id'    : "uEmF74eHRO8",
          'time'  : [3630, 6318]
        }
      ],
      'resources':[
        {
          'type': 'video',
          'title': 'CSS Tutorial',
          'desc': 'Ultimate CSS tutorial',
          'url': 'https://www.youtube.com/watch?v=yfoY53QXEnI'
        },
        {
          'type': 'link',
          'title': 'Bootstrap',
          'desc': 'Bootstrap Documentation',
          'url': 'https://getbootstrap.com/'
        },
        {
          'type': 'link',
          'title': 'Materialize',
          'desc': 'Materialize Documentation',
          'url': 'https://materializecss.com/'
        },
        {
          'type': 'link',
          'title': 'HOW TO EVERYTHING',
          'desc': 'The BIG List of "HOW TOs"',
          'url': 'https://www.w3schools.com/howto/default.asp'
        }
      ],
      'published': False
    }
  ],
  'MVC1'    :   [
    {
      'title':    "MVC: Flask",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vRzUoWmEYk--3RYwARkTGqQnTBzY5IdzJIhatNy1RZzsrsZfmPpoz-EIwWXZM1IVnUpR1GGKpLitx1T",
        }
      ],
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':   [
        {
          'title' : 'FLASK',
          'id'    : "pP23CtOI-1U",
          'time'  : [2475, 4845]
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type': 'video',
          'title': 'Flask Basics: part 1',
          'desc': 'Flask Controller basics',
          'url': 'https://www.youtube.com/watch?v=MwZwr5Tvyxo'
        }
      ],
      'published': False
    },
    {
      'title':    "MVC: Jinja2",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vTN91SQNPrNhKumWfv6gkekqzD2Mx6Tdaa4vt4Z4dtDaTBqx3Ypwbnqth8S258MTeFCjNYcNt7tnNRj",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':   [
        {
          'title' : 'FLASK',
          'id'    : "pP23CtOI-1U",
          'time'  : [2475, 4845]
        }
      ],
      'resources':[
        {
          'type': 'link',
          'title': 'HTTP REQUESTS and URL Handling',
          'desc': 'Understanding HTTP Requests',
          'url': 'https://docs.google.com/presentation/d/e/2PACX-1vRSCSLrWiQWshZfyL5iKAvqPO7sLXPW6-wO-QOuKeAgRarzlP7jBijjvPas9ck-UcJvSh9cvd05FYC5/pub?start=false&loop=false&delayms=3000'
        },
        {
          'type': 'video',
          'title': 'Flask Basics: part 2',
          'desc': 'Flask Templates',
          'url': 'https://www.youtube.com/watch?v=QnDWIZuWYW0'
        }
      ],
      'published': False
    }
  ],
  'MVC2'    :   [
    {
      'title':    "MVC: SQL",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQnDDYh29mtpgIvRZGhYRIfUAO-Kz5Nt1ZC-Eo7jBR5iWGRfZIBvBQAjfUIXHT82i6lBa-z7i5pTNl7",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':   [
        {
          'title' : 'SQL Overview',
          'id'    : "u5pDdEKnbKA",
          'time'  : [0, 2325]
        },
        {
          'title' : 'SQL and Graphical Interface',
          'id'    : "LxDetsPQAPQ",
          'time'  : [1747, 4374]
        }
      ],
      'resources':[
        {
          'type': 'link',
          'title': 'W3 School SQL tool',
          'desc': 'Practice SQL with W3 Schools SQL tool',
          'url': 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_op_in'
        },
        {
          'type': 'video',
          'title': 'IMPORTANT :: Flask Basics: part 4',
          'desc': 'SQL and Databases',
          'url': 'https://www.youtube.com/watch?v=cYWiDiIUxQc'
        }
      ],
      'published': False
    },
    {
      'title':    "MVC: CS50 SQL Library",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vRw9ITcyFBf_gC4vm2-bmcmMzdQEMlj8BFSxhSHKLM8FKA9teh8DU6bv6NpS3kOUlid9SQimCgYD3mL",
        }
      ],
      'recording':   "",
      'harvard_link': 'https://cs50.harvard.edu/college/2020/spring/weeks/0/',
      'harvard':   [
        {
          'title' : 'How to use CS50 SQL',
          'id'    : "LxDetsPQAPQ",
          'time'  : [4374, 6859]
        }
      ],
      'resources':[
        {
          'type': 'video',
          'title': 'IMPORTANT :: Flask Basics: part 3',
          'desc': 'Form Validation',
          'url': 'https://www.youtube.com/watch?v=UIJKdCIEXUQ'
        }
      ],
      'published': False
    }
  ],
  'Final'   :   [
    {
      'title':    "Final Week",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vSgq5_zCPFe5aaLBgOltujqv68y2DWXVpLdDOSODrioa1oJPwnPly8ipckso-RVBQwdQRH5liMjZUEp",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    },
    {
      'title':    "Building and App :: Planning",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vRsKgTPyiqHJCMvDNZv9LG2SA_Y59mmCE_rX9Ya2l8l4eWSuB79EHkzB5U1gP8F72Az1yNUp8nr697D",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    }
  ],
  'Full_app':   [
    {
      'title':    "APP: Designing and Planning",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    },
    {
      'title':    "App: Coordinating",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type': 'video',
          'title': 'Flask Basics: part 3',
          'desc': 'Form Validation',
          'url': 'https://www.youtube.com/watch?v=CSHx6eCkmv0'
        }
      ],
      'published': False
    }
  ],
  'Javascript': [
    {
      'title':    "Javacript: Intro",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vRuAODXHJdF1sTjJ0MgkiNzQ0FWYTzUUB_vurn_-2xcJir8keBI20LibT4EAfonwPlItXOmkcw06rPq",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type': 'video',
          'title': 'Vanilla JS',
          'desc':   'Learn vanilla JS in about 10 minutes',
          'url':    'https://www.youtube.com/watch?v=IQn_up6ZUkk'
        },
        {
          'type': 'video',
          'title': 'jQuery Tutorial #1',
          'desc': 'jQuery Tutorial for Beginners',
          'url': 'https://www.youtube.com/watch?v=hMxGhHNOkCU'
        }
      ],
      'published': False
    },
    {
      'title':    "Javacript: Ajax",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vRaNon1h8M8z1wUqx4fIfwLnLY01RSFPkzeguLgt5EvfC6xWhhsK4AtEI-ZfJnauGb24q1VeJ_-ry6i",
        }
      ],
      'recording':   "",
      'resources':[
        {
          'type': 'video',
          'title': 'jQuery/Ajax Tutorial',
          'desc': "Using AJAX & API's (jQuery Tutorial #7)",
          'url': 'https://www.youtube.com/watch?v=fEYx8dQr_cQ'
        }
      ],
      'published': False
    }
  ],
  'Github'  :   [
    {
      'title':    "Github: Basics",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQC0X7Ti8Y6TvZFpIy9lwtZxpeD3h9AFScVBdMUB8htHbdGw9ouYaEGz0HwGe3x3WAcY-xfmE7JHO0S",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    },
    {
      'title':    "Github: Collaborating",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "2PACX-1vQC0X7Ti8Y6TvZFpIy9lwtZxpeD3h9AFScVBdMUB8htHbdGw9ouYaEGz0HwGe3x3WAcY-xfmE7JHO0S",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    }
  ],
  'Bootstrap':  [
    {
      'title':    "Bootstrap / Get UI KIT",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    },
    {
      'title':    "Where to get assets",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    }
  ],
  'Last_week':  [
    {
      'title':    "Hack-a-thon",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    },
    {
      'title':    "Project Presentation",
      'desc':     """""",
      'ppts' : [
        {
          'title'   : "",
          'code': "",
        }
      ],
      'recording':   "",
      'resources':[],
      'published': False
    }
  ],
}