person1 = ['9404044044', 'Anna']   #list
person2 = ('9504044044', 'Boris')  #tuple
person3 = ('9604044044', 'Maria')  #tuple
person4 = {'9704044044': 'Elena'}  #dict
person5 = {'9704044044', 'Martin'} #set - ?

person6 = (('9404044044', 'Anna'), ('9504044044', 'Boris'), ('9604044044', 'Darina'), ('9704044044', 'Elena'), ('9704044044', 'Martin'))

name1 = person1[1]
print('person1: ',name1)
print('person3: ', person3[1])
print('person4: ', person4['9704044044'])
print('person5: ', person5)

print('1st letter : ', person6[4][1][0])


