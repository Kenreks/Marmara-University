--STORED PROCEDURES PART

--CREATE NEW ROOM RESERVATION
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_CreateNewReservation]    Script Date: 23.12.2021 18:20:52 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Procedure [dbo].[sp_CreateNewReservation]
	@InputCustomerSsn int,
	@InputStaffSsn int,
	@InputRoomID int,
	@InputMealID int,
	@InputCheckIn smalldatetime,
	@InputCheckOut smalldatetime
	as
	begin
		
		Declare @chosenMealPrice int 
		Set @chosenMealPrice= (Select m.MealPrice From Meal m Where @InputMealID=m.MealID)

		Declare @chosenRoomPrice int 
		Set @chosenRoomPrice= (Select r.Price From Room r Where @InputRoomID=r.RoomID)

		Declare @day int 
		Set @day=  (datediff(day,@InputCheckIn,@InputCheckOut))
		
		Declare @totalPrice int
		Set @totalPrice= (@chosenMealPrice+@chosenRoomPrice)*@day

		Declare @customerBudget int
		Set @customerBudget= (Select c.Budget From Customer c Where c.Ssn=@InputCustomerSsn)

		Declare @roomAvailability bit
		Set @roomAvailability=(Select r.Availibilty From Room r Where r.RoomID=@InputRoomID)

		IF(@customerBudget>@totalPrice)
		Begin
			IF(@roomAvailability=1)
			Begin
				Insert into Reservation(CustomerSsn,StaffSsn,RoomID,MealID,CheckIn,CheckOut,ReservationPrice)
				Values(@InputCustomerSsn,@InputStaffSsn,@InputRoomID,@InputMealID,@InputCheckIn,@InputCheckOut,@totalPrice)
			End
		End

	end

-- CREATE ROOM
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_CreateRoom]    Script Date: 23.12.2021 18:22:35 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Procedure [dbo].[sp_CreateRoom]
	@Capacity int,
	@Location nchar(25),
	@Price int,
	@RoomType nchar(25)

	as
	begin
		Insert into Room(Capacity,Location,Price,RoomType)
		values(@Capacity,@Location,@Price,@RoomType)
	end
	
--DELETE CUSTOMER
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_DeleteCustomer]    Script Date: 23.12.2021 18:24:36 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[sp_DeleteCustomer]
	@CustomerSsn int

AS
BEGIN
	DELETE FROM Reservation
	WHERE @CustomerSsn=CustomerSsn

	DELETE FROM Customer
	WHERE @CustomerSsn=Customer.Ssn
END

--DELETE ROOM
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_DeleteRoom]    Script Date: 23.12.2021 18:25:00 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER procedure [dbo].[sp_DeleteRoom]
	@roomID int


	as 
	begin
		declare @availability bit
		set @availability= (Select Room.Availibilty From Room where Room.RoomID=@roomID)
		If(@availability='1')
		begin
			DELETE FROM Room
			WHERE @roomID=RoomID
		end
	end

--DELETE STAFF
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_DeleteStaff]    Script Date: 23.12.2021 18:25:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[sp_DeleteStaff]
	@StaffSsn int

AS
BEGIN
	
	DECLARE @ManagerSsn int
	SET @ManagerSsn=(SELECT SuperSsn FROM Staff WHERE Ssn=@StaffSsn)

	DECLARE @DepartmentID int
	SET @DepartmentID=(SELECT DepartmentId FROM Staff WHERE Ssn=@StaffSsn)

	
	
	IF(@ManagerSsn IS NULL)
	BEGIN
		Update Department
		SET ManagerSsn=(SELECT TOP 1 Ssn FROM Staff WHERE DepartmentId=@DepartmentID and Ssn != @StaffSsn)
		Where @DepartmentID=DepartmentNum
		
		

		Update Staff
		SET SuperSsn=(SELECT ManagerSsn FROM Department WHERE DepartmentNum=@DepartmentID)
		Where Staff.DepartmentId=@DepartmentID


		Update Staff
		SET SuperSsn=null WHERE Ssn=(SELECT ManagerSsn FROM Department WHERE DepartmentNum=@DepartmentID) or Ssn=@StaffSsn

		
	END
	Delete From StaffDependent
	Where StaffDependent.Ssn=@StaffSsn



	DELETE FROM Staff
	WHERE @StaffSsn=Ssn

