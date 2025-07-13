import numpy as np
import pandas as pd


def Decrypt(mmatt):

    df = pd.DataFrame(mmatt)

    size = len(list(df.iloc[-1]))

    #step 1

    base1 = np.ones((size,size))

    one1 = [5,6,1]

    two1 = [9,6,7]

    three1 = [2,5,8]

    default2 = [[],[],[]]

    custom_default2 = []

    cnt4 = 0
    cnt5 = 0

    for i in range(3):

        if cnt4==0:
            
            for j in range(size):

                lst = default2[cnt4]
                lst.append(one1[cnt5])
                cnt5+=1
                
                if cnt5==2:

                    cnt5=0
            cnt4+=1
            cnt5=0
            
        elif cnt4==1:

            for k in range(size):

                lst = default2[cnt4]
                lst.append(two1[cnt5])
                cnt5+=1

                if cnt5==2:

                    cnt5=0
            cnt4+=1
            cnt5=0
            
        elif cnt4==2:

            for l in range(size):

                lst = default2[cnt4]
                lst.append(three1[cnt5])
                cnt5+=1

                if cnt5==2:
            
                    cnt5=0

            cnt4+=1
            cnt5=0
            cnt4=1

    cnt6 = 0

    for i in range(size):

        custom_default2.append(default2[cnt6])
        cnt6+=1
        if(cnt6==2):

            cnt6=0


    custom_default2 = np.array(custom_default2)

    EM3 = np.multiply(mmatt,custom_default2)

    power = np.power(custom_default2,2)

    pp1 = np.add(power,1)

    final = np.rint(np.divide(EM3,pp1)).astype(int)

    #step2

    base = np.ones((size,size))

    one = [3,2,4]

    two = [6,4,6]

    three = [5,3,7]

    default = [[],[],[]]

    custom_default = []

    cnt2 = 0
    cnt3 = 0

    for i in range(3):

        if cnt2==0:
            
            for j in range(size):

                lst = default[cnt2]
                lst.append(one[cnt3])
                cnt3+=1
                
                if cnt3==2:

                    cnt3=0
            cnt2+=1
            cnt3=0
            
        elif cnt2==1:

            for k in range(size):

                lst = default[cnt2]
                lst.append(two[cnt3])
                cnt3+=1

                if cnt3==2:

                    cnt3=0
            cnt2+=1
            cnt3=0
            
        elif cnt2==2:

            for l in range(size):

                lst = default[cnt2]
                lst.append(three[cnt3])
                cnt3+=1

                if cnt3==2:
            
                    cnt3=0

            cnt2+=1
            cnt3=0
            cnt2=1

    cnt = 0

    for i in range(size):

        custom_default.append(default[cnt])
        cnt+=1
        if(cnt==2):

            cnt=0


    custom_default = np.array(custom_default)

    prod = np.multiply(final,custom_default)

    div = np.power(custom_default,2)

    divp1 = np.add(div,1)

    #Decrypted Matrix
    final2 = np.rint(np.divide(prod,divp1)).astype(int)

    return final2

def dcr(a,b):
	
	wrd = ''
	
	for i in range(len(a)):
		
		c = int(a[i])-int(b[i])
		
		wrd+=chr(c)
		
	return wrd
