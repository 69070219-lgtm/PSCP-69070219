# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3135
 - ชื่อโจทย์ OJ: ของขวัญและขโมย
 - OJ submission ID: 640759
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 60-90 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : นับว่ามีทั้งหมดกี่คนที่ถูกพิจารณาในวงกลม โดยที่ถ้าเกิดได้พิจารณาที่คนขโมยก็จะหยุด และถ้าเกิดวงมาแล้วจนถึงจุดที่1ก็จะหยุด
 - Input: รับค่าทั้งหมด3ค่า 1.จำนวนคนทั้งหมดที่ยืนเป็นวงกลม 2.จำนวนที่นับต่อจากคนแรกนับต่อไปเป็นจำนวนNคน 3.ตำแหน่งของคนที่ขโมยไป
 - output: จำนวนคนที่ถูกพิจารณาทั้งหมดในวงกลม

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าทั้งหมด3ค่า 1.จำนวนคนทั้งหมดที่ยืนเป็นวงกลม 2.จำนวนที่นับต่อจากคนแรกนับต่อไปเป็นจำนวนNคน 3.ตำแหน่งของคนที่ขโมยไป
 - Step 2: สร้างตัวแปรขึ้นมาเพื่อเก็บค่าเอาไว้
 - Step 3: ใช้loopในการไล่พิจารณาแต่ละคนไปเรื่อยๆ
 - Step 4: แสดงจำนวนคนที่ถูกพิจารณา

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกับแผนแรกที่คิดไว้

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 9 7 4
 - Expected output : 4
 - Actual output : 4
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : คนที่ขโมยไปจะไม่ถูกพิจารณา
 - Input1 : 6 4 2
 - Expected output : 3
 - Actual output : 3
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : คนที่ขโมยคือคนที่1
 - Input1 : 5 4 1
 - Expected output : 1
 - Actual output : 1
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ได้คำแนะนำจากเพื่อนเรื่องของlogicในข้อนี้ในส่วนของการทำงานในloop
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
