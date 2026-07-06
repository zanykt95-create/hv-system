path = "HV_System_Kien_Truc.html"
data = open(path, encoding="utf-8").read()

def rep(old, new, count=1):
    global data
    n = data.count(old)
    assert n >= count, f"NOT FOUND ({n} occurrences): {old[:80]!r}"
    data = data.replace(old, new, count)

# 1. Remove CSS for phase-badge / roadmap / upcoming
rep("""  .phase-badge{
    display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;
    border-radius:999px;letter-spacing:.2px;margin-left:8px;vertical-align:middle;
    white-space:nowrap;
  }
  .phase-badge.p1{background:#E4F3E8;color:#1E7A42;border:1px solid #BFE3CB;}
  .phase-badge.p2{background:#FBF1DD;color:#96690F;border:1px solid #F0DDA9;}
  .pillar.upcoming{border-style:dashed;background:repeating-linear-gradient(135deg,var(--kh-bg),var(--kh-bg) 10px,#fdf6ea 10px,#fdf6ea 20px);}

  /* Roadmap banner in hero */
  .roadmap-banner{
    display:flex;gap:10px 20px;flex-wrap:wrap;align-items:center;
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.18);
    border-radius:10px;
    padding:13px 18px;
    margin-top:22px;
    font-size:13px;
    color:rgba(255,255,255,0.95);
  }
  .roadmap-banner b{color:#fff;}
  .roadmap-chip{
    background:rgba(255,255,255,0.14);padding:4px 11px;border-radius:999px;
    font-size:12px;font-weight:600;
  }
  .roadmap-chip.now{background:#2E8B57;color:#fff;}
  .roadmap-chip.later{background:rgba(255,255,255,0.14);color:#fff;border:1px dashed rgba(255,255,255,0.5);}""", "")

# 2. Remove phase-badge / roadmap-chip from the font-family selector list
rep(
 'h1,h2,h3,h4,.arch-root,.mf-box,.pillar h4,details.card summary,.eyebrow,nav.quicknav a,.phase-badge,.roadmap-chip{',
 'h1,h2,h3,h4,.arch-root,.mf-box,.pillar h4,details.card summary,.eyebrow,nav.quicknav a{'
)

# 3. Remove roadmap banner markup from hero
rep("""    <div class="roadmap-banner">
      <span>🗺️ <b>Lộ trình triển khai:</b></span>
      <span class="roadmap-chip now">Giai đoạn 1 — ATS + Information Employee (ưu tiên hiện tại)</span>
      <span class="roadmap-chip later">Giai đoạn 2 — Knowledge Hub (chuẩn bị từng bước, triển khai sau)</span>
    </div>
""", "")

# 4. Overview pillars: remove phase badges
rep('<h4>🎯 ATS<span class="phase-badge p1">Giai đoạn 1</span></h4>', '<h4>🎯 ATS</h4>')
rep('<h4>👤 Information Employee<span class="phase-badge p1">Giai đoạn 1</span></h4>', '<h4>👤 Information Employee</h4>')

# 5. Knowledge Hub pillar: remove upcoming style + badge + rewrite tag/chips
rep('<div class="pillar kh upcoming">', '<div class="pillar kh">')
rep("""          <h4>🧠 Knowledge Hub<span class="phase-badge p2">Giai đoạn 2</span></h4>
          <span class="tag">Chuẩn bị từng bước, triển khai sau</span>
          <div class="chip-list">
            <span class="chip">SOW của 6 team</span>
            <span class="chip">SOP của 6 team</span>
            <span class="chip">Kaizen cải tiến</span>
            <span class="chip">Trợ lý AI tra cứu nghiệp vụ</span>
          </div>""", """          <h4>🧠 Knowledge Hub</h4>
          <span class="tag">Nền tảng quản trị tri thức tập trung</span>
          <div class="chip-list">
            <span class="chip">Chuẩn hóa &amp; lưu trữ tài liệu</span>
            <span class="chip">Chia sẻ tri thức toàn HV</span>
            <span class="chip">AI Assistant tra cứu</span>
          </div>""")

# 6. Section headings: remove phase badges
rep('<h2>2. ATS — Hệ thống quản lý tuyển dụng<span class="phase-badge p1">Giai đoạn 1</span></h2>',
    '<h2>2. ATS — Hệ thống quản lý tuyển dụng</h2>')
rep('<h2>3. HR App — Information Employee (Thông tin nhân viên)<span class="phase-badge p1">Giai đoạn 1</span></h2>',
    '<h2>3. HR App — Information Employee (Thông tin nhân viên)</h2>')
rep('<h2>4. AI Agent &amp; Knowledge Hub<span class="phase-badge p2">Giai đoạn 2 — chuẩn bị sau</span></h2>',
    '<h2>4. AI Agent &amp; Knowledge Hub</h2>')

# 7. Knowledge Hub section description -> new condensed copy
rep(
 '<p class="section-desc">Lớp tri thức trung tâm — chưa triển khai ngay trong giai đoạn 1, sẽ chuẩn bị từng bước sau khi ATS &amp; Information Employee ổn định. Khi triển khai, Knowledge Hub sẽ chuẩn hóa tài liệu nội bộ từ cả 6 team (TA, HR, C&amp;B, Admin, L&amp;D, IC/Branding) và cung cấp trợ lý AI Agent cho toàn bộ HV Team.</p>',
 '<p class="section-desc">Nền tảng quản trị tri thức tập trung của HV Team — chuẩn hóa, lưu trữ và chia sẻ tài liệu nghiệp vụ. AI Assistant hỗ trợ tra cứu hướng dẫn nghiệp vụ bằng ngôn ngữ tự nhiên, nhanh chóng và thuận tiện.</p>'
)

# 8. kh-side note: drop "khi hoàn thiện" future framing
rep(
 '<b>Truy vấn thông tin nhân sự</b> — khi hoàn thiện, AI Agent sẽ kết nối hai chiều với dữ liệu nhân sự trong HV System (phân quyền truy cập, bảo mật), cho phép trả lời câu hỏi tra cứu bằng ngôn ngữ tự nhiên dựa trên cả tài liệu quy trình lẫn dữ liệu thực tế từ ATS &amp; Information Employee.',
 '<b>Truy vấn thông tin nhân sự</b> — AI Agent kết nối hai chiều với dữ liệu nhân sự trong HV System (phân quyền truy cập, bảo mật), trả lời câu hỏi tra cứu bằng ngôn ngữ tự nhiên dựa trên cả tài liệu quy trình lẫn dữ liệu thực tế.'
)

open(path, "w", encoding="utf-8").write(data)
print("OK, new length:", len(data))
