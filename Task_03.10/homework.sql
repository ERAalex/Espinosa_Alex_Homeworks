
-- tables Genre + Musician + M2M

CREATE TABLE IF NOT EXISTS Genre (
	id serial PRIMARY KEY,
	name_genre varchar(40) NOT NULL
);


CREATE TABLE IF NOT EXISTS Musician	(
	id serial PRIMARY KEY,
	name_musician varchar(40) NOT NULL
);


CREATE TABLE IF NOT EXISTS Genre_Musician (
	id serial PRIMARY KEY,
	genre_id int REFERENCES Genre (id) ON UPDATE CASCADE ON DELETE cascade,
	musician_id int REFERENCES Musician (id) ON UPDATE CASCADE ON DELETE CASCADE
);



-- tables Albums + Collection + M2M

CREATE TABLE IF NOT EXISTS Albums (
	id serial PRIMARY KEY,
	name_album varchar(40) NOT NULL,
	year INT NOT NULL
);


CREATE TABLE IF NOT EXISTS Collection (
	id serial PRIMARY KEY,
	name_collection varchar(40) NOT NULL,
	year INT NOT NULL
);



CREATE TABLE IF NOT EXISTS Musician_Album (
	id serial PRIMARY KEY,
	musician_id int REFERENCES Musician (id) ON UPDATE CASCADE ON DELETE cascade,
	albums_id int REFERENCES Albums (id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- tables Songs + O2M + M2M


CREATE TABLE IF NOT EXISTS Songs (
	id serial PRIMARY KEY,
	name_song varchar(40) NOT NULL,
	size_time time NOT NULL,
	album_id int REFERENCES Albums (id)
);


CREATE TABLE IF NOT EXISTS Collections_Songs (
	id serial PRIMARY KEY,
	collections_id int REFERENCES Collection (id) ON UPDATE CASCADE ON DELETE cascade,
	songs_id int REFERENCES Songs (id) ON UPDATE CASCADE ON DELETE CASCADE
);


-- Extra homework Workers + Boss

CREATE TABLE IF NOT EXISTS Department (
	id serial PRIMARY KEY,
	name_depart varchar(40) NOT NULL
);


CREATE TABLE IF NOT EXISTS Boss (
	id serial PRIMARY KEY,
	name_boss varchar(40) NOT NULL,
	department_id int REFERENCES Department(id)
);


CREATE TABLE IF NOT EXISTS Worker (
	id serial PRIMARY KEY,
	name_worker varchar(40) NOT NULL,
	surname_worker varchar(40) NOT NULL,
	boss_id int REFERENCES Boss (id),
	department_id int REFERENCES Department (id)
);

