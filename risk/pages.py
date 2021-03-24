from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


class Instructions(Page):
    def vars_for_template(self):
        self.player.load_flips()
        self.player.load_payoffs()

        return self.player.get_payoffs()


class Risk(Page):
    form_model='player'
    form_fields=['risk_choice']

    def vars_for_template(self):
        # flip coins twice
        variables = self.player.get_payoffs()
        variables.update({'flips': self.player.format_flips()})
        return variables

    def before_next_page(self):
        self.player.lottery_outcome = random.randint(0,1)
        self.player.risk_payment = self.participant.vars['lotteries'][self.player.risk_choice-1][self.player.lottery_outcome]
        self.player.payoff += self.player.risk_payment
        # print(f"PLAYER PAYOFF {self.player.payoff}")


class Results(Page):
    def vars_for_template(self):
        # flip coins twice
        variables = self.player.get_payoffs()
        outcome = 'TAILS' if self.player.lottery_outcome else 'HEADS'
        variables.update({'outcome': outcome})
        return variables

    def before_next_page(self):
        self.player.participant.vars['task_one_payoff'] = self.player.payoff
        # print(f"TASK ON PAYOFF: {self.player.payoff}")

page_sequence = [Instructions, Risk, Results]
