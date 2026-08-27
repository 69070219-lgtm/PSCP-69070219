# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3111
 - ชื่อโจทย์ OJ: สหกรณ์โรงเรียน
 - OJ submission ID: 631165
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : คําเงินค่าขนมในสหกรณ์โรงเรียน
 - Input: รับค่า ผู้ชื้อเป็นสมาชิกหรือไม่ ของที่ซื้อมีจำนวนกี่ชิ้น และรับค่าราคาของนั้นว่าราคากี่บาท
 - output: แสดงราคาทั้งหมดที่ต้องจ่าย พร้อมทั้งหักส่วนลด

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่า ผู้ชื้อเป็นสมาชิกหรือไม่ ของที่ซื้อมีจำนวนกี่ชิ้น และรับค่าราคาของนั้นว่าราคากี่บาท
 - Step 2: ทำloop เพื่อเก็บค่าราคาขนม และเก็บค่าเอาไว้ในตัวแปรที่สร้างไว้เป็นราคาทั้งหมด
 - Step 3: สร้างเงื่อนไขขึ้นมา และถ้าเข้าเงื่อนไขไหนก็นำ ราคาทั้งหมดไปหาส่วนลด และนำไปลบกับราคาทั้งหมดที่เก็บค่าเอาไว้
 - Step 4: แสดงค่าราคาทั้งหมดออกมา(ทศนิยม 2 ตําแหน่ง)

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับวิธีก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : Y
3
30
50
50
 - Expected output : 123.50
 - Actual output : 123.50
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : ราคารวมน้อยกว่า500
 - Input1 : Y
2
100
350
 - Expected output : 427.50
 - Actual output : 427.50
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ราคารวมมากกว่า500
 - Input1 : Y
2
400
350
 - Expected output : 712.50
 - Actual output : 712.50
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ได้คำแนะนำจากเพื่อน ให้เขียนแบบนี้ print(f"{all_price + 1e-9:.2f}") ในส่วนที่เพื่อนแนะนำให้เพิ่มเข้าไปคือ 1e-9 กันพลาดในกรณีที่ทศนิยมนั้นมีมากแล้วมีโอกาสคลาดเคลื่อน
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
