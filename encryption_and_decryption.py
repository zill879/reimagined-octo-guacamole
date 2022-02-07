#ENCRYPTION 
# This function takes no argument.It ask for message which you want to send and convert our message in number 0 and 1 but the list 
# of number it return is string 
def mess_to_val():
    binary_value=["0100000","1100001","1100010","1100011","1100100","1100101","1100110","1100111","1101000","1101001","1101010","1101011","1101100","1101101","1101110","1101111","1110000","1110001","1110010","1110011","1110100","1110101","1110110","1110111","1111000","1111001","1111010","1000001","1000010","1000011","1000100","1000101","1000110","1000111","1001000","1001001","1001010","1001011","1001100","1001101","1001110","1001111","1010000","1010001","1010010","1010011","1010100","1010101","1010110","1010111","1011000","1011001","1011010"]
    letter_list=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    message_value=[]
    message=input("Enter your message here but message only have to consist of alpabets no number or special character is allowed ")
    #this loop find value of letter from binary_value and appemd this value to message_value list
    for letter in message:
        for i in range(len(letter_list)):
            if(letter==letter_list[i]):
                message_value.append(binary_value[i])
    #this nested loop then take all values one by one and make a sinagle list of all numbers and append them to str_value         
    str_value=[]            
    for binval in message_value:
        for i in range(7):
            str_value.append(binval[i])
    return(str_value)

#This function takes one argument that is the value(list) in which you want to add hamming bits it returns list with hamming bits 
# and values in list of int
def add_ham_bits_int(str_value):
    #this convert each string to int and append it in intvalue
    intvalue=[]
    for i in range(len(str_value)):
        value=int(str_value[i])
        intvalue.append(value)    
    #this loop finds hamming position and add hamming bit to that position it will break when hamming position is great then list 
    # length
    hammingbits=0
    h="h"
    for i in range(len(intvalue)):
        hammingbits=2**i
        if(hammingbits>len(intvalue)):
            break    
        i=str(i+1)
        a=h+i
        intvalue.insert(hammingbits-1,a)
    return(intvalue)

#This function takes one argument and that is hamming bit int list after that it find hamming bit values and the scheme of hammming
#  bit is odd in this function and then it check that each hamming bit is odd and then make a list of index and check and return it 
def ham_bits_val(intvalue):
    #this loop picks all values of int hamming value list one by one 
    valuechart=[]
    for i in range(len(intvalue)):
        #for h1 
        if(i==0):    
            #the loop will start form first position and end at last position by skiping one number and append them in flat_list
            flat_list = []
            for k in range(0,len(intvalue),2):
                value=intvalue[k]
                flat_list.append(value)
        point=intvalue[i]
        #this if will find hamming(h) bits by checking each value to 1 and 0 if hamming bit comes it calculate its location by 
        # adding 1 and assign its index to number and append that index to pointindex
        pointindex=[]
        if((point!=1)and(point!=0)):
            index=i+1
            number=i
            pointindex.append(number)
        #this if will work when i is greater then 0 and when hamming bits come 
        if((i>0)and(number==i)):
            lists1=[]
            #adding index value to i so it being from that hamming position and not from start
            point=index+i
            #this loop will work for each hamming bit from h2 to onwards it will pick all values of intvalue one by one and 
            #append the h list in list 1
            for k in range(len(intvalue)):
                h=[]
                #this loop will make a list of each haming bit and it start form the position of hamming bits and skip value 
                # according to hamming bit condition and append them in h list
                for j in range(number,point):
                    shutdown=0
                    #it will break if j goes out of list
                    if (j>len(intvalue)-1):
                        shutdown=1
                        break
                    a=intvalue[j]
                    h.append(a)
                lists1.append(h)
                #if length of j goes out of list it will break out of k loop also making a complete list of all hamming bits one by
                # one 
                if (shutdown==1):
                    break
                #we add point to index so it skips the value accoring to hammming bit condition
                point1=point+index
                number=point1
                #we add point1 to index so the for loop runs only in range og hamming bit condition
                point=point1+index
            #to make list of list only single list
            flat_list = []
            for sublist in lists1:
                for item in sublist:
                    flat_list.append(item)
        #this loop will check the hamming schemes of all list of hamming if scheme is odd it will return 0 else 1
        pivot=0
        for k in range(len(flat_list)):
            if (flat_list[k]==1):
                pivot+=1
            ratio=pivot%2
            if (ratio==0):
                h1value=1
            else:
                h1value=0
        #it will apped check scheme output and hamming position to valuechart
        if((point!=1)and(point!=0)):        
            valuechart.append(pointindex)
            valuechart.append(h1value)
    return(valuechart)

#This function takes two arguments hamming bit int list annd valuechart containing position and value and return encrypted message
def encrypted_message(intvalue,valuechart):
    #this loop works in reversed 
    for i in range(-len(valuechart),0):
        ratio=i%2
        #it will check the position of number is odd or even if it is even then it will remove number from that position of intvalue 
        if(ratio==0):
            a=valuechart[i][0]
            intvalue.pop(a)
        #if odd it will insert that value at intvalue at the place of remove hamming(h) by its value   
        if(ratio!=0):
            intvalue.insert(a,valuechart[i])
    return(intvalue)    

