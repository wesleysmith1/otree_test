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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.StringField(
        label='What is your age?', 
        choices=[
            'Under 12 years old',
            '12 - 17 years',
            '18 - 24 years',
            '25 - 34 years',
            '35 - 44 years',
            '45 - 54 years',
            '55 - 64 years',
            '65 - 74 years',
            '75 years or above',
            'Prefer not to say',
        ]
    )

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
    )

    ethnicity = models.StringField(
        choices=['White', 'Black', 'Native Hawaiian', 'American Indian', 'Asian', 'Hispanic', 'Other'],
        label='What is your ethnic group?'
    )

    occupation = models.StringField(
        choices=['Full-time Student', 'Unemployed', 'Employed', 'House wife/husband', 'Retired', 'Other'],
        label='What is your occupation?',
    )

    economic_status = models.StringField(
        choices=[
            'Less than $14,000',
            '$15,000 to $24,999',
            '$25,000 to $34,999',
            '$35,000 to $49,999',
            '$50,000 to 74,999',
            '$75,000 to 99,999',
            '$100,000 to $149,999',
            '$150,000 to $199,000',
            '$200,000 or more',
        ]
    )
