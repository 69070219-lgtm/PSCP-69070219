# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3160
 - ชื่อโจทย์ OJ: หาจำนวนเฉพาะ
 - OJ submission ID: 640028
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : หาจํานวนเฉพาะ ตั้งแต่ค่าเริ่มต้นถึงค่าค่าสุดท้าย
 - Input: จํานวนเริ่มต้นและจํานวนสุดท้ายที่ต้องการหาจํานวนเฉพาะ
 - output: แสดงจํานวนเฉพาะ และบอกจํานวนของจํานวนเฉพาะที่หาได้

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าเริ่มต้นและค่าสุดท้าย พร้อมกับทำการsplitค่าออกมา
 - Step 2: สร้างตัวแปรขึ้นมาเพื่อเอาไว้เก็บค่าจำนวนของจำนวนเฉพาะท้ังหมด และสร้างlistขึ้นมาเพื่อเก็บค่าจำนวนเฉพาะ
 - Step 3: สร้างเงื่อนไขภายในloop และนำค่าแต่ละตัวมาเช้คว่าเป็นจำนวนเฉพาะหรือไม่
 - Step 4: แสดงว่ามีกี่จำนวนที่เป็นจำนวนเฉพาะ และมีตัวอะไรบ้าง

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติตั้งแต่1-10
 - Input1 : 1 10
 - Expected output : 2 3 5 7
Total primes: 4
 - Actual output : 2 3 5 7
Total primes: 4
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ค่าเริ่มต้นและค่าสุดท้ายห่างกัน1
 - Input1 : 52 53
 - Expected output : 53
Total primes: 1
 - Actual output : 53
Total primes: 1
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ใส่จำนวนเฉพาะให้เหมือนกันทั้งจำนวนแรกและค่าสุดท้าย
 - Input1 : 2 2
 - Expected output : 2
Total primes: 1
 - Actual output : 2
Total primes: 1
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
