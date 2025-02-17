# basketball_highlight_generator_v1
Generate basketball highlights automatically, a joint hackathon project with the
Haggerston Bball Crew.

# Setup the venv

```
$ python3 -m venv venv
```

Make sure you 'source' the appropriate 'activate' binary.

# Pip install required packages

```
$ pip install ultralytics
```

# Cutting videos down with ffmpeg

Cut videos down using ffmpeg (can also be used to reduce framerate).

```
$ ffmpeg -ss 00:10:00 -t 00:05:00 -i C0012.MP4 -c:v copy C0012_5mins.MP4
```

The `C0012_10sec.MP4` file is only around 500 frames and can be found in Albert's
google drive:

https://drive.google.com/drive/folders/166tjGMwNxX0GpwX1paxEbDBFdFWgG9Ji


# Run Yolov8 Python Script:

```
(venv) $ python try_run_yolov.py
```


# Stitching result images together back into a video with ffmpeg

Imagine the results look like:
result_0000.jpg
result_0001.jpg
result_0002.jpg
etc...

ffmpeg can stich together a video using the incantation:

```
$ ffmpeg -i result_%04d.jpg video_name.mp4
```

# Resources

https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode