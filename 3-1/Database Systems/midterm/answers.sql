--Tum departmanlarin ismini ve bu departmanlarda bulunan toplam ogrenci sayisini
--yaziniz.
SELECT dpt.dName, count(*)
FROM STUDENT st INNER JOIN DEPARTMENT dpt ON st.deptCode=dpt.deptCode
GROUP BY st.deptCode, dpt.dName

--Ogrenci sayisi 20 dan fazla olan departmanlarin ismini yaziniz.
SELECT dpt.dName
FROM STUDENT st INNER JOIN DEPARTMENT dpt ON st.deptCode=dpt.deptCode
GROUP BY st.deptCode, dpt.dName
HAVING count(*)>20

--Evli olan tum managerlerin yaslarini toplamini yaziniz
SELECT sum(stff.age)
FROM MANAGER mng INNER JOIN STAFF stff ON stff.staffID=mng.staffID
WHERE stff.isMarried=1

--CSE deparmanindaki ogrencilerin ortalama gradeini yaziniz.
SELECT avg(1.0*ts.grade4)
FROM STUDENT st INNER JOIN TRANSCRIPT ts ON ts.studentID=st.studentID
WHERE st.deptCode='CSE'

--Her bir deparmandaki ogrencilerin ortlama gradini, departman ismiyle beraber yaziniz.
SELECT avg(1.0*ts.grade4)
FROM STUDENT st INNER JOIN TRANSCRIPT ts ON ts.studentID=st.studentID
GROUP BY st.deptCode

--Danismani evli olan tum ogrencilerin toplamda almis oldugu ders saysini,
--ogrencilerin isim-soyisim leriyle beraber yaziniz.
SELECT st.fName AS Name, st.lName AS Surname, count(*) AS NumberOfCoursesTaken
FROM ((STUDENT st INNER JOIN TRANSCRIPT ts ON ts.studentID=st.studentID)
INNER JOIN ADVISOR ad ON st.advisorID=ad.staffID) INNER JOIN STAFF stff ON
stff.staffID=ad.staffID
WHERE stff.isMarried=1
GROUP BY ts.studentID, st.fName, st.lName

--[MY FAVORITE]
--Bilgisayar muh departmanindaki tum ogrencilerin gpalarini hesaplayiniz.
--Ogrencilerin isimlerini gpa lariyla beraber yaziniz. Yazarken ogrencilerin soy
--isimlerini artan sirada yaziniz. Kiz ogrencileri, erkek ogrencilerden once yaziniz.
--GPA hesaplanirken ogrencinin almis oldugu her bir kurs icin credi*grade yapip toplam
--crediye bolmeniz gerekmektedir.
SELECT st.studentID, st.fName, st.lName, sum(ts.grade4*(cs.credits*1.0))/sum(cs.credits) AS GPA
FROM (STUDENT st INNER JOIN TRANSCRIPT ts ON st.studentID=ts.studentID) INNER JOIN
COURSE cs ON ts.cCode=ts.cCode
WHERE st.deptCode='CSE'
GROUP BY st.studentID, st.fName, st.lName, st.gender
ORDER BY st.gender, st.lName

--CSE departmaninda ogrencilerin bildigi dillerin isimlerini ve bu dilleri
--toplamda kac ogrencinin bildigini yaziniz.
SELECT fl.foreignLanguage, count(*)
FROM STUDENT st INNER JOIN STUDENT_FOREIGN_LANGUAGE fl ON st.studentID=fl.studentID
WHERE st.deptCode='CSE'
GROUP BY fl.foreignLanguage

--Her bir departmanda toplamda kac ogrencinin Fransizca bildigini, departman ismiyle
--beraber yaziniz.
SELECT dpt.dName, count(*)
FROM DEPARTMENT dpt LEFT OUTER JOIN 
(STUDENT st INNER JOIN STUDENT_FOREIGN_LANGUAGE fl ON st.studentID=fl.studentID)
 ON dpt.deptCode=st.deptCode
WHERE fl.foreignLanguage='FR'
GROUP BY st.deptCode, dpt.dName

--Her bir departmanda kac tane bekar advisor oldugunu, departman ismiyle beraber yaziniz.
SELECT dName, count(*)
FROM (ADVISOR ad INNER JOIN STAFF stff ON ad.staffID=stff.staffID) RIGHT OUTER JOIN
DEPARTMENT dpt ON dpt.deptCode=stff.deptCode
WHERE stff.isMarried=0
GROUP BY stff.deptCode, dpt.dName

--Her bir departmanda kac tane advisor oldugunu, departman isimleriyle beraber yaziniz.
SELECT dpt.dName, count(stff.staffID)
FROM DEPARTMENT dpt LEFT OUTER JOIN (ADVISOR ad INNER JOIN STAFF stff ON stff.staffID=ad.staffID)
ON dpt.deptCode=stff.deptCode
GROUP BY dpt.deptCode, dpt.dName

