from sqlite3_methods import *


# ------------Create Table Queries----------
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

# ------------Insert Records Queries----------
create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('Alice', 19, 'female', 'USA'),
  ('Bob', 32, 'male', 'USA'),
  ('James', 35, 'male', 'England'),
  ('Tim', 40, 'male', 'India'),
  ('Candice', 24, 'female', 'Australia');
"""

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Excited", "So excited to join the new club", 1),
  ("Traffic", "There is a heavy traffic on Boulevard Street", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am pregnant", 5),
  ("Interesting Game", "It was a fantastic game of cricket", 3),
  ("Meetup", "Anyone up for an online meetup today?", 4);
"""

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in.What time?', 1, 6),
  ('What sort of help? I can be usefull if its about Javascript', 5, 3),
  ('Congrats!! So happy for you', 2, 4),
  ('I was rooting for Australia though', 5, 5),
  ('Help with your Portfolio Page?', 2, 3),
  ('Many congratulations', 2, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""
# ------------Select Records Queries----------

select_users = "SELECT * from users"

select_posts = "SELECT * FROM posts"

select_comments = "SELECT * FROM comments"

# ---------Update Query Ex 1------------

update_post_description = """
UPDATE
  posts
SET
  description = "The Boulevard Street is free of traffic now"
WHERE
  id = 2
"""

# --------Delete Query Ex 1---------

delete_comment = "DELETE FROM comments WHERE id = 5"


def main():

    # Creating/Connecting social media DB
    connection = create_connection("social_media.db")

    #Table creation
    print("-----Creating Table-----")
    execute_query(connection, create_users_table)
    execute_query(connection, create_posts_table)
    execute_query(connection, create_comments_table)  
    execute_query(connection, create_likes_table)

    # Insert Records
    print("-----Inserting Records----")
    execute_query(connection, create_users)
    execute_query(connection, create_posts)
    execute_query(connection, create_comments)
    execute_query(connection, create_likes)


    # Selecting and displaying records
    print("----Displaying all records-----")
    users = execute_read_query(connection, select_users)
    for user in users:
        print(user)


    comments = execute_read_query(connection, select_comments)
    for comment in comments:
        print(comment)

    
    posts = execute_read_query(connection, select_posts)
    for post in posts:
        print(post)
    

    # Updating record
    print("-----Posts before Updating----")
    posts = execute_read_query(connection, select_posts)
    for post in posts:
        print(post)

    execute_query(connection, update_post_description)

    print("-----Posts after Updating")
    posts = execute_read_query(connection, select_posts)
    for post in posts:
        print(post)

    
    #Deleting Records
    print("-----Comments before Deleting----")
    comments = execute_read_query(connection, select_comments)
    for comment in comments:
        print(comment)

    execute_query(connection, delete_comment)

    print("-----Comments after Deleting----")
    comments = execute_read_query(connection, select_comments)
    for comment in comments:
        print(comment)


    close_connection(connection)


if __name__=="__main__":
    main()
