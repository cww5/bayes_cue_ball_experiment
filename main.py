import turtle
import random


config = {
    'cue_hidden_on_start': False,
    'throws_hidden': False,
    'cue_color': 'blue',
    'throws_color': 'red',

    'num_guesses': 3
}

s = turtle.Screen()


def initialize_table():
    boundaries = turtle.Turtle()
    boundaries.fd(500)
    boundaries.bk(1000)


def initialize_table_actors():
    cue = turtle.Turtle(visible=config['cue_hidden_on_start'])
    throws = turtle.Turtle(visible=config['throws_hidden'])
    cue.color(config['cue_color'])
    throws.color(config['throws_color'])
    throws.up()
    cue.goto(x=random.randint(-500, 500), y=0)
    return cue, throws


def throw_ball(throws):
    throws.goto(x=random.randint(-500, 500), y=0)


def conduct_experiment(cue, thrown):
    num_turns = 0
    num_left, num_right = 0, 0
    num_correct, num_incorrect = 0, 0
    cue_pos = cue.xcor()
    while num_turns < config['num_guesses']:
        throw_ball(thrown)
        thrown_pos = thrown.xcor()
        while thrown_pos == cue_pos:
            throw_ball(thrown)
            thrown_pos = thrown.xcor()

        x_guess = input("Please guess if the thrown ball is 'left' or 'right' of the original cue ball").lower()
        while x_guess not in ('left', 'right'):
            x_guess = input("TYPO! Please guess 'left' or 'right'").lower()

        if x_guess == 'left':
            if thrown_pos < cue_pos:
                num_left += 1
                num_correct += 1
            elif thrown_pos > cue_pos:
                num_right += 1
                num_incorrect += 1
        elif x_guess == 'right':
            if thrown_pos > cue_pos:
                num_right += 1
                num_correct += 1
            elif thrown_pos < cue_pos:
                num_left += 1
                num_incorrect += 1
        print(f"Thrown ball positions compared to cue ball: #Left: {num_left} | #Right: {num_right}")
        # print(f"#Correct: {} | #Incorrect: {}")
        num_turns += 1


def main():
    initialize_table()
    cue_ball, thrown_ball = initialize_table_actors()
    conduct_experiment(cue_ball, thrown_ball)
    s.exitonclick()


if __name__ == "__main__":
    main()