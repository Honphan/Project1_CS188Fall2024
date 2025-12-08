

## TỔNG HỢP NHIỆM VỤ CÁC FILE TRONG DỰ ÁN PACMAN

### I. NHÓM LOGIC CỐT LÕI 
Code thuật toán và logic của game.

| Tên File | Nhiệm vụ chính | Chi tiết công việc |
| :--- | :--- | :--- |
| **`search.py`** | **Triển khai Thuật toán Tìm kiếm (AI Core)** | Chứa các thuật toán tìm kiếm phổ quát (generic) như **DFS**, **BFS**, **UCS**, và **A\***. Các hàm này chỉ làm việc với cấu trúc `SearchProblem`. |
| **`searchAgents.py`** | **Định nghĩa Bài toán & Heuristic** | Biến thế giới Pacman thành các bài toán: `CornersProblem`, `FoodSearchProblem`, v.v. Nó chứa logic của **`SearchAgent`** và là nơi bạn viết các hàm **Heuristic**. |
| **`util.py`** | **Cấu trúc Dữ liệu & Công cụ** | Cung cấp các cấu trúc dữ liệu cơ bản cho thuật toán: **`Stack`**, **`Queue`**, **`PriorityQueue`** (bắt buộc phải dùng cho các thuật toán tương ứng). Cung cấp hàm `manhattanDistance`. |

---

### II. NHÓM CƠ CHẾ TRÒ CHƠI 

Các file này tạo nên môi trường Pacman và quản lý trạng thái. ( **🔴 Lưu ý quan trọng:** Không sửa code).

| Tên File | Nhiệm vụ chính | Chi tiết công việc |
| :--- | :--- | :--- |
| **`pacman.py`** | **Quản lý Trạng thái Game (GameState)** | Chứa lớp **`GameState`** lưu trữ toàn bộ thông tin game tại một thời điểm (vị trí, thức ăn, điểm số). Quản lý logic va chạm cơ bản. |
| **`game.py`** | **Định nghĩa Khái niệm Cơ bản** | Định nghĩa các lớp cơ sở: `Agent`, `Directions`, `Configuration` (vị trí + hướng). Chứa lớp **`Grid`** (cấu trúc lưới 2D cho bản đồ). |
| **`layout.py`** | **Xử lý Bản đồ (Layout)** | Đọc file `.lay` (ví dụ: `mediumMaze.lay`), phân tích ký tự (`%`, `.`, `P`) và tạo ra đối tượng `Layout` chứa dữ liệu tĩnh của mê cung. |
| **`eightpuzzle.py`** | **Bài toán Mẫu (8-Puzzle)** | Định nghĩa game xếp hình 8-Puzzle. Dùng để kiểm tra tính tổng quát của các thuật toán tìm kiếm trong `search.py`. |

---

### III. NHÓM NHÂN VẬT & HIỂN THỊ 

  Các file để vẽ và hiển thị nhân vật, màn chơi.
  
| Tên File | Nhiệm vụ chính | Chi tiết công việc |
| :--- | :--- | :--- |
| **`ghostAgents.py`** | **Logic Agent Ma** | Chứa các lớp điều khiển Ma, từ `RandomGhost` (ngẫu nhiên) đến `DirectionalGhost` (theo hướng Pacman). |
| **`pacmanAgents.py`** | **Agent Pacman Cơ bản** | Cung cấp các Agent Pacman đơn giản cho mục đích thử nghiệm và so sánh. |
| **`keyboardAgents.py`** | **Điều khiển Bằng Bàn phím** | Cho phép người dùng điều khiển Pacman bằng các phím. |
| **`graphicsDisplay.py`** | **Hiển thị Đồ họa Game** | Quản lý việc vẽ các vật thể trong game lên cửa sổ đồ họa, sử dụng các hàm cấp thấp từ `graphicsUtils.py`. |
| **`graphicsUtils.py`** | **Công cụ Đồ họa Cấp thấp** | Cung cấp các hàm vẽ cơ bản (`circle`, `polygon`) dựa trên thư viện **`tkinter`** của Python. |
| **`textDisplay.py`** | **Hiển thị Văn bản ASCII** | Chế độ hiển thị tối giản, in trạng thái game dưới dạng ký tự ra terminal. |

---

### IV. NHÓM KIỂM THỬ & CẤU HÌNH 

  Các file để test logic game và chấm điểm

| Tên File | Nhiệm vụ chính | Chi tiết công việc |
| :--- | :--- | :--- |
| **`autograder.py`** | **Script Chấm điểm Chính** | Thực thi vòng lặp chấm điểm, chạy các test case, gọi các lớp test và so sánh kết quả của bạn với đáp án. |
| **`searchTestClasses.py`** | **Lớp Kiểm tra Chuyên biệt** | Định nghĩa cấu trúc của các bài kiểm tra Pacman cụ thể (`PacmanSearchTest`, `HeuristicTest`). |
| **`testParser.py`** | **Phân tích Cú pháp Test** | Đọc, phân tách nội dung từ các file `.test` và `.solution` thành dữ liệu có thể sử dụng được. |
| **`grading.py`** | **Tính điểm và Báo cáo** | Chứa logic lớp `Grades` để lưu trữ, tính toán điểm số và tạo ra các báo cáo cuối cùng. |
| **Thư mục `test_cases/`** | **Kho Kịch bản Test** | Chứa file đầu vào (`.test`) và đáp án (`.solution`) cho từng câu hỏi (q1-q8). |
