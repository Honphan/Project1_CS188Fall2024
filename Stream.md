Để chạy game Pacman và kiểm tra các thuật toán tìm kiếm , thì sẽ sử dụng file **`pacman.py`** cùng với các tham số (arguments) trên dòng lệnh (terminal).

Trong file autograder cũng có phần này dùng để dành riêng cho chấm điểm

Ví dụ: ```python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs```
---

## I. Ý nghĩa câu lệnh và tham số

- Đầu tiên khi `python pacman.py` thì nó chạy vào `pacman.py` và gọi vào khối lệnh cuối file để lấy các đối số truyền vào từ terminal
- Sau khi lấy các giá trị từ đối số đó thì nó tạo các đối tượng tương ứng để tạo ra game pacman

Tất cả các lệnh đều bắt đầu bằng `python pacman.py` theo sau là các tham số:
- Các đối số được định nghĩa trong file `pacman.py` là method `readCommand` vào để đọc đầy đủ

| Tham số | Ý nghĩa | Ví dụ |
| :--- | :--- | :--- |
| **`-l,--layaout [LAYOUT]`** | Chọn bản đồ (Layout) | `-l tinyMaze` |
| **`-p,--pacman [AGENT]`** | Chọn Agent Pacman | `-p SearchAgent` |
| **`-a,--agentArgs [ARGS]`** | Truyền tham số cho Agent | `-a fn=bfs` |



---

