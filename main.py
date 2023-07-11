import pandas as pd
import project_info_sheet
import employee_sheets
import summary_sheet_read
import employee_billing_matrix_generation
import timesheet_output

df = pd.read_excel(
    r"C:\Users\samar\Desktop\Timesheet_sample_input.xlsx",
    sheet_name=None,
)
del df["Summary"]

df_summary = pd.read_excel(
    r"C:\Users\samar\Desktop\Timesheet_sample_input.xlsx",
    sheet_name="Summary",
)

print("inserting the details of employee working on the project")
project_info_sheet.insert_employee(df_summary)

print("List of employees working on project")  # calling function without sheet name
# employee_sheets.display_employees(df)
employee_sheets.rename_employee_sheet_column(df)

print("inserting details into the tasks table")
employee_sheets.inserting_tasks(df)

print("moving project details to database")
project_info_sheet.insert_projectdetails(df_summary)

print("inserting details into timesheet")
summary_sheet_read.insert_timesheetgeneration(df_summary)


timesheet_output.create_timesheetOutput()
employee_billing_matrix_generation.insert_billingAmount(df_summary)
employee_billing_matrix_generation.cal_workingDays(df, df_summary)
