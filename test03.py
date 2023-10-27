# OOP

class IotSAU :
    # data/property/field/attribut
    major = 'SAU'
    name = ''

    # mathod (มันคือ function แต่เราไม่เรียกฟังก์ชัน)
    def showHi(self) :
        print('Hi.....')

    def introduceMySelf(self) :
        print(f'My name is {self.major}')
        print(f'My name is {self.major}')
        

# -------------------------------------
# สร้าง Object
obA = IotSAU( ) # เป็นการเรียกใช้ Constructor ของคลาสให้ทำงาน ( ถ้ามี )
obB = IotSAU( )

# การใช้งาน data ของ ocject คือ เอาค่ามันมาใช้ หรือเปลี่ยนค่าให้มันใหม่
