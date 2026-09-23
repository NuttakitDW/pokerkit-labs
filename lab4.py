# Use calculator

from pokerkit import (
    Card, Deck, StandardHighHand, calculate_equities, parse_range,
)

print(len(parse_range('AKs')), 'combos of AKs')
print(len(parse_range('AK')), 'combos of AK')
print(len(parse_range('22')), 'combos of 22')

eq = calculate_equities(
    (parse_range('AK') - parse_range('AKs'), parse_range('22-99')),
    Card.parse('QsJs2c'),
    2,
    5,
    Deck.STANDARD,
    (StandardHighHand,),
    sample_count=20000,
)

print('AsKs vs 7h7d on QsJs2c',eq)