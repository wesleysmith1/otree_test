from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['ethnicity', 'occupation', 'gender', 'age', 'economic_status']


page_sequence = [Survey,]
