# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3536
 - ชื่อโจทย์ OJ: isPrime_large
 - OJ submission ID: 695702
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : หาว่าค่าจำนวนที่ใส่เข้าไปเป็นจำนวนเฉพาะหรือไม่
 - Input:  เป็นจำนวนนับ
 - output: หนึ่งบรรทัดเท่านั้นเพียง YES ถ้าเป็นจำนวนเฉพาะ หรือ NO ถ้าไม่เป็นจำนวนเฉพาะ

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าเข้ามา1บรรทัด
 - Step 2: สร้างตัวแปรสำหรับนับจำนวนตัวเลขที่หาร n ลงตัว
 - Step 3: วนลูปตรวจสอบตัวเลขตั้งแต่ 1 ถึง n ว่ามีตัวไหนบ้างที่หารด้วย n ลงตัว โดยจะใช้ %
 - Step 4: ถ้ามีตัวหารมากกว่า 2 ตัว ให้แสดง NO แต่ถ้ามีตัวหารเท่ากับ 2 ตัว ให้แสดง YES

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : ทดสอบจำนวนเฉพาะที่มีค่าน้อย
 - Input1 : 7
 - Expected output : YES
 - Actual output : YES
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ทดสอบจำนวนที่ไม่เป็นจำนวนเฉพาะ
 - Input1 : 6
 - Expected output : NO
 - Actual output : NO
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ทดสอบจำนวนเฉพาะที่มีค่ามากขึ้น
 - Input1 : 97
 - Expected output : YES
 - Actual output : YES
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
