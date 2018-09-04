#!/usr/bin/python
"""
miniplay 1.0
dogan c. karatas

simple icy (shoutcast) protocol media player
(c) 2018 - Licensed with GNU GPL v3 
"""
import time, threading, os, vlc, json, requests

api_host = "http://api.radyofenomen.com/Channels/?appRef=FenomenWebV2"
update_interval = 20 # secs. default
current_channel = "Not Playing."

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def banner():
    clear()
    print "miniplay v1 // written by dogan c. karatas\nCurrent Channel: {} \
        \n\nChannel List:".format(current_channel)

def get_meta(host):
    r = requests.get(host)
    j = json.loads(r.content)
    return j
    # print json.dumps(j, indent=4)

def get_ch_list(jsonresp):
    chlist = []
    for chans in jsonresp['response']:
        chlist.append(chans['channel_seo_name'])
    return chlist

def get_ch_subjson(jsonresp, chan):
    for j in jsonresp['response']:
        if j['channel_seo_name'] == chan:
            return j

def get_ch_timeline(jsonresp, chan):
    return get_ch_subjson(jsonresp, chan)['timeline'][0]

def get_ch_url(jsonresp, chan):
    ch_url  = "" # channel url
    api_url = get_ch_subjson(jsonresp, chan)['channel_stream_url']
    # selected now has json api url
    js = get_meta(api_url)
    return js['response']['streamURL']

def dump_ch_list(jsonresp):
    for i, chan in enumerate(get_ch_list(jsonresp)):
        print u"{:3}: {:<15} | {}: {} - {}".format(i + 1, chan,
           get_ch_timeline(jsonresp, chan)['songStatus'].title(),
           get_ch_timeline(jsonresp, chan)['songTitle'],
           get_ch_timeline(jsonresp, chan)['artistTitle'])

def dump_ch_urls(jsonresp):
    # for debugging
    for i, chan in enumerate(get_ch_list(jsonresp)):
        print "{}->{}".format(chan, get_ch_url(jsonresp, chan))

def create_player(url):
    instance = vlc.Instance('--input-repeat=-1')
    player = instance.media_player_new()
    media = instance.media_new(url)
    player.set_media(media)
    player.audio_set_volume(100)
    return player

def update_meta():
    banner()
    dump_ch_list(get_meta(api_host))
    print "For help please type 'h' or '?'"
    t = threading.Timer(update_interval, update_meta)
    t.daemon = True
    t.start()

def load_ch(ch):
    global current_channel
    js = get_meta(api_host)
    chan = get_ch_list(js)
    selected = ''
    try:
        selected = chan[int(ch) - 1]
    except ValueError:
        pass

    if selected not in chan:
        print "Wrong Channel Selected."
        exit()
    current_channel = selected

    return create_player(get_ch_url(js, current_channel))

def player_controls():
    global current_channel
    banner()
    js = get_meta(api_host)
    dump_ch_list(js)
    update_meta()
    sel = raw_input("\nPlease select channel (with number or typing name)or hit CTRL+C to exit:")
    p = load_ch(sel)
    print "For help please type 'h' or '?'"
    #print json.dumps(js, indent=4)
    #p = create_player(get_ch_url(js, "radyofenomen"))
    p.play()

    while 1:
        try:
            cmd = raw_input("> ").lower()
            if cmd == "h" or cmd =="?":
                print "Help\n===\nz = stop \
                    \nx = stop and select new channel\nc = play\
                    \nv = refresh meta & clear screen\nq = quit\
		    \n[1-10] = select channel quickly\nh = help"
            # set command, e.g. set update_interval 10
            # set ...
	    elif cmd == "1":
		p.stop()
                # p = load_ch("radyofenomen")
		p = load_ch(1)
		p.play()
	    elif cmd == "2":
		p.stop()
		p = load_ch(2)
		p.play()
	    elif cmd == "3":
		p.stop()
		p = load_ch(3)
		p.play()
	    elif cmd == "4":
		p.stop()
		p = load_ch(4)
		p.play()
	    elif cmd == "5":
		p.stop()
		p = load_ch(5)
		p.play()
	    elif cmd == "6":
		p.stop()
		p = load_ch(6)
		p.play()
	    elif cmd == "7":
		p.stop()
		p = load_ch(7)
		p.play()
	    elif cmd == "8":
		p.stop()
		p = load_ch(8)
		p.play()
	    elif cmd == "9":
		p.stop()
		p = load_ch(9)
		p.play()
	    elif cmd == "10":
		p.stop()
		p = load_ch(10)
		p.play()
            elif cmd == ":q" or cmd == "q":
                print "Shutting down."
                p.stop()
                exit()
            elif cmd == "c":
                print "Playing.\n"
                p.play()
            elif cmd == "x":
                p.stop()
                clear()
                break
            elif cmd == "z":
                print "Stopped.\n"
                p.stop()
            elif cmd == "v":
                banner()
                dump_ch_list(get_meta(api_host))
                print "For help please type 'h' or '?'"
        except KeyboardInterrupt:
            p.stop()
            print "\nShutting down."
            exit()

if __name__ == "__main__":
    while 1:
        player_controls()

