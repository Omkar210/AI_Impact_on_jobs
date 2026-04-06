create table jobs1 (
    Job_Title VARCHAR(255),
    Average_Salary DECIMAL(10, 2),
    Years_Experience int,
    Education_Level VARCHAR(100),
    AI_Exposure_Index DECIMAL(5, 2),
    Tech_Growth_Factor DECIMAL(5, 2),
    Automation_Probablity_2030 DECIMAL(5, 2),
    Risk_Category ENUM('Low', 'Medium', 'High')
);

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/newAI_Impact_on_Jobs_2030.csv"
INTO TABLE jobs1
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

select * from jobs1;