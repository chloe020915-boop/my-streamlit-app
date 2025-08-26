import streamlit as st

# 页面标题
st.markdown("<h2 style='text-align:center;color:orange;'>请按照图示佩戴耳机</h2>", unsafe_allow_html=True)

# 佩戴耳机示意图
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("images/image1.jpg", width=150)
    st.markdown("<p style='color:blue; font-size:14px;'>话筒略低于嘴巴，距离嘴巴2–3cm。</p>", unsafe_allow_html=True)

with col2:
    st.image("images/image2.jpg", width=150)
    st.markdown("<p style='color:red; font-size:14px;'>录音过程中用手碰话筒</p>", unsafe_allow_html=True)

with col3:
    st.image("images/image3.jpg", width=150)
    st.markdown("<p style='color:red; font-size:14px;'>话筒距离太远</p>", unsafe_allow_html=True)

with col4:
    st.image("images/image4.jpg", width=150)
    st.markdown("<p style='color:red; font-size:14px;'>话筒距离太近</p>", unsafe_allow_html=True)

#测试标题
st.markdown("<h2 style='text-align:center;color:orange;'>录音、放音测试</h2>", unsafe_allow_html=True)

# 提示说明
st.markdown("""
<p style='text-align:left;color:blue;'>
朗读任意一段试音内容，并在界面右下角调节录（放）音音量。
</p>
""", unsafe_allow_html=True)

# 中英文文本框，带边框和背景色
st.markdown("""
<div style="border:2px solid #ccc; padding:15px; border-radius:10px;
            background-color:lightgreen; text-align:left; font-size:18px; line-height:1.8;">
            
 <span style="color:royalblue;">生活就像海洋，只有意志坚强的人，才能到达彼岸。
 
 <hr style="border:1px dashed #aaa;">
 
 <span style="color:royalblue;">This is an apple. I like apples. Apples are good for our health.
</div>
""", unsafe_allow_html=True)

# 模拟按钮
speak_button = """
<div style="text-align:center; margin-top:20px;">
    <button onclick="speak()" 
            style="padding:10px 20px; font-size:16px; background-color:#f4a261;
                   border-radius:5px; color:white; border:none; cursor:pointer;">
        开始朗读（并非朗读）
     </button>
</div>  

<script>
function speak(){
  let msg = new SpeechSynthesisUtterance(
      "生活就像海洋，只有意志坚强的人，才能到达彼岸。This is an apple. I like Apples. Apples are good for our health."
  );
  
  window.speechSynthesis.speak(msg);
}
</script>
"""

st.components.v1.html(speak_button, height=150)

