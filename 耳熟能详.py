import streamlit as st

st.title("朗读练习")

text = "生活就像海洋，只有意志坚强的人，才能到达彼岸。\nThis is an apple. I like apples. Apples are good for our health."

st.text_area("朗读文本：", text, height=150)

speak_button = """
<button onclick="speak()">🔊 点击朗读</button>
<script>
function speak(){
  let msg1 = new SpeechSynthesisUtterance("生活就像海洋，只有意志坚强的人，才能到达彼岸。");
  msg1.lang = "zh-CN";  // 中文
  
  let msg2 = new SpeechSynthesisUtterance("This is an apple. I like Apples. Apples are good for our health.");
  msg2.lang = "en-US";   //  英文
  
  window.speechSynthesis.speak(msg1);
  window.speechSynthesis.speak(msg2);
}
</script>
"""

st.components.v1.html(speak_button, height=100)

