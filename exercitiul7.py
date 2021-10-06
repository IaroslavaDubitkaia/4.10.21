cifre = [0,1,2,3,4,5,6,7,8,9]
cod = [['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001'],
['0000','0001','0011','0010','0110','0111','0101','0100','1100','1101'],
['0000','0001','0010','0011','0100','1011','1100','1101','1110','1111'],
['0011','0100','0101','0110','0111','1000','1001','1010','1011','1100'],
['0110000','0110001','0110010','0110011','0110100','0110101','0110110',,'0110111','0111000','0111001']]
s = input('introduceti sisitemul de codare:')
if s=='Direct':
    print('codul cifrelor zecimale este =',cod[0])
elif s=='Gray':
    print('codul cifrelor zecimale este =',cod[1])
elif s=='Aiken':
    print('codul cifrelor zecimale este =',cod[2])
elif s=='Exces 3':
    print('codul cifrelor zecimale este =',cod[3])
elif s=='ASCII':
    print('codul cifrelor zecimale este =',cod[4])
else:
    print('eroare')