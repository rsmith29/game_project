class Player:
    def __init__(self, name=''):
        self.name = name
    def get_name(self):
        self.name = input("What is your name? ")
player = Player()
player.get_name()

question_1 = "What is the capital of France?"
answer_1 = "Paris"
question_2 = "How many states does the United States have?"
answer_2 = 50
question_3 = "How many continents are there?"
answer_3 = 7
question_4 = "In what year did the Berlin Wall collapse?"
answer_4 = 1991
question_5 = "What country surrounds the Vatican?"
answer_5 = 'Italy'
question_6 = "What country is the 'Great Wall' in?"
answer_6 = 'China'
question_7 = "Canberra is the capital of which country?"
answer_7 = 'Australia'
question_8 = "What is the name of the tallest mountain in the world?"
answer_8 = 'Everest'
question_9 = "In what country would you find Stonehenge?"
answer_9 = "United Kingdom"
question_10 = "What is the name of the largest ocean?"
answer_10 = 'Pacific'

test_questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]
test_answers = [answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10]
answer_key = ['B', 'D', 'C', 'A', 'A', 'C', 'C', 'D', 'B', 'B']
test_prompts = ['A: Rome\nB: Paris\nC: Berlin\nD: Bern', 'A: 48\nB: 52\nC: 13\nD: 50', 'A: 6\nB: 5\nC: 7\nD: 4', 'A: 1991\nB: 1992\nC: 1990\nD: 1989', 'A: Italy\nB: France\nC: San Marino\nD: Spain', 'A: India\nB: United States\nC: China\nD: Japan', 'A: Italy\nB: Spain\nC: Australia\nD: New Zealand', 'A: Matterhorn\nB: K2\nC: Denali\nD: Everest', 'A: Iceland\nB: United Kingdom\nC: Greece\nD: Ireland', 'A: Indian\nB: Pacific\nC: Atlantic\nD: Arctic']
money_amounts = [0, 5000, 7000, 10000, 20000, 30000, 50000, 100000, 250000, 500000, 1000000]
test_dict = {key:value for key, value in zip(test_questions, test_answers)}

def who_wants_to_be_a_millionaire():
    print(f"{player.name}, welcome to Who Wants to Be a Millionaire. Good luck!")
    start_game = input('Are you ready to play? (yes or no) ')
    if start_game == 'yes':
        print('\nInstructions:\nFor each question, select the correct answer by choosing A, B, C or D.')

        for i in range(len(test_questions)):
            print('\n' + test_questions[i])
            print(test_prompts[i])
            answer = input("Answer: ").upper()
            if answer in answer_key[i]:
                print("\nThat is correct.")
                print('You have just earned ' + "${:,.0f}".format(money_amounts[i+1]) + '\n')
                if i < 9:
                    continue_quest = input("Answer the next question for a chance to win " + "${:,.0f}".format(money_amounts[i+2]) + ' (yes or no)')
                    if continue_quest == 'no' or '':
                        end_game = input("Are you sure you want to quit the game? ")
                        if end_game == 'yes':
                            print("\nCongratulations! You are going home with " + "${:,.0f}".format(money_amounts[i+1]) + '\n')
                            break
                        else:
                            continue
                else:
                    print("Congratulations! You are a Millionaire!")
            else:
                print(f"Correct Answer: {test_answers[i]}\n")
                if money_amounts[i] == 0:
                    print("Unfortunately you didn't get any correct. Please make sure to come back and play again!\n")
                    break
                else:
                    print("Congratulations! You are going home with " + "${:,.0f}".format(money_amounts[i]) + '\n')
    else:
        print("\nPlease come back when you are ready!")

    
who_wants_to_be_a_millionaire()