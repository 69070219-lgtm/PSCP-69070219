# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3071
 - ชื่อโจทย์ OJ: จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r
 - OJ submission ID: 576225
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : หาว่าในช่วงตัวแปร2ตัว มีกี่จำนวนที่หารด้วยค่าตัวแปรที่เราใส่เข้าไปแล้วเหลือค่าเท่ากับอีกตัวแปรหนึ่ง
 - Input: จำนวนนับมา2จำนวน , รับค่าตัวหาร และรับเศษ
 - output: จำนวนที่หารด้วยตัวการและเหลือเศษตามค่าที่เราใส่เข้าไป

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่า4ค่า
 - Step 2: สร้างตัวแปรขึ้นมาเพื่อเอาไว้รับค่า
 - Step 3: ใช้ forloopในการหารจำนวนที่อยู่ระหว่างตัวแปร2แปร และเมื่อเจอก็จะนำ1ในค่าตัวแปรที่เอาไว้เก็บค่า
 - Step 4: แสดงค่าที่นับได้ออกมา

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 20
 - Input2 : 40
 - Input3 : 5
 - Input4 : 2
 - Expected output : 4
 - Actual output : 4
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ค่าตัวแปรแรกมากกว่าตัวแปรที่สอง
 - Input1 : 10
 - Input2 : 5
 - Input3 : 5
 - Input4 : 2
 - Expected output : 0
 - Actual output : 0
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ค่าของเศษมากกว่าตัวหาร
 - Input1 : 10
 - Input2 : 50
 - Input3 : 5
 - Input4 : 6
 - Expected output : 0
 - Actual output : 0
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
