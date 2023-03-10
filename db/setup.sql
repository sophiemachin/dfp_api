DROP TABLE users;
DROP TABLE viewed;

CREATE TABLE users (
    user_id SERIAL,
    lifting_total FLOAT,
    bodyweight FLOAT,
    name VARCHAR,
    sumo BOOL,
    peds BOOL,
    PRIMARY KEY (user_id)
);

CREATE TABLE viewed (
    user_id INT,
    viewed_user INT,
    date DATE,
    liked BOOL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
