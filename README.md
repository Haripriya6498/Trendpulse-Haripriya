## TREND PULSE — WHATS ACTUALLY TRENDING RIGHT NOW ?

TrendPulse is a Python data analysis project that collects trending stories from the Hacker News API, cleans and analyzes the data, and creates visualizations to understand current trends.

## PROJECT OVERVIEW

The project is divided into four tasks:

Task 1 → Task 2 → Task 3 → Task 4

Fetch JSON → Clean CSV → Analyze Data → Visualize\

## PIPELINE

## TASK 1  — DATA COLLECTION
Fetches the top 500 story IDs from Hacker News.
Fetches individual story details.
Categorizes stories into five categories.
Saves the collected data as JSON.

## TASK 2 — DATA PROCESSING
Loads the JSON data using Pandas.
Removes duplicate and incomplete records.
Converts numeric columns to the correct data types.
Removes low-score stories.
Saves the cleaned data as CSV.

## TASK 3 — DATA ANALYSIS
Uses Pandas and NumPy to analyze the cleaned data.
Calculates statistical values such as mean, median, and standard deviation.
Finds the highest and lowest scores.
Finds the most common category.
Calculates story engagement.
Identifies popular stories.

## TASK 4 — VISUALIZATION
Creates three charts using Matplotlib.
Visualizes the top stories by score.
Shows the number of stories in each category.
Shows the relationship between scores and comments.
Creates a combined TrendPulse dashboard.
Categories

## STORIES ARE ASSIGNED TO CATEGORIES BASED ON KEYWORDS FOUND IN THEIR TITLES.

## CATEGORY	EXAMPLE KEYWORDS
Technology	AI, software, tech, code, computer, data, cloud, API, GPU, LLM
World News	war, government, country, president, election, climate, attack, global
Sports	NFL, NBA, FIFA, sport, game, team, player, league, championship
Science	research, study, space, physics, biology, discovery, NASA, genome
Entertainment	movie, film, music, Netflix, game, book, show, award, streaming

## TECHNOLOGIES USED
Python
Requests — for accessing the Hacker News API
Pandas — for data cleaning and analysis
NumPy — for statistical calculations
Matplotlib — for data visualization
JSON — for storing raw collected data
CSV — for storing cleaned and analyzed data
Git & GitHub — for version control and submission
