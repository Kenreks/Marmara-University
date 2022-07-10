/*
1- For this question, consider the season '13-14'.

a) Create a table 'number of goals forwarded' for the teams.

NumOfGoalsTeams(_TeamName_, NumOfGoals)

b) Implement stored procedure to initialize the table NumOfGoalsTeams table. It should calculate
Number of Goals Forwarded SO FAR for each team (IsOwnGoal=0) and insert it into NumOfGoalsTeams table along with the
team name.

sp_initializeNumOfGoalsTeams()

c) Implement a trigger so that, each insertion, deletion, update of a record in Goal table
should reflect on NumOfGoalsTeams table. For example, insertion of a new goal forwarded by BJK in the match BJK-FB,
should increase the GF for BJK by one. Please do not delete all NumberOfGoalsTeams records and recalculate them again.
So, you mustn't use the stored procedure you have created in part b.
Assume that there are thousands of teams, and we would like to change NumOfGoals record of only ONE TEAM.

trg_updateNumOfGoalsTeams()

To test your trigger use the following queries which are inserting 4 goals for Fenerbahce. So, NumOfGoals record of FB should increase by 4.

INSERT INTO Goals(MatchID,PlayerID,IsOwnGoal,Minute)
VALUES (50,54,0,1)

INSERT INTO Goals(MatchID,PlayerID,IsOwnGoal,Minute)
VALUES (50,54,0,2)

INSERT INTO Goals(MatchID,PlayerID,IsOwnGoal,Minute)
VALUES (50,54,0,3)

INSERT INTO Goals(MatchID,PlayerID,IsOwnGoal,Minute)
VALUES (50,54,0,4)
*/

/*
[MY FAVORITE]
2-Create a stored procedure which prints out name of the Goal Stars between particular dates.
A goal star is a player who forwarded maximum number of goals between particular dates.
There could be any goal stars between particular dates. You should print all of them.
You should only consider the matches played between the input dates when computing number of
goals scored for a player.

Make sure there is at least one goal scored between the dates @start and @end. Otherwise
return from the function without doing anything.
Also, dont forget to consider IsOwnGoal attribute.

sp_getGoalStars
@start smalldatetime,
@end smalldatetime

--WHERE match.DateOfMatch>=@start AND match.DateOfMatch<=@end

For this question, you may ignore season. Just consider date of the match.
*/

