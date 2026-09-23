from pokerkit import StandardHighHand, StandardLowHand

mine = StandardHighHand.from_game('AsKs', 'QsJsTs2d3d')
yours = StandardHighHand.from_game('AdAc', 'QsJsTs2d3d')

print(mine)
print(yours)
print(mine > yours)

# try it 
print(StandardHighHand('7c5d4h3s2c') > StandardHighHand('AcAd9h8s2c'))
print(StandardLowHand('7c5d4h3s2c') > StandardLowHand('AcAd9h8s2c'))