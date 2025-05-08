
# Tic-Tac-Toe Solver using Minimax with Alpha-Beta Pruning

This Python program determines the best move for player `X` on a given Tic-Tac-Toe board using the Minimax algorithm with Alpha-Beta pruning.

---

## 📁 File Structure

```
project/
├── main.py
├── testcase/
│   ├── testcase1.txt
│   ├── testcase2.txt
│   ├── testcase3.txt
│   └── testcase4.txt
```

---

## ▶️ How to Run

1. **Mở terminal hoặc PowerShell** tại thư mục gốc của project.

2. **Chọn testcase** muốn chạy bằng cách sửa dòng `file_path` trong `main.py`.  
   Ví dụ:

   - **Testcase 1**:
     ```python
     file_path = './testcase/testcase1.txt'
     ```

   - **Testcase 2**:
     ```python
     file_path = './testcase/testcase2.txt'
     ```

   - Các testcase khác: thay bằng `testcase3.txt`, `testcase4.txt` tương ứng.

3. **Chạy chương trình**:

   ```bash
   python main.py
   ```

---

## 📄 Format của file testcase

Mỗi file `.txt` gồm 3 dòng, mỗi dòng 3 ký tự.  
Các ký tự hợp lệ là:

- `X` – người chơi X
- `O` – người chơi O
- `.` – ô trống

**Ví dụ (`testcase1.txt`):**
```
.X.
OO.
.X.
```

---

## ✅ Kết quả

Chương trình sẽ in ra:

- Các nước đi có thể thử với điểm số và độ sâu.
- Nước đi tốt nhất mà `X` nên chọn.

Ví dụ:
```
Thử đi (0,0) → Score: 1, Depth: 2
Thử đi (2,0) → Score: 0, Depth: 3
Best move là (0, 0) với score 1, depth 2
(0, 0)
```

---

## 📝 Ghi chú

- Chương trình kiểm tra tính hợp lệ của bàn cờ trước khi chạy.
- Nếu bàn cờ đã kết thúc, sẽ in ra `Game over`.
