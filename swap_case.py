def swap_case(s):
    ne=""
    count1=0
    count2=0
    count3=0
    count4=0
    symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
    for _ in s:
        if(_.isupper())==True :
            count1+=1
            ne+=(_.lower())
        elif (_.islower())==True:
            count2+=1
            ne+=(_.upper())
        elif (_.isnumeric())==True:
            count4+=1
            ne+=_

        elif (_.isspace())==True:
            count3 +=1
            ne+=_ 
        elif _ in symbols:
            count4+=1
            ne+=_    
      


    return ne
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)