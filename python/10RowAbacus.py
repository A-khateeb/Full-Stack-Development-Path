def print_abacus(value):
    abacus = ['|00000*****   |','|00000****   *|',
              '|00000***   **|','|00000**   ***|',
              '|00000*   ****|','|00000   *****|',
              '|0000   0*****|','|000   00*****|',
              '|00   000*****|','|0   0000*****|']
    counter = 10
    digit = str(value)
    while(counter >=1):
        if(counter > len(digit)):
            print(abacus[0])
        else:
            print(abacus[int(digit[len(digit)-counter])])
        counter =   counter - 1




# print ("Abacus showing 0:")
# print_abacus(0)
#
# print ("Abacus showing 12345678:")
# print_abacus(12345678)
#
# print ("Abacus showing 1337:")
# print_abacus(1337)

print ("Abacus showing 1:")
print_abacus(1234)