#DECRYPTION
#This function takes one argument that is decrypted message it will find hamming position and return the list  of position
def hamming_position(messagepackage):
    hammingbits=0
    position=[]
    #work on complete list and append hamming position to position
    for i in range(len(messagepackage)):
        hammingbits=2**i
        # if hamming position is greater than list value it will break
        if(hammingbits>len(messagepackage)):
            break
        position.append(hammingbits-1)
    return(position)    

#This function takes two argument that is decrypted message and its position list it checks that the hamming bits come with right 
# value of hamming bit or not if it is right it will return 0 and create its list        
def hamming_checker(messagepackage,position):
    chart=[]
    on=0
    #this loop picks all values of decrypted list one by one 
    for i in range(len(messagepackage)):
        #it works only one time
        for p in range(1):
            #if i increase greater the list it will break otherwise it stores value in ind that is position
            if(i>len(position)-1):
                on=1
                break   
            ind=position[i]
        #if i increase then list it will break
        if(on==1):
            break
        if(ind==0):  
            flat_list=[]
            #this loop takes one value and skipn the other and append to flat_list
            for k in range(0,len(messagepackage),2):
                value=messagepackage[k]
                flat_list.append(value)
        #if ind means index is greater then 0
        if(ind>0):
            lists1=[]
            #we add 1 so it starts from next position
            index=ind+1
            number=ind
            #making stop point
            point=index+ind
            #it works for all values
            for k in range(len(messagepackage)):
                h=[]
                #start form hamming position and take values according to condition of hamming and leave values also and append 
                # them to list 1
                for j in range(number,point):
                    shutdown=0
                    #it wiil break if j increase from the length of decrypted list
                    if (j>len(messagepackage)-1):
                        shutdown=1
                        break
                    a=messagepackage[j]
                    h.append(a)
                lists1.append(h)
                #it will break as j increase the list length
                if (shutdown==1):
                    break
                #make start point of every hamming
                point1=point+index
                number=point1
                #end point of hamming bit
                point=point1+index
            flat_list = []
            #make list of list as singal list
            for sublist in lists1:
                for item in sublist:
                    flat_list.append(item)        
        pivot=0
        #work on hamming list and check the postion that it is even or odd  
        for k in range(len(flat_list)):
            if (flat_list[k]==1):
                pivot+=1
            ratio=pivot%2
            #if position is even it will return 1 else 0
            if (ratio==0):
                h1value=1
            else:
                h1value=0
        chart.append(ind)
        chart.append(h1value)
    return(chart)    

#This function encrypt the message by removing hamming bits and return the coming message
def decrypted_message(messagepackage,chart):
    #it will work in reverse
    for i in range(-1,-(len(chart)+1),-1):
         ratio=i%2
         #position is odd 
         if(ratio!=0):
            checkpoint=chart[i]
         #position is evennit will remove hamming bit from its position if it's value is right that means if it checkpoint is 0   
         if(ratio==0):
            index=chart[i]
            if (checkpoint==0):
                messagepackage.pop(index)
    return(messagepackage)

 #This function convert binary message into alphabets and return the message as alphabets it work on 7 bit of each character       
def binary_to_value(messagepackage):
    binary_value=["0100000","1100001","1100010","1100011","1100100","1100101","1100110","1100111","1101000","1101001","1101010","1101011","1101100","1101101","1101110","1101111","1110000","1110001","1110010","1110011","1110100","1110101","1110110","1110111","1111000","1111001","1111010","1000001","1000010","1000011","1000100","1000101","1000110","1000111","1001000","1001001","1001010","1001011","1001100","1001101","1001110","1001111","1010000","1010001","1010010","1010011","1010100","1010101","1010110","1010111","1011000","1011001","1011010"]
    letter_list=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list2=[]
    n=0
    start=0
    stop=7
    #till we come to list it will work
    while(n<=len(messagepackage)):
        n=n+7
        #if start value of loop increases the list length it will break out of while loop
        if(start>=len(messagepackage)):
            break
        list1=[]
        #it starts from the point of start and will continue from that point were it stops and not from start and make a list 
        # separate list of each variable
        for i in range(start,stop) :
            list1.append(str(messagepackage[i]))
        list2.append(list1)
        #so it starts from were it end
        start=start+7
        #stops after 7
        stop=stop+7
    final_str_list=[]
    #it will make all values of list as string hance making list of list as singal list of number
    for finval in list2:
        str_value="".join(finval)
        final_str_list.append(str_value)
    letter_message=[]
    #it will pick one value at a time from string number list
    for strfinalvalue in final_str_list:
        #it will pick one by one values from binary_Vlaue
        for i in range(len(binary_value)):
            #compare value from both list if it matches it wiil take value from letter_list at that position and apppend to 
            # letter_message
            if (strfinalvalue==binary_value[i]):
                letter_message.append(letter_list[i])
    #is will join list and give them as string
    return("".join(letter_message))   

stringnumberlist=mess_to_val()

hamming_message=add_ham_bits_int(stringnumberlist)

hamming_value_message=ham_bits_val(hamming_message)

encrypted_text=encrypted_message(hamming_message,hamming_value_message)
print("YOUR ENCRYPED MESSAGE IS {}".format(encrypted_text))
print("==========================================================================================================================")

position=hamming_position(encrypted_text)

chartofhamming=hamming_checker(encrypted_text,position) 

binaryvalue=decrypted_message(encrypted_text,chartofhamming)

final_message=binary_to_value(binaryvalue)
print("Your Meassage From The Sender is\n{}".format(final_message)) 
