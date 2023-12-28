ffmpeg -i https://pull-f5-tt01.tiktokcdn.com/game/stream-3573100610708833212_or4.flv -c copy -t 360 awe.flv

rem support m3u8 format
ffmpeg -i https://live-stream.tokopedia.net/live/v0.2/play_20231228132212_6fe94de2-a549-11ee-b02a-42010a294690/live/abr.m3u8 -c copy -t 360 tope.flv