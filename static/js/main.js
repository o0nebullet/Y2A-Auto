// File JavaScript chính
document.addEventListener('DOMContentLoaded', function() {
    console.log('Y2A-Auto đã tải xong');

    // --- Logic bảo vệ bằng mật khẩu của trang cài đặt ---
    const settingsForm = document.querySelector('form[method="post"][enctype="multipart/form-data"]');
    if (settingsForm) {
        const newPassword = document.getElementById('new_password');
        const confirmPassword = document.getElementById('confirm_password');
        const passwordError = document.getElementById('password-match-error');
        const passwordProtectionEnabled = document.getElementById('password_protection_enabled');
        const passwordFields = document.getElementById('password-fields');

        if (passwordProtectionEnabled) {
            function togglePasswordFields() {
                if (passwordProtectionEnabled.checked) {
                    passwordFields.style.display = 'block';
                } else {
                    passwordFields.style.display = 'none';
                }
            }

            // Initial state
            togglePasswordFields();
            passwordProtectionEnabled.addEventListener('change', togglePasswordFields);
        }

        settingsForm.addEventListener('submit', function(event) {
            // Chỉ kiểm tra khớp mật khẩu khi đã bật bảo vệ bằng mật khẩu
            if (passwordProtectionEnabled && passwordProtectionEnabled.checked &&
                newPassword && confirmPassword && newPassword.value !== confirmPassword.value) {
                event.preventDefault(); // Ngăn gửi form
                if (passwordError) {
                    passwordError.classList.remove('d-none');
                }
            } else {
                if (passwordError) {
                    passwordError.classList.add('d-none');
                }
            }
        });
    }


    // --- Logic nút dọn nhật ký của trang cài đặt ---
    // Gắn nút dọn nhật ký thủ công
    const manualCleanupBtn = document.getElementById('manual-cleanup-btn');
    const logCleanupHoursField = document.getElementById('log-cleanup-hours');
    const cleanupHoursHidden = document.getElementById('cleanup-hours-input');
    if(manualCleanupBtn) {
        manualCleanupBtn.addEventListener('click', function() {
            // Dùng số giờ vừa nhập (nếu có)
            if (logCleanupHoursField && cleanupHoursHidden) {
                const hours = parseInt(logCleanupHoursField.value, 10);
                if (!isNaN(hours) && hours > 0) {
                    cleanupHoursHidden.value = hours;
                }
            }
            const confirmMsg = `Bạn có chắc muốn dọn nhật ký cũ thủ công? Sẽ xóa nhật ký từ ${cleanupHoursHidden ? cleanupHoursHidden.value : ''} giờ trước các file nhật ký.`;
            if (confirm(confirmMsg)) {
                const form = document.getElementById('cleanup-form');
                if (form) form.submit();
            }
        });
    }

    // Gắn nút xóa ngay nhật ký
    const clearLogsBtn = document.getElementById('clear-logs-btn');
    const confirmClearBtn = document.getElementById('confirm-clear-btn');
    const cancelClearBtn = document.getElementById('cancel-clear-btn');
    const clearWarning = document.getElementById('clear-warning');

    if (clearLogsBtn) {
        clearLogsBtn.addEventListener('click', function() {
            clearLogsBtn.classList.add('d-none');
            confirmClearBtn.classList.remove('d-none');
            cancelClearBtn.classList.remove('d-none');
            clearWarning.classList.remove('d-none');
        });
    }

    if (cancelClearBtn) {
        cancelClearBtn.addEventListener('click', function() {
            clearLogsBtn.classList.remove('d-none');
            confirmClearBtn.classList.add('d-none');
            cancelClearBtn.classList.add('d-none');
            clearWarning.classList.add('d-none');
        });
    }
    
    if (confirmClearBtn) {
        confirmClearBtn.addEventListener('click', function() {
             document.getElementById('clear-form').submit();
        });
    }

    // --- Logic nút dọn nội dung đã tải của trang cài đặt ---
    // Gắn nút dọn nội dung đã tải thủ công
    const manualDownloadCleanupBtn = document.getElementById('manual-download-cleanup-btn');
    const downloadCleanupHoursField = document.getElementById('download-cleanup-hours');
    const downloadCleanupHoursHidden = document.getElementById('download-cleanup-hours-input');
    if(manualDownloadCleanupBtn) {
        manualDownloadCleanupBtn.addEventListener('click', function() {
            // Dùng số giờ vừa nhập (nếu có)
            if (downloadCleanupHoursField && downloadCleanupHoursHidden) {
                const hours = parseInt(downloadCleanupHoursField.value, 10);
                if (!isNaN(hours) && hours > 0) {
                    downloadCleanupHoursHidden.value = hours;
                }
            }
            const confirmMsg = `Bạn có chắc muốn dọn nội dung đã tải cũ thủ công? Sẽ xóa file và thư mục đã tải từ ${downloadCleanupHoursHidden ? downloadCleanupHoursHidden.value : ''} giờ trước các file và thư mục đã tải.`;
            if (confirm(confirmMsg)) {
                const form = document.getElementById('download-cleanup-form');
                if (form) form.submit();
            }
        });
    }
}); 