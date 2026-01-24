# all seeding code taken from https://woteq.com/how-to-build-a-torrent-seeder-using-python/
import libtorrent as lt # pip install python-libtorrent
import time
import os
import re
print("This marks you as a seeder for your Swffy server instead of other users. Other users can and will still be used if available, but this guarentees a download via torrent.")
print("This loops forever until ctrl+c'd and may slow down your server.")
print("You also have to restart the script for every new torrent file made. This is not done automatically!")
tpp = input("Input the path where your torrent files are stored (db/torrents): ")
swfpp = input("Input the path where your swf files are stored (db/swf): ")
ses = lt.session()
ses.listen_on(6881, 6891)
tpath = os.listdir(tpp)
spath = os.listdir(swfpp)
print(spath)
while True:
    for item in tpath:
        torrent_file = item
        save_path = f"{swfpp}/"
        info = lt.torrent_info(f"{tpp}/{torrent_file}")
        params = {
            'ti': info,
            'save_path': save_path,
            'storage_mode': lt.storage_mode_t.storage_mode_sparse,
        }
        handle = ses.add_torrent(params)