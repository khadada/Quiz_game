data_quiz = [
    {"category": "Entertainment: Cartoon & Animations", "type": "multiple", "difficulty": "medium",
     "question": "Which \"Toy Story\" character was voiced by Don Rickles?",
     "correct_answer": "Mr. Potato Head", "incorrect_answers": ["Slinky Dog", "Hamm", "Rex"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "The Great Wall of China is visible from the moon.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science & Nature", "type": "multiple", "difficulty": "easy",
                                      "question": "How many planets are in our Solar System?",
                                      "correct_answer": "Eight", "incorrect_answers": ["Nine", "Seven", "Ten"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "Which of these is NOT a main playable character in \"Grand Theft Auto V\"?",
     "correct_answer": "Lamar", "incorrect_answers": ["Trevor", "Michael", "Franklin"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "How many classes are there in Team Fortress 2?", "correct_answer": "9",
     "incorrect_answers": ["10", "8", "7"]},
    {"category": "Sports", "type": "multiple", "difficulty": "easy",
                                              "question": "Who won the 2015 Formula 1 World Championship?",
                                              "correct_answer": "Lewis Hamilton",
                                              "incorrect_answers": ["Nico Rosberg", "Sebastian Vettel",
                                                                    "Jenson Button"]},
    {"category": "Entertainment: Film", "type": "multiple", "difficulty": "medium",
     "question": "Which one of these actors is said to be cut from the film 'E.T. the Extra-Terrestrial'?",
     "correct_answer": "Harrison Ford",
     "incorrect_answers": ["Michael J. Fox", "Andy Kaufman", "Arnold Schwarzenegger"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "The Sniper's SMG in Team Fortress 2, was originally intended to be the Scout's primary weapon.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Television", "type": "multiple", "difficulty": "easy",
     "question": "The \"Psycho\" series of videos on YouTube was created by which of the following?",
     "correct_answer": "RiDGiD STUDiOS", "incorrect_answers": ["Dan Bell", "Billy Familia", "VeganGainz"]},
    {"category": "Science: Gadgets", "type": "multiple", "difficulty": "easy",
     "question": "Which buzzword did Apple Inc. use to describe their removal of the headphone jack?",
     "correct_answer": "Courage", "incorrect_answers": ["Innovation", "Revolution", "Bravery"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "Which Elite Four member from the first generation of Pok&eacute;mon became the champion in the next generation?",
     "correct_answer": "Lance", "incorrect_answers": ["Agatha", "Bruno", "Lorelei"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "In Overwatch, how old is Reinhardt Wilhelm?", "correct_answer": "61",
     "incorrect_answers": ["59", "65", "62"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "In \"Call Of Duty: Zombies\", what is the name of Samantha Maxis' dog?",
     "correct_answer": "Fluffy", "incorrect_answers": ["Baxter", "Fido", "Henry"]},
    {"category": "Entertainment: Music", "type": "multiple", "difficulty": "medium",
     "question": "The Who's eponymous line, \"Teenage Wasteland\", appears in which of their songs?",
     "correct_answer": "Baba O' Riley",
     "incorrect_answers": ["The Seeker", "Won't Get Fooled Again", "Pinball Wizard"]},
    {"category": "Science & Nature", "type": "multiple", "difficulty": "medium",
     "question": "On which mission did the Space Shuttle Columbia break up upon re-entry?", "correct_answer": "STS-107",
     "incorrect_answers": ["STS-51-L", "STS-61-C", "STS-109"]},
    {"category": "Entertainment: Comics", "type": "multiple", "difficulty": "medium",
     "question": "Who was the inspiration for Cuthbert Calculus in the Tintin series?",
     "correct_answer": "Auguste Picard", "incorrect_answers": ["Jacques Piccard", "Will Morris", "J. Cecil Maby"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Rhode Island is actually located on the US mainland, despite its name.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "multiple", "difficulty": "hard",
     "question": "Townsend Coleman provided the voice for which turtle in the original 1987 series of \"Teenage Mutant Ninja Turtles\"?",
     "correct_answer": "Michelangelo", "incorrect_answers": ["Leonardo", "Donatello", "Raphael"]},
    {"category": "History", "type": "multiple", "difficulty": "hard",
     "question": "The son of which pope supposedly held a lecherous f&ecirc;te involving 50 courtesans in the papal palace?",
     "correct_answer": "Alexander VI", "incorrect_answers": ["Innocent V", "Urban II", "Pius III"]},
    {"category": "History", "type": "multiple", "difficulty": "hard",
     "question": "Which of these theoretical phycisists first predicted the existence of antimatter?",
     "correct_answer": "Paul Dirac", "incorrect_answers": ["Niels Bohr", "Albert Einstein", "Werner Heisenberg"]}
]


logo = """

$$\   $$\ $$\                 $$\                 $$\                   $$\      $$\           $$\ $$\           $$\ 
$$ | $$  |$$ |                $$ |                $$ |                  $$$\    $$$ |          $$ |\__|          \__|
$$ |$$  / $$$$$$$\   $$$$$$\  $$ | $$$$$$\   $$$$$$$ |                  $$$$\  $$$$ | $$$$$$\  $$ |$$\ $$$$$$$$\ $$\ 
$$$$$  /  $$  __$$\  \____$$\ $$ |$$  __$$\ $$  __$$ |                  $$\$$\$$ $$ |$$  __$$\ $$ |$$ |\____$$  |$$ |
$$  $$<   $$ |  $$ | $$$$$$$ |$$ |$$$$$$$$ |$$ /  $$ |                  $$ \$$$  $$ |$$$$$$$$ |$$ |$$ |  $$$$ _/ $$ |
$$ |\$$\  $$ |  $$ |$$  __$$ |$$ |$$   ____|$$ |  $$ |                  $$ |\$  /$$ |$$   ____|$$ |$$ | $$  _/   $$ |
$$ | \$$\ $$ |  $$ |\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$$ |       $$\        $$ | \_/ $$ |\$$$$$$$\ $$ |$$ |$$$$$$$$\ $$ |
\__|  \__|\__|  \__| \_______|\__| \_______| \_______|$$$$$$\\__|$$$$$$\\__|     \__| \_______|\__|\__|\________|\__|
                                                      \______|   \______|                                            
                                                                                                                     
                                                                                                                     
 $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$$\        $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\                               
$$  __$$\ $$ |  $$ |\_$$  _|\____$$  |      $$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|                              
$$ /  $$ |$$ |  $$ |  $$ |      $$  /       $$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |                                    
$$ |  $$ |$$ |  $$ |  $$ |     $$  /        $$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\                                  
$$ |  $$ |$$ |  $$ |  $$ |    $$  /         $$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|                                 
$$ $$\$$ |$$ |  $$ |  $$ |   $$  /          $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |                                    
\$$$$$$ / \$$$$$$  |$$$$$$\ $$$$$$$$\       \$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\                               
 \___$$$\  \______/ \______|\________|       \______/ \__|  \__|\__|     \__|\________|                              
     \___|                                                                                                           
                                                                                                                     
                                                                                            
"""