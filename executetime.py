import time
a= range(5)
b= range(10)

#loop ด้วย 5 x 10
start = time.time()
for aa in a:
    for bb in b:
        print(aa,':',bb)
        
done = time.time()  
exec_time = done - start 
print('Execute time :',exec_time)   


#loop ด้วย 10 x 5
start = time.time()
for bb in b:
    for aa in a:
        print(aa,':',bb)
        
done = time.time()  
exec_time = done - start 
print('Execute time :',exec_time)   

#สิ่งที่ได้จาก การสาธิต จำ pattern ไว้ให้ขึ้นใจ
#สมาชิกน้อยสุดอยู่ loop แรกเสมอ เพราะมันหย่อน ทีละ 1 ไปหาใน loop 2
#จนกว่าจะครบครบสมาชิกใน 2 หรือ จนกว่าจะเจอ
#pointer ของ loop แรกถึงจะขยับไปยังสมาชิกตัวถัดไป แล้วก็ไปเริ่มต้นค้นหา ใน 2 แต่ต้น
#แต่ละ 1 การขยับจน จนได้ผลการวิ่งใน 2 จนครบหรือเจอ มันเก็บผลลัพธ์การวิ่งนั้นไว้ใน cache 
#ที่เราเรียกว่า page ถ้าใครจับ relation database จะคุ้นคำนี้ดี 
#แต่เราไม่รู้จัก เราถอดเอาจากเทปเสียงแม่ 555

#แต่เราเข้าใจเรื่อง execute time แล้วนะ
#สรุป pattern ก็คือ
# น้อยสุด
#     น้อยถัดไป
#         .
#             .จนมากสุด
    


