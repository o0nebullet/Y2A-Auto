# VI-SYNC-MAP — Y2A-Auto, nhánh vi-ui

- Fork: `o0nebullet/Y2A-Auto`; upstream khai báo: `fqscfqj/Y2A-Auto-tgbot`
- Commit gốc: `c5ce9f65a967fd966f8efb250417ebc3af57a674` (fork head, `feat(youtube-monitor): 支持标题包含关键词过滤 (#158) (#159)`)
- **LƯU Ý LỆCH UPSTREAM: fork và upstream KHÔNG chung lịch sử** (`git merge-base HEAD upstream/main` rỗng; fork hơn upstream 739 commit, upstream hơn fork 64 commit). Nhánh `vi-ui` gốc từ **fork head**, KHÔNG gốc từ upstream head như mẫu apkstart/android-ad-cleaner — gốc từ upstream sẽ là codebase khác hẳn. Đồng bộ upstream sau này phải xử lý riêng, không merge thẳng.
- Phạm vi dịch (theo mẫu các repo trước): giao diện + thông báo + README. Dịch hẳn sang tiếng Việt, không nút đổi ngôn ngữ. Không đổi logic, không đổi tên biến/hàm, không đổi tên field JSON/key dict.
- "Số dòng Trung đã dịch" = số dòng chứa CJK ở commit gốc trừ số dòng chứa CJK còn lại (đếm bằng regex `[\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF\U00020000-\U0002A6DF]`).
- Tổng phạm vi: 2.730 dòng Trung trong 18 file → còn 440 dòng → **đã dịch ròng 2.288 dòng** (`git diff c5ce9f6`: 2.305 dòng Trung xóa, 17 dòng Trung thêm — 17 dòng thêm đều là dòng sửa mà vẫn giữ chữ Trung có chủ đích, xem dưới).
- Thuật ngữ thống nhất: 设置=cài đặt, 任务=nhiệm vụ, 视频=video, 字幕=phụ đề, 上传=tải lên, 下载=tải xuống, 监控=giám sát, 频道=kênh, 标题=tiêu đề, 封面=ảnh bìa, 分辨率=độ phân giải, 编码=mã hóa, 转码=chuyển mã, 审核=kiểm duyệt, 通知=thông báo, 失败=thất bại, 成功=thành công, 配置=cấu hình, 保存=lưu, 删除=xóa, 编辑=chỉnh sửa, 搜索=tìm kiếm, 开始=bắt đầu, 停止=dừng, 暂停=tạm dừng, 继续=tiếp tục, 重试=thử lại, 队列=hàng đợi, 日志=nhật ký, 状态=trạng thái, 详情=chi tiết, 预览=xem trước, 完成=hoàn thành, 确认=xác nhận, 取消=hủy, 警告=cảnh báo, 错误=lỗi, 提示=thông báo, 登录=đăng nhập, 退出=đăng xuất, 启用=bật, 禁用=tắt, 默认=mặc định, 高级=nâng cao, 版本=phiên bản, 刷新=làm mới, 复制=sao chép, 分区 (bilibili)=chuyên mục, 标签=thẻ tag, 简介=mô tả, 分P=phần, 投稿=đăng tải, 弹幕=danmaku (bình luận chạy), 自部署=tự triển khai, 公共实例=instance công khai. Giữ nguyên: YouTube, AcFun, bilibili, Telegram, Flask, FFmpeg, OpenAI, API, API Key, Cookie, URL, JSON, x264/x265, SRT, ASS, MP4, tên model, đường dẫn, tên lệnh. `企业微信`→WeCom, `Server酱`→ServerChan, `必剪`→BiCut, `阿里云`→Alibaba Cloud.

## File đã dịch

