import pymysql
import pandas as pd


con = pymysql.connect(
    host="localhost", user="root", password="root", database="ttn", charset="utf8"
)


def create_connection(con):
    cur = con.cursor()
    return cur


# insert project details
def check_projectDetails():
    cur = create_connection(con)
    sql = "select contract from project_details"
    cur.execute(sql)
    data = cur.fetchall()
    y = list()
    data1 = list(data)
    print(len(data1))
    for i in range(len(data1)):
        x = data1[i][0]
        y.append(x)
    return y


def insert_projectdetails(df_summary):
    cur = create_connection(con)
    project = df_summary.iat[0, 1]
    contract = df_summary.iat[0, 3]
    billing_rate = df_summary.iat[4, 1]
    list1 = check_projectDetails()
    for i in list1:
        if contract == i:
            print("duplicate entry")
            return

    query2 = "insert into project_details(project, contract, billing_rate) values( %s, %s, %s)"
    values = (project, contract, billing_rate)
    cur.execute(query2, values)
    con.commit()


# insert employee summary create function
def insert_employee(df_summary):
    cur = create_connection(con)
    length = len(df_summary)
    new_header = df_summary.iloc[7]
    df_summary = df_summary[1:]
    df_summary.columns = new_header
    for i in range(8, length):
        record = tuple(df_summary.loc[i, "Name":"Designation":1])
        query3 = "INSERT INTO employees (employee_name, competency, designation) VALUES(%s, %s, %s)"
        cur.executemany(query3, [record])
        print(record)
    con.commit()
