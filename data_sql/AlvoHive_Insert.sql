/* comments to help set up the database */ 

/*

CREATE TABLE company(
    id_company SERIAL,
    company_name VARCHAR(100) NOT NULL,
    url VARCHAR(512),
    logo BYTEA
);

*/

insert into company (id_company, company_name, url) values (1, 'JD','https://www.jdfake.com');
insert into company (id_company, company_name, url) values (2, 'Wikipedia', 'https://www.wikipedia.org');
insert into company (id_company, company_name, url) values (3, 'ArchLinux', 'https://wiki.archlinux.org');
insert into company (id_company, company_name, url) values (4, 'Fedora', 'https://fedoraproject.org');
insert into company (id_company, company_name, url) values (5, 'Ubuntu', 'https://ubuntu.com');
insert into company (id_company, company_name, url) values (6, 'Red Hat', 'https://www.redhat.com');
insert into company (id_company, company_name, url) values (7, 'Rocky', 'https://rockylinux.org/fr');
insert into company (id_company, company_name, url) values (8, 'Debian', 'https://www.debian.org');
insert into company (id_company, company_name, url) values (9, 'Mint', 'https://www.linuxmint.com');
insert into company (id_company, company_name, url) values (10, 'Suse', 'https://www.suse.com');
insert into company (id_company, company_name, url) values (11, 'Manjaro', 'https://manjaro.org');
insert into company (id_company, company_name, url) values (12, 'KDE', 'http://kde.org');
insert into company (id_company, company_name, url) values (13, 'Gentoo', 'https://www.gentoo.org');
insert into company (id_company, company_name, url) values (14, 'Google', 'https://google.fr');
insert into company (id_company, company_name, url) values (15, 'Slackware', 'http://www.slackware.com');
insert into company (id_company, company_name, url) values (16, 'Gnome', 'https://www.gnome.org');
insert into company (id_company, company_name, url) values (17, 'Mozilla', 'https://www.mozilla.org');
insert into company (id_company, company_name, url) values (18, 'Thunderbird', 'https://www.thunderbird.net');
insert into company (id_company, company_name, url) values (19, 'Bash', 'https://www.gnu.org/software/bash');
insert into company (id_company, company_name, url) values (20, 'Docker', 'https://www.docker.com');
insert into company (id_company, company_name, url) values (21, 'PostgreSQL', 'https://www.postgresql.org');
insert into company (id_company, company_name, url) values (22, 'Kali', 'https://www.kali.org');
insert into company (id_company, company_name, url) values (23, 'CVE-Search', 'https://www.cve-search.org');
insert into company (id_company, company_name, url) values (24, 'Metasploitable 2', 'https://docs.rapid7.com/metasploit/metasploitable-2');
insert into company (id_company, company_name, url) values (25, 'Python', 'https://www.python.org');
insert into company (id_company, company_name, url) values (26, 'VirtualBox', 'https://www.virtualbox.org');
insert into company (id_company, company_name, url) values (27, 'VSCodium', 'https://vscodium.com');
insert into company (id_company, company_name, url) values (28, 'Apache', 'https://apache.org');
insert into company (id_company, company_name, url) values (29, 'HeidSql', 'https://www.heidisql.com');
insert into company (id_company, company_name, url) values (30, 'LXer', 'http://lxer.com');


/*

CREATE TABLE company_address(
    id_address SERIAL,
    id_company INTEGER NOT NULL,
    address1 VARCHAR(255) NOT NULL,
    address2 VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL
);

*/

insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (1, 1, '3132 Elgar Park', 'PO Box 29933', 'Jönköping', '554 52', 'Sweden');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (2, 2, '11133 Mariners Cove Crossing', '19th Floor', 'Purísima', '231547', 'Colombia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (3, 3, '2 Fordem Avenue', 'Suite 80', 'Pedrogão', '6090-425', 'Portugal');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (4, 3, '6844 Sage Point', 'Room 1788', 'Namyang-dong', '12356', 'North Korea');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (5, 3, '8052 Forest Dale Point', 'PO Box 57871', 'Jiupu', '64658', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (6, 4, '0 Annamark Way', 'PO Box 8630', 'Tiechang', '32131', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (7, 5, '30 Almo Court', 'Suite 92', 'Pytalovo', '181410', 'Russia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (8, 6, '3 Wayridge Hill', '3rd Floor', 'Balakhninskiy', '666921', 'Russia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (9, 7, '19647 Claremont Place', 'Room 683', 'Lugar Novo', '4820-013', 'Portugal');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (10, 8, '419 Eastlawn Way', '16th Floor', 'Gagarin', '545-j', 'Uzbekistan');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (11, 8, '67 Montana Way', 'Apt 221', 'Dulyapino', '157825', 'Russia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (12, 8, '51 Reindahl Drive', 'Suite 2', 'Likino-Dulevo', '142672', 'Russia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (13, 9, '5765 Westend Court', 'PO Box 32443', 'Negoslavci', '32239', 'Croatia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (14, 9, '65971 Elka Terrace', '9th Floor', 'Fenglai', '213233', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (15, 10, '37124 Stoughton Court', 'PO Box 31123', 'Bogi', '2123', 'Indonesia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (16, 11, '07 Union Alley', 'Apt 610', 'Shifan', '98545', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (17, 12, '86689 Brentwood Street', '17th Floor', 'Gumaus', '4606', 'Philippines');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (18, 13, '80 Lyons Alley', 'PO Box 4828', 'Coaraci', '45638-000', 'Brazil');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (19, 14, '1402 Lillian Junction', 'Suite 62', 'Kampen (Overijssel)', '8264', 'Netherlands');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (20, 15, '7467 Vidon Trail', 'Apt 1730', 'Vinica', '2310', 'Macedonia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (21, 15, '16 Stoughton Trail', 'Apt 632', 'Konispol', 'k85l', 'Albania');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (22, 16, '65 Quincy Parkway', 'Room 901', 'Severnyy', '346763', 'Russia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (23, 17, '57413 Boyd Junction', 'PO Box 17859', 'Huangmei', '9654', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (24, 18, '08 Fordem Junction', '20th Floor', 'Mytishchi', '141032', 'Russia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (25, 19, '17155 Schurz Place', 'Apt 415', 'Złocieniec', '78-524', 'Poland');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (26, 20, '07 Portage Place', 'Suite 95', 'Laoqiao', '76000', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (27, 20, '0 Schurz Drive', 'Room 872', 'Ciawitali', '27412', 'Indonesia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (28, 22, '72 Meadow Valley Alley', 'Suite 63', 'Évreux', '27036 CEDEX', 'France');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (29, 23, '6 High Crossing Circle', 'Suite 52', 'Dalsjöfors', '516 31', 'Sweden');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (30, 24, '329 Melvin Street', 'Apt 1380', 'Preston', 'PR1', 'United Kingdom');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (31, 24, '98173 Dwight Road', 'Room 356', 'Junyang', '245', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (32, 25, '91311 Pankratz Hill', 'Suite 88', 'Ōarai', '311-1500', 'Japan');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (33, 25, '6677 Cherokee Way', 'Suite 19', 'Taltal', '4562', 'Chile');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (34, 25, '7 Hallows Alley', 'Room 1998', 'Belos Ares', '4650-304', 'Portugal');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (35, 25, '71 Barnett Place', 'PO Box 66271', 'Dawu', '1238', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (36, 25, '70145 Farmco Pass', 'Room 528', 'Dióni', '159753', 'Greece');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (37, 26, '8691 Ruskin Center', 'Room 79', 'Vilarinho das Cambas', '4760-743', 'Portugal');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (38, 26, '836 Maple Parkway', '8th Floor', 'Tianning', '549', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (39, 26, '99 Little Fleur Plaza', 'Suite 72', 'Qiewa', '395', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (40, 26, '22214 Northfield Center', 'Suite 21', 'Korets’', '128', 'Ukraine');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (41, 27, '21586 Ryan Terrace', 'Room 1445', 'Jitan', 'lkj95', 'China');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (42, 27, '82856 Waubesa Drive', 'Suite 73', 'Nakhabino', '396072', 'Russia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (43, 27, '32651 Vahlen Circle', 'Suite 7', 'Gualaceo', '9671', 'Ecuador');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (44, 27, '9 Tony Park', 'PO Box 69915', 'Banjar Dauhpura', '1235', 'Indonesia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (45, 28, '0 Carberry Drive', 'PO Box 73713', 'San Carlos', '6459', 'Peru');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (46, 28, '2320 Hovde Junction', '16th Floor', 'Mehtar Lām', '2569', 'Afghanistan');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (47, 28, '37 Randy Center', 'Suite 23', 'Nossa Senhora da Glória', '49680-000', 'Brazil');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (48, 29, '4132 Esch Park', '5th Floor', 'Staryy Saltiv', '245', 'Ukraine');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (49, 30, '938 Raven Park', 'PO Box 61133', 'Kiuola', '323', 'Indonesia');
insert into company_address (id_address, id_company, address1, address2, city, postal_code, country) values (50, 30, '1 Sheridan Way', 'Suite 90', 'Kecskemét', '6004', 'Hungary');


/*

CREATE TABLE contact(
    id_contact SERIAL,
    id_address INTEGER NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    username VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(30) NOT NULL
);

*/

insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (1, 1, 'John', 'Doe', 'jdoe1', 'jdoe@jd.com', '+1 553 967 8824');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (2, 2, 'Fenelia', 'Picker', 'fpicker1', 'fpicker1@netlog.com', '+263 553 967 8824');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (3, 2, 'Fenelia', 'Picker', 'fpicker1', 'fpicker1@netlog.com', '+263 553 967 8824');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (4, 2, 'Deloria', 'Brandham', 'dbrandham2', 'dbrandham2@ow.ly', '+54 135 864 2294');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (5, 4, 'Elwira', 'Van der Kruijs', 'evanderkruijs3', 'evanderkruijs3@hc360.com', '+30 975 328 9269');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (6, 5, 'Theadora', 'Simonetti', 'tsimonetti4', 'tsimonetti4@xing.com', '+48 970 300 1620');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (7, 6, 'Terry', 'Quarrell', 'tquarrell5', 'tquarrell5@vkontakte.ru', '+86 427 482 5898');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (8, 7, 'Tiphani', 'Larrad', 'tlarrad6', 'tlarrad6@wp.com', '+33 264 325 1784');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (9, 8, 'Miof', 'Morillas', 'mmorillas7', 'mmorillas7@goo.ne.jp', '+63 440 303 9404');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (10, 9, 'Shauna', 'Tremble', 'stremble8', 'stremble8@123-reg.co.uk', '+998 348 735 0950');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (11, 10, 'Sheelagh', 'Coolson', 'scoolson9', 'scoolson9@ca.gov', '+504 663 122 2029');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (12, 11, 'Jenine', 'Ruddle', 'jruddlea', 'jruddlea@samsung.com', '+420 752 945 6437');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (13, 12, 'Charla', 'Halton', 'chaltonb', 'chaltonb@walmart.com', '+62 476 181 2845');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (14, 13, 'Gusti', 'Burford', 'gburfordc', 'gburfordc@hubpages.com', '+595 499 127 9925');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (15, 14, 'Blaire', 'Puve', 'bpuved', 'bpuved@cloudflare.com', '+30 783 463 9935');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (16, 15, 'Mirabelle', 'Guido', 'mguidoe', 'mguidoe@plala.or.jp', '+265 331 936 3340');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (17, 16, 'Cassie', 'Lansley', 'clansleyf', 'clansleyf@sakura.ne.jp', '+596 452 996 4308');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (18,17, 'Francesca', 'Fullilove', 'ffulliloveg', 'ffulliloveg@sakura.ne.jp', '+84 269 339 3703');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (19, 17, 'Hyacintha', 'Hedworth', 'hhedworthh', 'hhedworthh@arstechnica.com', '+54 561 314 1267');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (20, 19, 'Jen', 'Quidenham', 'jquidenhami', 'jquidenhami@rediff.com', '+86 892 364 2668');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (21, 20, 'Kalle', 'Spillett', 'kspillettj', 'kspillettj@discuz.net', '+55 987 446 2608');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (22, 21, 'Gilberto', 'Belvard', 'gbelvardk', 'gbelvardk@who.int', '+55 952 342 4405');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (23, 22, 'Ash', 'Vine', 'avinel', 'avinel@ed.gov', '+34 982 990 6420');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (24, 23, 'Elise', 'Raff', 'eraffm', 'eraffm@wisc.edu', '+66 453 874 6937');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (25, 24, 'Annabella', 'Devereux', 'adevereuxn', 'adevereuxn@vistaprint.com', '+504 962 729 9136');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (26, 25, 'Luci', 'Robjant', 'lrobjanto', 'lrobjanto@a8.net', '+63 960 348 6574');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (27, 26, 'Peirce', 'Rose', 'prosep', 'prosep@redcross.org', '+387 596 419 7164');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (28, 27, 'Goldia', 'Zanetto', 'gzanettoq', 'gzanettoq@gnu.org', '+81 884 504 1249');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (29, 28, 'Krystle', 'Gallienne', 'kgallienner', 'kgallienner@angelfire.com', '+86 580 581 1545');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (30, 29, 'Darryl', 'Garie', 'dgaries', 'dgaries@dyndns.org', '+1 210 671 8873');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (31, 30, 'Andros', 'Ingle', 'ainglet', 'ainglet@over-blog.com', '+33 344 472 5983');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (32, 31, 'Aldon', 'Creedland', 'acreedlandu', 'acreedlandu@joomla.org', '+55 687 937 1827');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (33, 32, 'Rivy', 'OFeeny', 'rofeenyv', 'rofeenyv@imgur.com', '+254 142 981 3734');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (34, 33, 'Willy', 'Linham', 'wlinhamw', 'wlinhamw@mlb.com', '+351 750 346 2624');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (35, 34, 'Carey', 'Laweles', 'clawelesx', 'clawelesx@discuz.net', '+86 485 103 6398');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (36, 35, 'Ailey', 'Fearey', 'afeareyy', 'afeareyy@msn.com', '+374 387 450 5718');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (37, 35, 'Giacomo', 'Belsher', 'gbelsherz', 'gbelsherz@hatena.ne.jp', '+81 970 252 6656');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (38, 37, 'Bernete', 'Coller', 'bcoller10', 'bcoller10@photobucket.com', '+7 228 314 0459');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (39, 38, 'Kerrin', 'Diggles', 'kdiggles11', 'kdiggles11@latimes.com', '+7 110 125 0470');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (40, 39, 'Abagail', 'Blaik', 'ablaik12', 'ablaik12@lulu.com', '+56 165 495 4602');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (41, 40, 'Madelaine', 'Stuther', 'mstuther13', 'mstuther13@pcworld.com', '+86 303 145 7917');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (42, 41, 'Haroun', 'Warratt', 'hwarratt14', 'hwarratt14@japanpost.jp', '+86 979 239 7901');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (43, 42, 'Lolly', 'DeSousa', 'ldesousa15', 'ldesousa15@ning.com', '+48 357 478 6045');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (44, 43, 'Trish', 'Terese', 'tterese16', 'tterese16@irs.gov', '+63 139 586 8553');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (45, 44, 'Uri', 'Rigmand', 'urigmand17', 'urigmand17@hexun.com', '+46 758 110 4032');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (46, 25, 'Luciano', 'Barstock', 'lbarstock18', 'lbarstock18@elpais.com', '+62 535 736 2225');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (47, 1, 'Teddy', 'Selwyne', 'tselwyne19', 'tselwyne19@cdbaby.com', '+62 233 152 2145');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (48, 48, 'Fabio', 'Caulton', 'fcaulton1a', 'fcaulton1a@whitehouse.gov', '+242 642 748 5946');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (49, 48, 'Sam', 'Sorton', 'ssorton1b', 'ssorton1b@163.com', '+57 911 364 3675');
insert into contact (id_contact, id_address, first_name, last_name, username, email, phone) values (50, 12, 'Karna', 'de Quesne', 'kdequesne1c', 'kdequesne1c@nymag.com', '+63 751 725 7492');


/*

Done by Metasploit: replicated into AlvoHibe db

CREATE TABLE hosts (
	"id" SERIAL NOT NULL,
	"created_at" TIMESTAMP NULL DEFAULT NULL,
	"address" INET NOT NULL,
	"mac" VARCHAR NULL DEFAULT NULL,
	"comm" VARCHAR NULL DEFAULT NULL,
	"name" VARCHAR NULL DEFAULT NULL,
	"state" VARCHAR NULL DEFAULT NULL,
	"os_name" VARCHAR NULL DEFAULT NULL,
	"os_flavor" VARCHAR NULL DEFAULT NULL,
	"os_sp" VARCHAR NULL DEFAULT NULL,
	"os_lang" VARCHAR NULL DEFAULT NULL,
	"arch" VARCHAR NULL DEFAULT NULL,
	"workspace_id" INTEGER NOT NULL,
	"updated_at" TIMESTAMP NULL DEFAULT NULL,
	"purpose" TEXT NULL DEFAULT NULL,
	"info" VARCHAR(65536) NULL DEFAULT NULL,
	"comments" TEXT NULL DEFAULT NULL,
	"scope" TEXT NULL DEFAULT NULL,
	"virtual_host" TEXT NULL DEFAULT NULL,
	"note_count" INTEGER NULL DEFAULT 0,
	"vuln_count" INTEGER NULL DEFAULT 0,
	"service_count" INTEGER NULL DEFAULT 0,
	"host_detail_count" INTEGER NULL DEFAULT 0,
	"exploit_attempt_count" INTEGER NULL DEFAULT 0,
	"cred_count" INTEGER NULL DEFAULT 0,
	"detected_arch" VARCHAR NULL DEFAULT NULL,
	"os_family" VARCHAR NULL DEFAULT NULL
);

*/

INSERT INTO hosts (id, created_at, address, mac, name, state, os_name, os_sp, workspace_id, purpose, os_family)
VALUES
    (2, '2024-06-12 19:03:02.25368', '192.168.56.108', '08:00:27:1a:45:e0', 'plin12', 'alive', 'Linux','2.4.x', 1, 'server', 'Linux'),
    (3, '2024-06-14 16:40:32.10256', '192.168.56.106', '08:00:27:1a:a0:c9', 'linuxt5', 'alive', 'Linux','3.14.x', 1, 'server', 'Linux'),
    (4, '2024-06-17 11:42:17.20134', '192.168.56.113', '08:00:27:1a:1b:c1', 'victim2', 'alive', 'Linux','4.0.x', 1, 'server', 'Linux'),
    (5, '2024-06-18 17:33:56.00256', '192.168.56.119', '08:00:27:1a:c8:e2', 'envlin4', 'alive', 'Linux','4.2.x', 1, 'server', 'Linux'),
    (6, '2024-06-20 08:24:20.32105', '192.168.56.118', '08:00:27:1a:1d:d5', 'metalin1', 'alive', 'Linux','3.42.x', 1, 'server', 'Linux'),
    (7, '2024-06-21 09:55:33.52105', '192.168.56.115', '08:00:27:1a:6e:b4', 'metalin2', 'alive', 'Linux','6.2.x', 1, 'server', 'Linux');


/*

CREATE TABLE contact_hosts(
    id_contact INTEGER NOT NULL,
    id_hosts BIGINT NOT NULL
);

*/
INSERT INTO contact_hosts(id_contact, id_hosts)
VALUES
    (1,1),	/* John Doe ==> host #1, car John Doe pourrait être associé à plusieurs hosts */
    (1,2),
    (1,3),
	(12,4),  /* Contact id 12 associé à host id 4 */
	(33,5),
	(7,6),
	(11,7);



/* 

Done by Metasploit: replicated into AlvoHibe db

CREATE TABLE "services" (
	"id" SERIAL NOT NULL,
	"host_id" INTEGER NULL DEFAULT NULL,
	"created_at" TIMESTAMP NULL DEFAULT NULL,
	"port" INTEGER NOT NULL,
	"proto" VARCHAR(16) NOT NULL,
	"state" VARCHAR NULL DEFAULT NULL,
	"name" VARCHAR NULL DEFAULT NULL,
	"updated_at" TIMESTAMP NULL DEFAULT NULL,
	"info" TEXT NULL DEFAULT NULL
)

*/

INSERT INTO services (id, host_id, created_at, port, proto, state, name, info)
VALUES
    (24, 2, '2024-06-12 19:03:02.25368',   21, 'tcp', 'open', 'ftp', 'vsftpd 3.0.3'),
    (25, 2, '2024-06-12 19:03:02.25368', 3306, 'tcp', 'open', 'mysql', 'MySQL 8.0.3'),
    (26, 3, '2024-06-14 16:40:32.10256',   22, 'tcp', 'open', 'ssh', 'OpenSSH 7.4p1'),
    (27, 4, '2024-06-17 11:42:17.20134', 3306, 'tcp', 'open', 'mysql', 'MySQL 5.5.53-1'),
    (28, 4, '2024-06-17 11:42:17.20134',   80, 'tcp', 'open', 'http', 'Apache 2.4.46'),
	(29, 5, '2024-06-18 17:33:56.00256',   22, 'tcp', 'open', 'ssh', 'OpenSSH 8.1p1'),
    (30, 6, '2024-06-17 12:05:02.25368',   22, 'tcp', 'open', 'ssh', 'OpenSSH 6.1'),
    (31, 6, '2024-06-17 12:05:02.25368', 5432, 'tcp', 'open', 'postgres', 'PostgreSQL 9.2.24'),
    (32, 7, '2024-06-21 09:55:33.52105',   25, 'tcp', 'open', 'smtpd', 'Postfix 3.4.7');


/*

CREATE TABLE service_version(
    id_service BIGINT NOT NULL,
    id_hosts BIGINT NOT NULL,
    service_name VARCHAR(50) NOT NULL,
    service_version VARCHAR(20) NOT NULL,
	cpe VARCHAR(100) NOT NULL
);

*/

/*
1 to 23: from Victim db_nmap Pentest
Victim: host #1 
*/
INSERT INTO service_version (id_service, id_hosts, service_name, service_version, cpe)
VALUES
    (1, 1, 'vsftpd', '2.3.4', 'cpe:2.3:a:vsftpd_project:vsftpd:2.3.4:*:*:*:*:*:*:*'),
    (2, 1, 'OpenSSH', '4.7p1', 'cpe:2.3:a:openbsd:openssh:4.7p1:*:*:*:*:*:*:*'),
    (3, 1, 'telnet', '0.17-35', 'cpe:2.3:a:telnetd:telnetd:0.17.25:*:*:*:*:*:*:*'),
    (4, 1, 'Postfix smtpd','2.5.1-2', 'cpe:2.3:a:postfix:postfix:2.4:*:*:*:*:*:*:*'),
    (5, 1, 'ISC BIND', '9.4.2', 'cpe:2.3:a:isc:bind:9.0:*:*:*:*:*:*:*'),
	(6, 1, 'Apache httpd', '2.2.8', 'cpe:2.3:a:apache:http_server:2.0.36:*:*:*:*:*:*:*'),
    (16, 1, 'ProFTPD', '1.3.1', 'cpe:2.3:a:proftpd_project:proftpd:1.3.0:*:*:*:*:*:*:*'),
    (17, 1, 'MySQL', '5.0.51a', 'cpe:2.3:a:oracle:mysql:5.0.51a:*:*:*:*:*:*:*'),
    (18, 1, 'PostgreSQL', '8.3.1', 'cpe:2.3:a:postgresql:postgresql:8.3.1:*:*:*:*:*:*:*'),
    (19, 1, 'VNC', '3.3', 'cpe:2.3:a:att:vnc:3.3.3:*:*:*:*:*:*:*'),
    (22, 1, 'Apache Jserv Protocol', '1.3', 'cpe:2.3:a:apache:tomcat:3.3:*:*:*:*:*:*:*'), 
	(23, 1, 'Apache Tomcat/Coyote JSP engine', '1.1', 'cpe:2.3:a:apache:tomcat_native:1.1.23:*:*:*:*:*:*:*'),
	(24, 2, 'vsftpd', '3.0.3', 'cpe:2.3:a:vsftpd_project:vsftpd:3.0.3:*:*:*:*:*:*:'),
	(25, 2, 'MySQL', '8.0.37-1', 'cpe:2.3:a:oracle:mysql:8.0.3:*:*:*:*:*:*:*'),
	(26, 3, 'OpenSSH', '7.4p1', 'cpe:2.3:a:openbsd:openssh:7.4:*:*:*:*:*:*:*'),
	(27, 4, 'MySQL', '5.5.53-1', 'cpe:2.3:a:oracle:mysql:5.5.53:*:*:*:*:*:*:*'),
	(28, 4, 'Apache', '2.4.46', 'cpe:2.3:a:apache:http_server:2.4.46:*:*:*:*:*:*:*'),
	(29, 5, 'OpenSSH', '8.1p1', 'cpe:2.3:a:openbsd:openssh:3.8.1p1:*:*:*:*:*:*:*'),
	(30, 6, 'OpenSSH', '6.1', 'cpe:2.3:a:openbsd:openssh:6.1:*:*:*:*:*:*:*'),
	(31, 6, 'PostgreSQL', '9.2.24', 'cpe:2.3:a:postgresql:postgresql:9.2.24:*:*:*:*:*:*:*'),
	(32, 7, 'Postfix', '3.4.7', 'cpe:2.3:a:postfix:postfix:3.4.7:*:*:*:*:*:*:*');
