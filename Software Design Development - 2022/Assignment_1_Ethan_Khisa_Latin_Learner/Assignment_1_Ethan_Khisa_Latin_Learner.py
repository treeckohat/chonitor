import random #used to generate random questions
import os #used to clear screen
import time #times the quiz
import sys #runs the slow type

def slow_type(t): #slow type to make the large blocks of texts not so jaring
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)#mimics the paterns of human typing
    print('')

def get_key(val): # function to return key for any value
    for key, value in all_sets.items():
         if val == value:
             return key
    return "key doesn't exist"

def question(difficulty_type): #function to generate a random question from the provided list
    qn = random.choice(list(difficulty_type))#calls a random choice from the provided list and attaches it to the qn variable
    return qn # returns a key as the questions

def incorrect(incorrect):
    #for all questions wrong they will be re asked
    print("These are the questions you got wrong, can you get them this time?")
    for quest in incorrect:
        answer = all_sets.get(quest)
        if answer == all_sets.get("invalid"):#invalid used to test weather it is an invalid answer and produces none
            answer = get_key(quest)
            ans = input(f"What is '{quest}' in latin? ").lower()
            if ans == answer:#if ans is correct tell them it is correct
                print(f"Correct the answer is '{answer}'")
            elif ans != answer:#if ans is wrong tell them it is wrong
                print(f"Sorry the answer is '{answer}'")
        else:
            ans = input(f"What is '{quest}' in english? ").lower()
            if ans == answer:#if ans is correct tell them it is correct
                print(f"Correct the answer is '{answer}'")
            elif ans != answer:#if ans is wrong tell them it is wrong
                print(f"Sorry the answer is '{answer}'")

def clear(): #function to clear the screen by trying to clean screen on either a windows or a mac
    try:
        os.system("cls")
    except:
        pass

def action():
    clear()#clear screen
    print("WARNING - Do not type press enter while text blocks are printing - WARNING")
    print(menu)
    act = input("What action would you like to take. Choose a number. ")
    while act not in ("1","2","3","4","5"):#if not a input that works asks again
        print("Not a valid input. Try again")
        act = input("What action would you like to take. Choose a number. ")
    return act

