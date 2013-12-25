# Identical code exists in scitools.easyviz.movie.html_movie and in
# doconce.DocWriter.html_movie

import re

def html_movie(plotfiles, interval_ms=300, width=800, height=600,
               casename='movie'):
    """
    Takes a list plotfiles which should be for example of the form::

        ['frame00.png', 'frame01.png', ... ]

    where each string should be the name of an image file and they should be
    in the proper order for viewing as an animation.

    The result is html text strings that incorporate javascript to
    loop through the plots one after another.  The html text also features
    buttons for controlling the movie.
    The parameter iterval_ms is the time interval between loading
    successive images and is in milliseconds.

    The width and height parameters do not seem to have any effect
    for reasons not understood.

    The following strings are returned: header, javascript code, form
    with movie and buttons, and footer. Concatenating these strings
    and dumping to an html file yields a kind of movie file to be
    viewed in a browser. The images variable in the javascript code
    is unique for each movie, because it is annotated by the casename
    string, so several such javascript sections can be used in the
    same html file. If casename is just 'movie', the name of the plot
    files is used as casename.

    This function is based on code written by R. J. LeVeque, based on
    a template from Alan McIntyre.
    """
    # Alternative method:
    # http://stackoverflow.com/questions/9486961/animated-image-with-javascript
    import os
    if not isinstance(plotfiles, (tuple,list)):
        raise TypeError('html_movie: plotfiles=%s of wrong type %s' %
                        (str(plotfiles), type(plotfiles)))
    # Check that the plot files really exist
    missing_files = [fname for fname in plotfiles if not os.path.isfile(fname)]
    if missing_files:
        raise ValueError('Missing plot files: %s' % str(missing_files)[1:-1])

    filestem, ext = os.path.splitext(plotfiles[0])
    if ext == '.png' or ext == '.jpg' or ext == '.jpeg' or ext == 'gif':
        pass
    else:
        raise ValueError('Plotfiles (%s, ...) must be PNG, JPEG, or GIF files with '\
                         'extension .png, .jpg/.jpeg, or .gif' % plotfiles[0])
    if casename == 'movie' : # default
        # Make a valid variable name for Javascript out of filestem
        filestem = re.sub(r'_?\d+\.', '', filestem)
        filestem = filestem.replace('/', '_')
        for c in """ ,.[]{}\\"'^&%$#@!=|?""":
            filestem = filestem.replace(c, '')
        casename = filestem

    header = """\
<html>
<head>
</head>
<body>
"""
    no_images = len(plotfiles)
    jscode = """
<script language="Javascript">
<!---
var num_images_%(casename)s = %(no_images)d;
var img_width_%(casename)s = %(width)d;
var img_height_%(casename)s = %(height)d;
var interval_%(casename)s = %(interval_ms)d;
var images_%(casename)s = new Array();

function preload_images_%(casename)s()
{
   t = document.getElementById("progress");
""" % vars()

    i = 0
    for fname in plotfiles:
        jscode += """
   t.innerHTML = "Preloading image ";
   images_%(casename)s[%(i)s] = new Image(img_width_%(casename)s, img_height_%(casename)s);
   images_%(casename)s[%(i)s].src = "%(fname)s";
        """ % vars()
        i = i+1
    jscode += """
   t.innerHTML = "";
}

function tick_%(casename)s()
{
   if (frame_%(casename)s > num_images_%(casename)s - 1)
       frame_%(casename)s = 0;

   document.name_%(casename)s.src = images_%(casename)s[frame_%(casename)s].src;
   frame_%(casename)s += 1;
   tt = setTimeout("tick_%(casename)s()", interval_%(casename)s);
}

function startup_%(casename)s()
{
   preload_images_%(casename)s();
   frame_%(casename)s = 0;
   setTimeout("tick_%(casename)s()", interval_%(casename)s);
}

function stopit_%(casename)s()
{ clearTimeout(tt); }

function restart_%(casename)s()
{ tt = setTimeout("tick_%(casename)s()", interval_%(casename)s); }

function slower_%(casename)s()
{ interval_%(casename)s = interval_%(casename)s/0.7; }

function faster_%(casename)s()
{ interval_%(casename)s = interval_%(casename)s*0.7; }

// --->
</script>
""" % vars()
    plotfile0 = plotfiles[0]
    form = """
<form>
&nbsp;
<input type="button" value="Start movie" onClick="startup_%(casename)s()">
<input type="button" value="Pause movie" onClick="stopit_%(casename)s()">
<input type="button" value="Restart movie" onClick="restart_%(casename)s()">
&nbsp;
<input type="button" value="Slower" onClick="slower_%(casename)s()">
<input type="button" value="Faster" onClick="faster_%(casename)s()">
</form>

<p><div ID="progress"></div></p>
<img src="%(plotfile0)s" name="name_%(casename)s" border=2/>
""" % vars()
    footer = '\n</body>\n</html>\n'
    return header, jscode, form, footer

def main():
    import sys
    try:
        plotfiles = sys.argv[1:]
    except IndexError:
        print 'Usage: %s plotfiles' % sys.arg[0]
        print 'plotfiles is a Unix wildcard description, e.g., frame_*.png'
        sys.exit(1)

    plotfiles.sort()
    header, jscode, form, footer = html_movie(plotfiles)
    print header
    print jscode
    print form
    print footer

if __name__ == '__main__':
    main()
