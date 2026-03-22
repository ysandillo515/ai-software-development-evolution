import sqlite3
from fastmcp import FastMCP

mcp = FastMCP("SQLite Tool")

@mcp.tool
def query_database(sql: str) -> str:
    """Run a read-only SQL query against the sample products database."""
    try:
        conn = sqlite3.connect("sample.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()

        if not rows:
            return "No results found."

        result = ", ".join(columns) + "\n"
        for row in rows:
            result += ", ".join(str(val) for val in row) + "\n"
        return result

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()