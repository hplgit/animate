import sys, os

def load(command_file):
    shfile = open(command_file, 'r')
    orig_lines = shfile.readlines()
    shfile.close()
    lines = []  # concatenate lines in orig_lines that end with \
    while orig_lines:
        line = orig_lines.pop(0).rstrip()  # strip '\n' away
        # Drop blank lines (rstrip results in '' if blank line)
        if not line:
            continue
        lines.append(line)
        while line.endswith('\\'):
            lines[-1] = lines[-1][:-1]  # don't include \
            line = orig_lines.pop(0).rstrip()
            lines[-1] += line
    return lines

def system(cmd):
    print cmd
    if cmd.startswith('cd '):
        os.chdir(cmd.split()[1])
        return
    failure = os.system(cmd)
    if failure:
        print 'error in execution of\n', cmd
        sys.exit(1)

def execute(lines, first_line_to_execute):
    for i in range(first_line_to_execute, len(lines)):
        print 'executing line', i
        system(lines[i])

if __name__ == '__main__':
    try:
        command_file = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        print 'Usage: %s command_file first_line_to_execute | list' % \
              sys.argv[0]
        sys.exit(1)
    lines = load(command_file)
    if arg2 == 'list':
        for i, line in enumerate(lines):
            print i, line
    else:
        first_line_to_execute = int(arg2)
        execute(lines, first_line_to_execute)


