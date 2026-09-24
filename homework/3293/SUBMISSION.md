# SUBMISSION.md

## 1. SUMISSION INFORMATION

 - หมายเลข OJ : oj3293
 - ชื่อโจทย์ OJ: BigFrame
 - OJ submission ID: 659778
 - สถานะ OJ: Passed
 - เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง : 15-30 minutes

 ---

## 2. ความเข้าใจโจทย์ของฉัน

 - สิ่งที่เข้าใจจากโจทย์ : นำข้อความที่เราใส่inputเข้าไปใส่ไว้ในกรอบ
 - Input: ข้อความที่เราต้องการใส่เข้าไป
 - output: ข้อความของเราที่ถูกใส่ไว้ในกรอบ

---

## 3. แผนแรกของฉัน

 - Step 1: รับinputเป็นข้อความที่เราต้องการจะใส่เข้าไปในกรอบ
 - Step 2: นำข้อความไปเก็บไว้ในlistเพื่อเช้คความยาวของข้อความ
 - Step 3: เช้คว่าข้อความไหนยาวสุดเพื่อหาความยาวของกรอบ
 - Step 4: แสดงข้อความที่ถูกล้อมรอบด้วยกรอบ

 ---

## 4. วิธีสุดท้ายที่ใช้จริง

เหมือนกับแผนแรกที่คิดไว้

---

## 5. การทดสอบของฉัน

### Test Case 1

 - เหตุผลที่เลือก : เป็นข้อความปกติ
 - Input : Hello
           my
           name
           is
           few
 - Expected output : *********
                     * Hello *
                     * my    *
                     * name  *
                     * is    *
                     * few   *
                     *********
 - Actual output : *********
                   * Hello *
                   * my    *
                   * name  *
                   * is    *
                   * few   *
                   *********
 - Result: Passed

 ### Test Case 2

 - เหตุผลที่เลือก : เว้นว่างไว้1บรรทัด
 - Input : Hello
           my
           name
           
           few
 - Expected output : *********
                     * Hello *
                     * my    *
                     * name  *
                     *       *
                     * few   *
                     *********
 - Actual output : *********
                   * Hello *
                   * my    *
                   * name  *
                   *       *
                   * few   *
                   ********* 
 - Result: Passed

 ### Test Case 3

 - เหตุผลที่เลือก : ทั้ง5บรรทัดมีแค่1บรรทัดที่มีข้อความ
 - Input : I





 - Expected output : *****
                     * I *
                     *   *
                     *   *
                     *   *
                     *   *
                     *****
 - Actual output : *****
                   * I *
                   *   *
                   *   *
                   *   *
                   *   *
                   *****
 - Result: Passed

 
---

## 6. ความช่วยเหลือจากคน / การร่วมมือ

 - ไม่ได้ถาม TA หรือบุคคลอื่นเพื่อช่วยเหลือในโจทย์ข้อนี้
 - ไม่ได้ใช้ AI


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
