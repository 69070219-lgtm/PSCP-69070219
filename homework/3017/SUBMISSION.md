# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3017
 - ชื่อโจทย์ OJ: Bill
 - OJ submission ID: 545276
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : รวมค่าบริการของทางร้าน และvat เพื่อหาราคาสุดท้ายของงินที่ลูกค้าต้องจ่าย
 - Input: ราคาอาหาร ที่ไม่รวมvat และค่าบริการ
 - output: ราคาอาหารที่รวมทั้งvat และค่าบริการ

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าอาหาร
 - Step 2: หาค่าบริการของทางร้าน และVAT 7%
 - Step 3: นำค่าทั้งหมดมาคิดรวมกัน
 - Step 4: พิมพ์ค่าอาหารที่รวมค่าบริการ และVAT 7%ไว้แล้ว

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับแผนแรกที่คิดไว้ เพราะก่อนจะลงมือเขียนโค้ด ทำการคิดlogicไว้คร่าวๆก่อนจะลงมือเขียนโค้ดจริงๆ

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input : 555
 - Expected output : 653.24
 - Actual output : 653.24
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ราคาที่ค่าบริการของร้านน้อยกว่า 50
 - Input : 50
 - Expected output : 107.00
 - Actual output : 107.00
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ราคาที่ค่าบริการของร้านมากกว่า 1000
 - Input : 20000
 - Expected output : 22470.00
 - Actual output : 22470.00
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ผมได้คำแนะนำมาจากเพื่อน ว่าให้ใช้ if else ในการเขียน เพราะในโจทย์ข้อนี้มี2กรณีที่จะคิดไม่เหมือนกัน
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
