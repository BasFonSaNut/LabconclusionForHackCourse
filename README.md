# LabconclusionForHackCourse

- node นี้ เป็นการสรูปว่าพวกเราได้อะไร ระหว่างที่แม่บุญญา ปล่อยให้ทำโจทย์กันเอง หา port/หาคำ  ที่ใช่
- ยิงไปยัง ip ที่คุณลุงวิศวะ บอกไว้ เพื่อได้มาซึ่ง link ของการสมัคร เข้า Hack course
- สิ่งที่พวกเราได้ระหว่างทาง โดยเฉพาะเรื่อง executetime, response time, pointer
- ทำไมพวกเราถึงเลือกจบ code แบบ step by step ทั้งที่ loop ไปเลยแต่ต้นก็ได้
- หัวข้อนี้ประกอบด้วย 2 ไฟล์ 
- file 1 solutionhackcourse.py ไฟล์นั้นสรุปกระบวนการทั้งหมด ที่พวกเราทำกันตั้งแต่เริ่มต้น โดยไม่มีการก้าวก่าย(interfere) จากโค้ช (แม่บุญญา)
- ไฟล์ดังกล่าวมีการ แก้ไขบางส่วนของ code ฉบับที่รันจริงให้เป็นลักษณะ pseducode บ้างเพราะไม่อย่างนั้นจะกลายเป็น เฉลยคำตอบ ซึ่งผิดข้อหนดของกลุ่ม
- ไฟล์ดังกล่าวได้สอดแทรกบทสนทนา และ discussion ไปใน comment เพื่อให้ผู้เข้ามาอ่าน ได้สามารถเข้าใจอย่างจะแจ้งว่า
  เหตุอันใด ถึงต้อง normalize code ,เหตุอันใดถึง เลือกจะใช้ try,cache แทนที่ while True: ในบางส่วนงานของ network programming
  การ normalize code แบบ step by step อันนำไปสู่ การเลือกวิธีการ implement ง่ายๆ (simple) แต่เวลาที่ดำเนินการ (execute time) ต่างกันราวฟ้ากับเหว
- file 2 executetime.py เป็น code ที่โค้ช(แม่บุญญ)ใช้ สาธิตให้ดูว่าทำไม ที่เราเขียน loop กันตอนแรกถึงต้อง normalize code

หลังดูสาธิตของแม่ไปแล้ว เข้าใจแล้ว วันข้างหน้าหากยังยืนอยู่บนเส้นทางนี้ และ relation database ยังไม่ตาย!!!!
ให้จำความรู้สึกกับตัวเลขที่ สาธิตนั้นไว้ให้ดี เพราะหลักการเดียวกัน cache,pointer retrieval 
ในวงการ relation database เรียกว่า cartesian product เรียกไทยก็ตามตัว ผลคูณคาร์ทีเซียน

ในแต่ละไฟล์ source code(.py) ได้สอดแทรกบทสนทนา และ discussion ไปใน comment เพื่อให้ผู้เข้ามาอ่าน ได้สามารถเข้าใจอย่างจะแจ้งว่า
เหตุอันใด ถึงต้อง normalize code ,เหตุอันใดถึง เลือกจะใช้ try,cache แทนที่ while True: ในบางส่วนงานของ network programming


-----------------------------------------------------------------------------------
- 👋 สวัสดีครับ, นี่คือ github ในนามกลุ่มของ นักเรียน ป.5 4 คน น้องบาส น้องฝน น้องสา น้องนัท
- 👀 github ตัวนี้เป้าเหมายเพื่อใช้ในการส่ง การบ้าน และ เวิร์คชอบ จากการเข้า คลาส Python bootcamp 2022 
- 🌱 ของคุณลุงวิศวะสอนคำนวน (UncleEngineering)
- 💞️ ถ้าพี่ๆ เข้ามาเพื่อหวังจะเห็น code เทพๆ บอกไว้ก่อนเลยว่า "อย่าหวัง" ครับ 
- 📫 ถ้ามีอะไรแนะนำพวกเรา comment ไว้เลยครับ เพราะกว่าพวกผมจะ ขึ้น ม.1 มีเวลาอีกเยอะ
- ✨ ต้องรีบเก็บเกี่ยวประสบการณ์ครับ เพราะเห็นแนวข้อสอบย้อนหลังเข้า ม.1 แล้วหืดจับเลย จะเป็นลม
