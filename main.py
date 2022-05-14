import os



directory = os.getcwd()

def deleting(directory, folder):
    for filename in os.listdir(os.path.join(directory,folder)):
        f = os.path.join(directory, folder, filename)
        if os.path.isfile(f) and os.path.splitext(f)[0].endswith('_thumb') or os.path.splitext(f)[0].endswith('(1)') or os.path.splitext(f)[0].endswith('(2)') or os.path.splitext(f)[0].endswith('(3)') or os.path.splitext(f)[0].endswith('(4)'):
            os.remove(f)
            print('[+] Deleted - ',os.path.basename(f))

    print(f'[+] {folder} done.')


# -----------------------------------------------------------------------------
#   you need to move this file to export chat folder and start using cmd or ide
# -----------------------------------------------------------------------------
            

def main():
    
    # for photos

    if os.path.exists(os.path.join(directory,'photos')):
        deleting(directory,'photos')

    # for stickers

    if os.path.exists(os.path.join(directory,'stickers')):
        deleting(directory,'stickers')

    # for files

    if os.path.exists(os.path.join(directory,'files')):
        deleting(directory,'files')
    
    # for videos

    if os.path.exists(os.path.join(directory,'video_files')):
        deleting(directory,'video_files')
    
    # for round videos

    if os.path.exists(os.path.join(directory,'round_video_messages')):
        deleting(directory,'round_video_messages')
    

if __name__ == '__main__':
    main()
    os.remove(os.path.join(directory,'main.py'))
    print('[+] Script deleted.')