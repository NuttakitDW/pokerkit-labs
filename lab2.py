# Play one hand with the Dealer

from pokerkit import Automation, NoLimitTexasHoldem

state = NoLimitTexasHoldem.create_state(
    (
        Automation.ANTE_POSTING,
        Automation.BET_COLLECTION,
        Automation.BLIND_OR_STRADDLE_POSTING,
        Automation.CARD_BURNING,
        Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
        Automation.HAND_KILLING,
        Automation.CHIPS_PUSHING,
        Automation.CHIPS_PULLING,
    ),
    True,
    0,
    (1, 2),
    2,
    200,
    2,
)

state.deal_hole('AsKs') # player 0
state.deal_hole('7h7d') # player 1
print('stacks :', state.stacks)
print('to act :', state.actor_index)
print('streets index :', state.street_index)

state.complete_bet_or_raise_to(6) # player one raise TO 6
state.check_or_call() # player 0 calls
state.deal_board('Qs Js 2c')

print('streets index :', state.street_index)

state.check_or_call() # player 0 checks
state.complete_bet_or_raise_to(8) # player 1 bets 8
state.check_or_call()

print('streets index :', state.street_index)

state.deal_board('Ts')
state.check_or_call()
state.check_or_call()

state.deal_board('7c')
state.complete_bet_or_raise_to(100)
state.check_or_call()

print('stacks :', state.stacks)
print('to act :', state.actor_index)

print('running? :', state.status)
print('stack :', state.stacks)
print('payoffs :', state.payoffs)

