from art import logo, vs
from random import choice
from game_data import data

def get_participant(current_participant_index):
    '''This function returns a random participant from the data list. 
    It picks another if the current_participant_index is the same already chosen.'''
    participant_index = choice(range(len(data)))
    while participant_index == current_participant_index:
        participant_index = choice(range(len(data)))
    return [participant_index, data[participant_index]]


def print_participant(participant, contender_place):
    print(f"Compare {contender_place}: {participant[1]['name']}, a {participant[1]['description']}, from {participant[1]['country']}")


def show_game_table(participant_a, participant_b, current_score):
    print(logo)
    if current_score > 0:
        print(f"You're right! Current score: {current_score}")
    print_participant(participant_a, 'A')
    print(vs)
    print_participant(participant_b, 'B')


def game():
    current_score = 0

    ## Get the first participant
    participant_a = get_participant(-1)
    participant_a_followers = participant_a[1]['follower_count']

    ## Get the second participant
    participant_b = get_participant(participant_a[0])
    participant_b_followers = participant_b[1]['follower_count']

    ## Print game table
    show_game_table(participant_a, participant_b, current_score)

    correct_answer = True

    while correct_answer:

        answer = ' '
        while answer != 'A' and answer !='B':
            answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        if answer == 'A':
            if participant_a_followers < participant_b_followers:
                correct_answer = False
        else:
            if participant_a_followers > participant_b_followers:
                correct_answer = False

        if correct_answer:
            current_score += 1
            
            participant_a = participant_b
            participant_a_followers = participant_b_followers
            participant_b = get_participant(participant_b[0])
            participant_b_followers = participant_b[1]['follower_count']

            show_game_table(participant_a, participant_b, current_score)
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")


continue_play = True
while continue_play:
    if input("Do you want to play a game of Higher & Lower? Type 'y' or 'n': ") == 'y':
        game()
    else:
        continue_play = False