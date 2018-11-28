x=1
while(x<=100):
        if(x%5==0 and x%3==0):
                print('fizzbuzz')
                
        elif(x%5==0):
                print('buzz')
        elif(x%2==0):
                print('fizz')
        else:                 
                print(x)
        x+=1  
