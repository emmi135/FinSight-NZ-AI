import streamlit as st
import pandas as pd

def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        return None

def get_public_orgs(df):
    public_df = df[df["Public?"] == 1]
    num = len(public_df)
    return num

def revenue_per_industry(df):
    revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
    count_by_industry = df["Industry"].value_counts()
    rev_ratio = revenue_by_industry / count_by_industry
    return rev_ratio

def highest_revenue_industry(df):
    revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
    top_revenue_industry = revenue_by_industry.idxmax()
    return top_revenue_industry

# Streamlit UI
st.title("FinSight NZ AI - Financial Dashboard")

uploaded_file = st.file_uploader("Upload your data.csv", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write("## Data Preview")
    st.dataframe(df.head())

    num_public_orgs = get_public_orgs(df)
    st.write(f"### Number of public organizations: {num_public_orgs}")

    rev_per_industry = revenue_per_industry(df)
    st.write("### Revenue per industry (average):")
    st.dataframe(rev_per_industry)

    highest_rev_industry = highest_revenue_industry(df)
    st.write(f"### Industry with the highest total revenue: {highest_rev_industry}")
else:
    st.info("Please upload a data.csv file to begin.")
