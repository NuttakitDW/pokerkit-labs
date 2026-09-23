from pokerkit import Automation, PotLimitOmahaHoldem

state = PotLimitOmahaHoldem.create_state(
    (
        Automation.ANTE_POSTING,
        Automation.BET_COLLECTION,
        Automation.BLIND_OR_STRADDLE_POSTING,
        Automation.CARD_BURNING,
        Automation.HOLE_DEALING,
        Automation.BOARD_DEALING,
        Automation.CHIPS_PUSHING,
        Automation.CHIPS_PUSHING,
    ),
    True,
    0,
    (1, 2),
    2,
    200,
    2
)

print(state.can_complete_bet_or_raise_to(3))
print(state.min_completion_betting_or_raising_to_amount)

try:
    state.complete_bet_or_raise_to(3)
except ValueError as e:
    print('ValueError:', e)
    
print(state.stacks)
print(state.max_completion_betting_or_raising_to_amount)