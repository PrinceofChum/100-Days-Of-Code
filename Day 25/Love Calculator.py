def LoveCalculator(name1,name2):
    counter=[]
    for let1 in name1:
        c=1
        if name2:
            for let2 in name2:
                if let1==let2:
                    c+=1
                    name2.remove(let2)
        counter.append(c)

    counter+=[1 for i in name2]

    def percentage(list1):
        newl=[]
        while len(list1)>1:
            newl.append(list1[0]+list1[len(list1)-1])
            del list1[0]
            del list1[len(list1)-1]
        else:
            newl+=list1

        if len(newl)==2:
            print(("\nThis feelingless Bot says just " +''.join(map(str, newl))+"%"))
            print("\nKeep supporting your Loved one and Spread Love \n")
        else:
            percentage(newl)
    
    percentage(counter)
    
    
    if __name__ == "__main__":
    choice=int(input("Press 1 for FLAMES \nPress 2 for Love Calculator\n"))
    if choice==2:
        print("\n<----- Love Calculator ----->\n")
        name1=list(input("Unga name sollunga.. --> ").lower().strip())
        name2=list(input("Avanga name enna.. --> ").lower().strip())
        LoveCalculator(name1,name2)
    else:
        print("Invalid Key")
