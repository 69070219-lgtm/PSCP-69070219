# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3538
 - ชื่อโจทย์ OJ: B - Fully pair?
 - OJ submission ID: 696285
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 60-90 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ :หาว่าตัวอักษรใดไม่มีคู่
 - Input: ตัวอักษรภาษาอังกฤษซึ่งจะเป็นตัวพิมพ์เล็กเท่านั้น
 - output: ตัวอักษรที่ไม่มีคู่ แต่ถ้าหากมีคู่ครบให้ตอบว่า fully paired

---

## 3. แผนแรกของฉัน

 - Step 1: รับข้อความเข้ามา 1 บรรทัด
 - Step 2: วนตรวจสอบตัวอักษรแต่ละตัวและนับจำนวนครั้งที่ตัวอักษรนั้นปรากฏในข้อความ
 - Step 3: ถ้าตัวอักษรปรากฏเป็นจำนวนคี่ให้เพิ่มตัวอักษรนั้นลงในคำตอบ
 - Step 4: ถ้าไม่มีตัวอักษรที่ไม่มีคู่ให้แสดง fully paired แต่ถ้ามีให้แสดงตัวอักษรที่เหลือ

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : ทดสอบกรณีที่มีตัวอักษรเพียงตัวเดียว ซึ่งไม่มีคู่
 - Input1 : a
 - Expected output : a
 - Actual output : a
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ทดสอบกรณีที่มีตัวอักษรซ้ำหลายตัวและมีตัวอักษรที่ไม่มีคู่มากกว่าหนึ่งตัว
 - Input1 : xxayybzzk
 - Expected output : xak
 - Actual output : xak
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ทดสอบกรณีที่ตัวอักษรเดียวกันปรากฏ 5 ครั้ง
 - Input1 : aaaaa
 - Expected output : a
 - Actual output : a
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ถามเพื่อน เพื่อนแนะนำวิธีคิด logic ในลูปที่ใช้ตรวจสอบตัวอักษรแต่ละตัว
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
