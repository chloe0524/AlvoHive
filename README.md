# **:construction: WORK IN PROGRESS :construction:**

# :lock: AlvoHive :honey_pot:

The goal is to create a tool to extract data gathered during a penetration test and organize it into a document template. It includes  charts, an executive summary, and a summary of the Common Vulnerabilities and Exposures (CVEs) identified.

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

### Technologies
![Kali Linux](https://img.shields.io/badge/kali%20linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Metasploitable2](https://img.shields.io/badge/metasploitable2-0091EA?style=for-the-badge&logo=metasploit&logoColor=white)
![Apache](https://img.shields.io/badge/apache-D22128?style=for-the-badge&logo=apache&logoColor=white)
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-316192?style=for-the-badge&logo=postgresql&logoColor=white)

- Kali Linux *VM*: Provides tools for pentesters/ethical hackers.\
    &#x21B3; (https://www.kali.org/get-kali/#kali-virtual-machines)\
    [VM installation and configuration](documentation_infra/Kali_VirtualBox.md)

- Metasploitable2 *VM*: Vulnerable Linux environment.\
    &#x21B3; (https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)

- CVE-Search *Docker*:  Tool used to import CVEs details in a local MongoDB. Provides REST API access.\
    &#x21B3; (https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)

- Apache + Python *Docker*: Apache HTTP server and Python for the back-end development.

- PostgreSQL *Docker*: Database for the front-end and back-end.

### Architecture
![AlvoHive_archi](https://github.com/chloe0524/AlvoHive/assets/127857895/818aa976-346e-4036-958e-4c86eed8cf39)

