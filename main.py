import os
import re
folders = ['photos','stickers','files','video_files','round_video_messages']

directory = os.getcwd()



def delete_thumbs(directory, folder):
    for filename in os.listdir(os.path.join(directory,folder)):
        f = os.path.join(directory, folder, filename)
        if os.path.isfile(f) and os.path.splitext(f)[0].endswith('_thumb') or re.search('_thumb|_thumb([1-9])',os.path.splitext(f)[0]):
            os.remove(f)
            print('[+] Deleted - ',os.path.basename(f))

    print(f'[+] {folder} done.')


if __name__ == '__main__':
    for folder in folders:
        if os.path.exists(os.path.join(directory,folder)):
            delete_thumbs(directory,folder)
    os.remove(os.path.join(directory,'main.py'))
    print('[+] Script deleted.')