# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3157
 - ชื่อโจทย์ OJ: เกมสะสมแต้ม
 - OJ submission ID: 635036
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : รวมคะแนนเก็บสะสมแต้ม
 - Input: รับค่าจำนวนของสัญลักษณ์ และรับสัญลักษณ์บวกหรือลบตามจำนวนที่ได้ใส่เข้าไป
 - output: แสดงผมรวมคะแนนของเกมสะสมแต้ม

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าจำนวนของสัญลักษณ์ และรับสัญลักษณ์บวกหรือลบตามจำนวนที่ได้ใส่เข้าไป
 - Step 2: สร้างตัวแปรขึ้นมาเพื่อเก็บค่าของคะแนนรวมเอาไว้
 - Step 3: สร้างloopชึ้นมาและตั้งเงื่อนขึ้นมาถ้าตรงกับสัญลักษณ์บวกคะแนนจะเพิ่ม10 ถ้าตรงกับสัญลักษณ์ลบจะลด5
 - Step 4: แสดงค่าของผมคะแนนรวมทั้งหมด

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 4
+
_
_
+
10
 - Expected output : 10
 - Actual output : 10
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ใส่แต่ค่าลบ
 - Input1 : 4
-
-
-
-
 - Expected output : -20
 - Actual output : -20
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ใส่ค่าไม่ตรงกับจำนวนทั้งหมดของinput
 - Input1 : 2
-
+
+
+
+
 - Expected output : 5
 - Actual output : 5
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
