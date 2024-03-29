-- Active: 1711697542077@@127.0.0.1@5432@ternesim

DROP TABLE IF EXISTS "user";
CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    name VARCHAR(20),
    role VARCHAR(5)
);

DROP TABLE IF EXISTS meet_room;
CREATE TABLE meet_room (
    id INT PRIMARY KEY,
    name VARCHAR(20)
);

DROP TABLE IF EXISTS meet_room_user;
CREATE TABLE meet_room_user (
    id INT PRIMARY KEY,
    user_id UUID,
    meet_room_id INT,
    start TIMESTAMP,
    finish TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES "user"(id),
    FOREIGN KEY (meet_room_id) REFERENCES meet_room(id)
);