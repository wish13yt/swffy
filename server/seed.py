# all seeding code taken from https://woteq.com/how-to-build-a-torrent-seeder-using-python/
# NOTICE: even legal torrents can be illegal in some places! please make sure you won't get arrested for it, but if you do get arrested for some reason, we are not liable
# this is your warning! I am not liable
import libtorrent as lt # pip install python-libtorrent
import time
import os
import re
print("This marks you as a seeder for your Swffy server instead of other users. Other users can and will still be used if available, but this guarentees a download via torrent.")
print("This loops forever until ctrl+c'd and may slow down your server.")
print("You also have to restart the script for every new torrent file made. This is not done automatically!")
tpp = input("Input the path where your torrent files are stored (default: db/torrents): ") or "db/torrents"
swfpp = input("Input the path where your swf files are stored (default: db/swf): ") or "db/swf"
try:
    ses = lt.session({'listen_interfaces': '0.0.0.0:6881,0.0.0.0:6891'})
except Exception as e:
    print(f"issue occured starting server.. ports are likely taken by something else! error: {e}")
tpath = os.listdir(tpp)
spath = os.listdir(swfpp)
print("Seeder is running!")
while True:
    try:
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
    except Exception as e:
        print(f"error! shutting down server with error {e}")