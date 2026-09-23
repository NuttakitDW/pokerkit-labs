from pokerkit import KuhnPoker, Automation

AUTO = (
        Automation.ANTE_POSTING,
        Automation.BET_COLLECTION,
        Automation.BLIND_OR_STRADDLE_POSTING,
        Automation.CARD_BURNING,
        Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
        Automation.HAND_KILLING,
        Automation.CHIPS_PUSHING,
        Automation.CHIPS_PULLING,
    )
CARD = ['Ks', 'Qs', 'Js']
ACTION = ['pp', 'pbp', 'pbb', 'bp', 'bb']

def apply(state, action):
    if action == 'pp':
        state.check_or_call()
        state.check_or_call()
    elif action == 'pbp':
        state.check_or_call()
        state.complete_bet_or_raise_to()
        state.fold()
    elif action == 'pbb':
        state.check_or_call()
        state.complete_bet_or_raise_to()
        state.check_or_call()
    elif action == 'bb':
        state.complete_bet_or_raise_to()
        state.check_or_call()
    elif action == 'bp':
        state.complete_bet_or_raise_to()
        state.fold()
    else:
        raise RuntimeError('impossible')
    
for i in CARD:
    for j in CARD:
        if i == j:
            continue
        for k in ACTION:
            game = KuhnPoker.create_state(AUTO)
            game.deal_hole(i)
            game.deal_hole(j)
            apply(game, k)
            assert not game.status
            print(f'{i[0]} vs {j[0]}  {k:<4} {game.payoffs}')


    
