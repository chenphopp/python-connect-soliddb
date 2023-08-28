from function import create_connection, fetch_column_data, check_for_spaces, close_connection, write_to_file

def main():
    dsn = 'MY-SERVER'
    user = 'dba'
    password = 'dba'
    filename = 'output.txt'

    # Get column name from user input
    column_name_input = input("Please enter the column name : ")

    # Validate column name to prevent SQL injection
    allowed_columns = ["SYSNAME", "SYSID", "VERSIONNO", "OBJNO", "STRUCTURETYPE", "STATICBITS", "INTSTAT", "ABBRNAME", "TAG", "CREATED", "UPTIMEID", "MODIFIED", "DELFLA", "ACTMASK2", "ACTMASK1", "AUTHMASK1", "AUTHMASK2", "VALIDITY", "COMMENTW", "OPERNAMEW"]
    if column_name_input not in allowed_columns:
        print("Invalid column name!")
        exit()

    # Establish the connection
    conn = create_connection(dsn, user, password)
    rows, cursor = fetch_column_data(conn, column_name_input)

    #for row in rows:
    #    result = check_for_spaces(row, column_name_input)
    #    if result:
    #        print(result)

    # Collecting the results
    results = []
    for row in rows:
        result = check_for_spaces(row, column_name_input)
        if result:
            results.append(result)
    
    # Write results to file
    write_to_file(filename, results)

    # Close the connection
    close_connection(conn, cursor)

if __name__ == "__main__":
    main()

