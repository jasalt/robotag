    WARNING broken code & landmines ahead

Proof of concept utility for enforcing user customizable tag hierarchy on a social bookmarking service Diigo data. This makes the tag-based datastorage more easily searchable and allows faster tagging by automated tag expansion.

Eg. bookmark with tags `flask` gets tagged `python`, `web` and `programming` automatically.

Multiplatform free but not open source [Yed Graph Editor](https://www.yworks.com/products/yed) is used for generating hierarchy schema in [graphml-format](http://graphml.graphdrawing.org/) that is readed by [Python NetworkX library](https://networkx.github.io/). [NetworkX](https://networkx.github.io/) then compares exported user bookmark json-file to a given graphml-schema and updates missing tags accordingly.

## [Video demo on Youtube](https://www.youtube.com/watch?v=d8GXXdiA__I)
[![Youtube Demo Video](https://raw.github.com/jasalt/robotag/master/diigo/misc/demo.gif)](https://www.youtube.com/watch?v=d8GXXdiA__I)

# Workflow
Export diigo bookmarks into a json file.

    python diigo/diigo-backup/diigo-backup.py -v 0 -u jasalt -a <APIKEY> -p <PASSWORD>  > jasalt.json
    
Search for missing tags and update them.

    python diigo/process.py
    
* [x] Build a hierarchy graph
* [x] Add missing tags via API
* [ ] Schedule with Cron

# Misc Notes
## Official Diigo API 
[Documentation](https://www.diigo.com/api_dev) is sloppy

* https://secure.diigo.com/api/v2/
* Update works by adding item with the same url via POST. 
* Annotations and created_at stay in place. 
* Rate limit is said to be 1 per second / apikey.

## Diigo Android API reverse engineering notes
### mitmproxy usage (Linux Mint 17.3)
sudo apt-get install python-libxml2 python-libxslt1 libxslt-dev libssl-dev
sudo apt-get --reinstall install python-pyasn1 python-pyasn1-modules


sudo mv /usr/lib/python2.7/dist-packages/OpenSSL /usr/lib/python2.7/dist-packages/OpenSSL.bak

sudo pip install mitmproxy ipaddress hyperframe hpack


sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 8080

### POST request
  2016-02-14 22:44:42 POST https://www.diigo.com/kree/pv=1/ct=android?cmd=uploadItems
    ← 200 text/plain 869B 342ms
     Request Response Detail
     Content-Length:  789                                                                                    Content-Type:    multipart/form-data; boundary=_rOLSsCYOdWelPxfc2eehGr-8IIGhUWhkBVsK2Ew                     host:            www.diigo.com                                                                              Connection:      Keep-Alive                                                                                 Cookie:          diigoandlogincookie=android-.-jasalt-.-android; CHKIO=71b7adf639c8a4e01fcff0c6a0206e5b; smasher_session=7d92765d79928b26be5d2f3a27a22342                                  
    
    Multipart form                                                                                                 [m:Auto]
    Form data:

    json: {"items":[{"cmd":2,"local_updated_at":1455482683,"local_created_at":1453102588,"desc":"","url":"https://shaunlebron.github.io/parinfer/","server_id":294257937,"outliners_id":[],"folder_server_id":[],"server_created_at":1453102588,"title":"Parinfer - simpler Lisp editing","mode":2,"server_updated_at":1453102588,"tags":"clojure,lisp,\"text editor\",ide,programming","type":3,"local_id":377,"unread":0}]}
    cv:   3.2.1


## Matplotlib
Install matplotlib from apt and symlink from dist-packages to virtualenv site-packages.

    sudo apt-get install python3-matplotlib
    ln -s /usr/lib/python3/dist-packages/matplotlib ~/.virtualenvs/diigo/lib/python3.4/site-package
    ln -s /usr/lib/python3/dist-packages/dateutil ~/.virtualenvs/diigo/lib/python3.4/site-packagess
    pip install pyparsing numpy

