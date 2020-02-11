activities = {
    "2a8a3r2c0"  :   {
        'id'        : '2a8a3r2c0',
        'title'     : 'We the Machines',
        'preview'   : "Can you communicate effectively as a team? Let's find out. ",
        'desc'  :    """
                        Use the following, to generate a radom task.
                        <h4 class="bold" class='bold'>
                            Random Task Generator:
                            <a href='/tools/random_task'> click here </a>
                        </h4>
                    """,
        'published' : True
    },
    "7g4k9c0o8"  :   {
        'id'        : '7g4k9c0o8',
        'title'     : 'Spy ypS Spy',
        'preview'   : "Binary is an ancient, lost forgoten language. Can you decode the secret message?",
        'desc'      : """
                        Binary is an ancient, lost forgoten language.<br>
                        That's why some deep underground gang of coders still use it to transfer hidden messages. <br>
                        <br>
                        <br>
                        <center>
                        <h3 class="bold"> Your mission should you choose to accept it:</h3>
                        You possess a rare skill to decypher the ancient circuitry<br>
                        Can you decode the secret message?
                        <br> <br>
                        <div id="error_message" style="color: red !important;"></div>
                        <br>
                        <div class="phase_1">
                            <h4 class="bold">Phase 1:</h4>
                            You must enter the password:<br>
                            <div id="password"></div><br>
                            <div class="uk-margin" style="max-width: 400px; margin: 5px auto;">
                                <input class="uk-input" type="text" id="thePassword" placeholder="Type password here">
                            </div> 
                            <button class="uk-button uk-button-primary submit_password"> submit password </button><br>
                        </div>
                        <div class="phase_2" style="display: none;">
                            <h4 class="bold">Phase 2:</h4>
                            WELL DONE!!! You are the nerds we're looking for! <br>
                            You will do well to decode our secret message. BUT, we had to kick it up a notch. <br>
                            Below are some legends to help you decypher the BINARY message.
                            <br><br>
                            Secret coded decypher thingy : 
                            <a href="/static/assets/activities/spy/Ascii_table.pdf" target="_blank"> Click Here </a>
                            <br><br><br>
                            <div class="row" style="max-width: 1000px; margin: auto;">
                                <div class="col-12 col-sm-5" style="text-align: left !important;">
                                    <div class="uk-margin">
                                        <textarea class="uk-textarea" rows="5" id="theCode" placeholder="Type the code here"></textarea><br>
                                    </div>
                                    <button class="uk-button uk-button-primary submit_thecode"> Submit Secret Code </button>
                                </div>
                                <div class="col-12 col-sm-7"><div class="the_secret_image"></div></div>
                            </div>
                        </div>
                        <div class="phase_3" style="display: none;">
                            <h1 class="bold">CONGRATULATIONS!!!!!!!</h1>
                            <h3 class="bold">You've decoded the message</h3>
                            <br>
                            <div class="message"></div>
                            <hr>
                            <img src="https://media.giphy.com/media/xTiTnEHBh7qapyuvwQ/giphy.gif" width="400px">
                            <br><br>
                            NOW HURRY! You want to be the first ones to deliver the message and CLAIM your prize!
                            <br>
                            If you're not, it's ok, you'll still win something.
                            <br><br>
                            BE SURE TO SHOW YOUR WORK.
                        </div>            
                        </center>
                    """,
        'published' : True
    },
    "2n4n5f0s0"  :   {
        'id'        : '2n4n5f0s0',
        'title'     : 'PSEUDOCODING',
        'preview'   : "Let's write code in english",
        'desc'      : """
                        Pseudo code is a term which is often used in programming and algorithm based fields. <br>
                        It is a methodology that allows the programmer to represent the implementation of an algorithm.<br>
                        Simply, we can say that it’s the cooked up representation of an algorithm. Often at times, algorithms are
                        represented with the help of pseudo codes as they can be interpreted by programmers no matter what
                        their programming background or knowledge is. <br>
                        Pseudo code, as the name suggests, is a false code or a representation of code which can be understood
                        by even a layman with some school level programming knowledge.
                        <br>
                        <h4 class="bold">EXAMPLES:</h4>

                        <div class="row">
                            <div class="col-sm-6">
                                <h5 class="bold">Steet Light</h5>
    <pre>
        SET VARIABLE light as the STRING 'Red'
        
        IF light is 'Green'
            MOVE FORWARD
        ELSE IF light is 'Yellow'
            SLOW DOWN
        ELSE IF light is 'Red'
            STOP
    </pre>
                            </div>
                            <div class="col-sm-6">
                                <h5 class="bold">Weather</h5>
    <pre>
        SET VARIABLE temperature as the STRING 'Cold'
        SET VARIABLE weather as the STRING 'Rainy'
        
        IF temperature is 'Hot'
            Leave Sweater Home
        ELSE IF temperature is 'Cold'
            Take Sweater
        ELSE
            Wear a nice sundress
    
        Check the weather
    
        IF weather is 'Rainy'
            Take Umbrella
        ELSE
            Leave Umbrella Home
    </pre>                    
                            </div>
                        </div>
                        <h4>
                            Below are 2 types of tasks. One life task, one coding task. <br>
                            Choose one of each task and write simple pseudo code to accomplish each task. <br>
                            The PSEUDOCODE should be simple and straight to the point.
                        </h4>
                        <br>


                        <hr>
                        <h2 class="bold"><u>Life Tasks:</u></h2><br>

                        <h4 class="bold">1- Grilled Cheese Sandwich.</h4>
                        <p>Write pseudocode on how to make a grilled cheese sandwich.</p>
                        <p>You can choose to put whatever you want in the sandwich.</p>
                        <p>Also, think about how long the bread needs to stay on the pan, what color to look for and when to flip it.</p>
                        <p>Good luck, I hope it's delicious.</p>
                        
                        <br><br>
                        <h4 class="bold">2- Cheesy Mac.</h4>
                        <p>Yes... I love cheese.</p>
                        <p>Write pseudocode on how to make a a simple mac and cheese.</p>
                        <p>You can choose to put whatever you want in there.</p>
                        <p>The idea is to not let it burn, or come out too lumpy</p>
                        
                        <br><br>
                        <h4 class="bold">3- Fill the Tanks:</h4>
                        <p>There are 4 cars parked in a gas station parking lot.</p>
                        <p>Write pseudocode to bring each car to the pump and fill them up until it's full.</p>
                        <p>Think about moving the car to the pump, and then moving it back to the parkign space.</p> 
                        <p class="bold">To make it extra fun, 2 of the cars are half full, one is quarter full and one is empty.</p>
                        
                        <br><br>
                        <h4 class="bold">4- Morning routine based time and weather.</h4>
                        <p>Write pseudocode for a simple morning routine.</p>
                        <p>Think about how many tasks you have to do and what steps you need to do in each task</p>
                        <p>Don't make it too complicated, just simple enough to get out the door.</p>
                        <p>Maybe find the group doing the grilled cheese sandwich and use their function? &#128521;</p>
                        
                        <hr>
                        <h2 class="bold"><u>Practical Coding Tasks:</u></h2><br>

                        <h4 class="bold">1- Guess the password.</h4>
                        <p>Write a pseudocode for a developer to figure ot the logic of a password tool</p>
                        <p>Think about getting the input from a user and saving it in a variable</p>
                        <p>Think about what you need to do everytime they input the password and what needs to happen next.</p>
                        
                        <br>
                        <h4 class="bold">2- Simple Loop.</h4>
                        <p>Write pseudo code to print all multiples of 5 between 1 and 100 (including both 1 and 100)</p>
                        <p>Let's use a FOR or loop in this PSEUDO and not repeat the same code 20 times 👀</p>
                        
                        <br>
                        <h4 class="bold">3- Sorting.</h4>
                        <p>Write pseudo code that takes 10 unique, random numbers and writes them all in sorted order.</p>
                        <p>Think about how you want to store each number and what you will compare thet number to in order to figure out where it goes.</p>
                        <p>At the end of the Pseudocode, the 10 numbers should be sorted from smallest to highest.</p>
                    """,
        'published' : True
    },
    "7g8h0m8j2"  :   {
        'id'        : '7g8h0m8j2',
        'title'     : 'LET THERE BE FILES',
        'preview'   : "In this activity, you will be creating a file structure and manipulating files and directories.",
        'desc'      : """
                    <h3>Let's create some files and mess with them</h3>
                    <p>In this excercise you will be creating a file structure and manupulate some files in there.</p>
                    <h4 class="bold">First, lets create folder ( directory ) called <code>myFirstApp</code></h4>
                    <p>In <code>myFirstApp</code>, let's create the following file structure.</p>
                    <pre>Hint: You are able to create multiple files or folders with one 'mkdir' command.</pre>
                    <p>PS: You are not allowed to use the UI until specifically asked to do so... I will be able to tell.</p>
                    <h3 class="bold">File Structure</h3>
                    <img src="/static/assets/activities/terminal/files.png" style="max-width: 400px; border: 2px dashed #000;">
                    <hr>
                    <h3 class="bold">Let the fun begin</h3>
                    <br>
                    <h4 class="bold">Creating files:</h4>
                    <p>
                        Navigate to the <code>assets</code> folder and create 3 <code>directories</code>:<br>
                        <ul>
                            <li>images</li>
                            <li>styles</li>
                            <li>javascript</li>
                        </ul>
                    </p>

                    <h4 class="bold">Moving files:</h4>
                    <p>
                        Move all the files with the extension <code>.css</code> into the <code>styles</code> folder. <br>
                        Move all the files with the extension <code>.js</code> into the <code>javascript</code> folder. <br>
                        <pre>Hint: You can move all the files with the same extension by using the (*) wildcard.</pre>
                        <pre>example: You can move all items with a '.png' extension by using '*.png'</pre>
                    </p>

                    <h4 class="bold">Renaming files:</h4>
                    <p>
                        In your <code>templates</code> folder, let's rename the following files.<br>
                        <ul>
                            <li>Rename <code>index.html</code> to <code>home.html</code></li>
                            <li>Rename <code>gallery.html</code> to <code>media.html</code></li>
                        </ul>
                    </p>

                    <h4 class="bold">Creating more files:</h4>
                    <p>
                        In the <code>root</code> folder off your app, create a folder called <code>temp</code>.<br>
                        Using the UI and your browser, find 4 images of cats and drag them to the <code>/temp</code> folder. <br>
                    </p>

                    <h4 class="bold">Moving more files:</h4>
                    <p>
                        While STILL in the <code>/temp</code> folder... (do not change directory).
                        Move the <code>notes.txt</code> file in <code>/temp</code> folder.<br>
                        Display a list of the contents of the <code>/temp</code> folder. <br>
                        Move the all the images into the <code>/assets/images</code> folder.<br>
                    </p>

                    <h4 class="bold">Displaying and Writing:</h4>
                    Almost Done.
                    <p>
                        While STILL in the <code>/temp</code> folder... (do not change directory). <br>
                        Display a list of the contents of the <code>/templates</code> folder. <br>
                        <h5 class="bold">Bonus:</h5>
                        Find out how to <code>add lines of code in a text file</code> from the terminal. <br>
                        Copy the name of EACH file in the <code>/templates</code> folder, and add it as a new line in the <code>notes.txt</code> file.
                        <pre>If I open the notes.txt file, I should the names of each file in the /templates on a new line.</pre>
                    </p>

                    <h4 class="bold">SHOW ME then Delete:</h4>
                    Now... come show me so that I can make sure you did everything. <br>
                    Then you can delete your <code>/temp</code> folder.
                    """,
        'published' : True
    },
    "y48203j0"  :   {
        'id'        : 'y48203j0',
        'title'     : "Let's Write some programs",
        'preview'   : "In this activity, you will practice writing some simple programs.",
        'desc'      : """
                    <h2 class="bold">Guessing game</h2>
                    <p>
                        Write a simple program in C that asks the user to guess a number. <br>
                        Think about how you will store the number they need to guess <br>
                        After they entered the number it, if they guessed it, print "HOORRAY!" <br>
                        If they did not guess it, print "Try Again". <br> <br>
                        You do not need to include a loop in this. Once they guess it and you print the result we can run the program again. <br>
                    </p> <br>
                    <hr>
                    <h2 class="bold">Simple Convo</h2>
                    <p>
                        Write a simple program that has a simple convo with the user.<br>
                        First, ask their name. <br>
                        Then print a response to the user's name like. "Hi there Bob." <br>
                        Then ask another follow-up question and answer that question in your program. <br>
                        You can ask up to 3 to 5 questions. <br>
                        <h4 class="bold">Bonus:</h4>
                        As a bonus to this task, you can ask a question and based on their answer, give a specific answer. <br><br>
                        <a href="https://www.programiz.com/c-programming/library-function/string.h/strcmp">How to compare 2 strings</a>
                    </p><br>
                    <hr>
                    <h2 class="bold">Calculator game</h2>
                    <p>
                        Write a simple program that asks the user to enter 2 numbers.<br>
                        After the user enters the 2 numbers. in your program perform a mathematical calculation and print the result.<br>
                        <h4 class="bold">Bonus:</h4>
                        As a bonus to this task, You can give the user some options as to what mathematical operation they would like to perform. <br> <br>
                        For example, You can ask them to type in one of the following operations "addition, subtraction, multiplication, division" <br>
                        <code>hint: tell them when they can write</code> <br>
                        An based on what they chose, use an if else to choose what operation to run.<br><br>
                        <a href="https://www.programiz.com/c-programming/library-function/string.h/strcmp">How to compare 2 strings</a>
                    </p><br>
                    <hr>
                    <h2 class="bold">Is this a 2 digit number?</h2>
                    <p>
                        Ask the user for a number. If the number is a 2 digit number between 10 and 99, print <code>“The number you entered is a 2 digit number”</code> else print out <code>“The number you entered is not a 2 digit number”</code>.<br>
                        <h4 class="bold">Bonus:</h4>
                        As a bonus to this task, use a chain of if/ifelse/else statements to print out if the number is a 1, 2, 3 or 4 digit number. <br>
                        Print out the output: <code>“The number you entered is {x} digits.”</code> <br>
                    </p>
                    """,
        'published' : True
    },
    "6a82js91"  :   {
        'id'        : '6a82js91',
        'title'     : "Let's Write Better programs",
        'preview'   : "In this activity, you will putting into practice some of the same concepts as last time, but this time using loops to make it more interesting.",
        'desc'      : """
                    <h2 class="bold">Password</h2>
                    <p>
                        Write a simple program that asks the user to enter a password.<br>
                        When they enter a wrong password, print that that they entered a wrong password and ask them to try again.<br>
                        When they enter the RIGHT password, print "ACCESS GRANTED!". <br>
                        Use a loop to keep asking them to guess the password until they get it right.<br><br>
                        Think about wether you would use a While or a DO WHILE Loop and why.<br><br>
                        <a href="https://www.programiz.com/c-programming/library-function/string.h/strcmp">How to compare 2 strings</a>
                    </p> <br>

                    <hr>

                    <h2 class="bold">For Names</h2>
                    <p>
                        Create an empty array that will be accepting names.<br>
                        Using a for loop of up to 4 times, ask the user to enter a name.<br>
                        Ideally the user should enter 4 names, one after the other, 4 times.<br>
                        Once they are done entering the names, using ANOTHER for loop. Go through the list of names and print each of them out with a greeting so that the output looks something like this.<br>
                        <pre>Good Morning Bob</pre>
                        <pre>Good Morning James</pre>
                        <pre>Good Morning Marie</pre>
                        <pre>Good Morning Sarah</pre>
                        After the greeting loop is over. Print out that it was nice to meet them.
                    </p> <br>

                    <hr>

                    <h2 class="bold">Guessing Game +</h2>
                    <p>
                        Using a WHILE or DO WHILE loop, write a program that asks the user to guess a number.<br>
                        Everytime the user guesses a wrong number, tell them if they should guess higher or lower next.<br>
                        You should not stop the loop until they guess the number.<br>
                        Once they find the number, print "HOORRAY!! You guessed it."
                    </p>
                    <h3 class="bold">Bonus Mode (put the pressure):</h3>
                    <p>
                        Let's improve on your Number Guessing Game.<br>
                        We can keep the same concept as above, but this time, add a limit to the numbers of guesses the user can guess. <br><br>
                        For example, everytime the user guesses, tell them how many guesses they have left.<br>
                        <pre>You have 4 guesses left.</pre>
                        <pre>You have 3 guesses left.</pre>
                        <pre>You have 2 guesses left.</pre>
                        ...
                        Once the number of guesses thy reach is zero <code>0</code>, Break out of the loop and tell them they have failed.<br><br>
                        <a href="https://www.programiz.com/c-programming/c-break-continue-statement">How to break out of a loop in c</a>
                    </p>
                    <h3 class="bold">Wizard Mode (warmer / colder):</h3>
                    <p>
                        Implement a way to tell them is they are getting Warmer of Colder.<br>
                        You will have to do some math here. Think about how you would figure out if they are getting warmer or colder.<br>
                        <code>Warmer:  Based on the number to guess, you are getting closer compared to the LAST number you guessed.</code><br>
                        <code>Colder:  Based on the number to guess, you are getting further away compared to the LAST number you guessed.</code><br><br>
                        Think of the number you are trying to guess as a center point.<br>
                        For example, if the number to guess is <code>10</code> and the last number I guessed was <code>6</code> and now I guess <code>1</code>, then I'm getting colder.<br>
                        But if I guess <code>8</code> then I'm getting warmer because <code>8</code> is between <code>6</code> and <code>10</code>.
                    </p>
                    <h3 class="bold">Mind Blown Mode (look at your mistakes):</h3>
                    <p>
                        After they've guessed using all their chances from Bonus mode. If they still got it wrong. Print out all their guesses back to them in the console.<br>
                        Think about how you would save all the gueses so that you can show it back to them later.
                    </p><br>
                    """,
        'published' : False
    }
}

def spydecoder( level, code ):
    failed = [ False, "SORRY TRY AGAIN" ]
    
    if level == '1':
        if code in ["PassWord", "bazinga"]:
            return  [ True, "2" ]
        if code in ["PizzA", "RedRum"]:
            return  [ True, "1" ]
        if code in ["maRio", "QWERTY"]:
            return  [ True, "3" ]
        return failed
    
    if level == '2':
        messages = [
            "The cake is a LIE!",
            "To above and Cs50",
            "Whoa I know kung fu!!"
        ]
        message = messages[ int(code.split('+')[0])-1 ]

        if code.split('+')[1] == message:
            return [ True, message ]
        return failed
    
    return failed