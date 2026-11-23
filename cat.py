'''
This program prints stdin to the screen.
'''
import sys

CHUNK_SIZE = 8192

def cat(file):
    output = sys.stdout.buffer
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        output.write(chunk)
        output.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            try:
                with open(filename, "rb") as f:
                    cat(f)
            except FileNotFoundError:
                print(f"cat: {filename}: No such file or directory", file=sys.stderr)
                sys.exit(1)
    else:
        cat(sys.stdin.buffer)
