select albums.Title as "Album name",
	genres.Name as "Genre",
	artists.Name as "Artist or Group",
	round((sum(tracks.Milliseconds) / 60000), 2) as "Duration (Minuts)",
	round(sum(tracks.Bytes / 1000000), 2) as "Size (Mb)",
	sum(tracks.UnitPrice) as "Album price",
	count(*) as "Count tracks"
from tracks
	join albums on tracks.AlbumId = albums.AlbumId
	join artists on albums.ArtistId = artists.ArtistId
	join genres on tracks.GenreId = genres.GenreId
	join media_types on tracks.MediaTypeId = media_types.MediaTypeId
where media_types.Name = "MPEG audio file"
group by albums.Title
order by genres.Name, artists.Name;