def start(difficulty):
    #sets regular set of questions at 5
    easyn = 5
    normaln = 5
    hardn = 5
    #for the chosen dificulty sets it to have 10 questions
    if difficulty == "easy":
        easyn = 10
    elif difficulty == "normal":
        normaln = 10
    elif difficulty == "hard":
        hardn = 10
    point_count = int(0)
    quest_list = []
    incorrect_list = []
    t0 = time.time() #start timer
    print("""You are now starting the EASY Questions""")
    for turn in range(easyn):
        print(f"Easy Question {turn+1}")
        quest = question(easy)
        while quest in quest_list: #check to see if the question has been asked before
            quest = question(easy) #generates a new question
        if quest not in quest_list:
            quest_list.append(quest)
        answer = easy.get(quest)
        if (turn%2) == 0: #checks to see if the turn is odd or even to decide weather to give a latin to english or english to latin question
            ans = input(f"What is '{quest}' in english? ").lower()
            while ans == "":
                print("Invalid answer, Try again")
                ans = input(f"What is '{quest}' in english? ").lower()
            if ans == answer:
                input(f"Correct the answer is '{answer}'. Press enter to continue.")
                point_count = point_count+15 #add to point total
            elif ans != answer:
                input(f"Sorry the answer is '{answer}'. Press enter to continue.")
                incorrect_list.append(quest) #add to questions gotten wrong
        else:
            ans = input(f"What is '{answer}' in Latin? ").lower()
            while ans == "":
                print("Invalid answer, Try again")
                ans = input(f"What is '{answer}' in english? ").lower()
            if ans == quest:
                input(f"Correct the answer is '{quest}'. Press enter to continue.")
                point_count = point_count+15 #add to point total
            elif ans != quest:
                input(f"Sorry the answer is '{quest}'. Press enter to continue.")
                incorrect_list.append(answer) #add to questions gotten wrong
        clear()
    print("""You are now starting the NORMAL Questions""")
    for turn in range(normaln):
        print(f"Normal Question {turn+1}")
        quest = question(normal)
        while quest in quest_list: #check to see if the question has been asked before
            quest = question(normal) #generates a new question
        if quest not in quest_list:
            quest_list.append(quest)
        answer = normal.get(quest)
        if (turn%2) == 0: #checks to see if the turn is odd or even to decide weather to give a latin to english or english to latin question
            ans = input(f"What is '{quest}' in english? ").lower()
            while ans == "":
                print("Invalid answer, Try again")
                ans = input(f"What is '{quest}' in english? ").lower()
            if ans == answer:
                input(f"Correct the answer is '{answer}'. Press enter to continue.")
                point_count = point_count+25#add to point total
            elif ans != answer:
                input(f"Sorry the answer is '{answer}'. Press enter to continue.")
                incorrect_list.append(quest) #add to questions gotten wrong
        else:
            ans = input(f"What is '{answer}' in Latin? ").lower()
            while ans == "":
                print("Invalid answer, Try again")
                ans = input(f"What is '{answer}' in english? ").lower()
            if ans == quest:
                input(f"Correct the answer is '{quest}'. Press enter to continue.")
                point_count = point_count+25#add to point total
            elif ans != quest:
                input(f"Sorry the answer is '{quest}'. Press enter to continue.")
                incorrect_list.append(answer) #add to questions gotten wrong
        clear()
    print("""You are now starting the HARD Questions""")
    for turn in range(hardn):
        print(f"Hard Question {turn+1}")
        quest = question(hard) #generates a new question
        while quest in quest_list: #check to see if the question has been asked before
            quest = question(hard)
        if quest not in quest_list:
            quest_list.append(quest)
        answer = hard.get(quest)
        if (turn%2) == 0: #checks to see if the turn is odd or even to decide weather to give a latin to english or english to latin question
            ans = input(f"What is '{quest}' in english? ").lower()
            while ans == "":
                print("Invalid answer, Try again")
                ans = input(f"What is '{quest}' in english? ").lower()
            if ans == answer:
                input(f"Correct the answer is '{answer}'. Press enter to continue.")
                point_count = point_count+35#add to point total
            elif ans != answer:
                input(f"Sorry the answer is '{answer}'. Press enter to continue.")
                incorrect_list.append(quest) #add to questions gotten wrong
        else:
            ans = input(f"What is '{answer}' in Latin? ").lower()
            while ans == "":
                print("Invalid answer, Try again")
                ans = input(f"What is '{answer}' in english? ").lower()
            if ans == quest:
                input(f"Correct the answer is '{quest}'. Press enter to continue.")
                point_count = point_count+35#add to point total
            elif ans != quest:
                input(f"Sorry the answer is '{quest}'. Press enter to continue.")
                incorrect_list.append(answer) #add to questions gotten wrong
        clear()
    t1 = time.time() #end timer
    time_taken = round((t1-t0)*1.5) #measures how long it took to answer all questions and magnifies the time
    total_points = time_taken-point_count #removes points from time taken to find total points
    input("Press enter to see your score")
    clear()
    print(f"""
Your score was
               *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .      {total_points} *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '
""")
    incorrect(incorrect_list)# run through questions that were wrong
    input("Press enter to move on.")

def learning(list_type):
    clear()
    lines = size.lines - 3 #finds the height of the window to set how many words to be learnt at a time. Removes 3 to make usre it does not go overboard
    if lines > 25: #sets lines at a max of 25 words at a time
        lines = 25
    line = 0
    if list_type == "1":
        for word in easy:
            line =  line + 1
            slow_type(f"{word} means {easy.get(word)}")
            if line == lines: #once the amount of lines has reached the set max, asks to enter and then resets and counts again
                input("Press enter to go to the next page.")
                clear()
                line = 0
    elif list_type == "2":
        for word in normal:
            line =  line + 1
            slow_type(f"{word} means {normal.get(word)}")
            if line == lines: #once the amount of lines has reached the set max, asks to enter and then resets and counts again
                input("Press enter to go to the next page.")
                clear()
                line = 0
    elif list_type == "3":
        for word in hard:
            line =  line + 1
            slow_type(f"{word} means {hard.get(word)}")
            if line == lines: #once the amount of lines has reached the set max, asks to enter and then resets and counts again
                input("Press enter to go to the next page.")
                clear()
                line = 0
    elif list_type == "4":
        for word in all_sets:
            line =  line + 1
            slow_type(f"{word} means {all_sets.get(word)}")
            if line == lines: #once the amount of lines has reached the set max, asks to enter and then resets and counts again
                input("Press enter to go to the next page.")
                clear()
                line = 0

