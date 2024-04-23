
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'first_part'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    session = subsession.session
    import random
    if subsession.round_number == 1:
        all_players = subsession.get_players()
        for player in all_players:
            player.treatment = random.choice([True, False])
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    treatment = models.BooleanField()
    answer_0 = models.LongStringField(blank=True)
    choice_0 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    answer_1 = models.IntegerField(blank=True)
    choice_1 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_2 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_3 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_4 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_5 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_6 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_7 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_8 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_9 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_10 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_11 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_12 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_13 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_14 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_15 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_16 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_17 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    choice_18 = models.BooleanField(choices=[[True, 'Оставить свой ответ'], [False, 'Использовать ответ ИИ']])
    answer_2 = models.IntegerField(blank=True)
    answer_3 = models.IntegerField(blank=True)
    answer_4 = models.IntegerField(blank=True)
    answer_5 = models.LongStringField(blank=True)
    answer_6 = models.IntegerField(blank=True)
    answer_7 = models.LongStringField(blank=True)
    answer_8 = models.IntegerField(blank=True)
    answer_9 = models.IntegerField(blank=True)
    answer_10 = models.IntegerField(blank=True)
    answer_11 = models.IntegerField(blank=True)
    answer_12 = models.IntegerField(blank=True)
    answer_13 = models.IntegerField(blank=True)
    answer_14 = models.IntegerField(blank=True)
    answer_15 = models.IntegerField(blank=True)
    answer_16 = models.IntegerField(blank=True)
    answer_17 = models.IntegerField(blank=True)
    answer_18 = models.IntegerField(blank=True)
    payoff1 = models.CurrencyField(initial=0, min=0)
    radio1 = models.IntegerField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']], widget=widgets.RadioSelectHorizontal)
    self_choice = models.IntegerField(choices=[[1, 'Топ 10%'], [2, 'Выше среднего, но не топ 10%'], [3, 'Ниже среднего']], widget=widgets.RadioSelect)
    payoff2 = models.CurrencyField(initial=0, min=0)
    answer_2_1 = models.IntegerField(blank=True)
    answer_2_2 = models.LongStringField(blank=True)
    answer_2_3 = models.IntegerField(blank=True)
    answer_2_4 = models.IntegerField(blank=True)
    answer_2_5 = models.IntegerField(blank=True)
    answer_2_6 = models.IntegerField(blank=True)
    answer_2_7 = models.IntegerField(blank=True)
    answer_2_8 = models.IntegerField(blank=True)
    email = models.LongStringField(label='1. Укажи свою почту РЭШ в формате ...@nes.ru')
    age = models.IntegerField(label='2. Сколько тебе лет?')
    faculty = models.IntegerField(choices=[[1, 'BAE'], [2, 'MAE'], [3, 'MAF'], [4, 'MIF'], [5, 'EDS'], [6, 'Другой'], [7, 'Выпускник(-ца)']], label='3. На каком факультете ты учишься?', widget=widgets.RadioSelect)
    year = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [0, 'Выпускник(-ца)']], label='4. На каком курсе ты учишься?', widget=widgets.RadioSelect)
    gender = models.IntegerField(choices=[[1, 'Мужской'], [0, 'Женский']], label='5. Укажи свой пол', widget=widgets.RadioSelect)
    success = models.CurrencyField(initial=0, min=0)
def is_displayed1(player: Player):
    participant = player.participant
    import time
    return participant.expiry1 - time.time() > 0
def is_displayed2(player: Player):
    participant = player.participant
    import time
    return participant.expiry2 - time.time() > 0
class Intro(Page):
    form_model = 'player'
class Instruction_1(Page):
    form_model = 'player'
class Example1(Page):
    form_model = 'player'
    form_fields = ['answer_0']
class Example2(Page):
    form_model = 'player'
    form_fields = ['choice_0']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_0'),)
