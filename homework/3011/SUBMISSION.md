# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3011
 - ชื่อโจทย์ OJ: Colors
 - OJ submission ID: 544590
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : ผสมแม่สีมีทั้งหมด3สี เมื่อผสมสี2สีจะได้สีใหม่จากแม่สี หากมีสีอื่นนอกเหนือจากแม่สีให้แสดงError
 - Input: นำสี 2 สีมาผสมกัน
 - output: สีใหม่ที่เกิดจากการผสมแม่สี 2 สี

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าสี 2 สี จากแม่สี
 - Step 2: ตั้งเงื่อนไขขึ้นมาเป็นกรณีของการผสมสี3สี
 - Step 3: เมื่อได้รับinputสีที่ไม่ตรงกับแม่สี ให้ขึ้นError
 - Step 4: แสดงสีที่ถูกผสมมา

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

พอตั้งเงื่อนไขขึ้นมาก็เกิดข้อผิดพลาดขึ้นมานั้นคือ การที่เงื่อนไขมันเยอะเกินไปทำให้ไม่ผ่าน จึงต้องใช้วิธีสร้าง dictionary ขึ้นมาเพื่อลดการใช้ if else ที่เยอะเกินไป แผนสุดท้ายที่ใช้คือวิธีนี้ก็ทำให้สามารถผ่านข้อนี้ไปได้

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : Red
 - Input2 : Blue
 - Expected output : Violet
 - Actual output : Violet
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : สีซ้ำกัน
 - Input1 : Blue
 - Input2 : Blue
 - Expected output : Blue
 - Actual output : Blue
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ทำเหมือน Test Case 1  แต่สลับลำดับการใส่ค่าสีเข้าไป
 - Input1 : Blue
 - Input2 : Red
 - Expected output : Violet
 - Actual output : Violet
 - Result: Passed

---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ผมได้คำแนะนำมาจากเพื่อนว่าให้ใช้ dictionary
 - ไม่ได้ใช้ AI

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
