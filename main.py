import os

directory = os.getcwd()

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f) and os.path.splitext(f)[0].endswith('_thumb'):
        os.remove(f)
        print('[DELETED] - ',os.path.basename(f))
        