#Variables and Dictionary for words being tested
difficulties = ["easy", "normal", "hard"]
all_sets = {"ad":"to","adest":"is there","advenit":"arrives","ager":"field","alii":"others","ambulat":"walks","amicus":"friend","aqua":"water","ascendit":"climbs","audit":"hears","bellum":"war","benigne":"kindly","bonus":"good","cadit":"falls","calathos":"baskets","canis":"dog","cara":"dear/expensive","casa":"house","celeriter":"quickly","cena":"dinner","cenat":"dines","cibus":"food","clamat":"shouts","colligit":"collects","colonus":"farmer","comes":"comrade","confecta":"finisher","consistit":"stops","convoco":"call together","corrigit":"corrects","cur":"why","currit":"runs","dat":"gives","diligenter":"carefully/hard","dimitto":"send away","domum":"home","dormit":"sleeps","ducit":"leads","eam":"her","ecce":"look","emit":"buys","erigunt":"put up","et":"and","eum":"him","exeo":"go out","exercitum":"army","fabula":"story","facit":"makes/does","femina":"woman","fessa":"tired","festinat":"hurries","fila":"daughter","filius":"son","fontem":"the spring","fortiter":"bravely","forum":"city centre","fracta":"broken","fugit":"flees","hastam":"spear","hi":"these","hortum":"garden","iacet":"lies down","ianua":"door","ieiuna":"starving","incendunt":"set fire to","inquit":"says","interdum":"sometimes","intrat":"enters","irata":"angry","itaque":"and so","iterum":"again","iuvat":"helps","laborat":"works","laeta":"happy","lapsat":"slips","laudat":"praises","lente":"slowly","ludit":"plays","ludus":"school","magnus":"great/big","mane":"early","manet":"stays","maturius":"too early","miser":"miserable","mittit":"sends","mox":"soon","multus":"many","nam":"for","narrat":"tells","navigo":"sail","navis":"ship","nec/neque":"and not/nor","nemo":"no one","nimium":"too much","non":"not","nundinae":"marketplace","obsident":"besiege","occido":"kill","olent":"smell","omnis":"all","oppugno":"attack","parat":"prepares","parata":"ready","per":"through","periculo":"danger","piscator":"fisherman","plenas":"full","ponit":"places/puts","portat":"carries","postridie":"the next day","princeps":"prince","prior":"first","puella":"girl","puer":"boy","pugno":"fight","pukchra":"pretty","querelas":"complaints","quiescit":"rests","quod":"because","quoque":"also","recte":"rightly","redit":"returns","respondet":"answers","rex":"king","rixam":"quarrel","rogat":"asks","saepe":"often","salutat":"greets","saucius":"hurt","sed":"but","sedet":"sits","sero":"late","sic":"thus","spectat":"watches","statim":"at once","stutus":"foolish","subito":"suddenly","tabernam":"pub","tandem":"at last","terra":"earth/land","totum":"whole","tuus":"your","ubi":"when","una":"together","urbis":"city","uvas":"grapes","vavuum":"empty","vendo":"selling","venit":"comes","via":"road/way","videt":"sees","vinco":"conquer","vocat":"calls"}
easy = {"ad":"to","ager":"field","ambulat":"walks","aqua":"water","ascendit":"climbs","audit":"hears","cadit":"falls","casa":"house","cena":"dinner","cenat":"dines","cibus":"food","colonus":"farmer","currit":"runs","ducit":"leads","eam":"her","ecce":"look","et":"and","eum":"him","fabula":"story","femina":"woman","fessa":"tired","festinat":"hurries","fila":"daughter","filius":"son","fugit":"flees","inquit":"says","intrat":"enters","irata":"angry","iuvat":"helps","laborat":"works","laeta":"happy","laudat":"praises","manet":"stays","mittit":"sends","mox":"soon","nam":"for","narrat":"tells","non":"not","parat":"prepares","parata":"ready","portat":"carries","puella":"girl","puer":"boy","quod":"because","redit":"returns","salutat":"greets","sed":"but","sedet":"sits","subito":"suddenly","terra":"earth/land","via":"road/way","videt":"sees","vocat":"calls"}
normal = {"amicus":"friend","benigne":"kindly","bonus":"good","canis":"dog","cara":"dear/expensive","clamat":"shouts","comes":"comrade","corrigit":"corrects","cur":"why","dat":"gives","diligenter":"carefully/hard","domum":"home","dormit":"sleeps","emit":"buys","exeo":"go out","fortiter":"bravely","forum":"city centre","fracta":"broken","hi":"these","hortum":"garden","iacet":"lies down","ieiuna":"starving","iterum":"again","lapsat":"slips","lente":"slowly","ludit":"plays","ludus":"school","magnus":"great/big","mane":"early","miser":"miserable","multus":"many","navis":"ship","omnis":"all","plenas":"full","princeps":"prince","prior":"first","pugno":"fight","querelas":"complaints","respondet":"answers","rex":"king","rogat":"asks","sic":"thus","spectat":"watches","tandem":"at last","totum":"whole","tuus":"your","urbis":"city","vavuum":"empty","vendo":"selling","venit":"comes"}
hard = {"adest":"is there","advenit":"arrives","alii":"others","bellum":"war","calathos":"baskets","celeriter":"quickly","colligit":"collects","confecta":"finisher","consistit":"stops","convoco":"call together","dimitto":"send away","erigunt":"put up","exercitum":"army","facit":"makes/does","fontem":"the spring","hastam":"spear","ianua":"door","incendunt":"set fire to","interdum":"sometimes","itaque":"and so","maturius":"too early","navigo":"sail","nec/neque":"and not/nor","nemo":"no one","nimium":"too much","nundinae":"marketplace","obsident":"besiege","occido":"kill","olent":"smell","oppugno":"attack","per":"through","periculo":"danger","piscator":"fisherman","ponit":"places/puts","postridie":"the next day","pukchra":"pretty","quiescit":"rests","quoque":"also","recte":"rightly","rixam":"quarrel","saepe":"often","saucius":"hurt","sero":"late","statim":"at once","stutus":"foolish","tabernam":"pub","ubi":"when","una":"together","uvas":"grapes","vinco":"conquer"}
menu = """
LATIN LEARNER

Actions
1 - Start
2 - Instructions
3 - Learn
 - Easy
 - Normal
 - Hard
4 - About
5 - Exit
"""
learn_type = """
Which set of words?
        
1 = easy   2 = normal   3 = hard
           4 = all
"""
typing_speed = 800 #wpm
size = os.get_terminal_size() #gets the dimensions of the window
run = "true"
act = action()
while run == "true": #run loop to repeat instructions
    while act == "1": # starts the questions
        print(" ".join(difficulties)) #prints the difficulties
        difficulty = input("What difficulty? ").lower()
        while difficulty not in difficulties: #Checks to make sure that the difficulty is a real difficulty
            difficulty = input("Sorry thats not one of our difficulites, try again please. ")
        start(difficulty)#starts the question portion at the set difficulty
        act = action() #asks for a new action
    while act == "2": #displays the instructions on how to use the program
        slow_type("The questions will increase in dificulty based on the chosen dificulty. It will have 5 questions of the other dificulties and 10 of your chosen dificulty. It wil aternate between latin to english translation, and english to latin translation. When answering do not include the pronoun. The lower your score the better as it is a time based test and questions that are answered correctly remove time.")
        input("Press enter to move on") #waits untill the user has finished reading to move on
        act = action() #asks for a new action
    while act == "3": #displays the sets of questions that could be asked
        type = input(learn_type) #asks for which set of words to learn
        while type not in ("1","2","3","4"): #checks to make sure the type is a valid type
            print("Not a valid input. Try again")
            type = input(learn_type) #asks for which set of words to learn
        learning(type)
        another = input("Would you like to see another set? ")
        while "yes" in another:
            type = input(learn_type) #asks for which set of words to learn
            while type not in ("1","2","3","4"): #checks to make sure the type is a valid type
                print("Not a valid input. Try again")
                type = input(learn_type) #asks for which set of words to learn
            learning(type)
            another = input("Would you like to see another set? ")
        act = action() #asks for a new action
    while act == "4": #displays the about page of the program
        slow_type("This is a latin learning guide, this can be used to develop your vocabulary. There are 100+ words for you to learn and use. It was made due to my regret of quiting latin after year 8. I hope to help other year 8s to continue after where i did. The words are from chapters 1 to 4. Although vocab is not required for the HSC it can be very helpful for understanding the language and developing your own english.")
        input("Press enter to move on")
        act = action() #asks for a new action
    while act == "5": #ends the program
        exit()