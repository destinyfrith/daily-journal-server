CREATE TABLE `Entry` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `concept` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
    );

INSERT INTO `Entry` VALUES (null, "4/22", "Today was great", "SQL", 2);
INSERT INTO `Entry` VALUES (null, "4/25", "Data is the best. I love it.", "SQL", 3);
INSERT INTO `Entry` VALUES (null, "4/30", "Today was not so great", "Python", 1);
INSERT INTO `Entry` VALUES (null, "5/4", "I think I forgot everything", "JavaScript", 5);

INSERT INTO `Mood` VALUES (null, "Elated");
INSERT INTO `Mood` VALUES (null, "Thankful");
INSERT INTO `Mood` VALUES (null, "Discouraged");
INSERT INTO `Mood` VALUES (null, "Hopeful");
INSERT INTO `Mood` VALUES (null, "Optimistic");
INSERT INTO `Mood` VALUES (null, "Angry");