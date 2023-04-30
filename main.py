import subprocess

# Test if WIFI is on.
ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
try:
    output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
    print(output)
except subprocess.CalledProcessError:
    # grep did not match any lines
    print("No wireless networks connected")