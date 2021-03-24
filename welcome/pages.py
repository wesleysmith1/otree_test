import datetime

from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Welcome(Page):
    pass

    def before_next_page(self):
        self.player.consent_time = str(datetime.datetime.now())


class ConsentForm(Page):
    pass


page_sequence = [ConsentForm, Welcome,]
