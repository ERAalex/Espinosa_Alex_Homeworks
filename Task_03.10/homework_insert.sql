
-- 5 genre

insert into genre (name_genre)
values ('rock')

insert into genre (name_genre)
values ('classic')

insert into genre (name_genre)
values ('pop')

insert into genre (name_genre)
values ('rock-n-roll')

insert into genre (name_genre)
values ('metall')


-- 8 musicians

insert into musician (name_musician)
values ('Lady Gaga')

insert into musician (name_musician)
values ('Imagine Dragons')

insert into musician (name_musician)
values ('The Rolling Stones')

insert into musician (name_musician)
values ('The Beatles')

insert into musician (name_musician)
values ('Led Zepellin')

insert into musician (name_musician)
values ('Mozart')

insert into musician (name_musician)
values ('Queen')

insert into musician (name_musician)
values ('Pink Floyd')


-- connection - genre_musician

insert into genre_musician (genre_id, musician_id)
values (1, 2)

insert into genre_musician (genre_id, musician_id)
values (1, 9)

insert into genre_musician (genre_id, musician_id)
values (1, 6)

insert into genre_musician (genre_id, musician_id)
values (2, 8)

insert into genre_musician (genre_id, musician_id)
values (3, 1)

insert into genre_musician (genre_id, musician_id)
values (4, 10)

insert into genre_musician (genre_id, musician_id)
values (5, 7)

insert into genre_musician (genre_id, musician_id)
values (1, 5)


-- 8 albums

insert into albums (name_album, year)
values ('Only One', 2007)

insert into albums (name_album, year)
values ('Take my to the Future', 1998)

insert into albums (name_album, year)
values ('The sign of winter', 1780)

insert into albums (name_album, year)
values ('Pop in your life', 2020)

insert into albums (name_album, year)
values ('Just do it', 2017)

insert into albums (name_album, year)
values ('Some road', 2018)

insert into albums (name_album, year)
values ('Texas', 2001)

insert into albums (name_album, year)
values ('Hands Up', 1996)




-- connection - musician_album

insert into musician_album (musician_id, albums_id)
values (8, 3)


insert into musician_album (musician_id, albums_id)
values (7, 1)


insert into musician_album (musician_id, albums_id)
values (6, 2)


insert into musician_album (musician_id, albums_id)
values (5, 4)


insert into musician_album (musician_id, albums_id)
values (9, 5)


insert into musician_album (musician_id, albums_id)
values (10, 6)


insert into musician_album (musician_id, albums_id)
values (2, 7)


insert into musician_album (musician_id, albums_id)
values (1, 8)





-- 15 Tracks


insert into songs (name_song, size_time, album_id)
values ('Takes', '00:02:30', 3)


insert into songs (name_song, size_time, album_id)
values ('Hello World', '00:02:12', 3)


insert into songs (name_song, size_time, album_id)
values ('Jimmy T', '00:01:55', 1)


insert into songs (name_song, size_time, album_id)
values ('Man in Black', '00:02:34', 1)


insert into songs (name_song, size_time, album_id)
values ('Key to you heart', '00:01:23', 2)


insert into songs (name_song, size_time, album_id)
values ('Stay at home', '00:01:55', 2)


insert into songs (name_song, size_time, album_id)
values ('Winter comming', '00:01:55', 4)


insert into songs (name_song, size_time, album_id)
values ('Some news', '00:02:34', 4)


insert into songs (name_song, size_time, album_id)
values ('Fifty one', '00:01:34', 5)


insert into songs (name_song, size_time, album_id)
values ('Serials', '00:02:32', 5)


insert into songs (name_song, size_time, album_id)
values ('Don"t go', '00:02:44', 6)


insert into songs (name_song, size_time, album_id)
values ('My family time', '00:02:12', 6)


insert into songs (name_song, size_time, album_id)
values ('Be happy', '00:01:36', 7)


insert into songs (name_song, size_time, album_id)
values ('Underwatter', '00:01:54', 8)

insert into songs (name_song, size_time, album_id)
values ('Hey hop-p-ppi po', '00:01:44', 8)





-- 8 Collections


insert into collection (name_collection, year)
values ('art collection', 2021)


insert into collection (name_collection, year)
values ('rock collection', 2022)

insert into collection (name_collection, year)
values ('denisty collection', 2014)

insert into collection (name_collection, year)
values ('just fine collection', 2017)

insert into collection (name_collection, year)
values ('new collection', 2019)

insert into collection (name_collection, year)
values ('foreign singers collection', 2015)

insert into collection (name_collection, year)
values ('Jimmy T collection', 2001)

insert into collection (name_collection, year)
values ('Enigma collection', 1998)



-- connection - collection_songs


insert into collections_songs (collections_id, songs_id)
values (1, 8)

insert into collections_songs (collections_id, songs_id)
values (2, 7)

insert into collections_songs (collections_id, songs_id)
values (3, 6)

insert into collections_songs (collections_id, songs_id)
values (4, 5)

insert into collections_songs (collections_id, songs_id)
values (5, 4)

insert into collections_songs (collections_id, songs_id)
values (6, 3)

insert into collections_songs (collections_id, songs_id)
values (7, 2)

insert into collections_songs (collections_id, songs_id)
values (8, 1)

--
insert into collections_songs (collections_id, songs_id)
values (1, 15)

insert into collections_songs (collections_id, songs_id)
values (2, 14)

insert into collections_songs (collections_id, songs_id)
values (3, 13)

insert into collections_songs (collections_id, songs_id)
values (4, 12)

insert into collections_songs (collections_id, songs_id)
values (6, 11)

insert into collections_songs (collections_id, songs_id)
values (7, 10)

insert into collections_songs (collections_id, songs_id)
values (8, 9)





-- TASK 2

-- department creating

insert into department (name_depart)
values ('ecnomy')

insert into department (name_depart)
values ('it-develpment')

insert into department (name_depart)
values ('marketing')



-- boss creating

insert into boss (name_boss, department_id)
values ('Jim Raynor', 1)

insert into boss (name_boss, department_id)
values ('Steve Maison', 2)

insert into boss (name_boss, department_id)
values ('Tommy Tims', 3)




-- workers creating


insert into worker (name_worker, surname_worker, boss_id, department_id)
values ('Samuel', 'Black', 1, 1)

insert into worker (name_worker, surname_worker, boss_id, department_id)
values ('Maria', 'Laser', 3, 3)


insert into worker (name_worker, surname_worker, boss_id, department_id)
values ('Frank', 'Moseos', 1, 1)

insert into worker (name_worker, surname_worker, boss_id, department_id)
values ('Jack', 'Richard', 2, 2)

insert into worker (name_worker, surname_worker, boss_id, department_id)
values ('Avan', 'Jons', 3, 3)

insert into worker (name_worker, surname_worker, boss_id, department_id)
values ('Liza', 'Smith', 2, 2)

