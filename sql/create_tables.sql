CREATE EXTERNAL TABLE IF NOT EXISTS standings (
    team_name STRING,
    matches_played INT,
    wins INT,
    draws INT,
    losses INT,
    goals_for INT,
    goals_against INT,
    goal_difference INT,
    points INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://awscookbook704-$RANDOM_STRING/raw-data/'
TBLPROPERTIES ('skip.header.line.count'='1');
