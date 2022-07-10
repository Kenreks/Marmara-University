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

CREATE TABLE NumOfGoalsTeams (
    TeamName nvarchar(50) PRIMARY KEY,
    NumOfGoals smallint
)



CREATE PROCEDURE sp_initializeNumOfGoalsTeams
AS
BEGIN
    DELETE FROM NumOfGoalsTeams
    --Delete if any records exist

    INSERT INTO NumOfGoalsTeams(TeamName, NumOfGoals)
    SELECT t.Name, SUM(CASE WHEN g.IsOwnGoal=1 THEN 0 ELSE 1 END) AS GF
    FROM (Team t LEFT OUTER JOIN PlayerTeam pt ON t.TeamID=pt.TeamID INNER JOIN Player p ON p.PlayerID=pt.PlayerID)
    INNER JOIN
    Goals g ON g.PlayerID=p.PlayerID
    WHERE pt.Season='13-14'
    GROUP BY t.TeamID, t.Name
END




ALTER TRIGGER trg_updateNumOfGoalsTeams
ON Goals
AFTER INSERT,DELETE,UPDATE 
AS
BEGIN
    UPDATE n
    SET n.NumOfGoals=n.NumOfGoals+1
    FROM (NumOfGoalsTeams n INNER JOIN (Team t LEFT OUTER JOIN PlayerTeam pt ON t.TeamID=pt.TeamID INNER JOIN Player p ON p.PlayerID=pt.PlayerID) ON n.TeamName=t.Name)
         INNER JOIN Inserted g ON g.PlayerID=p.PlayerID
    WHERE pt.Season='13-14' AND g.IsOwnGoal=0

    UPDATE n
    SET n.NumOfGoals=n.NumOfGoals-1
    FROM (NumOfGoalsTeams n INNER JOIN (Team t LEFT OUTER JOIN PlayerTeam pt ON t.TeamID=pt.TeamID INNER JOIN Player p ON p.PlayerID=pt.PlayerID) ON n.TeamName=t.Name)
         INNER JOIN Deleted g ON g.PlayerID=p.PlayerID
    WHERE pt.Season='13-14' AND g.IsOwnGoal=0
END


/*
[MY FAVORITE]
Create a stored procedure which prints out name of the Goal Stars between particular dates.
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


CREATE PROCEDURE sp_getGoalStars
@start smalldatetime,
@end smalldatetime
AS
BEGIN
    IF(EXISTS(
        SELECT *
        FROM Goals g INNER JOIN Match m ON g.MatchID=m.MatchID
        WHERE g.IsOwnGoal=0 AND (m.DateOfMatch>=@start AND m.DateOfMatch<=@end)
    ))
    BEGIN
        DECLARE @maxGoals smallint
        SET @maxGoals =     (SELECT MAX(PlayerGoals.NumOfGoals)
                            FROM
                                (SELECT p.FirstName + ' ' + p.LastName AS PlayerName, COUNT(*) AS NumOfGoals
                                FROM (Player p INNER JOIN Goals g ON p.PlayerID=g.PlayerID) INNER JOIN Match m ON m.MatchID=g.MatchID
                                WHERE g.IsOwnGoal=0 AND (m.DateOfMatch>=@start AND m.DateOfMatch<=@end)
                                GROUP BY p.PlayerID, p.FirstName, p.LastName) PlayerGoals
                            )

        SELECT p.FirstName + ' ' + p.LastName AS PlayerName, COUNT(*) AS NumOfGoals
        FROM (Player p INNER JOIN Goals g ON p.PlayerID=g.PlayerID) INNER JOIN Match m ON m.MatchID=g.MatchID
        WHERE g.IsOwnGoal=0 AND (m.DateOfMatch>=@start AND m.DateOfMatch<=@end)
        GROUP BY p.PlayerID, p.FirstName, p.LastName
        HAVING COUNT(*)=@maxGoals
    END
END
