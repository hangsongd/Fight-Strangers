import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
import pytz
st.set_page_config(
    page_title="Tâm Trạng Ký - Máy Đo Cảm Xúc",
    page_icon="🔮",
    layout="centered"
)
st.title("🔮 Máy Đo Tâm Trạng & Gợi Ý Vui Vẻ")
st.write("Hãy dành một phút để kiểm tra xem hôm nay bạn đang cảm thấy thế nào nhé!")
st.divider()
st.sidebar.header("⚙️ Cấu hình thời gian")
use_custom_time = st.sidebar.checkbox("Không thích thời gian hiện tại? Tùy chỉnh thời gian", value=False)
tz_VN = pytz.timezone('Asia/Ho_Chi_Minh')
now_VN = datetime.now(tz_VN)

if use_custom_time:
    custom_time_str = st.sidebar.text_input("📝 CÀI ĐẶT THỜI GIAN (Định dạng HH:MM:SS):", value="20:25:00")
    try:
        parsed_time = datetime.strptime(custom_time_str, "%H:%M:%S")
        current_hour = parsed_time.hour
        current_minute = parsed_time.minute
        time_display = custom_time_str
    except ValueError:
        st.sidebar.error("❌ Định dạng sai! Vui lòng nhập đúng kiểu HH:MM:SS (Ví dụ: 09:00:00 hoặc 22:15:00)")
        current_hour = now_VN.hour
        current_minute = now_VN.minute
        time_display = now_VN.strftime("%H:%M:%S")
else:
    current_hour = now_VN.hour
    current_minute = now_VN.minute
    time_display = now_VN.strftime("%H:%M:%S")
st.subheader("📝 Form Đánh Giá Cảm Xúc")
name = st.text_input("Tên của bạn là gì?", "Bạn giấu tên")

current_action = st.selectbox(
    "Bây giờ bạn đang làm gì?",
    ["Chơi game", "Chuẩn bị đi ngủ", "Đi tắm", "Ăn Vặt", "Làm Việc", "Ngồi Chill (Ngồi im)"]
)
diet_habit = st.radio(
    "Bạn thường xuyên ăn gì?",
    ["Đồ ăn nhà làm", "Đồ ăn nhanh"],
    horizontal=True
)
happiness_level = st.slider(
    "Mức độ năng lượng hiện tại (0: Kiệt quệ, 100: Bùng nổ):",
    min_value=0, max_value=100, value=50
)

if st.button("🔮 Phân tích tâm trạng của tôi ngay!"):
    
    with st.spinner("Đang đọc sóng não và phân tích dữ liệu..."):
        time.sleep(1)
        
    st.balloons()
    st.success(f"Phân tích hoàn tất! Chúc mừng {name} đã hoàn thành bài kiểm tra.")
    

    st.subheader("⏰ Phân tích mốc thời gian:")
    st.write(f"⏱️ **Mốc thời gian đang kiểm tra:** `{time_display}`")

    total_minutes = current_hour * 60 + current_minute
    early_bedtime_limit = 20 * 60 + 15  # Mốc 8:15 tối (20:15)
    
    if current_action == "Chơi game":
        if current_hour >= 22 or current_hour < 4:
            st.error(f"🌙 Đã {time_display} rồi! Bạn **nên tắt game và đi ngủ ngay** để bảo vệ sức khỏe, tránh thức cú đêm nhé!")
        else:
            st.success(f"🎮 Hiện tại là {time_display}. Bạn có thể **giải lao thêm một chút**, nhưng nhớ giới hạn thời gian chơi dưới 1 tiếng nhé!")
            
    elif current_action == "Chuẩn bị đi ngủ":
        if 4 * 60 <= total_minutes < early_bedtime_limit:
            st.warning(f"🥱 Thời gian này ({time_display}) hơi sớm phải không? Hãy đợi thêm 1 chút nữa để đi ngủ nhé!")
        elif current_hour >= 23 or current_hour < 4:
            st.error(f"⚠️ Đã {time_display} rồi, bạn ngủ quá muộn rồi đó! Nhắm mắt và ngủ sâu ngay thôi.")
        else:
            st.success(f"✨ Giờ giấc đi ngủ của bạn lúc {time_display} rất hợp lý và khoa học. Chúc bạn ngủ ngon!")
            
    elif current_action == "Làm Việc":
        if current_hour >= 21 or current_hour < 5:
            st.warning(f"⚠️ Đã {time_display} muộn rồi. Bạn nên hoàn thành nốt công việc và đi nghỉ, làm việc muộn giảm hiệu suất đấy.")
        else:
            st.info(f"💻 Giờ này ({time_display}) làm việc là rất tập trung. Cố lên nhé!")

    else:
        st.info(f"✨ Bạn đang `{current_action}` vào lúc {time_display}. Hãy tận hưởng khoảnh khắc này một cách thoải mái nhất.")
    st.subheader("📊 Kết quả phân tích từ AI:")
    if happiness_level >= 80:
        st.write(f"🎉 Tuyệt vời! Bạn đang tràn đầy năng lượng tích cực ({happiness_level}/100).")
        st.snow()
    elif happiness_level >= 40:
        st.write(f"🙂 Tâm trạng ở mức ổn định ({happiness_level}/100).")
    else:
        st.write(f"😟 Có vẻ hôm nay bạn hơi mệt mỏi ({happiness_level}/100).")
    chart_data = pd.DataFrame(
        np.random.randn(5, 1) * 10 + (happiness_level + 10),
        columns=['Mức năng lượng (%)']
    )
    chart_data.index = ['Giờ 1', 'Giờ 2', 'Giờ 3', 'Giờ 4', 'Giờ 5']
    st.line_chart(chart_data)
    st.subheader("🚫 Những lưu ý bạn KHÔNG NÊN làm lúc này:")
    
    if diet_habit == "Đồ ăn nhanh":
        st.warning("- **Không nên** tiếp tục ăn đồ ăn nhanh vào buổi tối hoặc ăn quá 3 lần/tuần để tránh thừa cân, béo phì.")
    else:
        st.info("- **Phát huy:** Đồ ăn nhà làm rất tốt, không nên bỏ bữa hoặc ăn ngoài khi không cần thiết.")
        
    if current_action == "Chuẩn bị đi ngủ":
        st.error("- **Không nên** bấm điện thoại, lướt TikTok hoặc xem phim kịch tính vì ánh sáng xanh sẽ làm bạn mất ngủ.")
    elif current_action == "Đi tắm":
        if current_hour >= 23 or current_hour < 4:
            st.error("- **Tuyệt đối KHÔNG NÊN** tắm đêm muộn sau 11h đêm vì rất nguy hiểm cho mạch máu và tim mạch.")
        else:
            st.warning("- **Không nên** tắm quá lâu bằng nước quá lạnh hoặc quá nóng.")
    elif current_action == "Ăn Vặt":
        st.warning("- **Không nên** ăn vặt sát giờ ngủ chính vì sẽ gây đầy bụng, khó tiêu và tích mỡ.")
    elif current_action == "Ngồi Chill (Ngôì im)":
        st.warning("- **Không nên** chìm đắm vào các suy nghĩ tiêu cực hoặc quá khứ buồn phiền khi ngồi một mình.")
