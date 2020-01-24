activities = {
    "2a8a3r2c0"  :   {
        'id'        : '2a8a3r2c0',
        'title'     : 'We the Machines',
        'preview'   : "Can you communicate effectively as a team? Let's find out. ",
        'desc'  :    """
                        Use the following, to generate a radom task.
                        <h4 class="bold" class='bold'>
                            Random Task Generator:
                            <a href='/random_task'> click here </a>
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
            "Whoa I know code fu!!"
        ]
        message = messages[ int(code.split('+')[0])-1 ]

        if code.split('+')[1] == message:
            return [ True, message ]
        return failed
    
    return failed