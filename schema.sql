create table department(
    dept_id int primary key AUTO_INCREMENT,
    dept_name varchar(50) NOT NULL,
    hod_name varchar(50)
);
-- mysql uses varchar not varchar 2 1st mistake auto increment is needed in primary key second mistake  NOT NULL is used when the data is mandatory 3rd mistake 

create table student(
    student_id primary key AUTO_INCREMENT,
    first_name varchar(50) NOT NULL,
    last_name varchar(50),
     email varchar(50) UNIQUE,
    --  unique should be used 
    dept_id int
    -- we must define the column before creating the foreign key 
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

create table courses(
    course_id int primary key AUTO_INCREMENT,
    course_name varchar(50) NOT NULL,
    credits int ,
    dept_id int,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

create table enrollments(
    enrollment_id  int primary key AUTO_INCREMENT,
    student_id int,
    course_id int,
    semester varchar(20),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

create table grades(
    grade_id int primary key AUTO_INCREMENT,
    enrollment_id int,
    FOREIGN KEY (enrollment_id) REFERENCES (enrollments),
    marks_obtained int,
    grade_letter char(2)
);