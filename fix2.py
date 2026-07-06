path = "HV_System_Kien_Truc.html"
data = open(path, encoding="utf-8").read()

def rep(old, new, count=1):
    global data
    n = data.count(old)
    assert n >= count, f"NOT FOUND: {old[:100]!r}"
    data = data.replace(old, new, count)

# 1. Remove hero-meta block
rep("""    <div class="hero-meta">
      <span>Nguồn: <b>Miro — Idea HV System</b></span>
      <span>Cập nhật: <b>03/07/2026</b></span>
      <span>Người tổng hợp: <b>Z — Communication Specialist, HV Team</b></span>
    </div>
""", "")

# 2. Add CSS for system-intro block (insert before /* Overview architecture */ block)
old_css_marker = "  /* Overview architecture */"
new_css = """  /* System intro list */
  .system-intro{display:flex;flex-direction:column;gap:14px;margin-bottom:26px;}
  .system-item{
    background:var(--card);border:1px solid var(--border);border-left:4px solid var(--accent);
    border-radius:10px;padding:20px 22px;
  }
  .system-item.s-ats{--accent:var(--ats);}
  .system-item.s-hr{--accent:var(--hr);}
  .system-item.s-kh{--accent:var(--kh);}
  .system-item h3{font-size:16px;margin:0 0 8px;color:var(--accent);}
  .system-item .sys-sub{font-size:12.5px;font-weight:400;color:var(--text-muted);margin-left:4px;}
  .system-item p{font-size:14px;color:var(--text-secondary);margin:0 0 10px;line-height:1.65;}
  .system-item p:last-child{margin-bottom:0;}
  .system-item ul{margin:6px 0 12px;padding-left:20px;}
  .system-item li{font-size:13.5px;color:var(--text-secondary);margin-bottom:4px;}

  /* Overview architecture */"""
rep(old_css_marker, new_css)

# 3. Replace section-desc + insert system-intro block, right before the <div class="arch">
old_block = '''    <p class="section-desc">Người dùng thao tác qua <b>AI Agent</b> — lớp giao tiếp phía trên <b>HV System</b>. HV System là hệ thống trung tâm, điều phối 3 nhánh nghiệp vụ: <b>ATS</b>, <b>Information Employee (HR App)</b> và <b>Knowledge Hub</b>. Dữ liệu ứng viên trúng tuyển từ ATS được đồng bộ tự động sang HR App khi Onboarding; HR App còn nhận dữ liệu từ 3 hệ thống nội bộ sẵn có (My Talent, Data BigQuery – Thor, My Profile).</p>

    <div class="arch">'''

new_block = '''    <p class="section-desc">Hiện nay, mỗi function đang sử dụng nhiều công cụ và phương thức quản lý khác nhau (Google Sheet, Excel, tài liệu rời rạc, biểu mẫu thủ công...), khiến dữ liệu phân tán, quy trình chưa được chuẩn hóa hoàn toàn và việc tra cứu, phối hợp giữa các bộ phận còn tốn nhiều thời gian. Để giải quyết các vấn đề trên và xây dựng một hệ sinh thái quản trị nhân sự đồng bộ, HV Team dự kiến triển khai 03 hệ thống trọng tâm, tương ứng với ba nhóm nghiệp vụ chính:</p>

    <div class="system-intro">
      <div class="system-item s-ats">
        <h3>1. ATS <span class="sys-sub">(Applicant Tracking System)</span></h3>
        <p>Xây dựng hệ thống quản lý tuyển dụng tập trung dành cho Talent Acquisition, hỗ trợ quản lý toàn bộ quy trình tuyển dụng từ nhu cầu tuyển dụng, pipeline ứng viên, phỏng vấn, đánh giá, offer đến onboarding, đồng thời giảm thao tác thủ công và nâng cao trải nghiệm của recruiter cũng như hiring manager.</p>
      </div>
      <div class="system-item s-hr">
        <h3>2. HR App</h3>
        <p>Xây dựng hệ thống quản lý thông tin nhân sự tập trung (Human Resource Information System), trở thành Single Source of Truth cho toàn bộ vòng đời nhân viên. Hệ thống sẽ quản lý các nghiệp vụ như:</p>
        <ul>
          <li>Onboarding</li>
          <li>Inboarding</li>
          <li>Quản lý hợp đồng &amp; cơ cấu tổ chức</li>
          <li>Phát triển nghề nghiệp &amp; biến động nhân sự</li>
          <li>Chế độ, đãi ngộ &amp; Compensation &amp; Benefits</li>
          <li>Hiệu suất, kỷ luật &amp; Employee Relations</li>
          <li>Offboarding</li>
        </ul>
        <p>Đây sẽ là nền tảng lưu trữ dữ liệu nhân sự xuyên suốt, giúp các function trong HV cùng khai thác trên một nguồn dữ liệu thống nhất.</p>
      </div>
      <div class="system-item s-kh">
        <h3>3. HV Knowledge Hub</h3>
        <p>Xây dựng nền tảng quản trị tri thức tập trung dành cho toàn bộ HV Team, giúp chuẩn hóa, lưu trữ và chia sẻ các tài liệu nghiệp vụ như SOW, SOP, Process, Guideline, Policy, Template và các tài liệu đào tạo. Bên cạnh việc là kho tri thức tập trung, hệ thống sẽ tích hợp AI Assistant, cho phép người dùng tra cứu hướng dẫn nghiệp vụ bằng ngôn ngữ tự nhiên, giúp tiếp cận thông tin nhanh chóng và thuận tiện hơn.</p>
      </div>
    </div>

    <div class="arch">'''

rep(old_block, new_block)

open(path, "w", encoding="utf-8").write(data)
print("OK new length", len(data))
