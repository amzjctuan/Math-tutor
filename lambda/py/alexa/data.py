# -*- coding: utf-8 -*-

STATES_LIST = [
    {
        'abbreviation': '2', 'answer': '2',
        'state': 'one_plus_one', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '4',
        'state': 'two_plus_two', 'capital': '4',
        'statehood_year': '4'
    },
    {
        'abbreviation': '2', 'answer': '6',
        'state': 'three_plus_three', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '8',
        'state': 'four_plus_four', 'capital': '4',
        'statehood_year': '4'
    },
    {
        'abbreviation': '2', 'answer': '10',
        'state': 'five_plus_five', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '12',
        'state': 'six_plus_six', 'capital': '4',
        'statehood_year': '4'
    },
    {
        'abbreviation': '2', 'answer': '29',
        'state': 'nineteen_plus_ten', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '40',
        'state': 'twenty_plus_twenty', 'capital': '4',
        'statehood_year': '4'
    },
    {
        'abbreviation': '2', 'answer': '132',
        'state': 'one_hundred_plus_thirty_two', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '4',
        'state': 'two_times_two', 'capital': '4',
        'statehood_year': '4'
    },
    {
        'abbreviation': '2', 'answer': '99',
        'state': 'nine_times_eleven', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '28',
        'state': 'fourty_minus_twelve', 'capital': '4',
        'statehood_year': '4'
    },
    {
        'abbreviation': '2', 'answer': '121',
        'state': 'eleven_times_eleven', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '91',
        'state': 'seven_times_thirteen', 'capital': '4',
        'statehood_year': '4'
    },
    {
        'abbreviation': '2', 'answer': '66',
        'state': 'eighty_minus_fourtten', 'capital': '2',
        'statehood_year': '2'
    },   
    {
        'abbreviation': '4', 'answer': '11',
        'state': 'fifteen_minus_four', 'capital': '4',
        'statehood_year': '4'
    },
      ]

SKILL_TITLE = "Math Tutor Quiz Game"

WELCOME_MESSAGE = ("Welcome to the Math Tutor Quiz Game!  "
                   "You can ask me about any of the "
                   "math questions, or you can ask me to "
                   "start a quiz.  What would you like to do? ")

START_QUIZ_MESSAGE = ("OK.  I will ask you 10 math questions ")

EXIT_SKILL_MESSAGE = ("Thank you for playing the Math Tutor Quiz Game!  "
                      "Let's play again soon!")

REPROMPT_SPEECH = "Which math questions would you like to know about?"

HELP_MESSAGE = ("I know lots of things about math.  "
                "You can ask me about a math question "
                "and I'll tell you what I know.  "
                "You can also test your knowledge by asking me to start "
                "a quiz.  What would you like to do? ")

CORRECT_SPEECHCONS = ['Booya', 'All righty', 'Bam', 'Bazinga', 'Bingo',
                      'Boom', 'Bravo', 'Cha Ching', 'Cheers', 'Dynomite',
                      'Hip hip hooray', 'Hurrah', 'Hurray', 'Huzzah',
                      'Oh dear.  Just kidding.  Hurray', 'Kaboom', 'Kaching',
                      'Oh snap', 'Phew', 'Righto', 'Way to go', 'Well done',
                      'Whee', 'Woo hoo', 'Yay', 'Wowza', 'Yowsa']

WRONG_SPEECHCONS = ['Argh', 'Aw man', 'Blarg', 'Blast', 'Boo', 'Bummer',
                    'Darn', "D'oh", 'Dun dun dun', 'Eek', 'Honk', 'Le sigh',
                    'Mamma mia', 'Oh boy', 'Oh dear', 'Oof', 'Ouch', 'Ruh roh',
                    'Shucks', 'Uh oh', 'Wah wah', 'Whoops a daisy', 'Yikes']

IMG_PATH = (
    "https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/"
    "alexa-skills-kit/tutorials/quiz-game/state_flag/{}x{}/{}._TTH_.png")

USE_CARDS_FLAG = True

MAX_QUESTIONS = 10

BAD_ANSWER = (
    "I'm sorry. {} is not something I know very much about in this skill.")

FALLBACK_ANSWER = (
    "Sorry. I can't help you with that. {}".format(HELP_MESSAGE))

SCORE = "Your {} score is {} out of {}. "

# SPEECH_DESC = (
#     "{} is the {}th state, "
#     "admitted to the Union in {}.  "
#     "The capital of {} is {}, and the "
#     "abbreviation for {} is "
#     "<break strength='strong'/><say-as interpret-as='spell-out'>"
#     "{}</say-as>.  I've added {} to "
#     "your Alexa app.  Which other state or capital would you like to "
#     "know about? ")