class Before1(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry1 = time.time() + 10*60
class R1Task1(Page):
    form_model = 'player'
    form_fields = ['answer_1']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice1(Page):
    form_model = 'player'
    form_fields = ['choice_1']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_1'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_1') == 100 and player.choice_1 == True:
                player.payoff1 += 10
            elif player.choice_1 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task2(Page):
    form_model = 'player'
    form_fields = ['answer_2']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice2(Page):
    form_model = 'player'
    form_fields = ['choice_2']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_2'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_2') == 11 and player.choice_2 == True:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task3(Page):
    form_model = 'player'
    form_fields = ['answer_3']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice3(Page):
    form_model = 'player'
    form_fields = ['choice_3']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_3'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_3') == 31 and player.choice_3 == True:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task4(Page):
    form_model = 'player'
    form_fields = ['answer_4']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice4(Page):
    form_model = 'player'
    form_fields = ['choice_4']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_4'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_4') == 24 and player.choice_4 == True:
                player.payoff1 += 10
            elif player.choice_4 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task5(Page):
    form_model = 'player'
    form_fields = ['answer_5']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice5(Page):
    form_model = 'player'
    form_fields = ['choice_5']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_5'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_5') == 'четверг' and player.choice_5 == True:
                player.payoff1 += 10
            elif player.field_maybe_none('answer_5') == 'четверг ' and player.choice_5 == True:
                player.payoff1 += 10
            elif player.field_maybe_none('answer_5') == 'Четверг' and player.choice_5 == True:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task6(Page):
    form_model = 'player'
    form_fields = ['answer_6']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice6(Page):
    form_model = 'player'
    form_fields = ['choice_6']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_6'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_6') == 6000 and player.choice_6 == True:
                player.payoff1 += 10
            elif player.choice_6 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task7(Page):
    form_model = 'player'
    form_fields = ['answer_7']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice7(Page):
    form_model = 'player'
    form_fields = ['choice_7']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_7'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_7') == 'dog' and player.choice_7 == True:
                player.payoff1 += 10
            elif player.field_maybe_none('answer_7') == 'dog ' and player.choice_7 == True:
                player.payoff1 += 10
            elif player.field_maybe_none('answer_7') == 'Dog' and player.choice7 == True:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task8(Page):
    form_model = 'player'
    form_fields = ['answer_8']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice8(Page):
    form_model = 'player'
    form_fields = ['choice_8']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_8'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_8') == 18 and player.choice_8 == True:
                player.payoff1 += 10
            elif player.choice_8 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task9(Page):
    form_model = 'player'
    form_fields = ['answer_9']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice9(Page):
    form_model = 'player'
    form_fields = ['choice_9']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_9'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_9') == 21 and player.choice_9 == True:
                player.payoff1 += 10
            elif player.choice_9 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task10(Page):
    form_model = 'player'
    form_fields = ['answer_10']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice10(Page):
    form_model = 'player'
    form_fields = ['choice_10']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_10'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_10') == 4 and player.choice_10 == True:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task11(Page):
    form_model = 'player'
    form_fields = ['answer_11']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice11(Page):
    form_model = 'player'
    form_fields = ['choice_11']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_11'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_11') == 24 and player.choice_11 == True:
                player.payoff1 += 10
            elif player.choice_11 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task12(Page):
    form_model = 'player'
    form_fields = ['answer_12']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice12(Page):
    form_model = 'player'
    form_fields = ['choice_12']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_12'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_12') == 7 and player.choice_12 == True:
                player.payoff1 += 10
            elif player.choice_12 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task13(Page):
    form_model = 'player'
    form_fields = ['answer_13']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice13(Page):
    form_model = 'player'
    form_fields = ['choice_13']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_13'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_13') == 63 and player.choice_13 == True:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task14(Page):
    form_model = 'player'
    form_fields = ['answer_14']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice14(Page):
    form_model = 'player'
    form_fields = ['choice_14']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_14'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_14') == 9 and player.choice_14 == True:
                player.payoff1 += 10
            elif player.choice_14 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task15(Page):
    form_model = 'player'
    form_fields = ['answer_15']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice15(Page):
    form_model = 'player'
    form_fields = ['choice_15']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_15'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_15') == 12 and player.choice_15 == True:
                player.payoff1 += 10
            elif player.choice_15 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task16(Page):
    form_model = 'player'
    form_fields = ['answer_16']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice16(Page):
    form_model = 'player'
    form_fields = ['choice_16']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_16'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_16') == 7 and player.choice_16 == True:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task17(Page):
    form_model = 'player'
    form_fields = ['answer_17']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice17(Page):
    form_model = 'player'
    form_fields = ['choice_17']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_17'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_17') == 24 and player.choice_17 == True:
                player.payoff1 += 10
            elif player.choice_17 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Task18(Page):
    form_model = 'player'
    form_fields = ['answer_18']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class R1Choice18(Page):
    form_model = 'player'
    form_fields = ['choice_18']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(answer = player.field_maybe_none('answer_18'),)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed1(player) == True:
            player.success += 1
            if player.field_maybe_none('answer_18') == 7 and player.choice_18 == True:
                player.payoff1 += 10
            elif player.choice_18 == False:
                player.payoff1 += 10
            else:
                if player.treatment == True and player.payoff1 > 0:
                    player.payoff1 -= 10
                else:
                    player.payoff1 -= 0
        else:
             player.payoff1 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry1 - time.time()
