-- Insert statements for Member table
INSERT INTO member (username, first_name, middle_name, last_name, date_of_birth, location, email, image_file, password, joined_date, active_record)
VALUES
    ('member1', 'Sam', 'Salty', 'Sardine', '1990-05-01', 'New York', 'john@example.com', 'default.jpg', 'password1', '2023-01-01 10:00:00', 1),
    ('member2', 'Jane', NULL, 'Johnson', '1985-08-15', 'Los Angeles', 'jane@example.com', 'default.jpg', 'password2', '2023-02-02 11:00:00', 1),
    ('member3', 'Michael', 'Robert', 'Williams', '1995-11-20', 'Chicago', 'michael@example.com', 'default.jpg', 'password3', '2023-03-03 12:00:00', 1);

-- Insert statements for Entry table (related to member1)
INSERT INTO entry (date, time_of_day, mood, status, weight, measurement_waist, keto, user_id, active_record)
VALUES
    ('2023-01-01 09:00:00', 'day', 'happy', 'normal', 170.5, 32.5, 1, 1, 1),
    ('2023-01-01 13:00:00', 'afternoon', 'happy', 'normal', 169.2, NULL, 0, 1, 1),
    ('2023-01-01 19:00:00', 'night', 'Sad', 'normal', 168.8, 32.2, 1, 1, 1);

-- Insert statements for Entry table (related to member2)
INSERT INTO entry (date, time_of_day, mood, status, weight, measurement_waist, keto, user_id, active_record)
VALUES
    ('2023-02-02 10:00:00', 'day', 'happy', 'normal', 155.5, 28.5, 1, 2, 1),
    ('2023-02-02 14:00:00', 'afternoon', 'happy', 'normal', 154.2, NULL, 0, 2, 1),
    ('2023-02-02 20:00:00', 'night', 'Sad', 'normal', 153.8, 28.2, 1, 2, 1);

-- Insert statements for Entry table (related to member3)
INSERT INTO entry (date, time_of_day, mood, status, weight, measurement_waist, keto, user_id, active_record)
VALUES
    ('2023-03-03 11:00:00', 'day', 'happy', 'normal', 180.5, 34.5, 1, 3, 1),
    ('2023-03-03 15:00:00', 'afternoon', 'happy', 'normal', 179.2, NULL, 0, 3, 1),
    ('2023-03-03 21:00:00', 'night', 'Sad', 'normal', 178.8, 34.2, 1, 3, 1);
