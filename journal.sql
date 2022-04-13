CREATE TABLE `Entry` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date`    TEXT NOT NULL,
    `entry`    TEXT NOT NULL,
    `concept`    TEXT NOT NULL,
    `moodId`    INTEGER NOT NULL
);

INSERT INTO `Entry` VALUES (null, 4/5/2021, "Today was great", "SQL", 2);