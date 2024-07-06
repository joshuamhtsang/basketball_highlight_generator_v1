# basketball_highlight_generator_v1
Generate basketball highlights automatically

# Setup the venv

$ python3 -m venv venv

# Pip install required packages

$ pip install ultralytics

# Cutting videos down

$ ffmpeg -ss 00:10:00 -t 00:05:00 -i C0012.MP4 -c:v copy C0012_5mins.MP4