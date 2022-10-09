
--1 -- количество исполнителей в каждом жанре;

select g.name_genre, COUNT(name_genre)
from genre g
join genre_musician gm on g.id = gm.genre_id
group by g.name_genre


--2 -- количество треков, вошедших в альбомы 2019-2020 годов;

select a.name_album, COUNT(name_album)
from albums a
join songs s ON s.album_id = a.id
where a.year >= 2019 and a.year <= 2020
group by a.name_album


--3 -- средняя продолжительность треков по каждому альбому;

select a.name_album, avg(s.size_time)
from albums a
join songs s ON s.album_id = a.id
group by a.name_album


--4 -- все исполнители, которые не выпустили альбомы в 2020 году;

select m.name_musician
from musician m
join musician_album ma on ma.musician_id = m.id
join albums a on a.id = ma.albums_id
where a.year != '2020'



--5 -- названия сборников, в которых присутствует конкретный исполнитель (выберите сами);

select c.name_collection
from collection c
join collections_songs cs on cs.collections_id = c.id
join songs s on cs.songs_id = s.id
join albums a on a.id = s.album_id
join musician_album ma on ma.albums_id = a.id
join musician m on m.id = ma.musician_id
where m.name_musician = 'Lady Gaga'


--6 -- название альбомов, в которых присутствуют исполнители более 1 жанра;

select a.name_album, count(m.id)
from albums a
join musician_album ma  on ma.albums_id = a.id
join musician m on m.id = ma.musician_id
join genre_musician gm on gm.musician_id = m.id
group by a.name_album
having count(m.id) > 1


--7 -- наименование треков, которые не входят в сборники;

select s.name_song
from songs s
left join collections_songs cs on s.id = cs.songs_id
group by s.name_song
having count(cs.collections_id) = 0


--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);

select m.name_musician, s.name_song, s.size_time
from songs s
join albums a on s.album_id = a.id
join musician_album ma on a.id = ma.albums_id
join musician m on ma.musician_id = m.id
where s.size_time =(select min(s.size_time) from songs s);


-- 9  -- название альбомов, содержащих наименьшее количество треков.