# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3296
 - ชื่อโจทย์ OJ: RGB Mixed
 - OJ submission ID: 661123
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 15-30 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : ผสมสี2สี โดยที่เราจะหาค่าเฉลี่ยจากค่าสีR,G,Bของสีนั้นๆ
 - Input: ค่าสีR,G,B ของสี2สี
 - output: ผลลัพธ์การผสมสี2สี R, G, B

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าสีทั้ง2สี
 - Step 2: splitค่าสี R, G, B ของทั้ง2สีออกมาแยกกัน
 - Step 3: นำค่าสีR, G, Bที่ตรงกันมาหาค่าเฉลี่ย
 - Step 4: แสดงผลลัพธ์การผสมสี2สี R, G, B

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับแผนแรกที่คิดไว้ เพราะ logic ที่คิดไว้ในแผนแรกเมื่อลองนำมาทำจริงก็ได้ผลว่าสามารถใช้ได้จริงและถูกต้อง

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : ค่าสีR, G, B ตรงกันทั้ง2สีที่นำมาผสม
 - Input1 : 50 25 120
 - Input2 : 50 25 120
 - Expected output : 50 25 120
 - Actual output : 50 25 120
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : เป็นค่า 0 ทั้งหมด
 - Input1 : 0 0 0
 - Input2 : 0 0 0
 - Expected output : 0 0 0
 - Actual output : 0 0 0
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ค่าสีR, G, B ต่างกันทั้ง2สีที่นำมาผสม
 - Input1 : 123 321 145
 - Input2 : 158 654 64458
 - Expected output : 140 487 32301
 - Actual output : 140 487 32301
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
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
