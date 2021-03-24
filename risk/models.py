from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'risk'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'prisoner/risk.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def flip_coin():
    f = random.random()
    # print(f"here is the flip result {f}")
    return True if f<0.5 else False

class Player(BasePlayer):
    risk_payment = models.CurrencyField(
        doc = "Payment received for the participants risk choice.",
        initial = 0
    )

    risk_choice = models.PositiveIntegerField(
        doc="Which choice the participant made in the Eckel/Grossman single choice list risk task.",
        choices=[1,2,3,4,5,6],
    )

    lottery_outcome = models.BooleanField()

    # for coin flips, False is Heads True is Tails
    first_flip = models.BooleanField()
    second_flip = models.BooleanField()

    def load_flips(self):
        self.first_flip = flip_coin()
        self.second_flip = flip_coin()

    def format_flips(self):
        a = 'TAILS' if self.first_flip else 'HEADS'
        b = 'TAILS' if self.second_flip else 'HEADS'
        return (a, b)

    def load_payoffs(self):
        self.participant.vars['lotteries'] =  [[0]*2 for i in range(6)]
        self.participant.vars['lotteries'][0][0] = c(28.00)
        self.participant.vars['lotteries'][0][1] = c(28.00)
        self.participant.vars['lotteries'][1][0] = c(24.00)
        self.participant.vars['lotteries'][1][1] = c(36.00)
        self.participant.vars['lotteries'][2][0] = c(20.00)
        self.participant.vars['lotteries'][2][1] = c(44.00)
        self.participant.vars['lotteries'][3][0] = c(16.00)
        self.participant.vars['lotteries'][3][1] = c(52.00)
        self.participant.vars['lotteries'][4][0] = c(12.00)
        self.participant.vars['lotteries'][4][1] = c(60.00)
        self.participant.vars['lotteries'][5][0] = c(2.00)
        self.participant.vars['lotteries'][5][1] = c(70.00)

    def get_payoffs(self):
        return{
         'option1A':self.participant.vars['lotteries'][0][0],
         'option1B':self.participant.vars['lotteries'][0][1],
         'option2A':self.participant.vars['lotteries'][1][0],
         'option2B':self.participant.vars['lotteries'][1][1],
         'option3A':self.participant.vars['lotteries'][2][0],
         'option3B':self.participant.vars['lotteries'][2][1],
         'option4A':self.participant.vars['lotteries'][3][0],
         'option4B':self.participant.vars['lotteries'][3][1],
         'option5A':self.participant.vars['lotteries'][4][0],
         'option5B':self.participant.vars['lotteries'][4][1],
         'option6A':self.participant.vars['lotteries'][5][0],
         'option6B':self.participant.vars['lotteries'][5][1],
        }
