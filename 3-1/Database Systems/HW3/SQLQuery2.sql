ALTER PROCEDURE sp_GetStandingsUpToDate @Date smalldatetime
AS
BEGIN
	SELECT ROW_NUMBER() OVER(ORDER BY name ASC) as pos, t.Name, Count(m.HomeTeamID) as GP
	FROM Team t, Match m
	Where  m.DateOfMatch BETWEEN '2013-08-16' and '2014-07-31' and m.DateOfMatch <= @Date and m.HomeTeamID=t.TeamID or m.VisitingTeamID=t.TeamID
	Group By t.Name
END