| File | Commit gốc | Số dòng Trung đã dịch | Ghi chú |
|---|---|---|---|
| README.md | c5ce9f6 | 350 (352→2) | Còn 2 dòng cố tình: anchor URL ngoài `#安装和部署` (trỏ heading tiếng Trung của repo gốc, dịch sẽ gãy link); placeholder `<服务器公网IP>` trong lệnh SSH |
| app.py | c5ce9f6 | 270 (700→430) | Chỉ dịch chuỗi hiển thị (flash/JSON/status dict/`TASK_STATES`/`SETTINGS_GUARD_LABELS`/health-check). Còn 430 dòng: comment, docstring, log nội bộ (không dịch theo phạm vi) |
| templates/settings.html | c5ce9f6 | 686 (686→0) | Hết tiếng Trung; `已配置`/`未配置` → `Đã cấu hình`/`Chưa cấu hình` đồng bộ cả Jinja + JS + phép so sánh |
| templates/youtube_monitor_config.html | c5ce9f6 | 221 (221→0) | Hết tiếng Trung; tên preset mặc định đã dịch (chỉ là giá trị ô tên) |
| templates/tasks.html | c5ce9f6 | 112 (112→0) | Xem mục sửa logic `hasProcessingTasks()` dưới |
| templates/youtube_monitor.html | c5ce9f6 | 109 (109→0) | `data-label` + selector CSS dịch đồng bộ |
| templates/edit_task.html | c5ce9f6 | 87 (87→0) | `content_type` chỉ hiển thị → dịch `Tiêu đề`/`Mô tả` |
| templates/partials/task_row.html | c5ce9f6 | 81 (83→2) | Còn 2 dòng: token `字幕质检失败` (xem dưới) |
| templates/partials/task_card.html | c5ce9f6 | 74 (76→2) | Còn 2 dòng: token `字幕质检失败` (xem dưới) |
| templates/youtube_monitor_history.html | c5ce9f6 | 71 (71→0) | Hết tiếng Trung |
| templates/manual_review.html | c5ce9f6 | 69 (69→0) | Hết tiếng Trung |
| templates/index.html | c5ce9f6 | 46 (46→0) | `toLocale*('zh-CN')` → `'vi-VN'` |
| templates/base.html | c5ce9f6 | 18 (18→0) | `lang="zh-CN"` → `lang="vi"` |
| static/js/main.js | c5ce9f6 | 14 (14→0) | Hết tiếng Trung |
| templates/login.html | c5ce9f6 | 8 (8→0) | Hết tiếng Trung |
| modules/notifications/renderers.py | c5ce9f6 | 43 (45→2) | Còn 2 dòng docstring, giữ nguyên |
| modules/notifications/service.py | c5ce9f6 | 10 (12→2) | Còn 2 dòng `logger.warning`, giữ nguyên |
| modules/notifications/adapters.py | c5ce9f6 | 7 (7→0) | Hết tiếng Trung; `CHANNEL_LABELS` đã dịch |

## Sửa logic do dịch (không chỉ đổi chuỗi)

- `templates/tasks.html` — hàm `hasProcessingTasks()` so chuỗi trạng thái tiếng Trung (`statusText.includes('下载中'|...)`) trong khi `task_status_display()` ở `app.py` đã dịch sang tiếng Việt → đổi thành `statusText.startsWith('Đang ')` (mọi trạng thái đang chạy đều bắt đầu bằng "Đang ", đúng tập hợp cũ: tải xuống/tải lên/dịch/tạo tag/gợi ý chuyên mục/kiểm duyệt/dịch phụ đề/chuyển giọng nói/chuyển mã/chờ xử lý/chờ kiểm duyệt/thu thập thông tin).
- `app.py` — 2 comment/docstring mô tả nhãn là "tên tiếng Trung" giờ đã sai nên sửa từ: `# 回退提示里的中文名称…` → `# 回退提示里的名称…`; docstring `_format_settings_revert_message` `中文名（配置键）` → `名称（配置键）`. Chỉ sửa 2 chỗ này, các comment/docstring khác giữ nguyên tiếng Trung.

## Chuỗi giữ nguyên + lý do

