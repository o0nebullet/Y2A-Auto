from __future__ import annotations

import json
from typing import Any

from .models import (
    EVENT_LOGIN_LOCKED,
    EVENT_LOGIN_SUCCESS,
    EVENT_QR_LOGIN_FAILED,
    EVENT_QR_LOGIN_SUCCESS,
    EVENT_TASK_ADDED,
    EVENT_TASK_COMPLETED,
    EVENT_TASK_FAILED,
    NotificationEvent,
    NotificationMessage,
)


def _as_text(value: Any) -> str:
    return str(value or "").strip()


def _truncate(text: str, limit: int = 240) -> str:
    clean = _as_text(text)
    if len(clean) <= limit:
        return clean
    return clean[: max(0, limit - 1)] + "…"


def _upload_target_label(upload_target: Any) -> str:
    target = _as_text(upload_target).lower()
    if target == "both":
        return "AcFun + bilibili"
    if target == "bilibili":
        return "bilibili"
    return "AcFun"


def _task_title(payload: dict[str, Any]) -> str:
    for key in ("video_title_translated", "video_title_original", "title"):
        value = _as_text(payload.get(key))
        if value:
            return value
    return "Nhiệm vụ chưa đặt tên"


def _task_platform_result(payload: dict[str, Any]) -> str:
    succeeded = []
    if payload.get("acfun_uploaded"):
        succeeded.append("AcFun")
    if payload.get("bilibili_uploaded"):
        succeeded.append("bilibili")
    if succeeded:
        return ", ".join(succeeded)
    return _upload_target_label(payload.get("upload_target"))


def _pretty_error_text(value: Any) -> str:
    text = _truncate(_as_text(value), 300)
    return text or "Chưa cung cấp chi tiết lỗi"


def _markdown_lines(*lines: str) -> str:
    return "\n".join(line for line in lines if _as_text(line))


def _kv(label: str, value: Any) -> str:
    """格式化一个键值行：**标签** 值"""
    text = _as_text(value)
    if not text:
        return ""
    return f"**{label}：**{text}"


def _section_block(*kv_lines: str) -> str:
    """将多行键值组装成引用块。"""
    return "\n".join(f"> {line}" for line in kv_lines if _as_text(line))


