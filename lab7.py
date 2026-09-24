from pokerkit import Automation, HandHistory, NoLimitTexasHoldem

game = NoLimitTexasHoldem(
    (
        Automation.ANTE_POSTING,
        Automation.BLIND_OR_STRADDLE_POSTING,
        Automation.BET_COLLECTION,
        Automation.CARD_BURNING,
        Automation.CHIPS_PUSHING,
        Automation.CHIPS_PULLING,
        Automation.HAND_KILLING,
        Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
    ),
    True,
    0,
    (1, 2),
    2
)

state = game(200, 2)
state.deal_hole('AsKs')
state.deal_hole('7d7c')
state.complete_bet_or_raise_to(6)
state.check_or_call()
state.deal_board('QsJs2c')
state.check_or_call()
state.complete_bet_or_raise_to(8)
state.fold()

hh = HandHistory.from_game_state(game, state)
hh.players = ['F', 'Bot']

with open('my_hand.phh', 'wb') as f:
    hh.dump(f)
print(open('my_hand.phh').read())

with open('my_hand.phh', 'rb') as f:
    replay = HandHistory.load(f)
for i, s in enumerate(replay):
    print(i, s.stacks)

