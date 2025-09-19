import sqlite3

conn = sqlite3.connect("fundamentals/databases/mini-project/blog.db")
cur = conn.cursor()

# Get all posts by user X
cur.execute("""
            SELECT p.*, u.username
            FROM posts p
            JOIN users u ON p.user_id = u.id
            WHERE u.username = ?
            """, ("userX",))
print(cur.fetchall())

# Get top 5 most recent posts
cur.execute("""
            SELECT p.*, u.username
            FROM posts p
            JOIN users u ON p.user_id = u.id
            ORDER BY p.created_at DESC
            LIMIT 5
            """)
print(cur.fetchall())

conn.close()