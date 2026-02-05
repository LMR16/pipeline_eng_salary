
-- Creating new table

-- DROP TABLE IF EXISTS salarios_engenharia;

CREATE TABLE IF NOT EXISTS salarios_engenharia (
    id SERIAL PRIMARY KEY,
    work_year SMALLINT NOT NULL,
    experience_level VARCHAR(2) NOT NULL,
    employment_type VARCHAR(2),
    job_title VARCHAR(100),
    salary DECIMAL(12,2) NOT NULL,
    salary_currency CHAR(3),
    salary_in_usd DECIMAL(12,2) NOT NULL,
    employee_residence VARCHAR(2),
    remote_ratio SMALLINT NOT NULL,
    company_location CHAR(2),
    company_size VARCHAR(1)
);