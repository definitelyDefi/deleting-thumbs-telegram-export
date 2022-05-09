import os

directory = os.getcwd()

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f) and os.path.splitext(f)[0].endswith('_thumb') or os.path.splitext(f)[0].endswith('(1)') or os.path.splitext(f)[0].endswith('(2)') or os.path.splitext(f)[0].endswith('(3)') or os.path.splitext(f)[0].endswith('(4)'):
        os.remove(f)
        print('[+] Deleted - ',os.path.basename(f))

print('[+] Done.')
os.remove(os.path.join(directory,'main.py'))
print('[+] Script deleted.')
