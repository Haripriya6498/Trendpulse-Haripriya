TrendPulse — What's Actually Trending Right Now

TrendPulse is a Python data analysis project that collects trending stories from the Hacker News API, cleans and analyzes the data, and creates visualizations to understand current trends.

## Project Overview

The project is divided into four tasks:

Task 1 → Task 2 → Task 3 → Task 4

Fetch JSON → Clean CSV → Analyze Data → Visualize\

Pipeline
Task 1 — Data Collection
Fetches the top 500 story IDs from Hacker News.
Fetches individual story details.
Categorizes stories into five categories.
Saves the collected data as JSON.
Task 2 — Data Processing
Loads the JSON data using Pandas.
Removes duplicate and incomplete records.
Converts numeric columns to the correct data types.
Removes low-score stories.
Saves the cleaned data as CSV.
Task 3 — Data Analysis
Uses Pandas and NumPy to analyze the cleaned data.
Calculates statistical values such as mean, median, and standard deviation.
Finds the highest and lowest scores.
Finds the most common category.
Calculates story engagement.
Identifies popular stories.
Task 4 — Visualization
Creates three charts using Matplotlib.
Visualizes the top stories by score.
Shows the number of stories in each category.
Shows the relationship between scores and comments.
Creates a combined TrendPulse dashboard.
Categories

Stories are assigned to categories based on keywords found in their titles.

Category	Example Keywords
Technology	AI, software, tech, code, computer, data, cloud, API, GPU, LLM
World News	war, government, country, president, election, climate, attack, global
Sports	NFL, NBA, FIFA, sport, game, team, player, league, championship
Science	research, study, space, physics, biology, discovery, NASA, genome
Entertainment	movie, film, music, Netflix, game, book, show, award, streaming
Technologies Used
Python
Requests — for accessing the Hacker News API
Pandas — for data cleaning and analysis
NumPy — for statistical calculations
Matplotlib — for data visualization
JSON — for storing raw collected data
CSV — for storing cleaned and analyzed data
Git & GitHub — for version control and submission
