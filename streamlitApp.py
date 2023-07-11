import streamlit as st
import pandas as pd
import subprocess


# Function to execute main.py with the provided Excel file path
def execute_main_py(excel_file_path):
    # Execute main.py using subprocess
    subprocess.run(["python", "main.py", excel_file_path])


# Streamlit app
def main():
    st.title("Excel File Processor")

    # File uploader for Excel file
    excel_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

    if excel_file:
        st.write("Excel file uploaded successfully!")

        # Display a button to execute main.py
        if st.button("Execute"):
            # Save the uploaded Excel file to a temporary location
            with open("temp_file.xlsx", "wb") as f:
                f.write(excel_file.read())

            # Execute main.py using the temporary file path
            execute_main_py("temp_file.xlsx")

            st.write("executed successfully!")

    st.write("Please upload an Excel file to get started.")


if __name__ == "__main__":
    main()
