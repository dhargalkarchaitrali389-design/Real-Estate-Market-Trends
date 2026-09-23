import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Real Estate Market Trends",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Real Estate Market Trends")
st.write("Analyze property prices, locations, and market trends using simple statistical analysis.")

# Sample dataset
data = {
    "Location": [
        "Mumbai", "Pune", "Bangalore", "Delhi", "Mumbai",
        "Pune", "Bangalore", "Delhi", "Mumbai", "Pune",
        "Bangalore", "Delhi"
    ],
    "Property_Type": [
        "Apartment", "Apartment", "Villa", "Apartment",
        "Villa", "Apartment", "Apartment", "Villa",
        "Apartment", "Villa", "Villa", "Apartment"
    ],
    "Area_sqft": [
        850, 1100, 1500, 950, 1800, 1200,
        1000, 1600, 900, 1700, 1550, 1050
    ],
    "Price_Lakhs": [
        95, 75, 120, 85, 180, 90,
        110, 150, 100, 135, 125, 88
    ],
    "Bedrooms": [
        2, 2, 3, 2, 4, 3,
        2, 4, 3, 4, 3, 2
    ]
}

df = pd.DataFrame(data)

st.subheader("📊 Property Dataset")
st.dataframe(df, use_container_width=True)

# Key metrics
st.subheader("📌 Market Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Price", f"₹{df['Price_Lakhs'].mean():.1f} Lakh")
col2.metric("Average Area", f"{df['Area_sqft'].mean():.0f} sq.ft")
col3.metric("Average Bedrooms", f"{df['Bedrooms'].mean():.1f}")
col4.metric("Properties", len(df))

# Location analysis
st.subheader("📍 Average Property Price by Location")

location_price = df.groupby("Location")["Price_Lakhs"].mean().sort_values(ascending=False)

fig, ax = plt.subplots()
location_price.plot(kind="bar", ax=ax)
ax.set_xlabel("Location")
ax.set_ylabel("Average Price (Lakhs)")
ax.set_title("Average Property Price by Location")
plt.xticks(rotation=45)
st.pyplot(fig)

# Area vs price
st.subheader("📈 Property Area vs Price")

fig2, ax2 = plt.subplots()
ax2.scatter(df["Area_sqft"], df["Price_Lakhs"])
ax2.set_xlabel("Area (sq.ft)")
ax2.set_ylabel("Price (Lakhs)")
ax2.set_title("Relationship Between Property Area and Price")
st.pyplot(fig2)

# Property type analysis
st.subheader("🏘️ Property Type Analysis")

type_summary = df.groupby("Property_Type").agg(
    Average_Price=("Price_Lakhs", "mean"),
    Average_Area=("Area_sqft", "mean"),
    Number_of_Properties=("Property_Type", "count")
).round(2)

st.dataframe(type_summary, use_container_width=True)

# Statistical analysis
st.subheader("📐 Statistical Analysis")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Minimum Price",
    f"₹{df['Price_Lakhs'].min():.0f} Lakh"
)

col2.metric(
    "Maximum Price",
    f"₹{df['Price_Lakhs'].max():.0f} Lakh"
)

col3.metric(
    "Median Price",
    f"₹{df['Price_Lakhs'].median():.0f} Lakh"
)

st.subheader("💡 Key Insights")

highest_location = location_price.idxmax()
lowest_location = location_price.idxmin()

st.write(
    f"• **{highest_location}** has the highest average property price in this sample."
)

st.write(
    f"• **{lowest_location}** has the lowest average property price in this sample."
)

st.write(
    "• Larger properties generally tend to have higher prices in this sample."
)

st.write(
    "• The dataset demonstrates how statistical analysis can be used to understand real-estate market patterns."
)

st.success("✅ Real Estate Market Trends analysis completed!")