CREATE DATABASE community_conversation;

USE community_conversation;

CREATE TABLE conversation_text(chat_row BIGINT AUTO_INCREMENT,text_message VARCHAR(2000),
PRIMARY KEY(chat_row));

CREATE TABLE bmi_data(bmi_value FLOAT,age INT);

CREATE TABLE login_information (
    s_no BIGINT AUTO_INCREMENT,
    de_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    email_id VARCHAR(50),
    user_name VARCHAR(40),
    password VARCHAR(40),
    PRIMARY KEY(s_no)
);

SELECT*FROM bmi_data;

SELECT*FROM conversation_text;

SELECT*FROM login_information;