Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Bài 19 — E11: "Purely Contrastive Evidence"

Chào các em! Bài này nói về E11: đôi khi **không thấy một kết quả ở nơi đáng lẽ phải thấy** lại trở thành bằng chứng cho một kết quả khác. Đây là kiểu bằng chứng tương phản.

---

## 1. Mục tiêu bài học

Sau bài này, các em có thể:

1. Hiểu “contrastive evidence” là bằng chứng dựa trên đối chiếu.
2. Biết vì sao một “không-click” có kiểm soát có thể mang thông tin.
3. Đọc suy luận đường A/đường B ở mức dễ hiểu.

---

## 2. RCA: lỗi gốc mà E11 xử lý

**Triệu chứng:** Ta dễ nghĩ chỉ detector click mới là bằng chứng, còn không click thì không có thông tin.

**5 Whys ngắn:**

1. Vì sao dễ nghĩ vậy? Vì click là tín hiệu rõ ràng nhất.
2. Vì sao không click vẫn có thể quan trọng? Vì trong một thiết lập có kiểm soát, không click có thể loại trừ một khả năng.
3. Vì sao loại trừ là thông tin? Vì khi loại trừ A, ta có thể suy ra B nếu hệ chỉ có các khả năng đó.
4. Vì sao cần điều kiện kiểm soát? Vì không click do hỏng máy thì không phải bằng chứng tốt.
5. Gốc vấn đề là gì? Nhầm **absence of click** với **absence of evidence** trong mọi trường hợp.

---

## 3. Bài giảng chính

Hãy tưởng tượng có hai cửa A và B. Nếu bạn đi qua cửa A, chuông A chắc chắn reo. Nếu chuông A không reo, trong điều kiện chuông hoạt động tốt và chỉ có hai cửa, ta có thể suy ra bạn đã đi qua cửa B.

Trong E11, kiểu suy luận này được dùng để nói về bằng chứng tương phản: không có tín hiệu ở nơi đáng lẽ có tín hiệu có thể trở thành thông tin.

Mẫu suy luận:

```text
Nếu đi đường A → Detector A click.
Detector A không click.
Vậy hệ không đi đường A; trong bối cảnh hai đường, suy ra đường B.
```

---

## 4. Công thức dễ hiểu

Dạng ngắn:

```text
A → click_A
not click_A
therefore not A
```

Nếu chỉ có A hoặc B:

```text
not A → B
```

Trong nguồn, có thể dùng xác suất null:

```text
P_null
```

Đọc dễ hiểu:

```text
P_null = xác suất của kết quả không-click có ý nghĩa trong thiết lập kiểm soát
```

---

## 5. Minh họa dễ nhớ

```text
Chuông A hoạt động tốt
Nếu ai đi cửa A thì chuông reo
Chuông không reo
→ người đó không đi cửa A
→ nếu chỉ còn cửa B, người đó đi cửa B
```

Điều dễ thương ở đây là: sự im lặng cũng có thể nói điều gì đó, nếu bối cảnh đủ rõ.

---

## 6. Điều cần tránh hiểu sai

Không nói:

> Mọi trường hợp không có tín hiệu đều là bằng chứng.

Nói đúng hơn:

> E11 chỉ xem “không có tín hiệu” là bằng chứng khi thiết lập kiểm soát làm cho sự vắng mặt đó có ý nghĩa.

---

## 7. Câu hỏi trắc nghiệm dễ thương

**Câu 1.** E11 nói về điều gì?

A. Bằng chứng tương phản từ kết quả không-click có kiểm soát  
B. Cách làm bánh quy  
C. Cách chọn màu áo  
D. Một bài hát ru

**Câu 2.** Không-click khi nào có thể có ý nghĩa?

A. Khi thiết lập kiểm soát cho biết đáng lẽ phải click nếu khả năng A xảy ra  
B. Khi máy hỏng mà không ai biết  
C. Khi trời mưa  
D. Khi lớp học ồn

**Câu 3.** Nếu A thì chuông reo; chuông không reo; trong bối cảnh chỉ có A hoặc B, ta suy ra gì?

A. Không A, nên có thể là B  
B. A chắc chắn xảy ra  
C. Chuông biết giận  
D. Không có logic nào cả

**Câu 4.** `P_null` gần với ý nào nhất?

A. Xác suất của kết quả không-click có ý nghĩa  
B. Xác suất ăn kem  
C. Xác suất mèo ngủ  
D. Xác suất bút chì biết bay

**Câu 5.** Điều kiện quan trọng của E11 là gì?

A. Bối cảnh kiểm soát rõ ràng  
B. Detector có cảm xúc  
C. Bỏ hết vật lý chuẩn  
D. Không cần kiểm tra gì

**Đáp án:** 1.A — 2.A — 3.A — 4.A — 5.A

---

## 8. Nguồn liên quan trong dự án

- [E11 Purely Contrastive Evidence](../research_documents/category/vvv_qmrf_category_01_e11_purely_contrastive_evidence.md)
- [E9 Null Registering-System Event](../research_documents/category/vvv_qmrf_category_06_e09_null_registering_system_event.md)
