#-----Dictionary คือ ข้อมูลหลายข้อมูล ที่เป็น key:value  ซ้ำกันได้ ไม่มีลำดับ  อีกทั้งแก้ไขได้ด้วย-------------------
# key เป็น Srinf หรือ Integer ส่วน value เป็นอะไรก็ได้ (Number, string, boolean, list, tuple, set, dictionary) ห้ามเป็น True, False
my_dictionary1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30]} 
my_dictionary2 = {  'data1' : [10,20,30],
                    'data2' :(2,3,6),
                    'data3' :(22,43,26),
                    'data4': {  'x' : 111,
                                'y' : 222
                            }
                }

# หารเข้าถึงข้อมูลใดข้อมมุลหนึ่ง
print(my_dictionary1['name'])
print(my_dictionary1[555])
my_dictionary1['age'] = 50
print(my_dictionary1)
# อยากแสดงผล 20 ออกมา
print(my_dictionary1['wow'][1])
# อยากแสดงผลแสดงผล 222 ออกมา
print(my_dictionary2['data4']['y'])
print(my_dictionary2['data4']['y'])
print(my_dictionary2)
my_dictionary2['data5'] = 444
print(my_dictionary2)

# การเข้าถึงทุกข้อมูล
for xx in my_dictionary1 :
    print(xx)

print('------------------------------')

for xx in my_dictionary1.keys() :
    print(xx)

print('------------------------------')

for xx in my_dictionary1.values( ) :
    print(xx)

print('------------------------------')

for xx in my_dictionary1.items( ) :
    print(xx)

print('------------------------------')

# Dictionary Mathod
my_dictionary1.popitem( )
my_dictionary1.popitem( )
my_dictionary1.popitem( )
print(my_dictionary1)
my_dictionary2.pop('data3')
print(my_dictionary2)
print('------------------------------')
print(my_dictionary2['data2'])
print(my_dictionary2.get('data2'))