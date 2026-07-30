# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3058
 - ชื่อโจทย์ OJ: BrickBridge
 - OJ submission ID: 574448
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : เราต้องการสร้างสะพาน และเรามีอิฐก้อนเล็กและใหญ่ เราต้องหาว่าจะต้องใช้อิฐก้อนเล็กกี่ก้อนน้อยที่สุด โดยที่จะใช้ก้อนใหญ่ให้มากที่สุดก่อนจึงจะใช้อิฐก้อนเล็ก
 - Input: รับค่ามา3ค่า โดยมีจำนวนของอิฐก้อนเล็กและใหญ่ และความยาวของสะพานที่เราต้องการสร้าง
 - output: จำนวนอิฐก้อนที่ใช้ในการสร้างสะพาน

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่า3ค่า
 - Step 2: หาจำนวนอิฐก้อนใหญ่ก่อนว่าเราจะใช้อิฐก้อนใหญ่น้อยสุดกี่ก้อน และหาว่าจำนวนที่เหลือของสะพานในการใช้อิฐสร้างมันเหลือเท่าไหร่
 - Step 3: ตั้งเงื่อนไขขึ้นมา ถ้าเกิดความยาวของสะพานที่เหลือ มันน้องกว่าหรือเท่ากับอิฐก้อนเล็กที่มีก็ให้แสดงค่าของความยาวสะพานที่เหลือออกมาเลย
 - Step 4: ถ้าไม่สามารถสร้างได้ ตอบ -1

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกันกับแผนแรกที่คิดไว้
---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 25
 - Input2 : 4
 - Input3 : 25
 - Expected output : 5
 - Actual output : 5
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : อิฐก้อนเล็กมีแค่1ก้อน และก้อนใหญ่ก็มีแค่1ก้อน
 - Input1 : 1
 - Input2 : 1
 - Input3 : 10
 - Expected output : -1
 - Actual output : -1
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : อิฐก้อนใหญ่มีมากกว่าอิฐก้อนเล็กและมากพอจะสร้างสะพานโดยที่ไม่จำเป็นต้องใช้อิฐก้อนเล็ก
 - Input1 : 2
 - Input2 : 5
 - Input3 : 15
 - Expected output : 0
 - Actual output : 0
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
