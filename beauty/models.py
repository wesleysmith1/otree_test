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
    name_in_url = 'beauty'
    players_per_group = None
    num_rounds = 1

    beauty_payment = {
        1:(5.67,0),
        2:(7,0),
        3:(4.43,0),
        4:(5,0),
    }

    """
    This is which question maps to which if the user is willing to pay to change from 
    attractive to unattractive or vice versa depending on which question was selected
    """
    swaps = {1:2, 2:1, 3:4, 4:3}
    # quesitons ids with type of group associated
    question_group_map = {1:"attractive men", 2:"unattractive men", 3:"attractive women", 4:"self-interested"}

    switch_increment = .25

    num_switch_increments = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


beauty_choices = [[True, "Generous givers (send more than $6)"], [False, "Self-interested (send less than $6)"]]

class Player(BasePlayer):
    beauty1 = models.BooleanField(
        choices=beauty_choices,
        label="Raters on average agreed these were attractive men. Do you think that they are “generous” givers (send more than $6) or “self-interested” givers?",
        widget=widgets.RadioSelect,
    )
    beauty2 = models.BooleanField(
        choices=beauty_choices,
        label="Raters on average agreed these were unattractive men. Do you think that they are “generous” givers (send more than $6) or “self-interested givers?",
        widget=widgets.RadioSelect,
    )
    beauty3 = models.BooleanField(
        choices=beauty_choices,
        label="Raters on average agreed these were attractive women. Do you think that they are “generous” givers (send more than $6) or “self-interested” givers?",
        widget=widgets.RadioSelect,
    )
    beauty4 = models.BooleanField(
        choices=beauty_choices,
        label=" Raters on average agreed these were unattractive women. Do you think that they are “generous” givers (send more than $6) or “self-interested” givers?",
        widget=widgets.RadioSelect,
    )

    beauty_payment = models.CurrencyField(
        doc="""
            Amount players earned from survey questions.
        """
    )
    task_2_payoff = models.CurrencyField(
        doc="""
            Payment after wtp selected
        """
    )

    cost_to_switch = models.FloatField()
    question_selected = models.IntegerField()

    switched = models.BooleanField()

    wtp = models.FloatField(
        label="What is the maximum amount of points you are willing to pay to switch?",
        choices = [
            0.0,
            0.25,
            0.5,
            0.75,
            1.0,
            1.25,
            1.5,
            1.75,
            2.0,
            2.25,
            2.5,
            2.75,
            3.0,
            3.25,
            3.5,
            3.75,
            4.0,
            4.25,
            4.5,
            4.75,
            5.00,
        ],
    )
    
