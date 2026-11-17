<div align="center">

# Y2A-Auto

<img src="static/img/favicon.png" width="96" alt="Y2A-Auto Logo" />

Công cụ tích hợp tự động chuyển video YouTube sang AcFun / bilibili.

[![License](https://img.shields.io/badge/license-GPL%20v3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://www.docker.com/)

Tự động hóa toàn bộ quy trình từ tải xuống, ASR, dịch phụ đề, kiểm tra chất lượng phụ đề, kiểm duyệt nội dung đến tải lên; tích hợp sẵn trang quản trị Web, giám sát YouTube và khả năng bảo trì.

[Bắt đầu nhanh](#bắt-đầu-nhanh) · [Tổng quan tính năng](#tổng-quan-tính-năng) · [Triển khai và chạy](#triển-khai-và-chạy) · [Bot Telegram](#phương-án-dbot-chuyển-tiếp-telegram-tùy-chọn) · [Hướng dẫn cấu hình](#hướng-dẫn-cấu-hình) · [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng) · [Thông báo đẩy](#thông-báo-đẩy) · [CookieCloud](#cookiecloud-tích-hợp) · [Tính năng bảo mật](#tính-năng-bảo-mật) · [Câu hỏi thường gặp](#câu-hỏi-thường-gặp)

---

</div>

<p align="center">
  <a href="https://t.me/Y2AAuto_bot" target="_blank">
    <img src="https://img.shields.io/badge/Telegram%20Bot-%40Y2AAuto__bot-2CA5E0?logo=telegram&logoColor=white" alt="Telegram Bot" />
  </a>
  <br/>
  <strong>Bot chuyển tiếp Telegram (instance công khai):</strong>
  <a href="https://t.me/Y2AAuto_bot">@Y2AAuto_bot</a>
  <br/>
  <sub>⚠️ Instance công khai được triển khai trên VPS cá nhân, máy chủ này đã bị chặn (tường lửa), không đảm bảo khả dụng; nếu không kết nối được, hãy làm theo
  <a href="#phương-án-dbot-chuyển-tiếp-telegram-tùy-chọn">hướng dẫn tự triển khai</a> để dựng bot của riêng bạn:
  <a href="https://github.com/fqscfqj/Y2A-Auto-tgbot">Y2A-Auto-tgbot</a></sub>
</p>

## Giới thiệu dự án

<p align="center">
  <img src="static/img/readme/dashboard-real.png" alt="Dashboard Screenshot" width="92%" />
</p>

<p align="center">
  <img src="static/img/readme/monitor-real.png" alt="Monitor Screenshot" width="45%" />
  <img src="static/img/readme/settings-real.png" alt="Settings Screenshot" width="45%" />
</p>

<div align="center">
  <sub>Trên đây là ảnh chụp màn hình các trang hiện tại.</sub>
</div>

## Điểm nổi bật

| Mô-đun tính năng | Mô tả |
| --- | --- |
| Tự động hóa toàn bộ quy trình | Xử lý trọn gói từ tải xuống, ASR, phụ đề, thông tin meta đến tải lên |
| Kiểm duyệt có thể kiểm soát | Hỗ trợ kiểm duyệt thủ công, tải lên bắt buộc, kiểm tra an toàn nội dung và bảo vệ đăng nhập |
| Triển khai linh hoạt | Hai chế độ Docker / local, hỗ trợ mã hóa bằng CPU và nhiều GPU |
| Giám sát và lấy dữ liệu | Hỗ trợ lấy dữ liệu định kỳ theo kênh / từ khóa YouTube và lưu lịch sử |
| Đẩy thông báo | Thông báo bất đồng bộ đa kênh qua WeCom, ServerChan, message-pusher |
| CookieCloud | Tự động đồng bộ YouTube Cookies từ dịch vụ CookieCloud |
| Bảo vệ an toàn | Bảo vệ bằng mật khẩu, khóa khi dò mật khẩu (brute-force), hết hạn phiên, chống path traversal |
| Bảo trì đầy đủ | Hỗ trợ dọn nhật ký, dọn file tải xuống, kiểm soát đồng thời và tự động bổ sung FFmpeg |

## Tổng quan tính năng

- Quy trình tự động
  - `yt-dlp` tải xuống video và ảnh bìa
  - Tự động hoặc theo yêu cầu nhận dạng giọng nói để tạo phụ đề, hỗ trợ Whisper, Voxtral
  - Dịch phụ đề, xử lý sau phụ đề, kiểm tra chất lượng phụ đề (QC) và burn-in phụ đề (ghép phụ đề vào video)
  - AI tạo tiêu đề, mô tả, thẻ tag và gợi ý chuyên mục
  - Kiểm duyệt an toàn nội dung (Alibaba Cloud Green)
  - Tự động tải lên AcFun / bilibili / cả hai nền tảng
- Trang quản trị Web
  - Danh sách nhiệm vụ, kiểm duyệt thủ công, tải lên bắt buộc
  - Trung tâm cài đặt quản lý theo nhóm: tổng quan vận hành, tài khoản và mạng, kiểm duyệt nội dung, mô hình AI, xử lý phụ đề, nhận dạng giọng nói, chuyển mã video, giám sát và bảo trì, bảo mật
  - Bảo vệ đăng nhập, khóa khi nhập sai quá số lần cho phép và quản lý mật khẩu
- Giám sát YouTube
  - Giám sát kênh và giám sát tìm kiếm theo từ khóa
  - Hỗ trợ chế độ latest / historical, lọc theo loại video và tự động thêm vào hàng đợi nhiệm vụ
  - Tích hợp sẵn lịch sử và khôi phục file cấu hình
- Thông báo đẩy
  - Ba kênh WeCom, ServerChan, message-pusher
  - Đẩy thông báo các sự kiện như thêm nhiệm vụ / hoàn thành / thất bại, đăng nhập thành công / bị khóa, đăng nhập bằng QR thành công / thất bại
  - Hàng đợi thử lại bất đồng bộ, khoảng thời gian tăng dần để đảm bảo gửi được
- Tích hợp CookieCloud
  - Tự động lấy YouTube / Google Cookies từ dịch vụ CookieCloud
  - Hỗ trợ chế độ mã hóa auto / legacy / aes-128-cbc-fixed
  - Kiểm tra và đồng bộ bằng một cú nhấp chuột trên Web UI
- Bot chuyển tiếp Telegram
  - Y2A-Auto-tgbot được triển khai độc lập, gửi trực tiếp link YouTube trong Telegram để gửi nhiệm vụ
  - Dùng API Token với quyền tối thiểu, instance công khai không đảm bảo khả dụng, nên tự triển khai
- Công cụ biến đổi phụ đề
  - Tự động tách dòng dài, chuẩn hóa dấu câu, lọc từ đệm / từ lặp
  - Phát hiện văn bản ảo giác (hallucination) và nhãn nhiễu, phát hiện mật độ văn bản quá cao
  - Xử lý sau như lệch thời gian, thời lượng tối thiểu, gộp các khoảng trống kề nhau
- Chuyển mã video
  - Hỗ trợ mã hóa phần cứng CPU / NVIDIA / Intel / AMD
  - Mặc định ưu tiên HEVC / H.265, nếu thất bại sẽ tự động quay về H.264
- Xác thực nền tảng
  - AcFun / bilibili hỗ trợ đăng nhập bằng cách quét mã QR
  - bilibili hỗ trợ nhập Cookie (định dạng Netscape / JSON)
- Bảo trì và môi trường
  - Windows có thể tự động bổ sung FFmpeg
  - Hỗ trợ dọn nhật ký, dọn file tải xuống và đường dẫn FFmpeg tùy chỉnh

## Cấu trúc dự án

```text
Y2A-Auto/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── docker-compose-build.yml
├── acfunid/
├── build-tools/
├── config/
├── cookies/
├── db/
├── downloads/
├── ffmpeg/
├── fonts/
├── logs/
├── modules/
├── static/
├── temp/
├── templates/
└── tests/
```

## Bắt đầu nhanh

Nên dùng Docker (không cần cài đặt thủ công Python, FFmpeg, yt-dlp).

1. Chuẩn bị Cookie (bắt buộc)
- `cookies/yt_cookies.txt`: Cookie đăng nhập YouTube
- `cookies/ac_cookies.json`: Cookie đăng nhập AcFun
- `cookies/bili_cookies.json`: Cookie đăng nhập bilibili
- Có thể dùng tiện ích trình duyệt để xuất `cookies.txt`, không commit file này vào kho (repo)

2. Khởi động dịch vụ

```bash
# Mặc định lấy image từ Docker Hub fqscfqj/y2a-auto:latest
# Nếu cần dùng GitHub Container Registry, có thể chuyển sang ghcr.io/fqscfqj/y2a-auto:latest
docker compose up -d
```

3. Mở Web
- Truy cập `http://localhost:5000`
- Khi vào lần đầu, nên cấu hình bảo vệ đăng nhập, tài khoản nền tảng và YouTube Cookie trước

Các thư mục sau được lưu trữ bền vững (persist) theo mặc định: `config/`, `db/`, `downloads/`, `logs/`, `temp/`, `cookies/`.

Lưu ý: phông chữ trong `fonts/` là dependency tích hợp sẵn của dự án, dùng để burn-in phụ đề; xem giấy phép tại `fonts/LICENSE.txt`.

## Triển khai và chạy

### Phương án A: Docker (khuyên dùng)

- Khởi động: `docker compose up -d`
- Dừng: `docker compose down`
- Khởi động lại: `docker compose restart`
- Nhật ký: `docker compose logs -f`

Nếu cần build image trên máy local, dùng:

```bash
docker compose -f docker-compose-build.yml up -d --build
```

Nếu nhật ký khởi động xuất hiện `PermissionError` khi ghi vào các thư mục mount như `config/`, `db/` hoặc `logs/`, hãy tạo các thư mục này trong thư mục dự án và đổi chủ sở hữu (owner) của chúng thành UID/GID mà ứng dụng trong container dùng (mặc định `1000:1000`):

```bash
mkdir -p config db downloads logs cookies temp
sudo chown -R 1000:1000 config db downloads logs cookies temp
```

Khi đã bật rootless Docker hoặc `userns-remap`, hãy dùng UID/GID thực tế mà UID 1000 trong container ánh xạ tới trên máy host; xem cách ánh xạ trong [tài liệu chính thức của Docker](https://docs.docker.com/engine/security/rootless/uid-gid-mapping/).

### Phương án B: Chạy trên máy local

Yêu cầu trước:
- Python 3.11+
- FFmpeg
- yt-dlp

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Truy cập `http://127.0.0.1:5000`.

### Phương án C: Gói portable Windows

- `build-tools/` cung cấp công cụ build file thực thi Windows
- Gói Windows Release chính thức thường đã tích hợp sẵn FFmpeg / FFprobe
- Nếu đóng gói thủ công, chỉ cần giữ nguyên vẹn thư mục `ffmpeg/`

### Phương án D: Bot chuyển tiếp Telegram (tùy chọn)

[Y2A-Auto-tgbot](https://github.com/fqscfqj/Y2A-Auto-tgbot) là một bot Telegram độc lập: gửi trực tiếp link video / playlist YouTube trong Telegram, bot sẽ gọi API `/tasks/add_via_extension` của dịch vụ này để gửi nhiệm vụ tải lên. Bot cần được triển khai riêng, không khởi động cùng dự án này.

> ⚠️ **Instance công khai không đảm bảo khả dụng.** [@Y2AAuto_bot](https://t.me/Y2AAuto_bot) chạy trên VPS cá nhân, máy chủ này đã bị chặn, có thể không truy cập được bất cứ lúc nào. Nếu cần dùng lâu dài và ổn định, hãy tự triển khai.

Các điểm chính khi tự triển khai (hướng dẫn đầy đủ về cách tạo Bot Token, phạm vi tác dụng của Token... xem [Y2A-Auto-tgbot README](https://github.com/fqscfqj/Y2A-Auto-tgbot#安装和部署)):

1. Tìm [@BotFather](https://t.me/BotFather) trên Telegram, gửi `/newbot` để tạo bot và lấy `TG_BOT_TOKEN` (có dạng `123456789:AAE...`)
2. Clone và khởi động bot:

   ```bash
   git clone https://github.com/fqscfqj/Y2A-Auto-tgbot.git
   cd Y2A-Auto-tgbot
   # Chỉnh sửa docker-compose.yml để điền TG_BOT_TOKEN (tùy chọn ADMIN_TELEGRAM_IDS), sau đó:
   docker compose up -d
   ```

3. Mở **Cài đặt → Vận hành và bảo mật → Telegram Bot API Token** trong dự án này, nhấp vào "Tạo Token" và sao chép ngay `y2a_tgbot_v1_...` (văn bản gốc chỉ hiển thị một lần)
4. Gửi `/settings` cho bot mới tạo trên Telegram, điền **Địa chỉ API** (địa chỉ của dự án này mà mạng nơi bot chạy có thể truy cập được, ví dụ cùng máy là `http://127.0.0.1:5000`, khác máy là `http://192.168.1.100:5000`) và **API Token**, rồi nhấp vào "🔬 Kiểm tra" để xác nhận kết nối thành công
5. Sau khi kiểm tra thành công, chỉ cần gửi trực tiếp link YouTube cho bot là có thể gửi nhiệm vụ

Token này chỉ được phép gọi `/tasks/add_via_extension`, không thể truy cập cài đặt, nhật ký hay các API khác, và có thể đặt lại hoặc thu hồi bất cứ lúc nào trên trang cài đặt.

## Hướng dẫn cấu hình

Lần chạy đầu tiên sẽ tự động tạo `config/config.json`. Nên cấu hình trước các nhóm tham số sau:

### Cơ bản và bảo mật

- `AUTO_MODE_ENABLED`: công tắc tổng cho chế độ đăng tải tự động không cần giám sát, mặc định `false`
- `password_protection_enabled`: bảo vệ Web bằng mật khẩu, mặc định `false`
- `LOGIN_MAX_FAILED_ATTEMPTS`: giới hạn số lần nhập sai liên tiếp, mặc định `5`
- `LOGIN_LOCKOUT_MINUTES`: thời gian khóa, mặc định `15`
- `LOGIN_SESSION_TIMEOUT_MINUTES`: thời gian chờ khi đăng nhập không hoạt động, mặc định `30` phút, tối thiểu `1`, việc truy cập trang được bảo vệ sẽ tự động gia hạn
- `UPLOAD_TARGET_DEFAULT`: nền tảng đăng tải mặc định, hỗ trợ `acfun`, `bilibili`, `both`
- `UPLOAD_APPEND_REPOST_NOTICE`: có tự động thêm tuyên bố đăng lại hay không, mặc định `true`

### Tài khoản và mạng

- `YOUTUBE_COOKIES_PATH`: đường dẫn YouTube Cookie
- `ACFUN_COOKIES_PATH`: đường dẫn AcFun Cookie
- `BILIBILI_COOKIES_PATH`: đường dẫn bilibili Cookie
- `BILIBILI_SUBMIT_API`: API đăng tải của bilibili, `auto` (mặc định, ưu tiên API PC của Bcut, nếu thất bại sẽ quay về Web) / `bcut_pc` / `web` (nếu sửa tay thành `bcut` hay các bí danh khác cũng sẽ được chuẩn hóa rồi mới lưu)
- `YOUTUBE_PROXY_ENABLED` / `YOUTUBE_PROXY_URL`: proxy tải xuống YouTube
- `YOUTUBE_API_PROXY_ENABLED` / `YOUTUBE_API_PROXY_URL`: proxy riêng cho API giám sát YouTube, không kế thừa proxy tải xuống
- `YOUTUBE_DOWNLOAD_THREADS`: số luồng tải xuống
- `YOUTUBE_THROTTLED_RATE`: giới hạn tốc độ tải xuống
- `YOUTUBE_API_KEY`: khóa YouTube Data API v3, tính năng giám sát cần khóa này
- `FFMPEG_LOCATION`: đường dẫn FFmpeg tùy chỉnh
- `FFMPEG_AUTO_DOWNLOAD`: tự động tải xuống FFmpeg khi thiếu trên Windows, mặc định `true`

> **Yêu cầu phiên bản FFmpeg: ≥ 5.1.** Tính năng burn-in phụ đề dùng `-fps_mode cfr` để kiểm soát chế độ tốc độ khung hình, tùy chọn này chỉ được thêm từ FFmpeg 5.1 (phiên bản 5.0 trở về trước chỉ nhận `-vsync` đã lỗi thời). FFmpeg đi kèm kho và FFmpeg tự động tải xuống (BtbN latest) đều cao hơn nhiều so với phiên bản này; nhưng nếu dùng `FFMPEG_LOCATION` để trỏ tới phiên bản cũ 5.0 trở về trước, đường dẫn mã hóa phần mềm sẽ thất bại ngay với lỗi `Unrecognized option 'fps_mode'` (bộ mã hóa không phải phần cứng không có cơ chế thử lại khi hạ cấp, nhiệm vụ sẽ báo lỗi trực tiếp).
>
> `VIDEO_CPU_CODEC=x265` còn yêu cầu thêm bản build FFmpeg đó có `libx265` (cần `--enable-gpl --enable-libx265`, cả BtbN và phiên bản đi kèm kho đều đáp ứng). Nếu thiếu, hệ thống sẽ tự động hạ cấp sang `libx264` và tiếp tục burn-in, không làm mất toàn bộ phụ đề chỉ vì thiếu thư viện.

### AI và đăng tải

- `OPENAI_API_KEY` / `OPENAI_BASE_URL` / `OPENAI_MODEL_NAME`: cấu hình AI toàn cục
- `OPENAI_THINKING_ENABLED`: có cho phép mô hình dùng chế độ suy nghĩ (thinking) hay không; khi tắt, hệ thống ưu tiên gửi công tắc gốc trong tài liệu của nhà cung cấp (DeepSeek Chat dùng `thinking`, Responses dùng `reasoning.effort=none`; Qwen Chat/Responses dùng `enable_thinking`; MiMo Chat dùng `thinking`, Responses dùng `reasoning.effort=none`). Nếu công tắc gốc bị endpoint từ chối với mã 400/422, hệ thống sẽ thử lại trong cùng một request với tham số chuẩn `reasoning_effort=none` / `reasoning.effort=none`, chỉ khi mọi dạng đều thất bại mới gỡ bỏ việc kiểm soát và ghi warning; lúc này mô hình có thể quay về hành vi suy nghĩ mặc định. DeepSeek/Ling/Hunyuan trên gateway bên thứ ba không có công tắc gốc đáng tin cậy, nên sẽ thử tham số chuẩn trước, rồi thử đối tượng `thinking` chung. Khi truy cập endpoint chính thức qua reverse proxy, không thể nhận diện nhà cung cấp từ tên miền, hệ thống sẽ thử từng cái theo thứ tự của bên thứ ba, nhưng sẽ không vì vậy mà bỏ qua việc thử tắt suy nghĩ. Các mô hình suy luận như dòng OpenAI o / GPT-5 có các giá trị `reasoning_effort` được hỗ trợ khác nhau theo từng thế hệ, công tắc này sẽ không tự động viết lại, cần kiểm soát ở phía gateway của mô hình
- `SUBTITLE_OPENAI_*`: cấu hình ghi đè chuyên cho dịch phụ đề, để trống sẽ quay về cấu hình toàn cục
- `SUBTITLE_QC_*`: cấu hình ghi đè chuyên cho kiểm tra chất lượng phụ đề, để trống sẽ quay về cấu hình dịch phụ đề / toàn cục
- `TRANSLATE_TITLE` / `TRANSLATE_DESCRIPTION` / `GENERATE_TAGS`: tự động tạo tiêu đề, mô tả, thẻ tag
- `RECOMMEND_PARTITION`: tự động gợi ý chuyên mục
- `FIXED_PARTITION_ID` / `FIXED_PARTITION_ID_BILIBILI`: chuyên mục cố định
- `YOUTUBE_UPLOADER_AS_FIRST_TAG`: lấy người tải lên làm thẻ tag đầu tiên
- `PRESET_TAGS_ENABLED` / `PRESET_TAGS`: thẻ tag đặt trước, mỗi dòng một thẻ (cũng chấp nhận phân tách bằng dấu phẩy, dấu 、, dấu chấm phẩy). Sau khi bật, thẻ tag đặt trước xếp trước thẻ tag của nhiệm vụ, khi `GENERATE_TAGS` được bật AI chỉ bổ sung số lượng còn thiếu; một bộ đặt trước phục vụ đồng thời AcFun (6 thẻ đầu, mỗi thẻ khoảng 10 ký tự) và bilibili (tối đa 12 thẻ, mỗi thẻ 20 ký tự)

Tính năng văn bản AI tương thích đồng thời với OpenAI Chat Completions và Responses API. `OPENAI_BASE_URL` có thể điền địa chỉ gốc của API (ví dụ `https://api.openai.com/v1`, mặc định dùng Chat Completions) hoặc địa chỉ đầy đủ `/chat/completions`, `/responses`; khi điền endpoint đầy đủ, hệ thống sẽ tự động chọn giao thức và chuẩn hóa. Request Responses sẽ tự động chuyển đổi tin nhắn, định dạng đầu ra JSON, công tắc suy nghĩ và tham số giới hạn token, giá trị trả về cũng được chuẩn hóa để các tính năng hiện có như dịch, kiểm tra chất lượng, phân đoạn thông minh sử dụng. Khi dịch vụ tương thích không hỗ trợ `response_format`, tham số giới hạn token, `temperature` tùy chỉnh hoặc vai trò instruction cụ thể, hệ thống sẽ thương lượng từng cấp theo lỗi thực tế của endpoint; nếu gateway chỉ trả về lỗi schema của request chung chung, hệ thống sẽ hạ cấp xuống request chuẩn tối thiểu chỉ gồm `model + user messages`. Khả năng chỉ được lưu vào bộ nhớ đệm theo endpoint, giao thức và mô hình sau khi request hạ cấp thành công.

### Xử lý phụ đề

- `SUBTITLE_TRANSLATION_ENABLED`: bật dịch phụ đề, mặc định `false`
- `YOUTUBE_AUTO_GENERATED_SUBTITLES_ENABLED`: tải xuống phụ đề tự động tạo của YouTube, mặc định `false`
- `SUBTITLE_SOURCE_LANGUAGE`: ngôn ngữ nguồn, mặc định `auto`
- `SUBTITLE_TARGET_LANGUAGE`: ngôn ngữ đích, mặc định `zh`
- `SUBTITLE_FONT_NAME`: tên phông chữ burn-in phụ đề, mặc định `NotoSansCJKsc-Regular.otf`
- `SUBTITLE_BATCH_SIZE`: kích thước lô dịch
- `SUBTITLE_MAX_RETRIES` / `SUBTITLE_RETRY_DELAY`: chiến lược thử lại khi dịch
- `SUBTITLE_EMBED_IN_VIDEO`: có nhúng phụ đề vào video hay không
- `SUBTITLE_KEEP_ORIGINAL`: có giữ lại file phụ đề gốc hay không
- `SUBTITLE_MAX_WORKERS`: số luồng đồng thời khi dịch phụ đề

Giao diện phụ đề khi burn-in (giá trị mặc định chính là giao diện đã dùng trước đây; thay đổi hành vi đối với nguồn `.ass`/`.ssa` xem phần giải thích bên dưới):

- `SUBTITLE_FONT_SIZE_SCALE` / `SUBTITLE_MARGIN_V_SCALE`: hệ số cỡ chữ và lề dưới, phạm vi `0.5-2.0`, mặc định `1.0`
- `SUBTITLE_FONT_COLOR` / `SUBTITLE_OUTLINE_COLOR`: màu chữ và màu viền, `#RRGGBB`, mặc định `#FFFFFF` / `#000000`
- `SUBTITLE_OUTLINE_ENABLED` / `SUBTITLE_OUTLINE_SCALE`: công tắc viền và hệ số độ dày (`0-3`)
- `SUBTITLE_SHADOW_ENABLED` / `SUBTITLE_SHADOW_SCALE`: công tắc bóng đổ và hệ số (`0-3`)
- `SUBTITLE_TEXT_BOLD`: có in đậm hay không, mặc định `true`
- `SUBTITLE_BACKGROUND_ENABLED` / `SUBTITLE_BACKGROUND_COLOR` / `SUBTITLE_BACKGROUND_OPACITY`: tấm nền bán trong suốt (`BorderStyle=4`) cùng màu sắc và độ mờ của nó (`0-1`). Sau khi bật, libass sẽ coi bóng đổ như phần mở rộng ra ngoài của khung nền, nên đồng thời tắt bóng đổ

> **Thay đổi hành vi (tài nguyên nguồn `.ass` / `.ssa`)**: các cấu hình giao diện trên hiện có hiệu lực thống nhất đối với **mọi nguồn phụ đề**. Trước đây, upstream chỉ ghi phông chữ và lề vào `force_style`, các khóa như màu chữ / màu viền / in đậm / tấm nền **không có hiệu lực** đối với nguồn `.ass` / `.ssa` (cùng một cấu hình, đưa `.srt` thì ra chữ đỏ, đưa `.ass` vẫn là chữ trắng của tác giả), giờ các khóa này được đổi thành ghi đè từng khóa lên kiểu của nguồn — nghĩa là **kiểu màu chữ / in đậm / tấm nền có sẵn trong tài nguyên nguồn sẽ bị cấu hình của ứng dụng ghi đè**, khi chưa cấu hình thì dùng mặc định là chữ trắng + in đậm + viền (giống hành vi của nguồn SRT). Sau khi nâng cấp, nếu muốn giữ giao diện có sẵn của tài nguyên nguồn, hãy đặt tường minh các mục cấu hình tương ứng thành giá trị giống với tài nguyên nguồn, hoặc dùng file phụ đề ngoài có sẵn kiểu mà không dựa vào tính năng này.

### Nhận dạng giọng nói (ASR)

- `SPEECH_RECOGNITION_ENABLED`: có bật nhận dạng giọng nói để tạo phụ đề hay không, mặc định `false`
- `SPEECH_RECOGNITION_PROVIDER`: hỗ trợ `whisper`, `voxtral`
- `VAD_ENABLED`: cửa sổ quét giọng nói VAD, mặc định `true`
- `WHISPER` đường dẫn mặc định dùng timestamp cấp `segment` và tự động tương thích với các API không hỗ trợ `timestamp_granularities`
- `WHISPER_LANGUAGE` / `WHISPER_PROMPT` / `WHISPER_TRANSLATE`: tham số chuyên dùng cho Whisper
- `VOXTRAL_TIMESTAMP_GRANULARITIES`: mặc định `segment,word`
- `VOXTRAL_DIARIZE` / `VOXTRAL_CONTEXT_BIAS` / `VOXTRAL_LANGUAGE`
- `VOXTRAL_MAX_AUDIO_DURATION_S` / `VOXTRAL_LONG_AUDIO_MARGIN_S` / `VOXTRAL_ENFORCE_MAX_DURATION`

### Chuyển mã video và bảo trì

- `VIDEO_ENCODER`: `auto` / `cpu` / `nvidia` / `intel` / `amd`
- `VIDEO_CPU_CODEC`: `x264` (H.264, mặc định) hoặc `x265` (H.265/HEVC). Chỉ có hiệu lực khi cuối cùng dùng mã hóa CPU: `VIDEO_ENCODER=cpu`, hoặc khi mã hóa phần cứng không khả dụng nên quay về CPU. Thời gian mã hóa bằng khoảng 5 lần `libx264`, ngân sách timeout cũng được nhân lên theo cùng hệ số; lợi ích về dung lượng **không được đảm bảo**, tùy thuộc vào tài nguyên nguồn và preset, nên tự so sánh sau khi bật
- `VIDEO_CPU_PRESET`: preset mã hóa mềm CPU thông thường, mặc định `medium`
- `VIDEO_CPU_PRESET_HD`: preset dùng khi video 1440p trở lên và dài hơn 10 phút, mặc định `veryfast`
- `VIDEO_QUALITY_MODE`: `auto` (gợi ý theo độ phân giải) hoặc `manual` (dùng `VIDEO_QUALITY_VALUE`), mặc định `auto`
- `VIDEO_QUALITY_VALUE`: giá trị chất lượng cố định CRF/CQ/QP, phạm vi `0-51`, càng nhỏ chất lượng càng cao. Giá trị gợi ý ở chế độ tự động là 4K `22.5` / 1440p `23` / 1080p `23.5` / 720p `24.5`
- `VIDEO_HW_QUALITY_BOOST`: công tắc tổng tăng cường chất lượng mã hóa (lượng tử hóa thích ứng, lookahead, phân tích nhiều lần...), mặc định `true`. Nó tác dụng đồng thời lên bộ mã hóa phần cứng và bộ mã hóa phần mềm: x264 ghi `-aq-mode 3 -aq-strength 0.8 -psy-rd 1.0:0.0`, đường dẫn preset không phải HD sẽ thêm `-rc-lookahead 40`; x265 chỉ ghi `aq-mode=3`, đường dẫn preset không phải HD sẽ thêm `rc-lookahead=40` (`psy-rd` / `aq-strength` / `psy-rdoq` **không ghi**, tức giữ nguyên giá trị mặc định của x265 là 2.00 / 1.0 / 1.00 — sao chép y nguyên giá trị của x264 sang x265 chẳng khác nào cắt giảm một nửa các tối ưu thị giác tâm lý này, ngược lại với "tăng cường chất lượng"). Khi video dài 1440p+ đi theo mức `VERYFAST`, lookahead sẽ theo giá trị mặc định của preset, không bị phóng đại. Khi driver GPU cũ không nhận các tham số này, có thể tắt đi, lệnh sẽ quay về tham số cơ bản và tự động thử lại
- `VIDEO_HW_QUALITY_LEVEL`: `fast` / `balanced` / `quality`, ánh xạ tới mức tốc độ của từng bộ mã hóa phần cứng, mặc định `quality`
- `VIDEO_COLOR_METADATA_MODE`: `auto` (truyền thẳng thông tin màu của luồng nguồn) / `bt709` (bắt buộc) / `off` (không ghi), mặc định `auto`. Khi không ghi, trình phát sẽ diễn giải theo gam màu mặc định, có thể bị lệch màu
- `VIDEO_X264_TUNE`: giá trị `-tune` cho mã hóa mềm (ví dụ `film` / `animation`), để trống sẽ không truyền. Giá trị được kiểm tra theo whitelist riêng của từng `VIDEO_CPU_CODEC`: `film` và `stillimage` chỉ hợp lệ với x264, khi chuyển sang x265 sẽ bị bỏ qua và ghi vào nhật ký nhiệm vụ
- `VIDEO_CUSTOM_PARAMS_ENABLED` / `VIDEO_CUSTOM_PARAMS`: tham số FFmpeg tùy chỉnh (sau khi bật sẽ ghi đè hoàn toàn tham số mã hóa tích hợp sẵn và tham số màu). Nếu trong tham số tùy chỉnh không ghi `-c:v`, hệ thống sẽ bổ sung `-c:v libx264` / `-c:v libx265` theo `VIDEO_CPU_CODEC` — nếu không, ffmpeg sẽ lấy bộ mã hóa mặc định của container (mp4 là libx264), `VIDEO_CPU_CODEC` bị bỏ qua một cách âm thầm và việc bổ sung VUI màu cũng mất hiệu lực theo; nếu bạn tự ghi `-c:v`, hệ thống sẽ dùng bộ mã hóa bạn chỉ định (chỉ bổ sung VUI màu khi nhận diện là libx264 / libx265, và giải thích trong nhật ký nhiệm vụ)
- `MAX_CONCURRENT_TASKS`: số nhiệm vụ đồng thời tối đa, mặc định `2`
- `MAX_CONCURRENT_UPLOADS`: số lượt tải lên đồng thời tối đa, mặc định `1`
- `LOG_CLEANUP_ENABLED` / `LOG_CLEANUP_HOURS` / `LOG_CLEANUP_INTERVAL`
- `DOWNLOAD_CLEANUP_ENABLED` / `DOWNLOAD_CLEANUP_HOURS` / `DOWNLOAD_CLEANUP_INTERVAL`
- `DELETE_DOWNLOAD_FILES_AFTER_UPLOAD`: ngay sau khi tải lên thành công lên mọi nền tảng đích, xóa ngay file tải xuống của nhiệm vụ đó (mặc định tắt)

### Thông báo đẩy

- `NOTIFY_ENABLED`: bật đẩy thông báo, mặc định `false`
- `NOTIFY_CHANNELS`: danh sách kênh đã bật, hỗ trợ `wecom`, `serverchan`, `message_pusher`
- `NOTIFY_EVENTS`: danh sách sự kiện đã đăng ký, có thể chọn `task_added`, `task_completed`, `task_failed`, `login_success`, `login_locked`, `qr_login_success`, `qr_login_failed`
- WeCom: `NOTIFY_WECOM_WEBHOOK_URL`
- ServerChan: `NOTIFY_SERVERCHAN_SENDKEY`
- message-pusher: `NOTIFY_MESSAGE_PUSHER_SERVER` / `NOTIFY_MESSAGE_PUSHER_USERNAME` / `NOTIFY_MESSAGE_PUSHER_TOKEN`

### CookieCloud

- `COOKIECLOUD_ENABLED`: bật đồng bộ CookieCloud, mặc định `false`
- `COOKIECLOUD_SERVER_URL`: địa chỉ dịch vụ CookieCloud
- `COOKIECLOUD_UUID`: UUID của CookieCloud
- `COOKIECLOUD_PASSWORD`: mật khẩu mã hóa CookieCloud
- `COOKIECLOUD_ENCRYPT_MODE`: chế độ mã hóa, hỗ trợ `auto` / `legacy` / `aes-128-cbc-fixed`

### Kiểm duyệt nội dung

- `CONTENT_MODERATION_ENABLED`: bật kiểm duyệt nội dung Alibaba Cloud, mặc định `false`
- `ALIYUN_ACCESS_KEY_ID` / `ALIYUN_ACCESS_KEY_SECRET`: AK/SK của Alibaba Cloud
- `ALIYUN_CONTENT_MODERATION_REGION`: khu vực của dịch vụ kiểm duyệt
- `ALIYUN_TEXT_MODERATION_SERVICE`: tên dịch vụ kiểm duyệt văn bản, mặc định `comment_detection_pro`

### Chất lượng tải xuống

- `YOUTUBE_DOWNLOAD_QUALITY_MODE`: chế độ chất lượng tải xuống
- `YOUTUBE_DOWNLOAD_MAX_HEIGHT`: giới hạn chiều cao độ phân giải tối đa

### Xử lý sau phụ đề

- `SUBTITLE_MAX_LINE_LENGTH`: số ký tự tối đa trên một dòng, mặc định `42`
- `SUBTITLE_MAX_LINES`: số dòng tối đa của một phụ đề, mặc định `2`
- `SUBTITLE_NORMALIZE_PUNCTUATION`: chuẩn hóa dấu câu, mặc định `true`
- `SUBTITLE_FILTER_FILLER_WORDS`: lọc từ đệm (um, uh...), mặc định `true`
- `SUBTITLE_TIME_OFFSET_S`: độ lệch thời gian của phụ đề (giây)
- `SUBTITLE_MIN_CUE_DURATION_S`: thời lượng phụ đề tối thiểu, mặc định `0.6`
- `SUBTITLE_MERGE_GAP_S`: ngưỡng gộp các khoảng trống kề nhau, mặc định `0.3`

### Ví dụ cấu hình

```json
{
  "AUTO_MODE_ENABLED": false,
  "password_protection_enabled": false,
  "password": "",
  "UPLOAD_TARGET_DEFAULT": "acfun",
  "OPENAI_API_KEY": "",
  "OPENAI_BASE_URL": "https://api.openai.com/v1",
  "OPENAI_MODEL_NAME": "gpt-3.5-turbo",
  "OPENAI_THINKING_ENABLED": false,
  "SUBTITLE_TRANSLATION_ENABLED": false,
  "SUBTITLE_QC_ENABLED": true,
  "SPEECH_RECOGNITION_ENABLED": false,
  "SPEECH_RECOGNITION_PROVIDER": "whisper",
  "VAD_ENABLED": true,
  "VIDEO_ENCODER": "auto",
  "VIDEO_CPU_CODEC": "x264",
  "VIDEO_CPU_PRESET": "medium",
  "VIDEO_CPU_PRESET_HD": "veryfast",
  "FFMPEG_AUTO_DOWNLOAD": true,
  "MAX_CONCURRENT_TASKS": 2,
  "MAX_CONCURRENT_UPLOADS": 1
}
```

## Hướng dẫn kiểm tra chất lượng phụ đề

`SUBTITLE_QC_ENABLED` mặc định là `true`: hệ thống sẽ kiểm tra trước phụ đề nguồn do ASR tạo ra.

- `SUBTITLE_QC_THRESHOLD`: giới hạn dưới của điểm AI kiểm tra lại (0 ~ 1, mặc định 0.60)
- `SUBTITLE_QC_SAMPLE_MAX_ITEMS`: giới hạn số mục AI lấy mẫu tối đa, mặc định 80
- `SUBTITLE_QC_MAX_CHARS`: giới hạn số ký tự tối đa AI gửi kiểm tra trong một lần, mặc định 9000
- `SUBTITLE_QC_MODEL_NAME`: chỉ định riêng mô hình QC, để trống sẽ dùng lại mô hình dịch phụ đề / toàn cục
- `SUBTITLE_QC_TIMELINE_ENABLED`: có bật đánh giá theo chiều thời gian hay không, mặc định `true`
- `SUBTITLE_QC_MIN_COVERAGE_RATIO`: giới hạn dưới của tỷ lệ bao phủ (tổng thời lượng phụ đề / thời lượng video), mặc định `0.15`
- `SUBTITLE_QC_MAX_GAP_S`: khoảng trống không có phụ đề liên tục tối đa cho phép (giây), mặc định `90`
- `SUBTITLE_QC_MAX_CPS`: tốc độ ký tự tối đa của một phụ đề (ký tự/giây), mặc định `25`

QC sẽ chặn cứng bằng quy tắc trước, chỉ các mẫu ở ranh giới mới gọi AI kiểm tra lại một cách nghiêm ngặt.

Khi gặp các phụ đề chất lượng thấp rõ ràng như dòng ghi tên tác giả, gợi ý nhiễu, từ thao tác giao diện, câu lặp theo mẫu, hệ thống sẽ cho thất bại ngay ở tầng quy tắc, không chuyển sang bước cho qua một cách lỏng lẻo nữa.

Chiều thời gian (tỷ lệ bao phủ / khoảng trống / tốc độ nói) sẽ cùng tham gia đánh giá với chế độ nghiêm ngặt khi nguồn ASR bị suy giảm (`subtitle_quality_state == degraded`).

Ba ngữ nghĩa ranh giới của chiều thời gian: dải dung sai cho phần trắng ở cuối video lấy **giá trị nhỏ hơn** trong hai giá trị "30 giây" và "25% độ dài video" (tài nguyên dài 60 giây sẽ không bị coi là phần trắng cuối video lành tính chỉ vì 23 giây cuối không có phụ đề); cue có thời lượng bằng 0 đạt "≥3 cue và ≥20%" sẽ được coi là khuyết điểm thực chất, khi AI không khả dụng thì không cho qua (≥25% sẽ thất bại cứng vô điều kiện); cue có timestamp dị dạng (không phân tích được dòng thời gian) sẽ bị bỏ qua và ghi warning, không còn âm thầm suy giảm về `0.0` nữa — suy giảm về 0.0 sẽ làm tỷ lệ bao phủ tăng ảo và ngược lại giúp QC đạt.

Các mẫu đáng ngờ khi AI không khả dụng, trả về bất thường hoặc đầu ra không hợp lệ sẽ mặc định được xử lý là thất bại. Khi QC thất bại, hệ thống sẽ bỏ qua bước burn-in phụ đề nhưng vẫn giữ lại file phụ đề và tiếp tục tải lên video gốc, nhiệm vụ cuối cùng được đánh dấu là hoàn thành và hiển thị dấu hiệu phụ đề bất thường.

Phụ đề ASR bị đánh giá là không đạt sẽ được đổi tên thành `*.rejected.txt` (giữ lại nội dung để kiểm tra thủ công) và bị loại khỏi phạm vi tái sử dụng, tránh việc nhiệm vụ chạy lại dùng phụ đề cũ nên không bao giờ lấy được phụ đề mới. Phụ đề có sẵn của nền tảng hoặc do người dùng cung cấp sẽ không bị ảnh hưởng.

### Công tắc kiểm soát burn-in

- `ASR_FAILURE_BLOCKS_EMBED` (mặc định `true`): khi kết quả chất lượng ASR/VAD là `failed` (nguồn không đáng tin cậy), hệ thống từ chối burn-in phụ đề đó. Đặt thành `false` sẽ khôi phục hành vi cũ, chỉ nới lỏng hai loại chặn là "kết quả nguồn ASR" và "QC không chạy được", **không** bỏ qua kết luận thất bại rõ ràng mà QC đưa ra — kết luận QC nhắm vào bản thân nội dung phụ đề, còn độ tin cậy của nguồn ASR là chuyện khác.
- `SUBTITLE_QC_ENABLED=false`: người dùng chủ động bỏ qua tuyến phòng thủ QC. Lúc này hệ thống không còn xem dấu hiệu QC trong lịch sử, cũng không còn yêu cầu tài nguyên `degraded` phải qua QC nghiêm ngặt (khi QC đã tắt thì điều kiện này không thể đáp ứng được, nếu vẫn chặn thì sẽ thành ra "tắt QC lại còn nghiêm ngặt hơn").

"QC không khả dụng" (thiếu file phụ đề / lỗi khi thực thi) và "người dùng chủ động tắt QC" là hai kết quả khác nhau: trường hợp trước xử lý theo hướng từ chối, trường hợp sau cho qua. Danh sách nhiệm vụ sẽ ghi rõ nguyên nhân cụ thể bằng `qc_unavailable` / `subtitle_qc_rejected` / `asr_failed_block_embed` / `asr_degraded_block_embed`.

## Hướng dẫn nhận dạng giọng nói

Hiện hỗ trợ hai loại nhà cung cấp ASR:

- Whisper: tương thích với API kiểu OpenAI, có thể dùng API Key, Base URL và tên mô hình riêng
- Voxtral: Mistral /v1/audio/transcriptions, mô hình mặc định là `voxtral-mini-latest`

Nên ưu tiên giữ `VAD_ENABLED=true`. Hiện mặc định dùng tham số cửa sổ quét ưu tiên chất lượng, đoạn cắt ngắn hơn và chồng lấn ít hơn, giúp nâng cao độ chính xác của ranh giới phụ đề.

Nếu kết quả VAD không lý tưởng, hệ thống sẽ tự động chuyển sang quy trình dự phòng theo đoạn cắt hoặc toàn bộ đoạn.

## Phông chữ phụ đề tích hợp sẵn

- Dự án mặc định tích hợp sẵn `SourceHanSansHWSC-VF.otf`, được phân phối cùng kho như một dependency cho việc burn-in phụ đề
- Có thể dùng `SUBTITLE_FONT_NAME` để chỉ định tên file phông chữ trong thư mục `fonts/`; chương trình sẽ đọc tên phông chữ thật của file đó để libass sử dụng
- Giấy phép phông chữ nằm tại `fonts/LICENSE.txt`

## Hướng dẫn sử dụng

1. Gửi link YouTube trên trang chủ hoặc trang nhiệm vụ để tạo nhiệm vụ.
2. Ở chế độ tự động, quy trình là: tải xuống -> ASR / xử lý phụ đề (tùy chọn) -> thông tin meta bằng AI -> kiểm duyệt -> tải lên nền tảng đích.
3. Trên trang kiểm duyệt thủ công, có thể điều chỉnh tiêu đề, mô tả, thẻ tag, chuyên mục và tải lên bắt buộc.
4. Sau khi bật giám sát YouTube, có thể lấy nhiệm vụ định kỳ theo kênh hoặc từ khóa và tự động thêm vào hàng đợi nhiệm vụ; khi chỉ muốn chuyển những video có tiêu đề khớp với nội dung cụ thể (ví dụ ASMR của một kênh nào đó), hãy điền "Tiêu đề chứa từ khóa" trong cấu hình giám sát và chọn khớp "Bất kỳ / Tất cả".
5. Trên trang cài đặt, có thể bảo trì theo nhóm các mục tài khoản, AI, phụ đề, ASR, chuyển mã, bảo trì và bảo mật.
6. AcFun / bilibili hỗ trợ đăng nhập bằng cách quét mã QR: nhấp vào "Đăng nhập bằng cách quét mã" trên trang cài đặt, dùng App trên điện thoại quét mã là hoàn tất xác thực.
7. Nếu đã triển khai dịch vụ CookieCloud, có thể cấu hình trên trang cài đặt rồi đồng bộ YouTube Cookies bằng một cú nhấp chuột, không cần xuất thủ công.
8. Sau khi bật thông báo đẩy, thay đổi trạng thái nhiệm vụ và sự kiện đăng nhập sẽ tự động được đẩy tới các kênh như WeCom.

## FFmpeg và tăng tốc phần cứng

- Mặc định ưu tiên dùng file nhị phân trong thư mục `ffmpeg/` của dự án
- Trong môi trường Windows, nếu thiếu `ffmpeg/`, hệ thống có thể tự động tải xuống và bổ sung
- `FFMPEG_LOCATION` có thể ghi đè đường dẫn mặc định, hỗ trợ trỏ trực tiếp tới `ffmpeg.exe` hoặc thư mục chứa nó
- Khi `VIDEO_ENCODER=cpu`, dùng mã hóa mềm CPU, bộ mã hóa do `VIDEO_CPU_CODEC` quyết định:
  - `x264` (mặc định): `libx264` (H.264)
  - `x265`: `libx265` (H.265/HEVC). Đo thực tế (1080p30, có burn-in phụ đề) tốn thời gian bằng khoảng 5 lần `libx264` (veryfast 1.70s → 8.44s), ngân sách timeout đã được nhân lên theo cùng hệ số
  - Lợi ích về dung lượng không ổn định: đo thực tế trên tài nguyên đồ họa tổng hợp (khớp SSIM), ở `veryfast` với cùng CRF, dung lượng ngược lại bằng 1.6~1.8 lần `libx264`, ở `medium` thì xấp xỉ bằng nhau. Có tiết kiệm hơn hay không tùy thuộc vào tài nguyên nguồn và preset, nên tự so sánh sau khi bật rồi mới quyết định; thang CRF của x265 và x264 không thể so sánh trực tiếp, mục này không tự động bù trừ gì
- Khi `VIDEO_ENCODER=auto|nvidia|intel|amd`, ưu tiên dùng mã hóa phần cứng HEVC / H.265:
  - NVIDIA: `hevc_nvenc`
  - Intel: `hevc_qsv`
  - AMD (Windows): `hevc_amf`
  - AMD (Linux): `hevc_vaapi`
- Nếu mã hóa phần cứng HEVC không khả dụng hoặc chuyển mã thất bại, hệ thống sẽ tự động quay về mã hóa mềm CPU (chọn bộ mã hóa theo `VIDEO_CPU_CODEC`)
- Nếu bộ mã hóa CPU chọn `x265` nhưng FFmpeg hiện tại không có `libx265`, hoặc `libx265` không chấp nhận một tham số nào đó, hệ thống sẽ tự động hạ cấp sang `libx264` để thử lại. Khi mã hóa phần cứng thất bại và quay về CPU, cấp dự phòng này vẫn được giữ lại: giai đoạn CPU sau khi quay về từ mã hóa phần cứng vẫn dùng `x265` mà bạn đã cấu hình, vì vậy vẫn cần đường dự phòng `x265 -> x264`; ngân sách timeout của giai đoạn này cũng được tính theo bộ mã hóa thực tế của nó (`x265` là 5 lần), chứ không dùng tiếp ngân sách của `x264`

### Ví dụ GPU cho Docker

NVIDIA (khuyên dùng):

```yaml
# Bỏ ghi chú các dòng sau trong docker-compose.yml là có thể bật:
# gpus: all
# environment:
#   - NVIDIA_VISIBLE_DEVICES=all
#   - NVIDIA_DRIVER_CAPABILITIES=compute,video,utility
```

Intel / AMD (Linux):

```yaml
devices:
  - /dev/dri:/dev/dri
group_add:
  - video
  - render
```

> File ghi đè chuyên dụng cho NVIDIA đã bị loại bỏ, các cấu hình liên quan đã được tích hợp trực tiếp vào `docker-compose.yml` chính.

## Giám sát YouTube

- Cần cấu hình `YOUTUBE_API_KEY` trước
- Hỗ trợ tìm kiếm theo từ khóa, kênh chỉ định, chuyển dữ liệu lịch sử và chế độ theo dõi mới nhất liên tục
- Hỗ trợ lọc theo từ khóa trong tiêu đề (khớp bất kỳ / tất cả), có thể chỉ chuyển những video có tiêu đề khớp với nội dung cụ thể (ví dụ ASMR của một kênh nào đó); nhiều từ khóa phân tách bằng dấu phẩy hoặc dấu cách, cụm từ chứa dấu cách dùng dấu ngoặc kép bao quanh (ví dụ `"deep sleep"`)
- Hỗ trợ lọc theo loại video: video / short / live
- Có thể đặt tự động thêm vào hàng đợi nhiệm vụ và giữ lại lịch sử giám sát
- File cấu hình sẽ được lưu vào `config/youtube_monitor/`, cơ sở dữ liệu lịch sử nằm tại `db/youtube_monitor.db`

## Thông báo đẩy

Hỗ trợ ba kênh đẩy thông báo, có thể bật kết hợp tự do trên trang cài đặt:

| Kênh | Định danh | Cấu hình bắt buộc |
| --- | --- | --- |
| WeCom | `wecom` | `NOTIFY_WECOM_WEBHOOK_URL` |
| ServerChan | `serverchan` | `NOTIFY_SERVERCHAN_SENDKEY` |
| message-pusher | `message_pusher` | `NOTIFY_MESSAGE_PUSHER_SERVER` + `USERNAME` + `TOKEN` |

Các loại sự kiện được hỗ trợ:

- `task_added`: thêm nhiệm vụ
- `task_completed`: hoàn thành nhiệm vụ
- `task_failed`: nhiệm vụ thất bại
- `login_success`: đăng nhập thành công
- `login_locked`: đăng nhập bị khóa
- `qr_login_success`: đăng nhập bằng mã QR thành công
- `qr_login_failed`: đăng nhập bằng mã QR thất bại

Thông báo dùng hàng đợi thử lại bất đồng bộ (SQLite outbox), khoảng thời gian tăng dần (30s → 120s → 600s → 1800s → 3600s) để đảm bảo gửi được cuối cùng. WeCom ưu tiên dùng định dạng Markdown, nếu thất bại sẽ tự động quay về văn bản thuần túy.

## Tích hợp CookieCloud

Hỗ trợ tự động lấy YouTube / Google Cookies từ dịch vụ [CookieCloud](https://github.com/easychen/CookieCloud), không cần xuất thủ công.

- Sau khi cấu hình `COOKIECLOUD_SERVER_URL`, `COOKIECLOUD_UUID`, `COOKIECLOUD_PASSWORD` là có thể bật
- Hỗ trợ ba chế độ mã hóa: `auto` (tự động dò), `legacy`, `aes-128-cbc-fixed`
- Tự động lọc, chỉ giữ lại Cookie của các tên miền `youtube.com`, `youtu.be`, `google.com`
- Đầu ra là file định dạng Netscape `cookies/yt_cookies.txt`
- Trang cài đặt Web cung cấp nút "Kiểm tra kết nối" và "Đồng bộ ngay"
- Trạng thái đồng bộ sẽ ghi lại dấu thời gian, thành công/thất bại và thông báo, thuận tiện cho việc khắc phục sự cố

## Tính năng bảo mật

- **Bảo vệ bằng mật khẩu**: bảo vệ Web UI bằng mật khẩu (tùy chọn), vào trang cài đặt lần đầu là có thể cấu hình
- **Chống dò mật khẩu (brute-force)**: nhập sai liên tiếp 5 lần sẽ tự động khóa 15 phút, khi bị khóa sẽ gửi thông báo
- **Hết hạn phiên**: đăng nhập không hoạt động trong 30 phút sẽ tự động hết hạn, truy cập trang được bảo vệ sẽ tự động gia hạn
- **Lưu trữ bền vững SECRET_KEY**: lần chạy đầu tiên sẽ tự động tạo khóa ngẫu nhiên 256-bit và lưu lại, khởi động lại không bị mất
- **Chống path traversal**: mọi thao tác file đều dùng `werkzeug.security.safe_join`, đường dẫn Cookie bị giới hạn trong thư mục dự án
- **Kiểm duyệt nội dung**: có thể kết nối dịch vụ kiểm duyệt Alibaba Cloud Green để kiểm tra tính tuân thủ của văn bản do AI tạo ra
- **Thông báo sự kiện đăng nhập**: các sự kiện như đăng nhập bằng QR thành công/thất bại, khóa mật khẩu có thể được đẩy tới các kênh như WeCom

## Câu hỏi thường gặp

### Không truy cập được giao diện Web trên máy chủ đám mây

Nhóm bảo mật (security group) / tường lửa mạng của nền tảng đám mây hoặc tường lửa của chính máy chủ có thể chưa mở cổng TCP 5000. Không nên mở trực tiếp cổng này ra toàn bộ Internet công khai: bảo vệ Web bằng mật khẩu mặc định đang tắt, và khi truy cập trực tiếp cũng dùng HTTP dạng văn bản gốc (không mã hóa).

Nên truy cập qua chuyển tiếp cổng local bằng SSH, không cần mở cổng 5000 ra Internet công khai:

```bash
ssh -N -L 5000:127.0.0.1:5000 -o ServerAliveInterval=30 user@<服务器公网IP>
```

Sau khi kết nối được thiết lập, mở `http://localhost:5000` trong trình duyệt local. Nếu thực sự cần truy cập công khai lâu dài, hãy bật bảo vệ Web bằng mật khẩu trước, cấu hình HTTPS qua reverse proxy, và giới hạn nguồn truy cập vào (inbound) của tường lửa đám mây và tường lửa máy chủ chỉ ở các IP hoặc dải mạng đáng tin cậy.

- 403 / cần đăng nhập / not a bot
  - Thường là vấn đề chống crawler hoặc quyền của YouTube, hãy cập nhật `cookies/yt_cookies.txt`
  - Cũng có thể đồng bộ tự động qua CookieCloud, không cần xuất thủ công
- Không tìm thấy FFmpeg / yt-dlp
  - Môi trường Docker thường không cần xử lý; khi chạy local, hãy đảm bảo PATH đúng
  - Nếu dùng gói Windows Release, thường sẽ không thiếu FFmpeg; nếu thiếu, hãy xác nhận `ffmpeg/` không bị phần mềm bảo mật cách ly
- Tải lên AcFun thất bại
  - Cập nhật `cookies/ac_cookies.json`, hoặc dùng mã QR để đăng nhập lại trên trang cài đặt
  - Kiểm tra xem thông tin meta trên trang kiểm duyệt thủ công có tuân thủ hay không
- Tải lên bilibili thất bại
  - Cập nhật `cookies/bili_cookies.json`, hoặc dùng mã QR để đăng nhập lại trên trang cài đặt
  - Lỗi 603 "Hệ thống phát hiện hành vi bất thường" là kiểm soát rủi ro ở cấp tài khoản: API đăng tải mặc định `auto` sẽ đi qua API PC của Bcut trước, nếu thất bại sẽ quay về Web; khi cả hai kênh đều bị chặn, hãy đăng nhập cùng tài khoản bằng trình duyệt và đăng tải thủ công một lần trong Trung tâm sáng tạo, hoặc hoàn tất xác minh tên thật / khiếu nại với bộ phận chăm sóc khách hàng theo hướng dẫn, đồng thời giữ IP đầu ra ổn định và giảm tần suất đăng tải
- Dịch phụ đề chậm
  - Điều chỉnh số lượng đồng thời và kích thước lô, đồng thời chú ý giới hạn tốc độ của API
- Docker chưa bật NVENC
  - Kiểm tra xem phần GPU trong `docker-compose.yml` đã được bỏ ghi chú hay chưa
  - Xác nhận máy host đã cài `nvidia-container-toolkit`
- Đồng bộ CookieCloud thất bại
  - Kiểm tra xem địa chỉ dịch vụ, UUID và mật khẩu có đúng hay không
  - Xác nhận dịch vụ CookieCloud có thể truy cập được, có thể dùng nút "Kiểm tra kết nối" trên trang cài đặt để khắc phục sự cố
- Không nhận được thông báo đẩy
  - Xác nhận `NOTIFY_ENABLED` đã được bật và kênh đích đã được cấu hình đúng
  - Kiểm tra webhook URL / SendKey có hợp lệ hay không

### Bot Telegram không dùng được

Instance công khai [@Y2AAuto_bot](https://t.me/Y2AAuto_bot) chạy trên VPS cá nhân, máy chủ này đã bị chặn, **không đảm bảo luôn khả dụng**, cũng có thể dừng dịch vụ bất cứ lúc nào. Khi gặp tình trạng không kết nối được, không phản hồi trong thời gian dài hoặc báo dịch vụ bất thường, hãy tự triển khai, xem [Phương án D: Bot chuyển tiếp Telegram](#phương-án-dbot-chuyển-tiếp-telegram-tùy-chọn).

Sau khi tự triển khai mà vẫn không chuyển tiếp được, hãy kiểm tra theo thứ tự sau:

- Địa chỉ API có phải là địa chỉ mà mạng nơi bot chạy không truy cập được hay không (khi khác máy thì đừng điền `localhost`)
- API Token có bị đặt lại hoặc thu hồi trên trang cài đặt hay không, Token đã lưu trong bot có phải là Token mới nhất hay không
- Nhật ký của dự án này có bản ghi request `/tasks/add_via_extension` hay không, và mã trạng thái trả về là gì

## Đóng góp và phản hồi

- Hoan nghênh gửi Issue / PR: `../../issues`
- Không gửi file chứa Cookie, khóa bí mật hay các thông tin nhạy cảm khác

## Lời cảm ơn

- [acfun_upload](https://github.com/Aruelius/acfun_upload)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
- [Flask](https://flask.palletsprojects.com/)
- Tài liệu tham khảo kỹ thuật cho việc tải lên nền tảng Bilibili
  - Phần `modules/bili_sdk` trong dự án tham khảo một phần dự án mã nguồn mở của cộng đồng và đã được điều chỉnh cho phù hợp với quy trình tải lên.
- [OpenAI](https://openai.com/)

## Giấy phép

Dự án này là mã nguồn mở theo [GNU GPL v3](LICENSE). Vui lòng tuân thủ các điều khoản của nền tảng liên quan và chỉ sử dụng cho mục đích học tập và nghiên cứu trong khuôn khổ hợp pháp và tuân thủ quy định.
