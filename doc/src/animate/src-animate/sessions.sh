# Shell session for various movie making commands
cd testfiles
frames=frames
movie=movie1
rm -rf ${movie}*  # clean up

# convert (use just a subset of the frames on small machines, otherwise
# the file takes a long time to produce and becomes very big)
subset_of_files=`/bin/ls $frames/frame_0[0-1]*.png`
convert -delay 8 $subset_of_files $movie.gif

# ffmpeg and avconv
programs="ffmpeg avconv"
for prog in $programs; do
$prog -i $frames/frame_%04d.png -r 12 -vcodec libx264   ${movie}_$prog.mp4
$prog -i $frames/frame_%04d.png -r 12 -vcodec libvpx    ${movie}_$prog.webm
$prog -i $frames/frame_%04d.png -r 12 -vcodec libtheora ${movie}_$prog.ogg
$prog -i $frames/frame_%04d.png -r 12 -vcodec flv       ${movie}_$prog.flv
done

# javascript code
python ../html_player.py $frames/frame_0*.png > ${movie}.html

# mencoder...

