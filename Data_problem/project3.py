import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

class Test:
    def countAndAmount(self):
        sum=0
        count=0
        k=[]
        with open("/home/ram/Downloads/customerdata(1).txt",'r') as f:
            for l in f:
               k.append(l.strip().split(","))
        for j in k:
            if len(j)==4 and j[-1]!="Amount":
                count=count+1
                sum=sum+int(j[-1])
        print("total amount="+str(sum))
        print("number of orders="+str(count))

    def custdetail(self):
        d={}
        k=[]
        with open("/home/ram/Downloads/customerdata(1).txt",'r') as f:
            for l in f:
                k.append(l.strip().split(","))

        for j in k:
            if len(j)==4 and j[-1]!="Amount":
                if j[-2] not in d:
                    d[j[-2]]=1
                else:
                    c=d[j[-2]]
                    c=c+1
                    d[j[-2]]=c
        print("customers with exactly 1 order:")                
        for key in d:
            if d[key]==1:
                print(key)  

    def distribution(self):
        d={}
        k=[]
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        with open("/home/ram/Downloads/customerdata(1).txt",'r') as f:
            for l in f:
                k.append(l.strip().split(","))

        for j in k:
            if len(j)==4 and j[-1]!="Amount":
                if j[-2] not in d:
                    d[j[-2]]=1
                else:
                    c=d[j[-2]]
                    c=c+1
                    d[j[-2]]=c                
        for key in d:
            if d[key]==1:
                count1 =count1+1

            elif d[key] == 2:
                count2 = count2+1

            elif d[key] == 3:
                count3 = count3+1

            elif d[key] == 4:
                count4 = count4+1                    
            else:
                count5 = count5+1
        print("customer order exactly one="+str(count1))
        print("customer order exactly two="+str(count2))
        print("customer order exactly three="+str(count3))
        print("customer order exactly four="+str(count4))  
        print("customer more than 4 ="+str(count5))  

        objects = ('order1', 'order2','order3','order4','order5')
        y_pos = np.arange(len(objects))
        performance = [count1,count2,count3,count4,count5]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('number of order')
        plt.show()


 

    
obj = Test()
obj.countAndAmount()
obj.custdetail()
obj.distribution()