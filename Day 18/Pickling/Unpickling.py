import pickle, HerCharacter, WhyShe, AdditionalReason

f=open('picklePack.dat', 'rb')

objectList=[]

try:
    while True:
        object1=pickle.load(f)
        objectList.append(object1)
except EOFError:
    print('<------- Unpickling complted --------->')

objectList.append(100) #Just to check different cases
print('Objetcs Count: ', objectList.__len__())

for obj in objectList:
    if isinstance(obj,HerCharacter.HerCharacter):
        obj.getHerCharacter()
    elif isinstance(obj,WhyShe.WhyShe):
        obj.getWhyShe()
    elif isinstance(obj,AdditionalReason.AdditionalReason):
        obj.getAdditionalReason()
    else:
        print('\nUnknown type ', type(obj))
