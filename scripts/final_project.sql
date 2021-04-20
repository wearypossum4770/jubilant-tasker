CREATE TABLE IF NOT EXISTS patient(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	full_name VARCHAR(100), 
	mobile_number VARCHAR(13), 
	primary_email VARCHAR(100)
); CREATE TABLE IF NOT EXISTS employee(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	first_name VARCHAR(50), 
	last_name VARCHAR(50)
); CREATE TABLE IF NOT EXISTS services(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	service_description VARCHAR(100), 
	-- 'hh:mm:ss'  or 'hhh:mm:ss'
	duration TIME, 
	price Decimal(12, 2)
); CREATE TABLE IF NOT EXISTS appointment(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	employee_id INT, 
	patient_id INT, 
	-- 'hh:mm:ss'  or 'hhh:mm:ss'
	start_time TIME, 
	-- 'hh:mm:ss'  or 'hhh:mm:ss'
	end_time TIME, 
	-- 'hh:mm:ss'  or 'hhh:mm:ss'
	expected_start_time TIME, 
	-- 'hh:mm:ss'  or 'hhh:mm:ss'
	expected_end_time TIME, 
	discount Decimal(12, 2), 
	price Decimal(12, 2), 
	is_cancelled BOOLEAN, 
	cancellation_reason TEXT, 
	FOREIGN KEY (employee_id) REFERENCES employee(id) ON DELETE CASCADE, 
	FOREIGN KEY (patient_id) REFERENCES patient(id) ON DELETE CASCADE
); CREATE TABLE IF NOT EXISTS schedule(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	-- 'hh:mm:ss'  or 'hhh:mm:ss'
	start_time TIME, 
	-- 'hh:mm:ss'  or 'hhh:mm:ss'
	end_time TIME, 
	employee_id INT, 
	FOREIGN KEY (employee_id) REFERENCES employee(id) ON DELETE CASCADE
); CREATE TABLE IF NOT EXISTS services_provided (
	id INT PRIMARY KEY AUTO_INCREMENT, 
	service_id INT, 
	appointment_id INT, 
	price Decimal(12, 2), 
	FOREIGN KEY (appointment_id) REFERENCES appointment(id) ON DELETE CASCADE, 
	FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
); CREATE TABLE IF NOT EXISTS services_booked(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	service_id INT, 
	price Decimal(12, 2), 
	FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
); 
SELECT 
	" CHECKING THE TABLE appointment "; 
SELECT 
	* 
FROM 
	appointment; 
SELECT 
	"THE TABLE DOES EXISTS, YOU CAN NOW FILL IT UP."; 
SELECT 
	" CHECKING THE TABLE services "; 
SELECT 
	* 
FROM 
	services; 
SELECT 
	"THE TABLE DOES EXISTS, YOU CAN NOW FILL IT UP."; 
SELECT 
	" CHECKING THE TABLE patient "; 
SELECT 
	* 
FROM 
	patient; 
SELECT 
	"THE TABLE DOES EXISTS, YOU CAN NOW FILL IT UP."; 
SELECT 
	" CHECKING THE TABLE employee "; 
SELECT 
	* 
FROM 
	employee; 
SELECT 
	"THE TABLE DOES EXISTS, YOU CAN NOW FILL IT UP."; 
SELECT 
	" CHECKING THE TABLE schedule "; 
SELECT 
	* 
FROM 
	schedule; 
SELECT 
	"THE TABLE DOES EXISTS, YOU CAN NOW FILL IT UP."; 
SELECT 
	" CHECKING THE TABLE services_provided "; 
SELECT 
	* 
FROM 
	services_provided; 
SELECT 
	"THE TABLE DOES EXISTS, YOU CAN NOW FILL IT UP."; 
SELECT 
	" CHECKING THE TABLE services_booked"; 
SELECT 
	* 
FROM 
	services_booked; 
SELECT 
	"THE TABLE DOES EXISTS, YOU CAN NOW FILL IT UP."; -- 
SELECT 
	employee.id AS employee_id, 
	employee.first_name, 
	employee.last_name, 
	patient.id AS patient_id, 
	patient.full_name 
FROM 
	employee, 
	patient; 
SELECT 
	employee.id as employee_id, 
	patient.id as patient_id, 
	COUNT(appointment.id) as "Total Appointments" 
FROM 
	employee 
	INNER JOIN appointment ON appointment.employee_id = employee.id 
	INNER JOIN patient on appointment.patient_id = patient.id 
GROUP BY 
	employee.id, 
	patient.id;