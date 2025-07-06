import streamlit as st

st.set_page_config(page_title="Cinespa Feedback Form", page_icon="🎬")

st.title("🎬 Cinespa – Lifestyle Home Technology Destination")
st.subheader("Feedback Form for Visiting Architects and Designers")

st.markdown("We’d love your thoughts about your visit to **Cinespa**! Please fill in the form below:")

# Form layout
with st.form("feedback_form"):
    name = st.text_input("👤 Your Name")
    firm = st.text_input("🏢 Name of your Architectural Firm")
    designation = st.text_input("💼 Your Designation")
    rating = st.slider("⭐ Rate your experience at Cinespa", 1, 5, 3)
    feedback = st.text_area("📝 Your Feedback about the Experience Centre")

    submitted = st.form_submit_button("Submit Feedback")

# Handle submission
if submitted:
    if not name or not firm or not designation or not feedback:
        st.error("❗ Please fill in all the required fields.")
    else:
        st.success("✅ Thank you for your feedback!")
        st.markdown("### 📋 Summary of Your Response:")
        st.write(f"**Name:** {name}")
        st.write(f"**Firm:** {firm}")
        st.write(f"**Designation:** {designation}")
        st.write(f"**Rating:** {rating}/5")
        st.write(f"**Feedback:** {feedback}")
        
        st.markdown("---")
        st.markdown("> 🧠 *“Technology is best when it brings people together.”*")
        st.markdown("Thank you for visiting **Cinespa – Lifestyle Home Technology Destination**. We look forward to hosting you again!")

