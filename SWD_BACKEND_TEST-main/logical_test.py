
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
thai_digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
special = ["ศูนย์", "เอ็ด", "ยี่"]
str = str("")
x = input()

max_digit = len(x)
for i in range(max_digit-1, -1, -1):
    if i == max_digit-1: # หลักหน่วย
        if max_digit == 1 and x[i] == "0": str = special[int(x[i])]
        elif max_digit == 1 and x[i] == "1": str = thai_digits[int(x[i])]
        elif x[i] == "1": str = special[int(x[i])]
        else: str = thai_digits[int(x[i])] + str
        
    elif i == max_digit-2: # หลักสิบ
        if x[i] == "0": continue
        str = " สิบ" + str
        if x[i] == "2": str = special[int(x[i])] + str
        else: str = thai_digits[int(x[i])] + str
        
    else:
        if x[i] == "0": continue
        elif i == max_digit-3:
            str = "ร้อย" + str
        elif i == max_digit-4:
            str = "พัน" + str
        elif i == max_digit-5:
            str = "หมื่น" + str
        elif i == max_digit-6:
            str = "แสน" + str
        elif i == max_digit-7:
            str = "ล้าน" + str
        
        str = thai_digits[int(x[i])] + str

print(str)