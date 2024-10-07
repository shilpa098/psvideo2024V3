

let data=("admin1","admin2");

#control statements
import random;
#generate 100 random numbers
genData=0;
for i in range(1,10):
    genData=random.randint(1,500);
    if (genData>100):
      print(genData,end="\t");
    
<<<<<<< HEAD
=======
    
    
    
 
    
    
    
    
    
#type conversions

#hex form conversion
memoryAddress=255;
hexData=hex(memoryAddress)
print(hexData);
print("Memory Address in hex form %X" %(memoryAddress));
#complex Number
real=56;
imaginary=45;
print(complex(real,imaginary));
#binary to decimal
print(int('10010',2));
#decimal to binary
print(bin(56));

from datetime import date;
#format the date
print(date.today().strftime("%d/%m/%Y"));

#multiple assignments
ipaddress=copyaddress='178.8.8.91';
print(ipaddress,'=>',copyaddress);

>>>>>>> b018db6 (identidier demo)