- Token `字幕质检失败` trong `task_row.html`/`task_card.html` (giá trị mặc định + phép so sánh `qc_reason_token`): backend (`modules/task_manager.py`) vẫn sinh token này bằng tiếng Trung — dịch template mà không dịch backend sẽ vỡ so sánh.
- `app.py`: toàn bộ comment/docstring/logging; `RuntimeError` bất biến lúc import; chuỗi chỉ dùng trong `logger.info`; tên hàm `get_aliyun_label_chinese`; key dict/field JSON.
- `README.md`: code block, URL, tên file/đường dẫn, tên biến/lệnh; anchor `#安装和部署`; placeholder `<服务器公网IP>`.
- `modules/notifications/*`: tên field/API, giá trị gửi/nhận từ platform.
- `settings.html`: tên preset chỉ dịch vì là giá trị mặc định ô tên, không bị code so sánh.

## Test đã sửa do dịch (assertion vỡ, chỉ đổi chuỗi kỳ vọng sang tiếng Việt)

- 7 file test: `test_app_logging_helpers.py` (API init status ×3 + health-check ×1), `test_edit_task_cover_mode_route.py` (×1), `test_force_upload_metadata.py` (nhãn chuyên mục ×1), `test_retry_metadata_translation.py` (câu cảnh báo template ×1), `test_settings_preset_tags.py` (×1), `test_settings_guards.py` (`生效`→`Có hiệu lực`, `配置已成功保存`→`Đã lưu cấu hình thành công`, `分片窗口`→`cửa sổ phân đoạn` ×2, `ASR 来源结局`→`Kết quả nguồn ASR`, `始终生效`→`luôn có hiệu lực`, `更严格`→`nghiêm ngặt`, `质检没跑成`→`Kiểm tra chất lượng không chạy được`, `没跑成`→`không chạy được`, `拦截`→`chặn` + 2 dòng docstring), `test_settings_search_keyboard.py` (SEARCH_MARKER theo comment mới trong `settings.html` + hint `按 Enter 跳转`→`bấm Enter để nhảy tới`).
- Sau khi sửa, test về đúng baseline cây sạch: **1.519 passed, 447 subtests passed, 7 failed** — 7 lỗi còn lại là lỗi có sẵn từ trước (`tests/test_ai_fallback_client.py`, httpx `Invalid port: ':1]'`, đã xác minh trên cây sạch `c5ce9f6` bằng worktree riêng).

## Chưa dịch (đợt sau)

- Toàn repo còn ~12.540 dòng Trung trong 158 file (đếm sau dịch): `modules/` engine (~10.000 dòng: `task_manager.py` 1.541, `youtube_monitor.py` 607, `ai_segmentation.py` 468, `video_encoder_params.py` 462, `subtitle_translator.py` 445… — log/error nội bộ, comment, docstring), `tests/` (fixture/chú thích/assert còn tiếng Trung), `docs/` + `build-tools/README.md` + `Makefile` + `Dockerfile` + `SECURITY.md` + `.github/ISSUE_TEMPLATE/*`, `modules/bili_sdk/data/*` (JSON dữ liệu platform, phải giữ tiếng Trung mới khớp API), `templates` đã hết nhưng chuỗi do backend sinh vẫn tiếng Trung lúc chạy (error_message, token `subtitle_qc_reason`, giá trị config) — muốn hết hẳn phải dịch backend đợt riêng.

## Chỗ mơ hồ cần AD quyết / kiểm lại khi review

- `必剪` → `BiCut` (tên tiếng Anh chuẩn của app, chưa kiểm chứng trong repo này).
- `署名行` (mục QC) → `dòng ghi tên tác giả` — có thể là dòng ghi công/chữ ký.
- Đoạn `OPENAI_THINKING_ENABLED` trong README dài, logic vendor/endpoint phức tạp — đã dịch sát từng mệnh đề, nên đọc kỹ lại khi review.
- `get_aliyun_label_chinese` (tên hàm) giữ nguyên vì là tên code; nhãn hiển thị đã dịch.
