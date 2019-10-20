# Ideas

## 19.10.2019
- note keeping tool
    - command line tool to keep notes:
        - send command line to a file
        - records date and time
        - add a description
        - add tags (*)
        - ~~add folder (#)~~ -might be unnecessary
        - search for notes on command line, by tag, folder or date 

    - gui to display at file
        - filter by tags
        - filter by date
        - add notes
        - markdown support (render and write)

    - send files to git wiki

    - tech-stack:
        - cmd tool:
            - python, C 
            - cmd args library
            - database connector
        - gui tool:
            - ~~kotlin, tornadofx~~
            - webapp, angular, spring
        - db:
            - relational, **nosql**
            - full blown or lightweight?
    
    - questions:
        - markdown rendering
        - git wiki handling

    - thoughts:
        - store notes directly in db 
        - export to markdown
        - have different services?
        - db service
        - rest-api to connect to db and expose data
        - cmd-line tool connects to rest-api service (sends and retrieves data)
        - gui tool connects to rest-api service (sends and retrieves data)

    - MVP:
        - command line tool
        - send notes to md file
        - display date, time, description and tags


>minimalist example of file layout:  
>> 19.10.2019 17:04 - #cmd *youtube-dl, audio  
youtube-dl -x --audio-quality 1 --audio-format mp3 \<url to song>  
-- downloads a video and extracts the audio stream to mp3 in high quality

>example of cmd line:
>>notes youtube-dl -x --audio-quality 1 --audio-format mp3 \<url to song> -f cmd -t youtube-dl -t audio
---














