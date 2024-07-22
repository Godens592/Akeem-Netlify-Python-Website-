import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('Monkeypox_Research_Summary_Data_20240721.csv')

# Data preprocessing
df['Topic'] = df['Topic'].fillna('Not Specified')
df['Anticipated Completion'] = pd.to_datetime(df['Anticipated Completion'], errors='coerce')

# Page 1: Introduction (3 graphs)

# 1. Top 5 Research Categories (Horizontal Bar Chart)
plt.figure(figsize=(10, 6))
topic_counts = df['Topic'].value_counts().head(5)
sns.barplot(y=topic_counts.index, x=topic_counts.values)
plt.title('Top 5 Monkeypox Research Categories')
plt.xlabel('Number of Projects')
plt.tight_layout()
plt.savefig('research_categories.png')
plt.close()

# 2. Timeline of Research Initiatives (Line Graph)
year_counts = df['Anticipated Completion'].dt.year.value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(year_counts.index, year_counts.values, marker='o')
plt.title('Timeline of Monkeypox Research Initiatives')
plt.xlabel('Year')
plt.ylabel('Number of Projects')
plt.xticks(year_counts.index)
plt.savefig('research_timeline.png')
plt.close()

# 3. Project Duration Distribution (Histogram)
df['Project Duration'] = (df['Anticipated Completion'] - pd.to_datetime('today')).dt.days / 365.25
plt.figure(figsize=(10, 6))
sns.histplot(df['Project Duration'].dropna(), bins=20, kde=True)
plt.title('Distribution of Project Durations')
plt.xlabel('Project Duration (Years)')
plt.ylabel('Number of Projects')
plt.savefig('project_duration_distribution.png')
plt.close()

# Page 2: Analysis (3 graphs)

# 4. Top 10 Countries Involved in Research (Horizontal Bar Chart)
countries = df['Country(ies) in which research is/will be conducted'].str.split(',').explode()
country_counts = countries.value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(y=country_counts.index, x=country_counts.values)
plt.title('Top 10 Countries Involved in Monkeypox Research')
plt.xlabel('Number of Projects')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('research_geography.png')
plt.close()

# 5. Top 5 Agencies Involved (Horizontal Bar Chart)
agency_counts = df['Agency and Office Name'].value_counts().head(5)
plt.figure(figsize=(10, 6))
sns.barplot(y=agency_counts.index, x=agency_counts.values)
plt.title('Top 5 Agencies Involved in Monkeypox Research')
plt.xlabel('Number of Projects')
plt.tight_layout()
plt.savefig('agency_involvement.png')
plt.close()

# 6. Research Focus Areas (Horizontal Bar Chart)
focus_areas = df['Topic'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(y=focus_areas.index, x=focus_areas.values)
plt.title('Top 10 Research Focus Areas')
plt.xlabel('Number of Projects')
plt.ylabel('Research Topic')
plt.tight_layout()
plt.savefig('research_focus_areas.png')
plt.close()

# Page 3: Conclusion (3 graphs)

# 7. Domestic vs International Research (Pie Chart)
def categorize_location(location):
    if pd.isna(location) or location == 'Domestic':
        return 'Domestic'
    elif 'Domestic' in location and 'International' in location:
        return 'Both'
    else:
        return 'International'

df['Research Location'] = df['Country(ies) in which research is/will be conducted'].apply(categorize_location)
location_counts = df['Research Location'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(location_counts.values, labels=location_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Domestic vs International Research')
plt.axis('equal')
plt.savefig('research_location_distribution.png')
plt.close()

# 8. Completion Timeline (Area Chart)
year_completion_counts = df['Anticipated Completion'].dt.year.value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.fill_between(year_completion_counts.index, year_completion_counts.values)
plt.title('Anticipated Completion Timeline of Research Projects')
plt.xlabel('Year')
plt.ylabel('Number of Projects')
plt.savefig('completion_timeline.png')
plt.close()

# 9. Project Milestones (Grouped Bar Chart)
df['Milestone Year'] = pd.to_datetime(df['Upcoming Milestones'].str.extract('(\d{4})')[0], errors='coerce').dt.year
milestone_counts = df['Milestone Year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.barplot(x=milestone_counts.index, y=milestone_counts.values)
plt.title('Project Milestones Distribution')
plt.xlabel('Year')
plt.ylabel('Number of Milestones')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('project_milestones.png')
plt.close()

print("All visualizations have been generated and saved.")