END

--INSERT NEW CUSTOMER
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_InsertNewCustomer]    Script Date: 23.12.2021 18:26:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Procedure [dbo].[sp_InsertNewCustomer]
    @CustomerSsn int,
    @Name nvarchar(15),
    @Surname nvarchar(15),
    @PhoneNum bigint,
    @Mail nvarchar(25),
    @Gender char(1),
	@BirthDate smalldatetime,
	@Address nvarchar(50),
	@Nationality nchar(15),
	@Budget int
	

    as
    begin
          Insert into Customer(Ssn,Name,Surname,PhoneNum,Mail,Gender,BÝrthDate,Address,Nationality ,Budget)
          Values(@CustomerSsn, @Name,@Surname,@PhoneNum,@Mail,@Gender,@BirthDate,@Address,@Nationality,@Budget)
        
    end

--INSERT STAFF
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_InsertStaff]    Script Date: 23.12.2021 18:26:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[sp_InsertStaff]
	@Ssn int,
	@Name nvarchar(15),
	@Surname nvarchar(15),
	@Gender char(1),
	@BirthDate smalldatetime,
	@Adress nvarchar(50),
	@Salary int,
	@DepartmentId int

AS
BEGIN
	
	DECLARE @StartedDate smalldatetime
	SET @StartedDate=GETDATE()

	DECLARE @SuperSsn int
	SET @SuperSsn=(SELECT ManagerSsn FROM Department WHERE @DepartmentId=DepartmentNum)
	
	INSERT INTO Staff(Ssn, Name, Surname, Gender, BirthDate, SuperSsn, Address, Salary, DepartmentId, StartedDate)
	Values (@Ssn, @Name, @Surname, @Gender, @BirthDate, @SuperSsn, @Adress, @Salary, @DepartmentId, @StartedDate)

END

--UPDATE CUSTOMER
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_UpdateCustomer]    Script Date: 23.12.2021 18:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[sp_UpdateCustomer]
	@CustomerSsn int,
	@Amount int

AS
BEGIN
	Update Customer 
	Set Customer.Budget=Customer.Budget + @Amount
	Where Customer.Ssn=@CustomerSsn
END

--UPDATE ROOM AVAILABILITY
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_UpdateRoomAvailability]    Script Date: 23.12.2021 18:27:39 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Procedure [dbo].[sp_UpdateRoomAvailability]
	@RoomID int

	as
	begin

		Update Room
		Set Room.Availibilty='1'
		Where Room.RoomID=@RoomID
	
	end

