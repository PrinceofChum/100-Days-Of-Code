import pickle, HerCharacter, WhyShe, AdditionalReason

characterPickle = HerCharacter.HerCharacter('very good')
whyPickle = WhyShe.WhyShe('Topper and also a Programmer')
ReasonPickle = AdditionalReason.AdditionalReason('short and cute ')

with open('picklePack.dat', 'wb') as f:
    pickle.dump(characterPickle , f)
    pickle.dump(whyPickle , f)
    pickle.dump(ReasonPickle , f)
    
    print('<------- Pickling complted --------->')
