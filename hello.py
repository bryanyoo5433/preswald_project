import preswald
from preswald import text, plotly, connect, get_df, table, slider, selectbox, button, sidebar
import pandas as pd
import plotly.express as px
import numpy as np
sidebar()
connect()
df = get_df('portfolio_csv')

df = df.astype({col: 'float64' for col in df.select_dtypes(include='floating').columns})


text("# 📊 Stock Portfolio Dashboard")
text("Created by Bryan Yoo")




# Slider to choose number of rows
num_rows = slider("Select number of rows to display", min_val=1, max_val=50, default=5)

# Optional: confirm current slider value
text(f"Current slider value: {num_rows}")

# Button to apply filter
if button("Show Rows"):
    filtered_df = df.head(num_rows)
    table(filtered_df, title=f"📄 Showing Top {num_rows} Rows")



text("## Filter by Column")
filter_col = selectbox("Filter by", options=["Ticker", "Sector", "Quantity", "Close", "Weight"])

filtered_df = df # Default to the original DataFrame

if button("Apply Filter"):
    # For categorical columns, show another selectbox
    if filter_col in ["Ticker", "Sector"]:
        text(f"### Filter by {filter_col}")
        filter_val = selectbox(f"Filter by {filter_col}", options=df[filter_col].dropna().unique().tolist())
        filtered_df = df[df[filter_col] == filter_val]
    else: # For numeric columns, show a slider
        min_val = float(df[filter_col].min())
        max_val = float(df[filter_col].max())
        threshold = slider(f"Minimum {filter_col}", min_val=min_val, max_val=max_val, default=min_val)
        filtered_df = df[df[filter_col] > threshold]

    # Display the filtered DataFrame
    table(filtered_df, title=f"Filtered by {filter_col}")


# Scatter plot
text("## Quantity vs. Close Price by Sector")
fig = px.scatter(df, x="Quantity", y="Close", size="Weight", color="Sector")
plotly(fig)

# Pie Chart
text("## Portfolio Weight by Stock")
fig = px.pie(df, names="Ticker", values="Weight")
plotly(fig)

# Bar Chart
text("## Portfolio Weight by Sector")
sector_weights = df.groupby("Sector")["Weight"].sum().reset_index()
fig = px.bar(sector_weights, x="Sector", y="Weight")
plotly(fig)

