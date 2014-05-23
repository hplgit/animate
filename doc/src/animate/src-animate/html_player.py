# Identical code exists in scitools.easyviz.movie.html_movie and in
# doconce.DocWriter.html_movie

def html_movie(plotfiles, interval_ms=300, width=800, height=600,
               casename=None):
    """
    Takes a list plotfiles, such as::

        'frame00.png', 'frame01.png', ...

    and creates javascript code for animating the frames as a movie in HTML.

    The `plotfiles` argument can be of three types:

      * A Python list of the names of the image files, sorted in correct
        order. The names can be filenames of files reachable by the
        HTML code, or the names can be URLs.
      * A filename generator using Unix wildcard notation, e.g.,
        ``frame*.png`` (the files most be accessible for the HTML code).
      * A filename generator using printf notation for frame numbering
        and limits for the numbers. An example is ``frame%0d.png:0->92``,
        which means ``frame00.png``, ``frame01.png``, ..., ``frame92.png``.
        This specification of `plotfiles` also allows URLs, e.g.,
        ``http://mysite.net/files/frames/frame_%04d.png:0->320``.

    If `casename` is None, a casename based on the full relative path of the
    first plotfile is used as tag in the variables in the javascript code
    such that the code for several movies can appear in the same file
    (i.e., the various code blocks employ different variables because
    the variable names differ).

    The returned result is text strings that incorporate javascript to
    loop through the plots one after another.  The html text also features
    buttons for controlling the movie.
    The parameter `iterval_ms` is the time interval between loading
    successive images and is in milliseconds.

    The `width` and `height` parameters do not seem to have any effect
    for reasons not understood.

    The following strings are returned: header, javascript code, form
    with movie and buttons, footer, and plotfiles::

       header, jscode, form, footer, plotfiles = html_movie('frames*.png')
       # Insert javascript code in some HTML file
       htmlfile.write(jscode + form)
       # Or write a new standalone file that act as movie player
       filename = plotfiles[0][:-4] + '.html'
       htmlfile = open(filename, 'w')
       htmlfile.write(header + jscode + form + footer)
       htmlfile.close

    This function is based on code written by R. J. LeVeque, based on
    a template from Alan McIntyre.
    """
    # Alternative method:
    # http://stackoverflow.com/questions/9486961/animated-image-with-javascript

    # Start with expanding plotfiles if it is a filename generator
    if not isinstance(plotfiles, (tuple,list)):
        if not isinstance(plotfiles, (str,unicode)):
            raise TypeError('plotfiles must be list or filename generator, not %s' % type(plotfiles))

        filename_generator = plotfiles
        if '*' in filename_generator:
            # frame_*.png
            if filename_generator.startswith('http'):
                raise ValueError('Filename generator %s cannot contain *; must be like http://some.net/files/frame_%%04d.png:0->120' % filename_generator)

            plotfiles = glob.glob(filename_generator)
            if not plotfiles:
                raise ValueError('No plotfiles on the form' %
                                 filename_generator)
            plotfiles.sort()
        elif '->' in filename_generator:
            # frame_%04d.png:0->120
            # http://some.net/files/frame_%04d.png:0->120
            p = filename_generator.split(':')
            filename = ':'.join(p[:-1])
            if not re.search(r'%0?\d+', filename):
                raise ValueError('Filename generator %s has wrong syntax; missing printf specification as in frame_%%04d.png:0->120' % filename_generator)
            if not re.search(r'\d+->\d+', p[-1]):
                raise ValueError('Filename generator %s has wrong syntax; must be like frame_%%04d.png:0->120' % filename_generator)
            p = p[-1].split('->')
            lo, hi = int(p[0]), int(p[1])
            plotfiles = [filename % i for i in range(lo,hi+1,1)]

    # Check that the plot files really exist, if they are local on the computer
    if not plotfiles[0].startswith('http'):
        missing_files = [fname for fname in plotfiles
                         if not os.path.isfile(fname)]
        if missing_files:
            raise ValueError('Missing plot files: %s' %
                             str(missing_files)[1:-1])

    if casename is None:
        # Use plotfiles[0] as the casename, but remove illegal
        # characters in variable names since the casename will be
        # used as part of javascript variable names.
        casename = os.path.splitext(plotfiles[0])[0]
        # Use _ for invalid characters
        casename = re.sub('[^0-9a-zA-Z_]', '_', casename)
        # Remove leading illegal characters until we find a letter or underscore
        casename = re.sub('^[^a-zA-Z_]+', '', casename)

    filestem, ext = os.path.splitext(plotfiles[0])
    if ext == '.png' or ext == '.jpg' or ext == '.jpeg' or ext == 'gif':
        pass
    else:
        raise ValueError('Plotfiles (%s, ...) must be PNG, JPEG, or GIF files with '\
                         'extension .png, .jpg/.jpeg, or .gif' % plotfiles[0])

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
    return header, jscode, form, footer, plotfiles


def main():
    import sys
    try:
        plotfiles = sys.argv[1:]
    except IndexError:
        print 'Usage: %s plotfiles' % sys.arg[0]
        print 'plotfiles is a Unix wildcard description, e.g., frame_*.png'
        sys.exit(1)

    plotfiles.sort()
    header, jscode, form, footer, plotfiles = html_movie(plotfiles)
    print header
    print jscode
    print form
    print footer

if __name__ == '__main__':
    main()
