# :lock: AlvoHive :honey_pot:

#### The goal is to create a tool to extract data gathered during a ``penetration test`` and organize it into a document template. It includes  charts, an executive summary, and a summary of the Common Vulnerabilities and Exposures (``CVEs``) identified.

### Features (TL;DR style)
- Data Extraction: Extracts data from penetration test results.
- Organized Documentation: Organizes data into a document template with charts and summaries.
- Executive Summary: Provides a concise summary of test outcomes and key findings.
- CVE Summary: Includes a summary of identified Common Vulnerabilities and Exposures (CVEs).
- Multi-Format Reports: Generates reports in various formats (HTML/CSS, Markdown, PDF).
- REST API Integration: Automatically fetches summaries for CVE IDs.

### Virtualization

![Docker](https://img.shields.io/badge/docker-0091EA?style=for-the-badge&logo=docker&logoColor=white)
![VirtualBox](https://img.shields.io/badge/virtualbox-183A61?style=for-the-badge&logo=virtualbox&logoColor=white)

### Technologies / Related Projects
![Kali Linux](https://img.shields.io/badge/kali%20linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Metasploitable2](https://img.shields.io/badge/metasploitable2-0091EA?style=for-the-badge&logo=metasploit&logoColor=white)
![Apache](https://img.shields.io/badge/apache-D22128?style=for-the-badge&logo=apache&logoColor=white)
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-316192?style=for-the-badge&logo=postgresql&logoColor=white)

- Kali Linux *VM*: Provides tools for pentesters/ethical hackers.\
    &#x21B3; (https://www.kali.org/get-kali/#kali-virtual-machines)
    \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2911; [VM installation and configuration Kali](documentation_infra/Kali_VirtualBox.md)


- Metasploitable2 *VM*: Vulnerable Linux environment.\
    &#x21B3; (https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)
    \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2911; [VM installation and configuration Metasploitable2](documentation_infra/Metasploitable_VirtualBox.md)

- CVE-Search *Docker*:  Tool used to import CVEs details in a local MongoDB. Provides REST API access.\
    &#x21B3; (https://github.com/cve-search/cve-search)
    \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2911; [Docker image installation, configuration and runtime](documentation_infra/Cve-search_docker.md)

- Apache + Python *Docker*: Apache HTTP server and Python for the back-end development.
\
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2911; [Docker image installation, configuration and runtime Apache](documentation_infra/Apache_Postgres_docker.md)
- PostgreSQL *Docker*: Database for the front-end and back-end.
\
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2911; [Docker image installation, configuration and runtime PostgreSQL](documentation_infra/Apache_Postgres_docker.md)

## Installation
To install and run AlvoHive locally, follow these steps:
1. Clone the repository:
   ```
   git clone https://github.com/chloe0524/AlvoHive.git
   ```
2. Navigate to the project directory.
3. Follow the specific installation guides provided for each component (Kali Linux VM, Metasploitable2 VM, Docker containers). The documentation is available [here](https://github.com/chloe0524/AlvoHive/tree/AlvoMain/documentation_infra)


## Usage
After installation, start the containers by running:
```
docker-compose up
```
Access the application at `http://localhost:5000` in your web browser.

## Contribution/Author
Chloe - https://github.com/chloe0524

## Related Projects
- [Kali Linux](https://www.kali.org/)
- [Metasploit](https://www.metasploit.com/)
- [Docker](https://www.docker.com/)
- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Screenshots

![Capture d'écran 2024-07-12 222927](https://github.com/user-attachments/assets/218841b4-bc05-4d42-b605-b730092661e8)

![Capture d'écran 2024-07-12 222940](https://github.com/user-attachments/assets/56536d66-f44a-43f5-92bd-f014942c296f)

![Capture d'écran 2024-07-12 222716](https://github.com/user-attachments/assets/6404f5b8-e70b-4c51-ac5b-fdc9d0ad7134)

## Timeline

![timeline_alvohive](https://github.com/chloe0524/AlvoHive/assets/127857895/c2e7f190-e1a8-4c8b-b263-0ac77d630efe)


## Architecture
![Alvo_archi_slides drawio](https://github.com/chloe0524/AlvoHive/assets/127857895/ec9952c4-6dca-4cb6-a3da-420c81fcc8ac)

## Licensing
This project is licensed under the MIT License. See the LICENSE file for details.
