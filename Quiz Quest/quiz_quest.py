import random

question = {
    "science": [{"q":"What is the chemical symbol for water?", "a": "H2O"},
                {"q":"What planet is known as the Red Planet?", "a": "Mars"},
                {"q":"What is the powerhouse of the cell?", "a": "Mitochondria"},
                {"q":"What is the speed of light?", "a": "299,792,458 m/s"},
                {"q":"What is the boiling point of water?", "a": "100°C"}                
                ]
    ,
    "history": [{"q":"Who was the first president of the United States?", "a": "George Washington"},
                {"q":"In what year did the Titanic sink?", "a": "1912"},
                {"q":"Who was known as the Iron Lady?", "a": "Margaret Thatcher"},
                {"q":"What was the name of the ship that brought the Pilgrims to America?", "a": "Mayflower"},
                {"q":"Who discovered penicillin?", "a": "Alexander Fleming"}
                ]
    ,
    "pop culture": [{"q":"Who is the author of the Harry Potter series?", "a": "J.K. Rowling"},
                    {"q":"What is the highest-grossing film of all time?", "a": "Avatar"},
                    {"q":"Who sang 'Thriller'?", "a": "Michael Jackson"},
                    {"q":"What is the name of the fictional wizarding school in Harry Potter?", "a": "Hogwarts"},
                    {"q":"Who played Jack Dawson in Titanic?", "a": "Leonardo DiCaprio"}
                    ]
}

players = []
scores = {}
rounds = 3

def ask_question(player):
    cat=input("Choose a category: science, history, pop culture: ").lower()
    if cat not in question:
        print("Invalid category. moving to next player.")
        return None
    else:
        random_question=random.choice(question[cat])
        print(random_question["q"])
        return random_question["a"]

def show_scores():
    print("Scores: ")
    for player in players:
        print(f"{player} score is: {scores.get(player, 0)}")

def declare_winner():
    high=0
    winner=[]
    for player, score in scores.items():
        if score>high:
            high=score
            winner=[player]
        elif score == high:
            winner.append(player)
    if winner:
            print(f"The winner(s) is/are: {winner} with a score of {high}!")
    else:
            print("No one scored any points!")  

def main():
    print("Welcome! ")
    while True:
        try:    
            plnum=int(input("How many players? "))
            if plnum<1:
                print("Error, exiting the game ")
            else:
                break
        except ValueError:
            print("Invalid input, exiting")
            return

    for i in range(plnum):
        addplayer=input(f"Enter the {i+1} player name: ")
        players.append(addplayer)
        scores[addplayer]=0

    for round in range(rounds):
        print(f"Round number {round+1}")
        for player in players:
            correct_answer = ask_question(player) 
            if correct_answer:
                user_answer = input("Your answer: ")
                if user_answer.lower() == correct_answer.lower():
                    print("Correct!")
                    scores[player] = scores.get(player, 0) + 1
                else:
                    print(f"Wrong! The correct answer is: {correct_answer}")
            print("-" * 20)
        show_scores()
        
    declare_winner()

main()