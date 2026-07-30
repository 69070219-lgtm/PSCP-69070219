# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3042
 - ชื่อโจทย์ OJ: หาร 10
 - OJ submission ID: 560886
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : รับค่าแล้วหาว่ามีตัวเลขใดบ้างที่หารด้วย 10 ลงตัว และแสดงค่านั้นออกมา
 - Input: รับค่าเป็นจำนวนเต็มบวก
 - output: แสดงจำนวนตั้งแต่ค่าจำนวนเต็มบวกที่ใส่เข้าไปจนถึง 0  ที่หารด้วย 10 ลงตัว 

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าจำนวนเต็มบวกเข้ามา1จำนวน
 - Step 2: นำค่าที่ได้มาทำมาหาเศษแล้วไปลบกับตั้งต้นที่ใส่เข้าไปเพราะ ค่าที่ใส่เข้าไปตอนแรกมีโอกาสจะมีหลักหน่วยตั้งแต่1-9
 - Step 3: นำค่าจำนวนนั้นไปลบ10เรื่อยๆจนถึง0
 - Step 4: แสดงจำนวนตั้งแต่แรกจนถึง0

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับแผนแรกที่คิดไว้

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 150
 - Expected output : 150 140 130 120 110 100 90 80 70 60 50 40 30 20 10 0
 - Actual output : 150 140 130 120 110 100 90 80 70 60 50 40 30 20 10 0
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : หลักหน่วยมีค่าตั้งแต่1-9
 - Input1 : 118
 - Expected output : 110 100 90 80 70 60 50 40 30 20 10 0
 - Actual output : 110 100 90 80 70 60 50 40 30 20 10 0
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : มีหลักหน่วยเพียงหลักเดียว
 - Input1 : 6
 - Expected output : 0
 - Actual output : 0
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - เพื่อนสอนวิธีการใช้ whileในข้อนี้ว่าควรใช้อย่างไร
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
