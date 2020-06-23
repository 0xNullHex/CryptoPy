'''
class reverse():
    def string(): 
        welcome=' Welcome to Strings reverser '
        p=welcome.center(80,'*')
        print(p)
        while True:
            name=input('enter whatever you want: \n>>> ')
            result=''
            a=len(name)

            for x in name:
                if len(name)!=0:
                    y=name[a-1]
                    a-=1
                    result+=y
            print(result)
'''
'''
    def for_lists():
        welcome=' Welcome to list reverser '
        p=welcome.center(80,'*')
        print(p)
        lists=[]
        a=len(lists)
        result=[]
        sign=True
        while sign==True:
            storing=input('enter your list value or press enter to exit: \n>>> ')
            if len(storing)!=0:
                lists.append(storing)
                print(lists,len(lists))
            else:
                sign=False
        for x in range(0,len(lists)):
            if len(lists)!=0:
                y=lists[a-1]
                a-=1
                result.append(y)
        if len(result)!=0:
            print(result)

'''
'''    
if __name__ == "__main__":
    w=reverse.string()
    #w=reverse.for_lists()
  '''  