--UPDATE STAFF
USE [HotelDataBase]
GO
/****** Object:  StoredProcedure [dbo].[sp_UpdateStaff]    Script Date: 23.12.2021 18:32:54 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[sp_UpdateStaff]
	@Ssn int,
	@Value int


AS
BEGIN

	
	Declare @bonus int
	Set @bonus=  datediff(year,(Select StartedDate  From  Staff Where Staff.Ssn=@Ssn),getdate()) * 50

	Update Staff
	Set Staff.Salary= Staff.Salary+ @Value+ @bonus
	Where Staff.Ssn=@Ssn


END


--TRIGGERS PART

--CHANGE AVAILABILITY
USE [HotelDataBase]
GO
/****** Object:  Trigger [dbo].[changeAvailability]    Script Date: 23.12.2021 18:33:52 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[changeAvailability]
	ON [dbo].[Reservation]
	AFTER DELETE
AS
BEGIN
	Declare @InputRoomID int
	Set @InputRoomID=(Select RoomID From deleted)

	Declare @checkIn smalldatetime
	Set @checkIn=(Select CheckIn FROM deleted)

	Declare @checkOut smalldatetime
	Set @checkOut=(Select CheckOut FROM deleted)

	Declare @now smalldatetime
	
	IF(@now BETWEEN @checkIn and @checkOut)
	BEGIN
		Update Room
		Set Room.Availibilty='1'
		Where Room.RoomID=@InputRoomID
	END
END

--TRG UPDATE BUDGET
USE [HotelDataBase]
GO
/****** Object:  Trigger [dbo].[trg_UpdateBudget]    Script Date: 23.12.2021 18:35:02 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Trigger [dbo].[trg_UpdateBudget]
    on [dbo].[Reservation]
    after insert

As 
Begin
 Declare @InputCustomerSsn int
 Set @InputCustomerSsn= (Select CustomerSsn From inserted)

 Declare @InputTotalPrice int
 Set @InputTotalPrice =(Select ReservationPrice From inserted)

 Update Customer 
 Set Customer.Budget=Customer.Budget- @InputTotalPrice
 Where Customer.Ssn=@InputCustomerSsn
 
 Declare @InputRoomID int
 Set @InputRoomID=(Select RoomID From inserted)

 Update Room
 Set Room.Availibilty='0'
 Where Room.RoomID=@InputRoomID


End

--TRG UPDATE NUMBER OF ROOMS

USE [HotelDataBase]
GO
/****** Object:  Trigger [dbo].[trg_Update_NumOfRoom]    Script Date: 23.12.2021 18:35:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Trigger [dbo].[trg_Update_NumOfRoom]
	on [dbo].[Room]
	after insert 

	as
	Begin
		Declare @CompanyId int
		Set @CompanyId= (Select CompanyId From inserted)

		Update Company
		Set NumOfRoom=NumOfRoom+1
		where @CompanyId=Company.ID
	end

--UPDATE ON DELETE NUMBER OF ROOMS

USE [HotelDataBase]
GO
/****** Object:  Trigger [dbo].[trg_UpdateOnDelete_NumOfRoom]    Script Date: 23.12.2021 18:36:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Trigger [dbo].[trg_UpdateOnDelete_NumOfRoom]
	on [dbo].[Room]
	after delete 

	as
	Begin
		Declare @CompanyId int
		Set @CompanyId= (Select CompanyId From inserted)

		Update Company
		Set NumOfRoom=NumOfRoom-1
		where @CompanyId=Company.ID
	end

--VIEWS

--CUSTOMER MAN GREATER THAN 25
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Ssn]
      ,[FullName]
      ,[Age]
      ,[PhoneNum]
      ,[Mail]
      ,[Gender]
      ,[Address]
      ,[Nationality]
      ,[Budget]
      ,[Capacity]
      ,[ReservationPrice]
      ,[RoomID]
  FROM [HotelDataBase].[dbo].[Customer_Man_Greater_Than_25]

 --GENERAL COMPANY INFORMATION
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Name]
      ,[TotalRevenue]
      ,[TotalExpenditure]
      ,[NumOfStaff]
      ,[NumOfRoom]
  FROM [HotelDataBase].[dbo].[General_Company_Information]

--MANAGER WITH SUBWORKER
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [DeparmentName]
      ,[NumStaff]
      ,[Name]
      ,[Surname]
      ,[Salary]
  FROM [HotelDataBase].[dbo].[Manager_With_Subworker]

--MEAL PREFERANCE CUSTOMER
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [MealType]
      ,[NumberOfCustomer]
      ,[TotalRevenue]
  FROM [HotelDataBase].[dbo].[Meal_Preference_Customer]

--STAFF DEPENDENT MORE THAN1
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [NumOfDependent]
      ,[FullName]
      ,[DependentName]
  FROM [HotelDataBase].[dbo].[Staff_Dependent_MoreThan1]