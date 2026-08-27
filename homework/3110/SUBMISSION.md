# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3110
 - ชื่อโจทย์ OJ: สงคราม...ส่งด่วน
 - OJ submission ID: 599816
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : คํานวณค่าธรรมเนียมการส่งพัสดุจากที่หนึ่งไปอีกที่หนึ่ง
 - Input: รับค่าสถานที่ต้น ปลายทาง และน้ำหนักของพัสดุที่ต้องการส่ง
 - output: แสดงราคาทั้งหมดที่ต้องจ่าย

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าสถานที่ต้น ปลายทาง และน้ำหนักของพัสดุที่ต้องการส่ง
 - Step 2: ทำการsplitข้อความในบรรทัดที่1 และสร้างเงื่อนไขขึ้นมา
 - Step 3: เมื่อตรงกับเงื่อนไขนั้นๆจะแสดงจำนวนเงินทั้งหมดที่ต้องจ่ายออกมา และค่าที่แสดงเป็นทศนิยม2ตำแหน่ง
 - Step 4: แต่เมื่อค่าinputที่รับเข้ามาไม่ตรงกับเงื่อนไขใดๆเลยจะแสดงข้อความerror

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติที่มีอยู่ในเงื่อนไข
 - Input1 : CNX UBP
 - Input2 : 15
 - Expected output : 615.00
 - Actual output : 615.00
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ต้นทาง และปลายทาง เป็นสถานที่เดียวกัน
 - Input1 : CNX CNX
 - Input2 : 15
 - Expected output : Error
 - Actual output : Error
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : น้ำหนักพัสดุที่ส่งมีค่าเป็น0
 - Input1 : CNX UBP
 - Input2 : 0
 - Expected output : 15
 - Actual output : 15
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
