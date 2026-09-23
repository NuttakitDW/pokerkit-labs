import random
from pokerkit import Automation, NoLimitTexasHoldem

AUTO = (
    Automation.ANTE_POSTING,
    Automation.BET_COLLECTION,
    Automation.BLIND_OR_STRADDLE_POSTING,
    Automation.CARD_BURNING,
    Automation.HOLE_DEALING,
    Automation.BOARD_DEALING,
    Automation.RUNOUT_COUNT_SELECTION,
    Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
    Automation.HAND_KILLING,
    Automation.CHIPS_PULLING,
    Automation.CHIPS_PUSHING
)

game = NoLimitTexasHoldem(AUTO, True, 0, (1,2), 2)

def random_bot(state):
    choices = []
    if state.can_fold():
        choices.append('fold')
    if state.can_check_or_call():
        choices.append('call')
    if state.can_complete_bet_or_raise_to():
        choices.append('raise')
    
    pick = random.choice(choices)
    if pick == 'fold':
        state.fold()
    elif pick == 'call':
        state.check_or_call()
    else:
        lo = state.min_completion_betting_or_raising_to_amount
        hi = state.max_completion_betting_or_raising_to_amount
        state.complete_bet_or_raise_to(random.randint(lo, hi))
        
def calling_station(state):
    if not state.can_check_or_call():
        raise RuntimeError(f'calling_station cannot check call at seat {state.actor_index}')
    state.check_or_call()
        

        
random.seed(1)
totals = [0, 0, 0]
for _ in range(5000):
    state = game(100, 3)
    while state.status:
        if state.actor_index == 0:
            calling_station(state)
        else:
            random_bot(state)
    assert sum(state.payoffs) == 0
    totals = [ t + p for t, p in zip(totals, state.payoffs)]

print('net chips after 5000 hands:', totals)
print('sum:', sum(totals))