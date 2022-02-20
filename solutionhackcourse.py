
import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)


# BAS
word = ['chayote fruit', 'kundong', 'dekopon', 'rose apple', 'mamey sapote', 'ackee', 'agave plant', 'bilimbi', "dead man's fingers", 'korlan', 'charichuelo fruit', 'kahikatea', 'babaco', 'bilimbi', 'calamansi', 'clementines', 'nere', 'loquat', 'fibrous satinash', 'batuan fruit']

str =''
wordset = []
for i in range(len(word)):
    for j in range(len(word)):
        for k in range(len(word)):
            str = word[i]+'-'+word[j]+'-'+word[k]
            wordset.append(str)
            k+=1
        j+=1
    i+=1    
        
#นัทเสร็จแล้ว ได้คำมา 8000 set of words fruit-fruit-fruit


# FON
port = []
x = range(20000,65535)
for j in x:
    var1 =  str(j)
    var2 = var1[3:5]
    if int(var2) == 17:
        port.append(j)
# นัทนายเอาไปทำต่อได้เลยตัดแล้วเหลือ  456 ports

#NUT
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

for j in range(len(wordset)):
    for i in port:
        # {
            # CODE ส่วนนี้ไปหาคำตอบจาก page ลุงเอง
            # ลุงให้ไว้หมดแล้ว
        # }
        j+=1  
    i+=1
    
#ส่งให้แม่ดู แล้วแม่ก็พูดว่า ถ้าไม่ขี้เกียจรอ เอาแบบนั้นก็ได้ลูก
#ยิงกันไปครึ่งวันกว่าจะเสร็จ ก็ไม่ได้ สงสัย server ปิด port ช่วงนั้น  
#แต่รอนานมาก

#แล้วแม่ก็เรียกไปคุย โดยถามว่า 
# 8000x456 กับ 456 x 8000 เท่ากันไม๊
# เราก็ตอบไปว่า เท่ากัน แม่บอกว่าเท่ากันในเรื่องจำนวนรอบ แต่ไม่เท่ากันในเรื่องเวลา
# 456 x 8,000 = 8,000x456 = 3,648,000 มันคือจำนวนรอบ

#แล้วแม่ก็ สาธิตด้วย testexecutetime.py ให้

#ถึงตรงนี้ก็ไปเปิด python testexecutetime.py รันได้เลย


#เข้าใจล่ะ โมนิดหน่อย
for i in port:
    for j in range(len(wordset)):
        # {
            # CODE ส่วนนี้ไปหาคำตอบจาก page ลุงเอง
            # ลุงให้ไว้หมดแล้ว
        # }
        j+=1  
    i+=1

#เร็วขึ้น แต่รอนานอยู่ดี กว่าจะครบ 

# แม่เรียกคุยรอบสอง
# รอกันจนเบื่อยังลูก normalize กันหน่อยไหม
# ต้นฉบับที่ลุงให้มานั้นคือเหมาะที่จะเอามาใช้ในกรณี รู้ port แล้ว
# network ถ้า connect ไม่ได้ มัน response time เร็ว
# เราจะไปเสียเวลา นั่งรอ loop ของ 8000 set ของ word ไปทำไม
# แล้วก็ไม่จำเป็นต้องไปนั่งรอว่า ส่งคำ หรือ รอรับ response กลับจาก server ในเมื่อที่ยิงสุ่มไปยังรู้ใช่หรือไม่
# ก็ในเมื่อเชื่อมต่อกันยังไม่ได้ แล้วจะส่งคำไปทำไม 
# โอเค โมกันใหม่ อีกรอบ เอาแค่หา port ที่มันเชื่อมกันติดพอ  

for j in port:
    try:
        s.connect(('104.248.39.146', j))
        print('Correct PORT :',j,"ESTABLISHED") 
        correctport = j
        break
    except:
        print('Sent port :',j,"Connection failed") 
    j+=1
    s.close()   
#ควรได้ correct port ใน step นี้

#สาได้ port ล่ะ เอาไป loop ยิงคำเลย
#SA
HOST = '104.248.39.146'  
PORT = correctport
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.connect((HOST, PORT))
for j in range(len(wordset)):
    # {
        # CODE ส่วนนี้ไปหาคำตอบจาก page ลุงเอง
        # ลุงให้ไว้หมดแล้ว
    # }
    j+=1        
    s.close()