import streamlit as st

# 页面标题
st.markdown("<h1 style='text-align:center;color:orange;'>录音、放音测试</h1>", unsafe_allow_html=True)

# 提示说明
st.markdown("""
<p style='text-align:left;color:blue;'>
朗读任意一段试音内容，并在界面右下角调节录（放）音音量。
</p>
""", unsafe_allow_html=True)

# 中英文文本框，带边框和背景色
st.markdown("""
<div style="border:2px solid #ccc; padding:15px; border-radius:10px;
            background-color:green; text-align:left; font-size:18px; line-height:1.8;">
            
 <span style="color:blue;">生活就像海洋，只有意志坚强的人，才能到达彼岸。
 
 <hr style="border:1px dashed #aaa;">
 
 <span style="color:blue;">This is an apple. I like apples. Apples are good for our health.
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
  msg.lang = "zh-CN";   //  中文优先，能同时识别英文
  window.speechSynthesis.speak(msg);
}
</script>
"""

st.components.v1.html(speak_button, height=150)

