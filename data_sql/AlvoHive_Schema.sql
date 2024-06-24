/* 
	Table replicated from Postgres Metasploit already exist : services, hosts
*/

\! echo "-----------------------------------------------------------"
\! echo "Dropping all the tables"
\! echo "-----------------------------------------------------------"
DROP TABLE contact CASCADE;
DROP TABLE company CASCADE;
DROP TABLE company_address CASCADE;
DROP TABLE contact_hosts CASCADE;
DROP TABLE service_version CASCADE;
DROP TABLE report CASCADE;

\! echo "-----------------------------------------------------------"
\! echo "Creating table: contact"
\! echo "-----------------------------------------------------------"
CREATE TABLE contact(
    id_contact SERIAL,
    id_address INTEGER NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    username VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(30) NOT NULL
);
ALTER TABLE
    contact ADD PRIMARY KEY(id_contact);
CREATE INDEX contact_id_address_index ON
    contact(id_address);

\! echo "-----------------------------------------------------------"
\! echo "Creating table: company"
\! echo "-----------------------------------------------------------"
CREATE TABLE company(
    id_company SERIAL,
    company_name VARCHAR(100) NOT NULL,
    url VARCHAR(512),
    logo BYTEA
);
ALTER TABLE
    company ADD PRIMARY KEY(id_company);


\! echo "-----------------------------------------------------------"
\! echo "Creating table: company_address"
\! echo "-----------------------------------------------------------"
CREATE TABLE company_address(
    id_address SERIAL,
    id_company INTEGER NOT NULL,
    address1 VARCHAR(255) NOT NULL,
    address2 VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL
);
ALTER TABLE
    company_address ADD PRIMARY KEY(id_address);
CREATE INDEX company_address_id_company_index ON
    company_address(id_company);


\! echo "-----------------------------------------------------------"
\! echo "Creating table: contact_hosts"
\! echo "-----------------------------------------------------------"
CREATE TABLE contact_hosts(
    id_contact INTEGER NOT NULL,
    id_hosts BIGINT NOT NULL
);

\! echo "-----------------------------------------------------------"
\! echo "Creating table: service_version"
\! echo "-----------------------------------------------------------"
CREATE TABLE service_version(
    id_service BIGINT NOT NULL,
    id_hosts BIGINT NOT NULL,
    service_name VARCHAR(50) NOT NULL,
    service_version VARCHAR(20) NOT NULL,
	cpe VARCHAR(100) NOT NULL
);


\! echo "-----------------------------------------------------------"
\! echo "Creating table: report"
\! echo "-----------------------------------------------------------"
CREATE TABLE report(
    id_report SERIAL,
    id_company INTEGER NOT NULL,
    id_contact INTEGER NOT NULL,
    id_hosts BIGINT NOT NULL,
	report_date TIMESTAMP NOT NULL,
    markdown VARCHAR(300) NOT NULL,
    html VARCHAR(300),
    pdf VARCHAR(300)
);
ALTER TABLE
    report ADD PRIMARY KEY(id_report);

\! echo "-----------------------------------------------------------"
\! echo "Adding Foreign constraints"
\! echo "-----------------------------------------------------------"
ALTER TABLE
    contact ADD CONSTRAINT contact_id_address_foreign FOREIGN KEY(id_address) REFERENCES company_address(id_address);
ALTER TABLE
    contact_hosts ADD CONSTRAINT contact_hosts_id_contact_foreign FOREIGN KEY(id_contact) REFERENCES contact(id_contact);
ALTER TABLE
    company_address ADD CONSTRAINT company_address_id_company_foreign FOREIGN KEY(id_company) REFERENCES company(id_company);
ALTER TABLE
    report ADD CONSTRAINT report_id_company_foreign FOREIGN KEY(id_company) REFERENCES company(id_company);
ALTER TABLE
    report ADD CONSTRAINT report_id_contact_foreign FOREIGN KEY(id_contact) REFERENCES contact(id_contact);
ALTER TABLE
    report ADD CONSTRAINT report_id_hosts_foreign FOREIGN KEY(id_hosts) REFERENCES hosts(id);