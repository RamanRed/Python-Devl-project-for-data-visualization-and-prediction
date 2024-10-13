bivariate_analysis = {
    ('score', 'votes'): 'Scatter plot to analyze how the number of votes correlates with the movie score. Investigate whether highly-rated movies receive more votes.',
    ('budget', 'gross'): 'Scatter plot or correlation analysis to check if movies with higher budgets tend to generate higher gross earnings.',
    ('genre', 'score'): 'Box plot to observe the distribution of movie scores across different genres. This helps to see which genres generally receive higher ratings.',
    ('rating', 'gross'): 'Box plot to evaluate the gross earnings based on movie ratings (e.g., R, PG). It helps in understanding whether movie ratings affect box office performance.',
    ('director', 'score'): 'Bar plot or average score comparison to analyze whether certain directors consistently produce higher-rated movies.',
    ('country', 'gross'): 'Bar plot to explore the gross earnings distribution across different countries. This can reveal which countries have higher box office performance.',
    ('runtime', 'score'): 'Scatter plot to analyze the relationship between the runtime of a movie and its score. It helps determine whether longer movies tend to be rated higher or lower.'
}
bivariate_pairs = [
    ('score', 'votes'),
    ('budget', 'gross'),
    ('genre', 'score'),
    ('rating', 'gross'),
    ('director', 'score'),
    ('country', 'gross'),
    ('runtime', 'score')
]
