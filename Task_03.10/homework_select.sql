
-- название и год выхода альбомов, вышедших в 2018 году;

select name_album, year from albums
where "year" = '2018'


-- название и продолжительность самого длительного трека;

select name_song, size_time from songs
order by size_time desc
limit 1

-- название треков, продолжительность которых не менее 3,5 минуты;

select name_song, size_time from songs
where size_time > '00:03:30'

-- названия сборников, вышедших в период с 2018 по 2020 год включительно;

select name_collection, year from collection
where year >= 2018 and year <= 2020

-- исполнители, чье имя состоит из 1 слова;

select name_musician from musician
where name_musician not LIKE '% %'

-- название треков, которые содержат слово "мой"/"my".

select name_song from songs
where name_song LIKE '%My%' or name_song like '%мой%'





