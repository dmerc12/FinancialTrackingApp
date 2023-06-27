CREATE SCHEMA social_media_app

CREATE TABLE social_media_app.users(user_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), username VARCHAR(30), passwrd VARCHAR(60), email VARCHAR(255), birthdate DATE, created DATETIME);

CREATE TABLE social_media_app.posts(post_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, content TEXT, image_url TEXT, created DATETIME, CONSTRAINT user_post_fk FOREIGN KEY (user_id) REFERENCES social_media_app.users(user_id));

CREATE TABLE social_media_app.friends(friendship_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, friend_id INT, status VARCHAR(8), created DATETIME, updated DATETIME, CONSTRAINT user_friend_fk FOREIGN KEY (user_id) REFERENCES social_media_app.users(user_id), CONSTRAINT friend_user_fk FOREIGN KEY (friend_id) REFERENCES social_media_app.users(user_id));

CREATE TABLE social_media_app.likes(like_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, post_id INT, created DATETIME, CONSTRAINT user_like_fk FOREIGN KEY (user_id) REFERENCES social_media_app.users(user_id), CONSTRAINT like_post_fk FOREIGN KEY (post_id) REFERENCES social_media_app.posts(post_id));

CREATE TABLE social_media_app.comments(comment_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, post_id INT, content TEXT, created DATETIME, CONSTRAINT user_comment_fk FOREIGN KEY (user_id) REFERENCES social_media_app.users(user_id), CONSTRAINT post_comment_fk FOREIGN KEY (post_id) REFERENCES social_media_app.posts(post_id));

CREATE TABLE social_media_app.notifications(notification_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, sender_id INT, notification_type VARCHAR(255), is_read BOOLEAN, created DATETIME, CONSTRAINT user_notification_fk FOREIGN KEY (user_id) REFERENCES social_media_app.users(user_id), CONSTRAINT notification_sender_fk FOREIGN KEY (sender_id) REFERENCES social_media_app.users(user_id));