--Ankaradan gelen tum kiz ogrencilerin toplamda kactane yabanci dil bildigini,
--ogrencilerin isim-numaralariyla beraber yaziniz. Ogrencileri soy isimleriyle
--artan sirada sirayiniz.
SELECT st.studentID, st.fName, st.lName, count(fl.studentID)
FROM (STUDENT st LEFT OUTER JOIN STUDENT_FOREIGN_LANGUAGE fl ON st.studentID=fl.studentID)
WHERE st.gender='F' AND st.city='Ankara'
GROUP BY fl.studentID, st.fName, st.lName, st.studentID
ORDER BY st.lName ASC

--Her bir deparmanda toplam kiz ogrencilerin sayisini toplam ogrencilerin
--sayisina oranini, departman idleriyle beraber yaziniz.
SELECT girls.deptCode, (girls.numOfGirls*1.0)/(boys.numOfBoys*1.0+girls.numOfGirls*1.0)
FROM
(SELECT dpt.deptCode,count(st.studentID) AS numOfGirls
FROM DEPARTMENT dpt LEFT OUTER JOIN STUDENT st ON dpt.deptCode=st.deptCode
WHERE st.gender='F'
GROUP BY dpt.deptCode) girls
INNER JOIN 
(SELECT dpt.deptCode,count(st.studentID) AS numOfBoys
FROM DEPARTMENT dpt LEFT OUTER JOIN STUDENT st ON dpt.deptCode=st.deptCode
WHERE st.gender='M'
GROUP BY dpt.deptCode) boys
ON girls.deptCode=boys.deptCode

--Yasi 40 tan fazla en az dort calisani bulunan derpartmanlari isimleriyle beraber yaziniz.
SELECT dpt.dName
FROM STAFF stff RIGHT OUTER JOIN DEPARTMENT dpt ON dpt.deptCode=stff.deptCode
WHERE stff.age>40
GROUP BY dpt.deptCode, dpt.dName
HAVING count(stff.staffID)>=4

--Bilgisayar muh departmanindaki tum ogrencilerin isimlerini ve toplamda almis oldugu
--ders kredilerini yaziniz. Ogrencileri, soy isimleri azalicak sirada yaziniz. Ayrica
--kiz ogrencileri erkek ogrencilerden once yaziniz.
SELECT st.fName + ' ' + st.lName AS StudentFullName, sum(cs.credits)
FROM ((STUDENT st INNER JOIN DEPARTMENT dpt ON st.deptCode=dpt.deptCode) INNER JOIN
TRANSCRIPT ts ON st.studentID=ts.studentID) INNER JOIN COURSE cs ON cs.cCode=ts.cCode
WHERE dpt.dName='Computer Engineering'
GROUP BY st.studentID, st.fName, st.lName, st.gender
ORDER BY st.gender, st.lName

--Universitedeki tum ogrencilerin GPAsini, student IDleriyle beraber yaziniz.
SELECT st.studentID, sum(ts.grade4*(cs.credits*1.0))/sum(cs.credits) AS GPA
FROM (STUDENT st INNER JOIN TRANSCRIPT ts ON st.studentID=ts.studentID) INNER JOIN
COURSE cs ON cs.cCode=ts.cCode
GROUP BY st.studentID

--Her bir departman icin tum ogrencilerin ortalama GPAsini, departmanin ismiyle
--beraber yaziniz. (departmandaki ogrencilerin ortalama basarisi)
SELECT dpt.dName, avg(studentGPAs.GPA*1.0) AS AverageGPA
FROM
	(SELECT st.studentID, st.deptCode, sum(ts.grade4*(cs.credits*1.0))/sum(cs.credits) AS GPA
	FROM (STUDENT st INNER JOIN TRANSCRIPT ts ON st.studentID=ts.studentID) INNER JOIN
	COURSE cs ON cs.cCode=ts.cCode
	GROUP BY st.studentID, st.deptCode) studentGPAs
	INNER JOIN
	DEPARTMENT dpt
	ON dpt.deptCode=studentGPAs.deptCode
GROUP BY dpt.deptCode, dpt.dName

--Her bir departman icin toplamda Ingilizce(EN) bilmeyen kac ogrenci oldugunu 
--departman isimiyle beraber yaziniz.
SELECT dpt.dName, count(st.studentID) AS StudentsDontKnowEnglish
FROM STUDENT st INNER JOIN DEPARTMENT dpt ON st.deptCode=dpt.deptCode
WHERE st.studentID NOT IN
	(SELECT st.studentID
	FROM STUDENT st INNER JOIN STUDENT_FOREIGN_LANGUAGE fl ON st.studentID=fl.studentID
	WHERE fl.foreignLanguage='EN')
GROUP BY dpt.deptCode, dpt.dName
