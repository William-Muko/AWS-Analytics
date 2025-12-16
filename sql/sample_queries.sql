-- Current standings
SELECT team_name, matches_played, wins, draws, losses, points, goal_difference
FROM standings
ORDER BY points DESC, goal_difference DESC;

-- Top 5 teams
SELECT team_name, points, wins, goal_difference
FROM standings
ORDER BY points DESC
LIMIT 5;

-- Win percentage
SELECT team_name, wins, matches_played, 
       ROUND(CAST(wins AS DOUBLE) / matches_played * 100, 2) as win_percentage
FROM standings
ORDER BY win_percentage DESC;

-- Teams with positive goal difference
SELECT team_name, goals_for, goals_against, goal_difference, points
FROM standings
WHERE goal_difference > 0
ORDER BY goal_difference DESC;
