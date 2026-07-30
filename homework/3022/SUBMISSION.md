# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3022
 - ชื่อโจทย์ OJ: Temperature
 - OJ submission ID: 576026
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : คำนวณสูตรการเปลี่ยนค่าอุณหภูมิ เป็นหน่วยอุณหภูมิที่เราต้องการ
 - Input: ค่าอุณหภูมิ , หน่วยของค่าอุณหภูมิที่ใส่เข้าไป และ หน่วยของอุณหภูมิที่เราต้องแปลงค่าเป็นหน่วยนั้นๆ
 - output: อุณหภูมิที่ถูกแปลงค่าแล้ว

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าอุณหภูมิ และหน่วยของค่าที่ใส่เข้าไป พร้อมทั้งหน่วยที่ต้องการแปลงเป็นหน่วยนั้นๆ
 - Step 2: เปลี่ยนค่าทุกหน่วยของค่าที่ใส่เข้าใปในบรรทัดที่1ให้กลายเป็นหน่วยเซลเซียส(C)ทั้งหมด
 - Step 3: นำค่าอุณหภูมิที่ถูกแปลงค่าแล้วมาเข้าสูตรเพื่อหาค่าที่เราต้องการ
 - Step 4: แสดงอุณหภูมิที่ถูกแปลงค่าแล้ว

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

้เหมือนกับแผนแรกที่คิดเอาไว้ เมื่อลองทำตามก็ได้ผลออกมาว่าส่วนของlogicถูกต้อง

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 37.5
 - Input2 : C
 - Input3 : F
 - Expected output : 99.50
 - Actual output : 99.50
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : มีค่าเป็นจำนวนเต็มลบ
 - Input1 : -229.5
 - Input2 : F
 - Input3 : C
 - Expected output : -145.28
 - Actual output : -145.28
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : หน่วยของอุณหภูมิใส่เป็นตัวเล็ก 
 - Input1 : 69.85
 - Input2 : c
 - Input3 : k
 - Expected output : 343.00
 - Actual output : 343.00
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ได้คำแนะจากเพื่อนให้ใช้floatในการรับinput ตอนแรกผมใช้เป็นint
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
