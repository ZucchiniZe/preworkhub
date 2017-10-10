# Prework Hub

## Structure

(explanation of folder structure)

```
.
├── README.md           # this file
├── core                # django app that stores stuff that doesn't 
│                         fit well into other apps (in this case, classes)
├── manage.py           # file to manage everything django related
├── preworkhub          # the project root folder
│   ├── settings.py     # settings for the project
│   ├── static          # static assets go here (js, css, images)
│   ├── templates       # base and override templates here
│   ├── urls.py         # define the urls for the entire application
├── requirements.txt    # dependencies for the project
└── videos              # django app that stores all information pertaining 
                          to the prework videos
```

## Notes

All the videos are recoreded with the same aspect ratio and are uploaded to google drive so we can easily embed the
videos in the current page using the following code:

`<iframe src="https://drive.google.com/file/d/{file_id}/preview" width="770" height="480"></iframe>`

Note the width and height in the URL. A width of 770 and height of 480 makes the video be perfectly stretched to fill
the iframe.