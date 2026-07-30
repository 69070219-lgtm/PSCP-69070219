# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3025
 - ชื่อโจทย์ OJ: Season
 - OJ submission ID: 550275
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 30-60 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : รับค่าเดือน และวันมา เพื่อตรวจสอบว่าเป็นฤดูกาลอะไร
 - Input: รับค่าเดือน และวันที่ของเดือนนั้นๆ
 - output: ฤดูกาล(ฤดูใบไม้ผลิ , ฤดูร้อน , ฤดูใบไม้ร่วง , ฤดูหนาว)

---

## 3. แผนแรกของฉัน

 - Step 1: รับค่าเดือนและวันที่
 - Step 2: ตั้งเงื่อนไขขึ้นมาถ้าเลขของเดือนเป็นค่านี้จะเป็นฤดูกาลอะไร
 - Step 3: ตั้งเงื่อนไขขึ้นมาอีกหนึ่งเงื่อนไขคือ ถ้าเกิดเป็นเดือนที่หารด้วย3ลงตัว และเป็นที่21ของเดือนนั้น จะกลายเป็นฤดูถัดไป
 - Step 4: แสดงค่าว่าได้ฤดูอะไร

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

ไม่เหมือนกับแผนแรกที่คิดไว้ เพราะผมลืมจุดนี้ไปว่า ถ้าเดือนนั้นเป็นเดือนที่3หารลงตัวและเป็นวันที่21จะกลายเป็นฤดูถัดไป แต่ถ้าเกิดก่อนวันที่21มันจะอยู่จะเป็นฤดูอะไร แผนสุดท้ายผมต้องเพิ่มเงื่อนไขเข้าไปเพิ่มอีกเงื่อนไขคือ ถ้าวันที่น้อยกว่าวันที่21จะกลายเป็นฤดูเหมือนเดือนก่อนหน้า

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นค่าที่ฤดูจะตรงตามเดือน
 - Input1 : 1
 - Input2 : 15
 - Expected output : winter
 - Actual output : winter
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : เป็นเดือนที่3นั้นหารลงตัว และวันที่มากกว่า21 จะทำให้เปลี่ยนเป็นฤดูถัดไป
 - Input1 : 6
 - Input2 : 25
 - Expected output : summer
 - Actual output : summer
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : เป็นเดือนที่3นั้นหารลงตัว แต่วันที่จะน้อยกว่า21
 - Input1 : 6
 - Input2 : 15
 - Expected output : spring
 - Actual output : spring
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
