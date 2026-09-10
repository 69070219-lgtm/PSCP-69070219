# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3232
 - ชื่อโจทย์ OJ: กบน้อยกระโดด
 - OJ submission ID: 646162
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 40-70 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : กบต้องการจะกระโดดไปข้างหน้าจนถึง y เมตร โดยที่จะกระโดดได้ครั้งละ x เมตร แต่หลังจากกระโดดไปค่า ของx จะลดลงไปเรื่อยๆครั้งละ2เมตร เราต้องหาว่ากบจะกระโดดกี่ครั้งจนถึงเป้าหมาย
 - Input: รับค่าว่ากบกระโดดได้กี่เมตร และกบต้องไปถึงระยะที่เท่าไหร่
 - output: จํานวนครั้งกระโดด

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่า x และ y และทำการsplitข้อความ
 - Step 2: สร้างตัวแปรเพื่อเก็บค่าเอาไว้
 - Step 3: ใชwhile loop ในการนับครั้งที่กบต้องกระโดด
 - Step 4: สร้างเงื่อนไขขึ้นมาถ้าถึงระยะyเมตรก็จะแสดงค่านั้นออกมา แต่ถ้าไม่ถึงก็จะแสดค่า -1

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 8 16
 - Expected output : 3
 - Actual output : 3
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : เป็นค่าที่ไม่มีวันไปถึงเป็าหมายแน่ๆ
 - Input1 : 1 10
 - Expected output : -1
 - Actual output : -1
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ที่กระโดดได้ กับเป้าหมายที่ต้องการไปเท่ากัน
 - Input1 : 10 10
 - Expected output : 1
 - Actual output : 1
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ไม่ได้ถาม TA หรือผู้อื่น
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
