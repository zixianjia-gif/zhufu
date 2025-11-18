import streamlit as st
import random
import datetime

def generate_positive_fortune():
    """生成一个积极的运势描述，并加上特定前缀"""
    positive_fortunes = [
        "今天，幸运女神将格外眷顾你，一切都将顺心如意！",
        "你的魅力值今日飙升，人际关系和谐，贵人运极佳！",
        "财运亨通，意外之喜可能降临，小投入大回报！",
        "健康活力充沛，精神饱满，是开启新挑战的好时机！",
        "学业或事业上会有突破性进展，灵感源源不断！",
        "爱情运甜蜜升温，和心爱的人关系更进一步，单身者可能遇到心仪对象！",
        "心情愉悦，充满正能量，周围的人都会被你感染！",
        "小幸运不断，可能会收到意想不到的礼物或好消息！",
        "今日宜大胆尝试新事物，会有意想不到的收获和惊喜！",
        "内心平静，充满智慧，今日的每一个决定都将是明智之举！",
        "遇到困难时总有贵人相助，逢凶化吉，一切顺利！",
        "创意无限，是发挥才能、展现独特想法的好日子！",
        "旅行运佳，即使是短途出行也能收获美好体验和放松心情！",
        "友情升华，与朋友们共同创造美好回忆，感受温暖与支持！",
        "今天适合整理思绪，做出重要规划，会发现前路豁然开朗！"
    ]
    
    selected_fortune = random.choice(positive_fortunes)
    return f"贾子先觉得{selected_fortune}"

def main():
    st.set_page_config(
        page_title="每日好运势 ✨",
        page_icon="🍀",
        layout="centered"
    )

    st.title("💖 贾子先的运势计算器 ✨")
    st.write("---")
    
    # 注意：这里使用了三引号，必须成对出现
    st.markdown(
        """
        ### 亲爱的朋友，愿你的每一天都充满阳光和好运！
        点击下方按钮，看看贾子先觉得你今天运势如何吧！
        """
    )

    # 获取今天的日期
    today = datetime.date.today()
    today_str = today.strftime("%Y-%m-%d")

    # 使用session state来存储今天的运势
    if f"fortune_for_{today_str}" not in st.session_state:
        st.session_state[f"fortune_for_{today_str}"] = generate_positive_fortune()
        st.session_state["last_draw_date"] = today_str 

    # 检查是否是新的一天
    if st.session_state.get("last_draw_date") != today_str:
        st.session_state[f"fortune_for_{today_str}"] = generate_positive_fortune()
        st.session_state["last_draw_date"] = today_str

    st.subheader(f"🗓️ {today_str} 的专属好运势：")

    # 创建一个大的容器来显示运势
    with st.container():
        # 这里使用的是f-string多行拼接，注意不要漏掉引号
        st.markdown(
            f"<div style='background-color:#E8F8F5; padding: 20px; border-radius: 10px; border: 2px solid #2ECC71; text-align: center; font-size: 24px; color: #2C3E50; font-weight: bold;'>"
            f"{st.session_state[f'fortune_for_{today_str}']}"
            f"</div>",
            unsafe_allow_html=True
        )

    st.write("---")
    
    # 【易错点】这里的 markdown 也是三引号，请检查你的代码这里是否漏了 """
    st.markdown(
        """
        <p style='text-align: center; font-style: italic; color: #888;'>
        贾子先祝你拥有美好的一天！
        </p>
        """,
        unsafe_allow_html=True
    )

    # 额外添加一个“分享”按钮
    if st.button("🎉 谢谢贾子先！", help="点击领取祝福"):
        st.balloons() 

if __name__ == "__main__":
    main()