# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3024
 - ชื่อโจทย์ OJ: SurprisingVote
 - OJ submission ID: 560725
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : รับคะแนนรวมของ3คนและคะแนนสูงสุด ถ้าเกิดคะแนนสูงสุดและต่ำสุดห่างกันเกิน2คะแนน จะทำให้คนดูประหลาดใจ
 - Input: รับคะแนนรวมของ3คนและคะแนนสูงสุด 
 - output: ถ้าเกิดคะแนนห่างกันเกิน2คะแนนคนดูจะ "Surprising" แต่ถ้าห่างไม่เกิน2คะแนนคนดู "Not surprising"
---

## 3. แผนแรกของฉัน

 - Step 1: รับคะแนนรวมของ3คนและคะแนนสูงสุด
 - Step 2: หาคะแนนต่ำสุดเท่าที่จะเป็นไปได้
 - Step 3: สร้างเงื่อนไขขึ้นมา เมื่อนำคะแนนต่ำาุดที่เป็นไปได้มาบวก2แล้วแต่ยังน้อยกว่าคะแนนสูงสุดคนดูก็จะประหลาดใจ แต่ถ้าไม่เกินก็จะไม่ประหลาดใจ
 - Step 4: แสดงค่าออกมาว่าคนดูนั้นประหลาดใจหรือไม่

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกับแผนแรกที่คิดไว้
เมื่อลองทำตามก็ได้ผลออกมาว่าส่วนของlogicถูกต้อง

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าปกติ
 - Input1 : 30
 - Input2 : 15
 - Expected output : Surprising
 - Actual output : Surprising
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : เป็นจุดทศนิยม
 - Input1 : 25.5
 - Input2 : 12.36
 - Expected output : Surprising
 - Actual output : Surprising
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ใส่ค่าเข้าไปต่างกันให้มากที่สุดเท่าที่จะเป็นไปได้
 - Input1 : 30
 - Input2 : 1
 - Expected output : Not surprising
 - Actual output : Not surprising
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
