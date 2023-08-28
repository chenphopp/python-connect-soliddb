import pyodbc

def create_connection(dsn, user, password):
    connection_string = f'DSN={dsn};UID={user};PWD={password}'
    return pyodbc.connect(connection_string)

def fetch_column_data(conn, column_name_input):
    cursor = conn.cursor()
    #query = f"SELECT SYSID, {column_name_input} from sysobj"
    query = f"SELECT SYSID, {column_name_input} from sysobj"
    cursor.execute(query)
    return cursor.fetchall(), cursor

def check_for_spaces(row, column_name_input):
    sysid_value = row.SYSID
    column_value = getattr(row, column_name_input)
    
    if column_value is None:
        return f"SYSID: {sysid_value}, {column_name_input} ' '"

    elif column_value and isinstance(column_value, str) and (column_value.startswith(' ') or column_value.endswith(' ')):
        return f"SYSID: {sysid_value}, {column_name_input}: '{column_value}' contains space"

    elif column_value and isinstance(column_value, str) and "  " in column_value:
        return f"SYSID: {sysid_value}, {column_name_input}: '{column_value}' contains double space"
        
    return None

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            if line:  # Only write non-empty lines
                file.write(line + '\n')

def close_connection(conn, cursor):
    cursor.close()
    conn.close()
