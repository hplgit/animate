#!/bin/sh
# Examples on movie making with ffmpeg and avconv

# Problem: -x264opts  is not recognized
#ffmpeg -i frames/frame_%04d.png -vcodec libx264 keyint=12 -r 12 movie1.mp4
#avconv -i frames/frame_%04d.png -vcodec libx264 -x264opts keyint=12 -r 12 movie1.mp4

# Problem: "Unable to find a suitable output format for keyint=12"
# (keyint is needed for effective searching within the movie)
#ffmpeg -i frames/frame_%04d.png keyint=12 -r 12 movie1.mp4

# This one works and applies the encoder Lavf53.21.1
ffmpeg -i frames/frame_%04d.png -r 12 movie1.mp4
# Problem 1: low quality with some red mirror line and the
# curve is in black instead of red as in the plotfile
# Problem 2: will not play in HTML5

# This one works
ffmpeg -i frames/frame_%04d.png -r 12 -vcodec libx264 movie1.mp4
# Problem 1: low quality with some red mirror line and the
# curve is in black instead of red as in the plotfile
# Problem 2: Does not recognize libx264 (but at some point it did!)
# Plays in HTML5

# Can convert from .mp4 to .ogg
ffmpeg -i movie1.mp4 movie1.ogg
# Works fine in HTML

# This one works but applies the encoder Lavf53.21.1
ffmpeg -i frames/frame_%04d.png -r 12 -acodec libvorbis -vcodec libtheora movie1.ogg
# Problem: same low quality as the one above i mplayer, but fine in vlc
# Works fine in HTML5
# Seems to give identical movie to the command without codec specification:
#ffmpeg -i frames/frame_%04d.png -r 12 movie1.ogg

# Replacing ffmpeg by avconv gives (exactly?) the same output
#avconv -i frames/frame_%04d.png -r 12 movie1.ogg

# This one works but applies the encoder Lavf53.21.1
ffmpeg -i frames/frame_%04d.png -r 12 -acodec libvorbis -vcodec libvpx movie1.webm
# Problem: mplayer and vlc show the disturbing mirrored red line and the
# curve is in black instead of red as in the plotfile
# totem and gxine work fine (perfect red curve)

# Flash
ffmpeg -i frames/frame_%04d.png -r 12 -vcodec flv movie1.flv
# Same problem with red mirror line as the ones above