def build_notification_message(event: NotificationEvent) -> NotificationMessage:
    payload = event.as_payload()
    event_type = event.event_type

    if event_type == EVENT_TASK_ADDED:
        title = "Y2A-Auto 📋 Đã thêm nhiệm vụ"
        summary = f"{payload.get('task_id', '')[:8]} | {_upload_target_label(payload.get('upload_target'))}"
        body = _section_block(
            _kv("ID nhiệm vụ", f"`{_as_text(payload.get('task_id'))}`"),
            _kv("Nền tảng đăng tải", _upload_target_label(payload.get("upload_target"))),
            _kv("YouTube URL", _truncate(_as_text(payload.get("youtube_url")), 500)),
            _kv("Thời gian", _as_text(payload.get("occurred_at"))),
        )
        markdown = _markdown_lines("**📋 Đã thêm nhiệm vụ**", "", body)
        return NotificationMessage(title=title, summary=summary, markdown=markdown)

    if event_type == EVENT_TASK_COMPLETED:
        task_title = _task_title(payload)
        platform_result = _task_platform_result(payload)
        title = "Y2A-Auto ✅ Nhiệm vụ đã hoàn thành"
        summary = f"{task_title} | {platform_result}"
        body = _section_block(
            _kv("Tiêu đề video", _truncate(task_title, 120)),
            _kv("ID nhiệm vụ", f"`{_as_text(payload.get('task_id'))}`"),
            _kv("Kết quả đăng tải", platform_result),
            _kv("Nền tảng đăng tải", _upload_target_label(payload.get("upload_target"))),
            _kv("Thời gian", _as_text(payload.get("occurred_at"))),
        )
        markdown = _markdown_lines("**✅ Nhiệm vụ đã hoàn thành**", "", body)
        return NotificationMessage(title=title, summary=summary, markdown=markdown)

    if event_type == EVENT_TASK_FAILED:
        task_title = _task_title(payload)
        error_text = _pretty_error_text(payload.get("error_message"))
        title = "Y2A-Auto ❌ Nhiệm vụ thất bại"
        summary = f"{task_title} | {error_text}"
        body = _section_block(
            _kv("Tiêu đề video", _truncate(task_title, 120)),
            _kv("ID nhiệm vụ", f"`{_as_text(payload.get('task_id'))}`"),
            _kv("Trạng thái hiện tại", _as_text(payload.get("status")) or "failed"),
            _kv("Nền tảng đăng tải", _upload_target_label(payload.get("upload_target"))),
        )
        markdown = _markdown_lines("**❌ Nhiệm vụ thất bại**", "", body, "", f"> **Chi tiết lỗi:**", f"> {error_text}", "", f"> {_kv('Thời gian', _as_text(payload.get('occurred_at')))}")
        return NotificationMessage(title=title, summary=summary, markdown=markdown)

    if event_type == EVENT_LOGIN_SUCCESS:
        ip = _as_text(payload.get("ip_address")) or "unknown"
        occurred_at = _as_text(payload.get("occurred_at"))
        title = "Y2A-Auto 🔐 Đăng nhập trang quản trị thành công"
        summary = f"{ip} | {occurred_at}"
        body = _section_block(
            _kv("IP nguồn", ip),
            _kv("Thời gian", occurred_at),
        )
        markdown = _markdown_lines("**🔐 Đăng nhập trang quản trị thành công**", "", body)
        return NotificationMessage(title=title, summary=summary, markdown=markdown)

    if event_type == EVENT_LOGIN_LOCKED:
        ip = _as_text(payload.get("ip_address")) or "unknown"
        failed = _as_text(payload.get("failed_attempts"))
        max_att = _as_text(payload.get("max_attempts"))
        lock_min = _as_text(payload.get("lock_minutes"))
        occurred_at = _as_text(payload.get("occurred_at"))
        title = "Y2A-Auto 🚫 Đăng nhập đã bị khóa"
        summary = f"{failed}/{max_att} | {lock_min} phút"
        body = _section_block(
            _kv("IP nguồn", ip),
            _kv("Số lần thất bại", f"{failed}/{max_att}"),
            _kv("Thời gian khóa", f"{lock_min} phút"),
            _kv("Thời gian", occurred_at),
        )
        markdown = _markdown_lines("**🚫 Đăng nhập đã bị khóa**", "", body)
        return NotificationMessage(title=title, summary=summary, markdown=markdown)

    if event_type in (EVENT_QR_LOGIN_SUCCESS, EVENT_QR_LOGIN_FAILED):
        platform = _as_text(payload.get("platform")) or "nền tảng"
        is_success = event_type == EVENT_QR_LOGIN_SUCCESS
        icon = "✅" if is_success else "❌"
        status_text = "Thành công" if is_success else "Thất bại"
        message = _truncate(_as_text(payload.get("message")) or ("Đã lưu Cookies" if is_success else "Đăng nhập thất bại"), 300)
        occurred_at = _as_text(payload.get("occurred_at"))
        title = f"Y2A-Auto {icon} {platform} đăng nhập bằng mã QR {status_text}"
        summary = f"{platform} | {message}"
        body = _section_block(
            _kv("Nền tảng", platform),
            _kv("Kết quả", message),
            _kv("Thời gian", occurred_at),
        )
        markdown = _markdown_lines(f"**{icon} {platform} đăng nhập bằng mã QR {status_text}**", "", body)
        return NotificationMessage(title=title, summary=summary, markdown=markdown)

    title = "Y2A-Auto 💬 Thông báo hệ thống"
    serialized = json.dumps(payload, ensure_ascii=False)
    summary = _truncate(serialized, 180)
    body = _section_block(
        _kv("Sự kiện", event_type),
        _kv("Nội dung", _truncate(serialized, 1500)),
    )
    markdown = _markdown_lines("**💬 Thông báo hệ thống**", "", body)
    return NotificationMessage(title=title, summary=summary, markdown=markdown)
