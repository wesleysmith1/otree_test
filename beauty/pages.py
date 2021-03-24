from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, beauty_choices

import random


class Transition(Page):
    pass


class Instructions(Page):
    pass


class BeautySurvey(Page):
    form_model = 'player'
    form_fields = ['beauty1', 'beauty2', 'beauty3', 'beauty4']

    def vars_for_template(self):
        questions = [
            dict(
                name="beauty1",
                label="Raters on average agreed these were attractive men. Do you think that they are “generous” givers (send more than $6) or “self-interested” givers?",
                choices=beauty_choices,
            ),
            dict(
                name="beauty2",
                label="Raters on average agreed these were unattractive men. Do you think that they are “generous” givers (send more than $6) or “self-interested givers?",
                choices=beauty_choices,
            ),
            dict(
                name="beauty3",
                label="Raters on average agreed these were attractive women. Do you think that they are “generous” givers (send more than $6) or “self-interested” givers?",
                choices=beauty_choices,
            ),
            dict(
                name="beauty4",
                label=" Raters on average agreed these were unattractive women. Do you think that they are “generous” givers (send more than $6) or “self-interested” givers?",
                choices=beauty_choices,
            ),
        ]
        random.shuffle(questions)
        return dict(
            questions=questions
        )

    def before_next_page(self):
        # randomize question for payment
        question = random.randint(1,4)
        self.player.question_selected = question
        # convert from bool to int which maps to the index of the payoff
        answer = int(eval(f"self.player.beauty{question}"))

        # print(f"HERE IS THE ANSWER {answer}")

        self.player.beauty_payment = Constants.beauty_payment[question][answer]

        # print(f"ANSWER TO BEAUTY QUESTION {answer} BEAUTY PAYMENT {self.player.beauty_payment}")


class WillingToPaySwitch(Page):
    form_model = 'player'
    form_fields = ['wtp',]

    def vars_for_template(self):
        self.player.cost_to_switch = random.randint(0,Constants.num_switch_increments) * Constants.switch_increment

        # print(f"PLAYER COST TO SWITCH {self.player.cost_to_switch}")

        selected_group = Constants.question_group_map[self.player.question_selected]

        switch_num = Constants.swaps[self.player.question_selected]
        switch_group = Constants.question_group_map[switch_num]

        return dict(
            selected_group=selected_group,
            switch_group=switch_group,
        )

    def before_next_page(self):
        if self.player.wtp < self.player.cost_to_switch:
            self.player.task_2_payoff = self.player.beauty_payment
            self.player.switched = False
            # print(f"PLAYER DID NOT SWITCH")
        else: 
            # print(f"PLAYER SWITCHED")
            self.player.switched = True
            
            question_response = eval(f"self.player.beauty{self.player.question_selected}")
            other_question = Constants.swaps[self.player.question_selected]
            other_group_payoff = Constants.beauty_payment[other_question][question_response]
            self.player.task_2_payoff = other_group_payoff - self.player.wtp
            # print(f"OTHER GROUP PAYOFF PLAYER IS WITCHING TO: {other_group_payoff}. PLAYER WILLINGNESS TO PAY {self.player.wtp}")

        self.player.payoff = self.player.task_2_payoff + self.player.participant.vars.get('task_one_payoff', -100)

        # print(f"FINAL PLAYER PAYOFF {self.player.payoff}")

class Results(Page):
    def vars_for_template(self):
        return dict(
            task_1_payoff=self.player.participant.vars.get('task_one_payoff', -100)
        )


page_sequence = [Transition, Instructions, BeautySurvey, WillingToPaySwitch, Results]
