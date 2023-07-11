import pymysql
import pandas as pd

con = pymysql.connect(
    host="localhost", user="root", password="root", database="ttn", charset="utf8"
)


def create_connection(con):
    cur = con.cursor()
    return cur


def get_projectid(df_summary):
    cur = create_connection(con)
    project_name = df_summary.iat[0, 1]
    sql = "select id from project_details where project ='%s'" % (project_name,)
    cur.execute(sql)
    data = cur.fetchall()
    x = data[0][0]
    return x


# insert timesheet config info
def check_timesheetGeneration():
    cur = create_connection(con)
    sql = "select generation_date from timesheet_generation"
    cur.execute(sql)
    data = cur.fetchall()
    y = list()
    data1 = list(data)
    print(len(data1))
    for i in range(len(data1)):
        x = data1[i][0]
        y.append(x)
    return y


def insert_timesheetgeneration(df_summary):
    cur = create_connection(con)
    billing_rate = df_summary.iat[4, 1]
    start_date = df_summary.iat[1, 1]
    end_date = df_summary.iat[1, 3]
    generation_date = df_summary.iat[2, 3]
    total_days = df_summary.iat[3, 1]
    total_hours = df_summary.iat[2, 1]
    company_holiday = df_summary.iat[3, 3]
    adjustment = df_summary.iat[3, 5]
    total_billing_days = total_days - (adjustment + company_holiday)
    per_day_billing = billing_rate / total_billing_days
    project_id = get_projectid(df_summary)
    list1 = check_timesheetGeneration()
    generation_date1 = str(generation_date)
    for i in list1:
        print("hello")
        if generation_date1 == i:
            print("duplicate entry")
            return

    query1 = "INSERT INTO timesheet_generation (start_date, end_date, generation_date, total_days, total_hours, per_day_billing, total_billing_days, company_holiday, adjustment, project_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        start_date,
        end_date,
        generation_date,
        total_days,
        total_hours,
        per_day_billing,
        total_billing_days,
        company_holiday,
        adjustment,
        project_id,
    )
    cur.execute(query1, values)
    con.commit()
