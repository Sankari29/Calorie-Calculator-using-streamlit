import streamlit as st

# Title
st.title("🔥 Daily Calorie Needs Calculator")

# User Inputs
gender = st.radio("Select your gender:", ("Male", "Female"))
age = st.number_input("Enter your age (years)", min_value=1, max_value=120, step=1)
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (cm)", min_value=50.0, format="%.2f")

# Activity Level Selection
activity_levels = {
    "Sedentary (little to no exercise)": 1.2,
    "Lightly active (1-3 days of exercise)": 1.375,
    "Moderately active (3-5 days of exercise)": 1.55,
    "Very active (6-7 days of exercise)": 1.725,
    "Super active (athlete level)": 1.9
}
activity = st.selectbox("Select your activity level:", list(activity_levels.keys()))

# Calculate BMR (Basal Metabolic Rate)
if height > 0 and weight > 0 and age > 0:
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Calculate TDEE (Total Daily Energy Expenditure)
    tdee = bmr * activity_levels[activity]
    
    st.write(f"### Your Basal Metabolic Rate: {bmr:.2f} kcal/day")
    st.write(f"### Your Total Daily Energy Expenditure: {tdee:.2f} kcal/day")

    # Calorie Recommendations
    st.subheader("🍽️ Calorie Recommendations:")
    st.info(f"**To maintain weight:** {tdee:.2f} kcal/day")
    st.success(f"**To lose weight (deficit 500 kcal/day):** {tdee - 500:.2f} kcal/day")
    st.warning(f"**To gain weight (surplus 500 kcal/day):** {tdee + 500:.2f} kcal/day")

# Run the app using: streamlit run calorie_calculator.py
