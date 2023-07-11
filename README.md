# Timesheet-generation-and-storage-in-database
this web app takes a sample input excel file which is used to store project timesheet details in a company like per day billing, total billing rate, company holidays, adjustments, list of employees working on the project and their everyday tasks.
the sql commands to create tables is given in the txt file. mysql database has relevant tables that would record information from timesheet_sample_input and store it into the database. the sql commands maybe missing with fields like auto increment of primary key, so add them where you feel it is necessary.
whenever the excel file is updated the data is stored into the database and this data is not redundant. our web app generated a new excel doc which calculated billing amount of employees based on their no. of working days after considering the company holidays and the adjustment.
TO RUN THE APP TYPE streamlit run streamlitApp.py in the command line.
