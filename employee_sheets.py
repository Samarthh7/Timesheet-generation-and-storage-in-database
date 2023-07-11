import pymysql
import pandas as pd


# getting employee id from employee table
con = pymysql.connect(
    host="localhost", user="root", password="root", database="ttn", charset="utf8"
)


def create_connection(con):
    cur = con.cursor()
    return cur


def get_employee_id(employee):
    cur = create_connection(con)
    query = "select id from employees where employee_name = '%s'" % (employee,)
    cur.execute(query)
    data = cur.fetchall()
    print(data)
    x = data[0][0]
    return x


def display_employees(df):
    print("List of employees working on the project: \n")
    for employee in df.keys():
        employee_id = get_employee_id(employee)
        print(f"employee id for employee: {employee} is {employee_id}")


# Renaming columns
def rename_employee_sheet_column(df):
    for value in df.keys():
        df[value].rename(
            {
                "Name": "Day",
                value: "Date",
                "Unnamed: 2": "Task",
                "Unnamed: 3": "Hours",
                "Unnamed: 4": "Comment",
            },
            axis=1,
            inplace=True,
        )
        df[value] = df[value].fillna("NULL")

    for value in df.keys():
        df[value].Date = df[value].Date.astype("string")


# reading all the data of the employees into sql database


def inserting_tasks(df):
    cur = create_connection(con)
    for name in df.keys():
        employee_id = get_employee_id(name)
        length = len(df[name])
        for i in range(4, length):
            record = tuple(df[name].loc[i, "Date":"Comment":1])
            record = record + (employee_id,)
            sql = "INSERT INTO tasks (date, task, working_hours,comment,employee_id) VALUES(%s, %s, %s, %s, %s)"
            cur.executemany(sql, [record])
            print(record)
    con.commit()
