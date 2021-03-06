challenges = {
	"random_task":	{
		'title'	: "Task Generator",
		'desc'	: """
			Use the following, to generate a radom task.
			<h4 class="bold" class='bold'>
				Random Task Generator:
				<a href='/tools/random_task'> click here </a>
			</h4>
		""",
		'solution': {}
	},
	"binary_password": {
		'title': "Binary Spy",
		'desc': """
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
		'solution': {}
	},
	"grilled_cheese":	{
		'title'	: "Life Task: Grilled Cheese Sandwich",
		'desc'	: """
			<p>Write pseudocode on how to make a grilled cheese sandwich.</p>
			<p>You can choose to put whatever you want in the sandwich.</p>
			<p>Also, think about how long the bread needs to stay on the pan, what color to look for and when to flip it.</p>
			<p>Good luck, I hope it's delicious.</p>
		""",
		'solution': {}
	},
	"cheesy_mac":	{
		'title'	: "Life Task: Cheesy Mac",
		'desc'	: """
			<p>Yes... I love cheese.</p>
			<p>Write pseudocode on how to make a a simple mac and cheese.</p>
			<p>You can choose to put whatever you want in there.</p>
			<p>The idea is to not let it burn, or come out too lumpy</p>
		""",
		'solution': {}
	},
	"gas_tanks":	{
		'title'	: "Life Task: Fill the Tanks",
		'desc'	: """
			<p>There are 4 cars parked in a gas station parking lot.</p>
			<p>Write pseudocode to bring each car to the pump and fill them up until it's full.</p>
			<p>Think about moving the car to the pump, and then moving it back to the parkign space.</p>
			<p class="bold">To make it extra fun, 2 of the cars are half full, one is quarter full and one is empty.</p>
		""",
		'solution': {}
	},
	"morning_weather":	{
		'title'	: "Life Task: Morning routine based time and weather.",
		'desc'	: """
			<p>Write pseudocode for a simple morning routine.</p>
			<p>Think about how many tasks you have to do and what steps you need to do in each task</p>
			<p>Don't make it too complicated, just simple enough to get out the door.</p>
			<p>Maybe find the group doing the grilled cheese sandwich and use their function? &#128521;</p>
		""",
		'solution': {}
	},
	"password_pseudo":	{
		'title'	: "Coding Tasks: Guess the Password",
		'desc'	: """
			<p>Write a pseudocode for a developer to figure ot the logic of a password tool</p>
			<p>Think about getting the input from a user and saving it in a variable</p>
			<p>Think about what you need to do everytime they input the password and what needs to happen next.</p>
		""",
		'solution': {}
	},
	"loop_pseudo":	{
		'title'	: "Coding Tasks: Simple loop",
		'desc'	: """
			<p>Write pseudo code to print all multiples of 5 between 1 and 100 (including both 1 and 100)</p>
			<p>Let's use a FOR or loop in this PSEUDO and not repeat the same code 20 times 👀</p>
		""",
		'solution': {}
	},
	"sorting_pseudo":	{
		'title'	: "Coding Tasks: Sorting",
		'desc'	: """
			<p>Write pseudo code that takes 10 unique, random numbers and writes them all in sorted order.</p>
			<p>Think about how you want to store each number and what you will compare thet number to in order to figure out where it goes.</p>
			<p>At the end of the Pseudocode, the 10 numbers should be sorted from smallest to highest.</p>
		""",
		'solution': {}
	},
	"simple_convo":	{
		'title'	: "Simple Convo",
		'desc'	: """
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
		""",
		'solution': {}
	},
	"guessing_game":	{
		'title'	: "Guessing game",
		'desc'	: """
			<p>
				Write a simple program in C that asks the user to guess a number. <br>
				Think about how you will store the number they need to guess <br>
				After they entered the number it, if they guessed it, print "HOORRAY!" <br>
				If they did not guess it, print "Try Again". <br> <br>
				You do not need to include a loop in this. Once they guess it and you print the result we can run the program again. <br>
			</p>
		""",
		'solution': {}
	},
	"calculator_game":	{
		'title'	: "Calculator game",
		'desc'	: """
			<p>
				Write a simple program that asks the user to enter 2 numbers.<br>
				After the user enters the 2 numbers. in your program perform a mathematical calculation and print the result.<br>
				<h4 class="bold">Bonus:</h4>
				As a bonus to this task, You can give the user some options as to what mathematical operation they would like to perform. <br> <br>
				For example, You can ask them to type in one of the following operations "addition, subtraction, multiplication, division" <br>
				<code>hint: tell them what they can write</code> <br>
				An based on what they chose, use an if else to choose what operation to run.<br><br>
				<a href="https://www.programiz.com/c-programming/library-function/string.h/strcmp">How to compare 2 strings</a>
			</p><br>
		""",
		'solution': {}
	},
	"two_digit":	{
		'title'	: "Is this a 2 digit number?",
		'desc'	: """
			<p>
				Ask the user for a number. If the number is a 2 digit number between 10 and 99, print <code>“The number you entered is a 2 digit number”</code> else print out <code>“The number you entered is not a 2 digit number”</code>.<br>
				<h4 class="bold">Bonus:</h4>
				As a bonus to this task, use a chain of if/ifelse/else statements to print out if the number is a 1, 2, 3 or 4 digit number. <br>
				Print out the output: <code>“The number you entered is {x} digits.”</code> <br>
			</p>
		""",
		'solution': {}
	},
	"simple_loop":	{
		'title'	: "Simple Loop",
		'desc'	: """
			<p>
				Write a simple program that asks a user to input a number and use a for loop to count from <code>0</code> to that number.
			</p><br>
		""",
		'solution': {
			'title'	: 'Simple loop 1',
			'video_host'	: 'loom',
			'video_url'	: 'ec398b8e9c364d27892ccefd443dc554',
			'url'		:	''
		}
	},
	"simple_loop_2":	{
		'title'	: "Simple Loop 2",
		'desc'	: """
		<p>
			Write a simple program that asks a user to input a number and counts with steps. <br>
			So... First, you ask the user to input a <code>number</code>. <br>
			Then, you ask them to input another number that you will use as a <code>step</code>.<br>
			Now, you will use a for loop to count from <code>0</code> to that number, but instead of counting by one digit, count by the <code>step</code> number. <br><br>
			Example:<br>
			If the <code>number</code> is <code>10</code> and the <code>step</code> is <code>2</code>, the output will look like this:<br>
			<div class="codeBlock">
				<code>0</code>
				<code>2</code>
				<code>4</code>
				<code>6</code>
				<code>8</code>
				<code>10</code>
			</div>
		</p> <br>
		""",
		'solution': {
			'title'	: 'Simple loop 2',
			'video_host'	: 'loom',
			'video_url'	: 'f79a8181fcb94842afb8248c049d47d2',
			'code'		:	'https://www.codepile.net/raw/dmGn9oPG.cpp'
		}
	},
	"password":	{
		'title'	: "Password",
		'desc'	: """
			<p>
				Write a simple program that asks the user to enter a password.<br>
				When they enter a wrong password, print that that they entered a wrong password and ask them to try again.<br>
				When they enter the RIGHT password, print "ACCESS GRANTED!". <br>
				Use a loop to keep asking them to guess the password until they get it right.<br><br>
				Think about wether you would use a While or a DO WHILE Loop and why.<br><br>
				Now, in C, you can't just compare 2 strings just like you can compare 2 numbers with the <code>==</code> operator. <br>
				Click here to find out <a href="https://www.programiz.com/c-programming/library-function/string.h/strcmp">how to compare 2 strings</a>.
			</p> <br>
		""",
		'solution': {
			'title'	: 'Password',
			'video_host'	: 'loom',
			'video_url'	: '48b65271fd914c1a9a4ccaa7be56238b',
			'code'		:	'https://www.codepile.net/raw/rqraYYLJ.cpp'
		}
	},
	"for_names":	{
		'title'	: "For Names",
		'desc'	: """
			<p>
				Create an empty array that will be accepting names.<br>
				Using a for loop of up to 4 times, ask the user to enter a name.<br>
				Ideally the user should enter 4 names, one after the other, 4 times.<br>
				Once they are done entering the names, using ANOTHER for loop. Go through the list of names and print each of them out with a greeting so that the output looks something like this.<br>
				<code>Good Morning Bob</code>
				<code>Good Morning James</code>
				<code>Good Morning Marie</code>
				<code>Good Morning Sarah</code>
				After the greeting loop is over. Print out that it was nice to meet them.
			</p> <br>
		""",
		'solution': {}
	},
	"guessing_game":	{
		'title'	: "Guessing Game +",
		'desc'	: """
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
		'solution': {}
	},
	"function_refactoring":	{
		'title'	: "Refactoring into functions",
		'desc'	: """
			<h2 class="bold"></h2>
			Let's revisit our <a href="/activity/y48203j0">Calculator Game</a> and refactor the calculations in fucntions we can use in other places. <br> <br>
			We will use the boiler plate below in order to refactor our calculations into calculating functions and call them when we need them. <br> <br>
			<b>First</b>, Above the main function, we will write each function and declare what parameters they will need to be passed.<br> <br>
			<b>Second</b>, we'll decide if the functions are Fruitful or Non-fruitful functions.<br>
			<a href="/lecture/7"> Data vs Void functions.</a><br><br>
			<b>Then</b> we will write our Program in the Main function to ask the user for the numbers and the operation they would like to run. <br><br>
			<b>Finally</b> with an IF / ELSE statement, we will call the appropriate function based on the user's input. <br><br>
			Below is a starting point to this Program, complete each function to do what it's supposed to do and the IF / ELSE statement below.
			<div class="codeBlock">
				<code>// Include the correct libraries</code>
				<code>   </code>
				<code>int add( ){ ... }</code>
				<code>int substract( ){ ... }</code>
				<code>int divide( ){ ... }</code>
				<code>int multiply( ){ ... }</code>
				<code>   </code>
				<code>int main( void ){</code>
				<code>	// Ask the user for the numbers</code>
				<code>	int num1 = get_int("number 1:");</code>
				<code>	int num2 = get_int("number 2:");</code>
				<code>   </code>
				<code>	// Ask the user for the operation they would like to run.</code>
				<code>	string operation = get_string("operation:");</code>
				<code>	</code>
				<code>	// Write the IF ELSE statement that calls the right function based on the user's input</code>
				<code>}</code>
			</div>
		""",
		'solution': {
			'title'	: 'Function Refactoring',
			'video_host'	: 'loom',
			'video_url'	: '2b610ec80b494353a235666da565b730',
			'code'		:	'https://www.codepile.net/raw/nD9Gmr3W.cpp'
		}
	},
	"hello_world":	{
		'title'	: "Hello World",
		'desc'	: """
			<p>
				Let's start small. Let's create an app that takes One command line argument and make it say "Hello".<br>
				The command line argument will be a name.<br><br>
				when is it excecuted like so:<br>
				<code>./app Bob</code><br>
				It should print out:<br>
				<code>Hello Bob, How are you?</code><br>
			</p>
		""",
		'solution': {}
	},
	"add_2_numbers":	{
		'title'	: "Add 2 numbers",
		'desc'	: """
			<h2 class="bold"></h2>
			<p>
				Now, Let's create an app that takes TWO command line arguments and adds them together.<br>
				The command line argument will be 2 numbers.<br><br>
				when is it excecuted like so:<br>
				<code>./app 10 50</code><br>
				It should print out:<br>
				<code>60</code><br><br>
				To Convert a string into an integer in C, you need to use the <code>atoi()</code> function from the <code>stdlib.h</code> Library<br><br>
				<a href="https://www.tutorialspoint.com/c_standard_library/c_function_atoi.htm"> Converting string to int in C using <code>atoi( ... )</code>.</a><br><br>
			</p>
		""",
		'solution': {}
	},
	"refactoring_cla":	{
		'title'	: "Refactoring to Command Line Arguments",
		'desc'	: """
			<p>
				Let's create a new file and revisit our <a href="/activity/5h23kw23">Calculator Game Refactor</a> from last activity and refactor yet again, in order to use the command line arguments. <br> <br>
				The goal is to pass in the numbers and the operation right when you call to tun the app. <br>
			</p>
			<p>
				<h3 class="bold">What you had before</h3>
				<div class="codeBlock">
					<code>./app</code>
					<code>Number 1: 10</code>
					<code>Number 2: 20</code>
					<code>multiply</code>
					<code>Your result is 200</code>
				</div>
			</p>
			<p>
				<h3 class="bold">What you should have now:</h3>
				<code>./app multiply 10 20</code><br>
				<code>Your result is 200</code><br>
			</p>
			<p>
				<b>First</b>, Let's remove the <code>void</code> parameter from the main function and replace it with the arguments we learned in class.<br> <br>
				<b>Second</b>, We can now remove the <code>get_int(...)</code> and <code>get_string(...)</code> functions to ask user input.<br>
				Instead, we will use <code>argv</code> and get the right position of the arguements we passed by indexing it at the right place<br>
				<b>Finally</b> Make sure to properly Type Cast the data you are passed in order to perform operations on the numbers passed as arguments. Remember, they come in as strings. <br><br>
				To Convert a string into an integer in C, you need to use the <code>atoi()</code> function from the <code>stdlib.h</code> Library<br><br>
				<a href="https://www.tutorialspoint.com/c_standard_library/c_function_atoi.htm"> Converting string to int in C using <code>atoi( ... )</code>.</a><br><br>
				<a href="https://www.geeksforgeeks.org/type-conversion-c/"> Type Casting in C.</a><br><br>

				I should be able to run <code>./app add 10 20</code><br> and get the output <code>Your result is 30</code><br>
			</p>
		""",
		'solution': {}
	},
	"big_o":	{
		'title'	: "Calculate the Big O Complexity",
		'desc'	: """
			<br>
			<h3 class="bold">Algorithm A:</h3>
			<div class="codeBlock">
				<code>int count = 0;</code>
				<code>for (int j = 0; j < 50; j++) {</code>
				<code> printf( "%i", j );</code>
				<code>}</code>
			</div>

			<br>

			<h3 class="bold">Algorithm B:</h3>
			<div class="codeBlock">
				<code>int count = 0;</code>
				<code>for (int i = N; i > 0; i /= 2) {</code>
				<code> for (int j = 0; j < i; j++) {</code>
				<code>  count += 1;</code>
				<code> }</code>
				<code>}</code>
			</div>
			<br>
			<h3 class="bold">Algorithm C:</h3>
			<div class="codeBlock">
				<code>int name = "Al";</code>
				<code>int num = 100;\n\n</code>
				<code>if( strcmp( name, "Bob") {</code>
				<code> for (int j = 0; j < num; j++) {</code>
				<code>   printf( "%i", j );</code>
				<code>   num = num / 2;</code>
				<code> }</code>
				<code>} else { </code>
				<code> printf( "inalid name" );</code>
				<code>}</code>
			</div>
		""",
		'solution': {}
	},
	"size_of_names":	{
		'title'	: "Name Comparison",
		'desc'	: """
			Create a library named libs.<br>
			In that Library, create a function called <code>longerName()</code><br>
			In this function, you will require 2 parameters: <code>name1</code> and <code>name2</code>.<br>
			Both of those parameters are strings.<br>
			In the function, we will build an Algorithm that will compare the length of the 2 names and return the name with the most letters.<br><br>
			To do that, in the <code>longerName()</code> function we will need to do the following:<br>
			- Find how long each name is.<br>
			- Compare the length of both names.<br>
			- If name1 is longer, return name1.<br>
			- If name2 is longer, return name2.<br>
			<br>
			Lets look at the <code>strlen()</code> Library and see how we can get the size of a string:<br>
			<a href="https://www.geeksforgeeks.org/strlen-function-in-c/" target="_blank">The <code>strlen()</code> Function</a><br>
			<a href="https://www.geeksforgeeks.org/difference-strlen-sizeof-string-c-reviewed/" target="_blank">strlen() vs sizeof()</a><br>
			Now, we can go to our Main function and ask the user to give us 2 names that we then pass to the longerName() function.<br>
			Remember to include the library on the top of your code.<br>
			<br>
			<h3 class="bold">Bonus:</h3><br>
			Let's now write a <code>longestName()</code> function that will take a list of names and return the one that is the longest out of all of them.<br>
			In this function, you will also require 2 parameters: <code>nameList</code> and <code>sizeOfNameList</code>.<br>
			The <code>nameList</code> will be an array of all the names I'm passing.<br>
			The <code>sizeOfNameList</code> will be lenght of my <code>nameList</code> array.<br>
			Remember to calculate the size of the array in order to send it to the function.<br><br>
			To do that, in the <code>longestName()</code> function we will need to do the following:<br>
			- Use a for loop to go through the array of names.<br>
			- Find how long each name is.<br>
			- keep track of the longest name in a variable called longName.<br>
			- return the longuest name after the loop ends.<br>
		""",
		'solution': {
			'title'	: 'Size of names',
			'video_host': '',
			'video_url'	: '',
			'code'		: 'https://www.codepile.net/raw/6radvMZJ.cpp'
		}
	},
	"tax_calculator":	{
		'title'	: "Tax Calculator",
		'desc'	: """
			Let's create a simple Tax Calculator.<br><br>
			The task is to: <br>
			- Ask the User how many items they would like to add<br>
			- Ask the user for an item name.<br>
			- Add the name to an items array.<br>
			- Then ask for the price of that <code>item</code>.<br>
			- Add the price to an <code>itemPrices</code> array.<br>
			<br>
			When the loop is over. Ask the User what they would like to get:<br>
			<code>total</code>, <code>tax</code><br>
			<br>
			If they choose <code>total</code>. Run code to return them the total price of all Items.<br>
			<div class="codeBlock">
				<code>Total Price: $5.000000</code>
			</div><br><br>

			If they choose <code>tax</code>. Run code to show them the modified price of each item and a total of All the items with tax.<br>
			In our program, we will set the Tax to <code>7%</code> or <code>0.07</code> cents to the dollar. <br><br>
			The output should look like:
			<div class="codeBlock">
				<code>Banana: $1.00, with tax: $1.070000 </code>
				<code>Milk: $3.00, with tax: $3.210000 </code>
				<code>Brad: $2.00, with tax: $2.140000 </code>
				<code>Total Price: 6.420000</code>
			</div>
		""",
		'solution': {}
	},
	"linear_search":	{
		'title'	: "Linear Search",
		'desc'	: """
			Let's implement a <code>Linear Search</code> algorithm.<br>
			Your job will be to come up with the pseudocode that we will follow in class to find a search term that the user will type in.<br>
			First we will ask the user to search for a specific thing. it could be a word, a name, a number, a car model, ect. You decide.<br>
			Next, we will establish a list of names, or numbers, or car model, or whatever you decide your data set will be comprized of.<br>
			Next, as a team, you will write in Pseudocode how the developer will go about searching that list and finding the search term the user has typed.<br>
			<br>
			The goal is to find it in as little steps as possible. So we have to think about a couple things:<br>
			- Have a message for when you DO find the search term.<br>
			- Have a message for when you DONT find the search term.<br>
			- Keep track of how many loops you are doing.<br>
			- Keep track of what index you found the search term at.<br>
			<br>
			<h4 class="bold">FOR EXAMPLE</h4>
			The output should look something like this:<br>
			Let's say your DataSet is of 50 items.<br>
			<br>
			When they search something that is in the list:<br>
			<div class="codeBlock">
				<code>We found your search for "Toyota" within our list.</code>
				<code>It was at index 15.</code>
				<code>It took 16 searches.</code>
			</div><br>

			When they search something that is NOT the list:<br>
			<div class="codeBlock">
				<code>We could not find your search term after 50 searches.</code>
			</div>
		""",
		'solution': {
			'title'	: 'Linear Search',
			'video_host': '',
			'video_url'	: '',
			'code'		: 'https://www.codepile.net/raw/l649LnpE.cpp'
		}
	},
	"count_algorithm":	{
		'title'	: "Count Algorithm",
		'desc'	: """
			Let's build on our <code>Linear Search</code> Algorithm above.<br>
			Instead of just FINDING the item and returning if we did or did not find it, this time, we're going to count how many times that item is in the list.<br>
			Your job will be to come up with the pseudocode that we will follow in class to find a search term that the user will type in.<br>
			<br>
			If you do find instances of the search term, our output should look like this:<br>
			<div class="codeBlock">
				<code>We found your search term: "Banana" 3 times in our list.</code>
			</div>
			<br>
			If you DONT find instances of the search term, our output should look like this:<br>
			<div class="codeBlock">
				<code>We did not find your search term: "Banana" in our list.</code>
			</div><br>

			What is the maind difference you notice in our algorithm?<br>
		""",
		'solution': {
			'title'	: 'Count Algorithm',
			'video_host': '',
			'video_url'	: '',
			'code'		: 'https://www.codepile.net/raw/jEalRzDy.cpp'
		}
	},
	"binary_search":	{
		'title'	: "Binary Search",
		'desc'	: """
			Let's implement a <code>Binary Search</code> algorithm.<br>
			Your job will be to come up with the pseudocode that we will follow in class to find a search term that the user will type in.<br>
			This time though, we will assume that the list we have is ordered in Ascending Alphabetical or Numerical order.<br>
			<br>
			Remember that Binary search cuts the list in half at every loop, so, think about:<br>
			- How you will set a BEGINNING index to limit your list.<br>
			- How you will set an ENDING index to limit your list.<br>
			- How you will update that BEGINNING or ENDING index at every loop to cut down your list every time.<br>
			<br>
			Like our linear search, the goal is to find it in as little steps as possible:<br>
			- Have a message for when you DO find the search term.<br>
			- Have a message for when you DONT find the search term.<br>
			- Keep track of how many loops you are doing.<br>
			- Keep track of what index you found the search term at.<br>
			<br>
			<h3 class="bold">FOR EXAMPLE</h3>
			The output should look something like this:<br>
			Let's say your DataSet is of 50 items.<br>
			<br>
			When they search something that is in the list:<br>
			<div class="codeBlock">
				<code>We found your search for "Mango" within our list.</code>
				<code>It was at index 7.</code>
				<code>It took 3 searches.</code>
			</div><br>

			When they search something that is NOT the list:<br>
			<div class="codeBlock">
				<code>We could not find your search term after 5 searches.</code>
			</div>
		""",
		'solution': {
			'title'	: 'Binary Search',
			'video_host': '',
			'video_url'	: '',
			'code'		: 'https://www.codepile.net/raw/1RqbzzMo.cpp'
		}
	},
	"bubble_sort":	{
		'title'	: "Bubble Sort",
		'desc'	: """
			Let's build a <code>Bubble Sort</code> Algorithm.<br>
			The bubble sort algorithm goes though an array, compares the <code>current</code> element to the element next to it. <br>
			If the element next to it is bigger, then it swaps places with it and then keeps on doing that until it reaches the end of the array.<br><br>
			Whenever it does a swap, we should record that somehow to make sure we know to check the list one last time.
			Everytime it repeats the loop, it will do the same thing to bubble the largest number to the end of the array.
			It will keep on repeating the whole loop again until it hasnt recorded a swap during a loop.


			<h3 class="bold">FOR EXAMPLE</h3>
			The output should look something like this:<br>
			<br>
			Given this list:  <code>2,5,6,3,1</code><br>
			Our loops would look like this at every iteration.
			<code><b>loop: 1 => {  2,5,3,1,6  }, swapped => 1</b></code> <br>
			Notice that the 1 and the 2 swapped places. How did we do this? <br><br>

			Let's keep looking.
			<div class="codeBlock">
				<code><b>loop: 2 => {  2,3,1,5,6  }, swapped => 1</b></code>
				<code><b>loop: 3 => {  2,1,3,5,6  }, swapped => 1</b></code>
				<code><b>loop: 4 => {  1,2,3,5,6  }, swapped => 1</b></code>
				<code><b>loop: 5 => {  1,2,3,5,6  }, swapped => 0</b></code>
			</div><br>
			And we're done.<br>
			Notice that we have an extra loop at the bottom as Loop 5.<br>
			Because we performed a swap at loop 4, we have to check one more time to make sure we have no more swaps to perform.<br>
			Now, Let's figure out the Pseudocode to tho this together and you can start coding.
			<br>
			<br>
		""",
		'solution': {
			'title'	: 'Bubble Sort',
			'video_host': '',
			'video_url'	: '',
			'code'		: 'https://www.codepile.net/raw/mBLQwP93.cpp'
		}
	},
	"selection_sort":	{
		'title'	: "Selection Sort",
		'desc'	: """
			Let's build a <code>Selection Sort</code> Algorithm.<br>
			The selection sort algorithm finds the minimum element from and moves it at the beginning of the array. <br>
			To prevent shifting of all the other elements to another index, we will swap the element found with the element currently at the beggining of the array.<br><br>

			Once the item is moved to the front of the array, you no longer need to care about it anymore and you can keep sorting the remainder fo the array.<br>
			At every loop, your array should be smaller and smaller to search.<br><br>

			<h4 class="bold">FOR EXAMPLE</h4>
			The output should look something like this:<br>
			<br>
			Given this list:  <code>2,5,6,3,1,8,7,9</code><br>
			Our loops would look like this at every iteration.
			<code><b>loop: 1 => {  1,5,6,3,2,8,7,9  }</b></code> <br>
			Notice that the 1 and the 2 swapped places. How did we do this? <br><br>

			Let's keep looking.
			<div class="codeBlock">
				<code><b>loop: 2 => {  1,2,6,3,5,8,7,9  }</b></code>
				<code><b>loop: 3 => {  1,2,3,6,5,8,7,9  }</b></code>
				<code><b>loop: 4 => {  1,2,3,5,6,8,7,9  }</b></code>
				<code><b>loop: 5 => {  1,2,3,5,6,8,7,9  }</b></code>
				<code><b>loop: 6 => {  1,2,3,5,6,7,8,9  }</b></code>
				<code><b>loop: 7 => {  1,2,3,5,6,7,8,9  }</b></code>
			</div><br>
			And we're done.<br>
			Notice that Loops 4 and 5 are the same and Loops 6 an 7 are the same.<br>
			The reason they are the same is because even though 6,8,7,9 in loop 4 were already ordered, we still had to go through it to make sure it in fact was picking the smallest item and moving it to the front.<br>
			In this case the smallest item was already 6.<br><br>
			Let's figure out the Pseudocode to tho this together and you can start coding.
			<br>
			<br>
		""",
		'solution': {
			'title': 'Selection Sort',
			'video_host': '',
			'video_url'	: '',
			'code'		: 'https://www.codepile.net/raw/ald3g6X1.cpp'
		}
	},
	"insertion_sort":	{
		'title'	: "Insertion Sort",
		'desc'	: """
			Let's build a <code>Insertion Sort</code> Algorithm.<br>
			Insertion Sort is like sorting cards.<br>
			As you go through the list, you pick the current item, then go back to the begining of the list and do a mini loop up to the current index.<br>
			As you are going through that sublist, you are comapring it with each item of the sublist.<br><br>
			If it's bigger then then current sublist item, keep going up that sublist until you reach the end and put it at the end.<br>
			If it's smaller then then current sublist item, place the current main item in front of the sublist item, then move on to the next main list item.<br><br>

			Let's figure out the Pseudocode to tho this together and you can start coding.
		""",
		'solution': {
			'title'	: 'Insertion Sort',
			'video_host': '',
			'video_url'	: '',
			'code'		: ''
		}
	},
	"python_shopping_cart" : {
		'title'	: "",
		'desc'	: """
			<h2> Welcome to PYTHON</h2>
            I hope you're ready to have some fun :)<br><br>

            Now that we've introduced python a bit compare to C. Let's see how we can recreate and improve a C assignement in python.<br>

            First, we create a python file with the <code>.py</code> extension.<br>
            We can name it <code>ShoppingCart.py</code><br> <br>

            Ok, now that you have the file, here is your assignment:<br>
            You are building a shopping cart for a store.<br>

            You will need to first create a dictionaty of available items.<br>
            The dictionarie's keys will be the name of the items.<br>
            The values will be their respective prices.<br><br>

            Example:<br>
            <div class="codeBlock">
                <code>inventory = {</code>
                <code>    "Banana" : 1.97,</code>
                <code>    "Milk"   : 2.45,</code>
                <code>    ...</code>
                <code>}</code>
            </div>

            <p>
                Next, we create a user <code> cart </code> variable.<br>
                You can make it an array or a dictionary. ( You can decide that after a few steps ).
            </p>
            <p>
                <h3>From there, you can start writing your code.</h3>
                The program will first ask the user for his name using a python <code>input("...")</code>.<br>
                Then it will welcome the user to the store.<br><br>
                The program will then ask the user what items they would like to buy.<br>
                <code>note:</code> Do not show the available items to the user.<br>
                The user will them type the item they want to buy.<br>
                <code>note:</code> You should consider using a for loop or a while loop to keep asking the user to type items untill they type <code>done</code>
            </p>
            <p>
                If the item exists in the inventory, you can go ahead and add it to the user's cart.
                <code>Bonus: </code>
                <div class="codeBlock">
                    <code>Remember when you created the cart variable above? now is the time to decide what it should be.</code>
                    <code>You can do one of 2 things, you can save the items names in an array.</code>
                    <code>or you can same the name and the quantity in a dictionary where the key is the item name and the values is the quantity they wanna buy.</code>
                    <code>If you do that however, you have to also ask the user how many they want right after you ask them the name of the item.</code>
                </div>
            </p>
            <p>
                If the item is not in the list of inventory. print out a message that tells the user that the item does not exist in the store.<br>
                <code>Bonus: </code> Make to keep capitalization in mind. Users don't tend to be gramatically perfect.
            </p>

            <p>
                OUUUFFF!!!! ok... you've gotten pretty far. Now let's finish this<br>
                Now that the user has typed <code>done</code>. You can now do the final total.<br>
                As a final output result for the program, run a for loop that adds the items that the user typed in and generated a total.<br><br>
                <code>Bonus: </code> If you asked the user the amount of items they want each time, remember to multiply that by the cost of the item.<br>
                <code>Example: 2 bananas at $1.97 would cost $3.94. so make sure to add $3.94 to the total, NOT $1.97</code>
            </p>

            <hr>

            <h3><code>SUPER BONUS:</code></h3>
            <p>Remember your tax Calcualtor from C?</p>
            <p>Attempt to implement that same function in Python.</p>
            <p>Use that function to calculate the final price of the cart including tax.</p>

            <hr>

            <h3><code>NINJA BONUS:</code></h3>
            <p>In the tax Calcualtor, consider having a dictionary of different states and their respective tax.<br>
            Ask the user their State<br>
            Use the correct tax for that state in your final price calculation.</p>

            <p>Maybe you want to also introduce a shipping cost function?.<br>
            Use the same phylosophy as the tax calculator fucntion.<br>
            Ask the user their State<br>
            Use the correct shipping cost for that state and include that in your final price calculation.</p>
            <hr>
            <h3><code>WIZARD BONUS:</code></h3>
            Let's kick it up a notch.<br>
            Let's improve the inventory by adding a quantity and a price.<br><br>
            Example:<br>
            <div class="codeBlock">
                <code>inventory = {</code>
                <code>    "Banana" : {"qty": 12, "price": 1.97},</code>
                <code>    "Milk"   : {"qty": 20, "price": 2.45},</code>
                <code>    ...</code>
                <code>}</code>
            </div>

            Now... Every time a user types in an item that is in the list, you should remove one item from the inventory.<br>
            When the user has taken everything from the inventory, you should not add anymore of that item to his cart.<br>
            For example if they've added all 12 bananas to their cart, and they try to add one more.<br>
            You should tell them that there are no more bananas.<br>
            The rest of the code continues as usual.
		"""
	},
	"python_store_classes" : {
		"title" : "Python Store Classes",
		"desc" : """
			Awesome, you've mad it quite far.<br>
            Now... let's take it up a notch.<br>
            There are many things you can do to improve your past code... but let's focus on moving things forward. You can refactor later and spend more time playing with it.<br><br>

            So far, you've been playing with functions and simple loops and writing everything in one page.<br>
            Next you started working on moving code to separate helpers and modules.<br>
            Now, let's work on building classes that help you perform operations in a more understandable manner :)<br><br>

            First let's take a look at the project, whet do we have?<br>
            <ul>
                <li>A store.</li>
                <li>A store's inventory.</li>
                <li>Some products in that inventory with prices and quantity.</li>
                <li>A shopping cart that holds the item and it's cart quantity.</li>
                <li>A Tax formula by State.</li>
                <li>A Shipping Formula by State.</li>
            </ul><br>

            We can think about breaking this down in a couple ways.<br>
            What are they individual ELEMENTS of this particular scenario?<br>

            <hr>

            We can break it down to:<br>
            <ul>
            <li>Product</li>
            <li>Inventory</li>
            <li>Cart</li>
            <li>Store</li>
            </ul><br>

            Each of these elements are responsible for their own set of attributes/states and actions/methods.<br>

            For example:<br>
            - A Product can have <code>name, price, type, sale_percentage</code> attributes amongst others.<br>
            - If you want to be more specific, you can add: <code>id, barcode, expiration_date</code>, and other details tha individualize the product.<br><br>

            Ok cool, a product doesn't exactly have any actions it can perform, but you can set some actions that you want the developer to be able to access from that product class.<br>
            Here are a couple to get started:<br>
            <code>def availabe()</code> This could return you a boolean of wether there is still some of that product in inventory.<br>
            <b>BONUS:</b> <code>def expired()</code> Using the dateime module, this could compare the current date with the expiration date and return if the product is expired or not.<br><br>

            Now that you have a <b>Product</b> class, we can think about the inventory.<br>
            The Inventory class could be thought of like so...<br>
            It has ONE attribute that holds a dictionary of <code>Product</code> objects, along with the <code>quantity</code> of products in the inventory.<br><br>

            The actions an <b>Inventory</b> class can perform are to:<br>
            <code>def addProduct(product, x)</code> This should take the product you want to add the to he Inventory and how many you would like to add.<br>
            <code>def removeProduct(product, x)</code> This should take the product you want to remove the to he Inventory and how many you would like to remove.<br>
            These can be used whenever you want to remove an item when you add to cart or when you confirm purchase.<br><br>
            Finally, <code>def list()</code> This could print you a lisf of the items in inventory along with their prices.<br><br>

            <hr>

            Similarly, you can think about the <b>Cart</b> class in a similar manner:<br>
            It has ONE attribute that holds a dictionary of <code>Product</code> objects, along with the <code>quantity</code> of products in the cart.<br><br>

            The actions a <b>Cart</b> class can perform are to:<br>
            <code>def addProduct(product, x)</code> This should take the product you want to add the to he Cart and how many you would like to add.<br>
            <code>def removeProduct(product, x)</code> This should take the product you want to remove the to he Cart and how many you would like to remove.<br>
            You should think about using the Inventory's classes to update the inventory.<br><br>
            <code>def list()</code> This could print you a lisf of the items in the Cart along with their prices.<br>
            <code>def total()</code> This could print you a SUM total of your cart's item prices.<br>

            <hr>

            <h3>NINJA BONUS:</h3><br>
            Implement the __repr__ function in each class so that when I print the object alone, it prints me a summary of the object.<br><br>
            Example:<br>

            <div class="codeBlock">
                <code>banana = Product("Banana", "Fruit", 0.4)</code>
                <code>print( banana )</code>
                <code>>> This is a Banana (Fruit) at $0.4</code>
            </div>

            <hr>

            <h3>WIZARD BONUS:</h3><br>
            In the Wizard Bonus, let's work on the <b>Store</b> Class.<br>
            By now, you've go the gist of things.<br>
            I want you to work on a Store Class that has the following attributes and actions:<br>

            <b>Attributes</b><br>
            <code>- name</code><br>
            <code>- address</code><br>
            <code>- type</code><br><br>

            <b>Actions</b><br>
            <code>greet_customer()</code> <br>
            This is where you should ask the customer their names and greet them.<br><br>

            <code>checkout()</code><br>
            This is  where you should perform the inventory update. You've already done it in th Cart actions, you can do them here instead and save your system the repetition of doing it everytime you add the item to the cart.<br><br>
            ... and any other actions that a store in the general sense can perform.<br>
		"""
	}

}

