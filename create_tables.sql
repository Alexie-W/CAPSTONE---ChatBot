DROP DATABASE IF EXISTS chatbot2;
CREATE DATABASE chatbot2;
USE chatbot2;

-- Users Table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    UID VARCHAR(50) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Goals Table
DROP TABLE IF EXISTS goals;
CREATE TABLE goals (
    GID INT AUTO_INCREMENT PRIMARY KEY,
    UID VARCHAR(50),
    g_description TEXT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UID) REFERENCES users(UID)
);

-- Journal Entries Table
DROP TABLE IF EXISTS jounral_entries;
CREATE TABLE journal_entries (
    JID INT AUTO_INCREMENT PRIMARY KEY,
    UID VARCHAR(50),
    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    entry_text TEXT NOT NULL,
    FOREIGN KEY (UID) REFERENCES users(UID)
);

-- Mood Tracking Table
DROP TABLE IF EXISTS mood_tracking;
CREATE TABLE mood_tracking (
    MID INT AUTO_INCREMENT PRIMARY KEY,
    UID VARCHAR(50),
    mood_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mood VARCHAR(50) NOT NULL,
    FOREIGN KEY (UID) REFERENCES users(UID)
);

-- Conversations Table
DROP TABLE IF EXISTS conversations;
CREATE TABLE conversations (
    CID INT AUTO_INCREMENT PRIMARY KEY,
    UID VARCHAR(50),
    conversation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    conversation_text TEXT NOT NULL,
    FOREIGN KEY (UID) REFERENCES users(UID)
);

-- Requests Table
DROP TABLE IF EXISTS requests;
CREATE TABLE requests (
    RID INT AUTO_INCREMENT PRIMARY KEY,
    UID VARCHAR(50),
    symptom TEXT NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UID) REFERENCES users(UID)
);

-- Quizzes Table
DROP TABLE IF EXISTS quizzes;
CREATE TABLE quizzes (
    QID INT AUTO_INCREMENT PRIMARY KEY,
    UID VARCHAR(50),
    quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UID) REFERENCES users(UID)
);

-- Questions Table
DROP TABLE IF EXISTS questions;
CREATE TABLE questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    QID INT,
    question_text TEXT NOT NULL,
    FOREIGN KEY (QID) REFERENCES quizzes(QID)
);

-- Answers Table
DROP TABLE IF EXISTS answers;
CREATE TABLE answers (
    answer_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT,
    answer_text TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(question_id)
);
