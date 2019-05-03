print("----ยินดีต้อนรับสู่ร้าน Nutzu Shop----")
print("---------โปรดเข้าสู่ระบบ----------")
usernameinput = input("Username ::")
passwordinput = input("Password ::")
if usernameinput == ("admin")and passwordinput == ("1234"):
    print("ยินดีต้อนรับ!!")
    print("รายการสินค้าทั้งหมด")
    print("================")
    print("1.Iphone 6 ราคา 15,000 บาท")
    print("2.Iphone 6s ราคา 16,000 บาท")
    print("3.Iphone 7 ราคา 18,000 บาท")
    print("4.Iphone 8 ราคา 19,900 บาท")
    print("5.Iphone X ราคา 22,000 บาท")
    userselected = int(input("คุณต้องการซื้อสินค้าลำดับที่ :: "))
    if userselected == 1:
        firstitem = int(input("โปรดกรอกจำนวนสินค้าที่ต้องการซื้อ :: "))
        print("ภาษีมูลค่าเพิ่ม :: 7%")
        print("ยอดรวมราคาสินค้าที่คุณต้องจ่าย :: ",(15000+((15000*7)/100))*firstitem,"บาท")
    if userselected == 2:
        firstitem = int(input("โปรดกรอกจำนวนสินค้าที่ต้องการซื้อ :: "))
        print("ภาษีมูลค่าเพิ่ม :: 7%")
        print("ยอดรวมราคาสินค้าที่คุณต้องจ่าย :: ",(16000+((16000*7)/100))*firstitem,"บาท")
    if userselected == 3:
        firstitem = int(input("โปรดกรอกจำนวนสินค้าที่ต้องการซื้อ :: "))
        print("ภาษีมูลค่าเพิ่ม :: 7%")
        print("ยอดรวมราคาสินค้าที่คุณต้องจ่าย :: ",(18000+((18000*7)/100))*firstitem,"บาท")
    if userselected == 4:
        firstitem = int(input("โปรดกรอกจำนวนสินค้าที่ต้องการซื้อ :: "))
        print("ภาษีมูลค่าเพิ่ม :: 7%")
        print("ยอดรวมราคาสินค้าที่คุณต้องจ่าย :: ",(19900+((19900*7)/100))*firstitem,"บาท")
    if userselected == 5:
        firstitem = int(input("โปรดกรอกจำนวนสินค้าที่ต้องการซื้อ :: "))
        print("ภาษีมูลค่าเพิ่ม :: 7%")
        print("ยอดรวมราคาสินค้าที่คุณต้องจ่าย :: ",(22000+((22000*7)/100))*firstitem,"บาท")
else:
    print("รหัสผ่านไม่ถูกต้อง โปรดลองใหม่อีกครั้ง")