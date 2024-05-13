import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("scraped.csv")

# Encode the 'Category' column
label_encoder = LabelEncoder()
data['Category_encoded'] = label_encoder.fit_transform(data['Category'])

# KMeans clustering
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data[['Category_encoded']])
cluster_assignments = kmeans.labels_
data['cluster'] = cluster_assignments

# Sidebar
st.sidebar.title("Cluster Selection")
selected_cluster = st.sidebar.selectbox("Select Cluster", sorted(data['cluster'].unique()))

# Display records for selected cluster
st.write(f"Records for Cluster {selected_cluster}:")
cluster_data = data[data['cluster'] == selected_cluster]
# Concatenate category and URL columns

st.write(cluster_data[['Category','URL', 'Headline', 'Summary']])
