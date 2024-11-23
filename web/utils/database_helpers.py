from django.db import connection

def is_table_exists(table_name):
    """
    Check if a specific table exists in the database.
    """
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name=%s)",
            [table_name]
        )
        return cursor.fetchone()[0]