class Before2(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry2 = time.time() + 5*60
class R2Task1(Page):
    form_model = 'player'
    form_fields = ['answer_2_1']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_1') == 54:
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class R2Task2(Page):
    form_model = 'player'
    form_fields = ['answer_2_2']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_2') == 'Витя':
                player.payoff2 += 10
            elif player.field_maybe_none('answer_2_2') == 'Витя ':
                player.payoff2 += 10
            elif player.field_maybe_none('answer_2_2') == 'витя':
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class R2Task3(Page):
    form_model = 'player'
    form_fields = ['answer_2_3']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_3') == 2:
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class R2Task4(Page):
    form_model = 'player'
    form_fields = ['answer_2_4']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_4') == 32:
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class R2Task5(Page):
    form_model = 'player'
    form_fields = ['answer_2_5']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_5') == 300:
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class R2Task6(Page):
    form_model = 'player'
    form_fields = ['answer_2_6']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_6') == 22:
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class R2Task7(Page):
    form_model = 'player'
    form_fields = ['answer_2_7']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_7') == 40:
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class R2Task8(Page):
    form_model = 'player'
    form_fields = ['answer_2_8']
    timer_text = 'Осталось времени для завершения этого раунда:'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if is_displayed2(player) == True:
            if player.field_maybe_none('answer_2_8') == 48:
                player.payoff2 += 10
            else:
                player.payoff2 += 0
        else:
             player.payoff2 += 0
    @staticmethod
    def get_timeout_seconds(player: Player):
        participant = player.participant
        import time
        return participant.expiry2 - time.time()
class SelfEsteem(Page):
    form_model = 'player'
    form_fields = ['radio1', 'self_choice']
    timer_text = 'Осталось времени для завершения этого раунда:'
class SocDem(Page):
    form_model = 'player'
    form_fields = ['email', 'age', 'faculty', 'year', 'gender']
class Results(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(payoff_final = player.payoff1 + player.payoff2,)
page_sequence = [Intro, Instruction_1, Example1, Example2, Before1, R1Task1, R1Choice1, R1Task2, R1Choice2, R1Task3, R1Choice3, R1Task4, R1Choice4, R1Task5, R1Choice5, R1Task6, R1Choice6, R1Task7, R1Choice7, R1Task8, R1Choice8, R1Task9, R1Choice9, R1Task10, R1Choice10, R1Task11, R1Choice11, R1Task12, R1Choice12, R1Task13, R1Choice13, R1Task14, R1Choice14, R1Task15, R1Choice15, R1Task16, R1Choice16, R1Task17, R1Choice17, R1Task18, R1Choice18, Before2, R2Task1, R2Task2, R2Task3, R2Task4, R2Task5, R2Task6, R2Task7, R2Task8, SelfEsteem, SocDem, Results]