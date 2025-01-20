import os
import streamlit as st

# عرض المسار الحالي
st.write("المسار الحالي:", os.getcwd())

# عرض الملفات في المجلد الحالي
st.write("الملفات في المجلد الحالي:", os.listdir())

# إذا كان الملف موجودًا في المجلد الحالي أو في مجلد فرعي
model_path = "C:/Users/PC/digit_recognizer/dig_model.keras"

# التحقق من وجود الملف
if os.path.exists(model_path):
    st.success(f"تم العثور على الملف في المسار: {model_path}")
else:
    st.warning(f"الملف {model_path} غير موجود!")
