# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3537
 - ชื่อโจทย์ OJ: Impostor
 - OJ submission ID: 695799	
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ :หาผู้ที่ยังอยู่ในยานอวกาศ และ ถูกขับไล่ออกนอกยานอวกาศไปแล้ว
 - Input: ชื่อและบทบาทระหว่างCrewmate หรือ Impostor และจะมีชื่อของผู้ที่ถูกใส่ร้ายและถูกไล่ออกจากยาน
 - output: จำนวน Impostor และ Alive ที่เหลืออยู่ พร้อมบอกชื่อและบทบาท และบบอกผู้ที่ตายด้วย

---

## 3. แผนแรกของฉัน

 - Step 1: รับชื่อและบทบาทของสมาชิกแต่ละคน แล้วนำมาเก็บไว้ใน Dict ที่สร้างขึ้น
 - Step 2: รับข้อมูลสมาชิกไปเรื่อยๆจนได้รับคำว่า Start จากนั้นเริ่มรับชื่อผู้ที่ถูกโหวตออกจนเจอคำว่าEnd
 - Step 3: ใช้ชื่อที่ถูกโหวตออกไปลบออกจาก Dict ของผู้ที่ยังมีชีวิตอยู่ และเก็บข้อมูลผู้ที่ถูกโหวตออกไว้ใน Dictionary อีกชุดหนึ่ง
 - Step 4: เรียงชื่อสมาชิกที่ยังอยู่และสมาชิกที่ถูกโหวตออก นับจำนวน Impostor ที่ยังเหลืออยู่ แล้วแสดงผลทั้งคนที่ยังมีชีวิตและตาย

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : ทดสอบข้อมูลตามตัวอย่างของโจทย์ มีทั้ง Crewmate และ Impostor และมีสมาชิกถูกโหวตออกหลายคน
 - Input1 : {"Green" : "Crewmate"}
 {"Cyan" : "Crewmate"}
 {"Red" : "Crewmate"}
 {"Pink" : "Crewmate"}
 {"Lime" : "Impostor"}
 {"Blue" : "Impostor"}
 {"White" : "Crewmate"}
 {"Orange" : "Crewmate"}
 Start
 Green
 Cyan
 White
 End
 - Expected output : 2 Impostor Remains
 ***Alive***
 Blue : Impostor
 Lime : Impostor
 Orange : Crewmate
 Pink : Crewmate
 Red : Crewmate
 ***Dead***
 Cyan : Crewmate
 Green : Crewmate
 White : Crewmate
 - Actual output : 2 Impostor Remains
 ***Alive***
 Blue : Impostor
 Lime : Impostor
 Orange : Crewmate
 Pink : Crewmate
 Red : Crewmate
 ***Dead***
 Cyan : Crewmate
 Green : Crewmate
 White : Crewmate
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ทดสอบกรณีไม่มีใครถูกโหวตออก
 - Input1 : {"Red" : "Impostor"}
 {"Blue" : "Crewmate"}
 {"Green" : "Crewmate"}
 Start
 End
 - Expected output : 1 Impostor Remains
 ***Alive***
 Blue : Crewmate
 Green : Crewmate
 Red : Impostor
 ***Dead***
 - Actual output :  1 Impostor Remains
 ***Alive***
 Blue : Crewmate
 Green : Crewmate
 Red : Impostor
 ***Dead***
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ทดสอบกรณีโหวต Impostor ออกทั้งหมด
 - Input1 : {"Red" : "Impostor"}
 {"Blue" : "Crewmate"}
 {"Green" : "Impostor"}
 Start
 Red
 Green
 End
 - Expected output : 0 Impostor Remains
 ***Alive***
 Blue : Crewmate
 ***Dead***
 Green : Impostor
 Red : Impostor
 - Actual output :  0 Impostor Remains
 ***Alive***
 Blue : Crewmate
 ***Dead***
 Green : Impostor
 Red : Impostor
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - เพื่อนในคำแนะนำเรื่อง logic ของโจทย์ข้อนี้
 - ไม่ได้ใช่ AI


---

## 8. คำรับรองของนักศึกษา

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
