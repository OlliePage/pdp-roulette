import random


class MagicBall:
    history_of_recommendations = dict()

    def __init__(self, available_options):
        self.options = available_options

    def add_option(self, new_option):
        self.options.append(new_option)

    def remove_option(self, existing_option):
        self.options.remove(existing_option)

    def shake_ball(self):

        session_choice = random.sample(self.options, k=1)[0]

        if session_choice in MagicBall.history_of_recommendations:
            MagicBall.history_of_recommendations[session_choice] += 1
        else:
            MagicBall.history_of_recommendations[session_choice] = 1

        return f"You have been given {session_choice}"

    @staticmethod
    def return_shake_counts():
        return MagicBall.history_of_recommendations

    def __repr__(self):
        return f"MagicBall({self.options})"


mball = MagicBall(['Kaggle Notebooks',
                   'Academic Articles',
                   'Crack open a textbook',
                   'Side project',
                   'Youtube Lecture',
                   'MOOC Course', ])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(mball.__repr__())