activities = {
	"2a8a3r2c0"  :   {
		'id'        : '2a8a3r2c0',
		'title'     : 'We the Machines',
		'preview'   : "Can you communicate effectively as a team? Let's find out.",
		'desc'  : """""",
		'challenges': [challenges['random_task']],
		'published' : True
	},
	"7g4k9c0o8"  :   {
		'id'      : '7g4k9c0o8',
		'title'   : 'Spy ypS Spy',
		'preview' : "Binary is an ancient, lost forgoten language. Can you decode the secret message?",
		'desc'    : """
			Binary is an ancient, lost forgoten language.<br>
			That's why some deep underground gang of coders still use it to transfer hidden messages. <br>
			<br><br>
		""",
		'challenges': [challenges['binary_password']],
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
					<div class="codeBlock">
						<code>SET VARIABLE light as the STRING 'Red'</code><br>
						<br>
						<code>IF light is 'Green'</code><br>
						<code>	MOVE FORWARD</code><br>
						<code>ELSE IF light is 'Yellow'</code><br>
						<code>	SLOW DOWN</code><br>
						<code>ELSE IF light is 'Red'</code><br>
						<code>	STOP</code><br>
					</div>
				</div>
				<div class="col-sm-6">
					<h5 class="bold">Weather</h5>
					<div class="codeBlock">
						<code>SET VARIABLE temperature as the STRING 'Cold'</code><br>
						<code>SET VARIABLE weather as the STRING 'Rainy'</code><br>
						<br>
						<code>IF temperature is 'Hot'</code><br>
						<code>	Leave Sweater Home</code><br>
						<code>ELSE IF temperature is 'Cold'</code><br>
						<code>	Take Sweater</code><br>
						<code>ELSE</code><br>
						<code>	Wear a nice sundress</code><br>
						<br>
						<code>Check the weather</code><br>
						<br>
						<code>IF weather is 'Rainy'</code><br>
						<code>	Take Umbrella</code><br>
						<code>ELSE</code><br>
						<code>	Leave Umbrella Home</code><br>
					</div>
				</div>
			</div>
			<h4>
				Below are 2 types of tasks. Life tasks and Ccoding task. <br>
				Choose one of each task and write simple pseudo code to accomplish each task. <br>
				The PSEUDOCODE should be simple and straight to the point.
			</h4>
			<br>
		""",
		'challenges': [
			challenges['grilled_cheese'],
			challenges['cheesy_mac'],
			challenges['gas_tanks'],
			challenges['morning_weather'],
			challenges['password_pseudo'],
			challenges['loop_pseudo'],
			challenges['sorting_pseudo']
		],
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
			'desc'      : """""",
			'challenges': [
				challenges['simple_convo'],
				challenges['two_digit']
			],
			'published' : True
	},
	"6a82js91"  :   {
			'id'        : '6a82js91',
			'title'     : "Let's Write Better programs",
			'preview'   : "In this activity, you will putting into practice some of the same concepts as last time, but this time using loops to make it more interesting.",
			'desc'      : """
			""",
			'challenges': [
				challenges['simple_loop'],
				challenges['simple_loop_2'],
				challenges['password'],
				challenges['for_names'],
				challenges['guessing_game']
			],
			'solutions' : [],
			'show_solutions': True,
			'published' : True
	},
	"5h23kw23"  :   {
			'id'        : '5h23kw23',
			'title'     : "Let's make our programs dynamic.",
			'preview'   : "In this activity, you will go back to some of your past programs and refactor them into functions that can be re-used.",
			'desc'      : """""",
			'challenges': [
				challenges['calculator_game'],
				challenges['function_refactoring'],
			],
			'solutions' : [],
			'show_solutions': True,
			'published' : True
	},
	"6dj72j28"  :   {
		'id'        : '6dj72j28',
		'title'     : "Straigh through the command line",
		'preview'   : "In this activity, you will revisit yet again th calculator game and some other past activites and make them use the command line arguments.",
		'desc'      : """""",
		'challenges': [
			challenges['hello_world'],
			challenges['add_2_numbers'],
			challenges['refactoring_cla'],
			challenges['big_o']
		],
		'solutions' : [],
		'show_solutions': False,
		'published' : True
	},
	"k232kn34"  :   {
		'id'        : 'k232kn34',
		'title'     : "Lets build some programs",
		'preview'   : "In this activity, We will build some more complex programs and review the past activities if we have some time left.",
		'desc'      : """""",
		'challenges': [
			challenges['size_of_names'],
			challenges['tax_calculator']
		],
		'solutions' : [],
		'show_solutions': True,
		'published' : True
	},
	"h5j30345"  :   {
		'id'        : 'h5j30345',
		'title'     : "Searcing Algorithms",
		'preview'   : "In this activity, we will build some searching algorithms and figure out the logic of finding a item in a list.",
		'desc'      : """""",
		'challenges': [
			challenges['linear_search'],
			challenges['count_algorithm'],
			challenges['binary_search']
		],
		'solutions' : [],
		'show_solutions': True,
		'published' : True
	},
	"344ij0i5"  :   {
		'id'        : '344ij0i5',
		'title'     : "Sorting Algorithms",
		'preview'   : "In this activity, we will build some sorting algorithms and figure out the logic of ordering items in a list.",
		'desc'      : """""",
		'challenges': [
			challenges['bubble_sort'],
			challenges['selection_sort'],
			challenges['insertion_sort']
		],
		'solutions' : [],
		'show_solutions': True,
		'published' : True
	},
	"H2oj30-203jwjwj"  :   {
		'id'        : 'H2oj30-203jwjwj',
		'title'     : "Python Shopping Cart",
		'preview'   : "In this activity, we will build a shopping cart in python",
		'desc'      : """""",
		'challenges': [
			challenges['python_shopping_cart']
		],
		'solutions' : [],
		'show_solutions': False,
		'published' : True
	},
	"HA20u1e1n1i"  :   {
		'id'        : 'HA20u1e1n1i',
		'title'     : "Python Shopping Cart Classes",
		'preview'   : "In this activity, we will inprove on our shopping cart and make it stronger using python classes.",
		'desc'      : """""",
		'challenges': [
			challenges['python_store_classes']
		],
		'solutions' : [],
		'show_solutions': False,
		'published' : True
	},
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
