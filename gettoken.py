from flask import Flask, Response, jsonify, abort, make_response,  render_template, redirect, request, send_from_directory
#from faster_than_requests import requests
import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json, requests, traceback, os, lxml, re, urllib, urllib3, urllib.parse, argparse, pytz, urllib.request, time, httpx


app = Flask(__name__, static_url_path="/qrimage")

#@app.route('/')
#def home():
#    """Landing page."""
#    return render_template('FILE-HTML-LO.html')

@app.route("/impossible/<path:q>", methods=['GET', 'POST'])
def api(q):
    if q == "jz":
        ret = "Access Denied"
        return make_response(jsonify(ret))
    elif q == "arti":
        twit = request.args.get("nama", "")
        link = "http://primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(urllib.parse.quote(twit))
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        a = soup.find('div', attrs={'id':'body','class':'width'}).text
        ret = {}
        ret["result"] = a.replace("\n","").replace("Nama:ARTI NAMA (JAWA)Berikut ini adalah kumpulan arti nama lengkap dari A-Z dalam budaya (bahasa) Jawa untuk Laki-laki (L) dan Perempuan (P).Arti Nama (L) Arti Nama (P)ARTI NAMA (ARAB / ISLAM)Berikut ini adalah kumpulan arti nama lengkap dari A-Z dalam budaya (bahasa) Arab atau bernuansa Islami untuk Laki-laki (L) dan Perempuan (P).Arti Nama (L) Arti Nama (P)Catatan: Gunakan juga aplikasi numerologi Kecocokan Nama, untuk melihat sejauh mana keselarasan nama anda dengan diri anda.","")
        return make_response(jsonify(ret))

@app.route("/xs/<path:q>")
def one(q):
    if q == "xz":
        try:
            key = request.args.get("key", "")
            type = "flex"
            link = "https://api.vx6-ct.com/zodiak.php?key={}&type={}".format(key,flex)
            r = requests.get(link)
            resultdictjson = r.json()
            resultdict = resultdictjson
            return make_response(jsonify(resultdictjson))
        except Exception as error:
            return str(error)

@app.route("/xz/<path:q>")
def two(q):
    if q == "xs":
        try:
            jdl = request.args.get("search", "")
            link = "https://mnazria.herokuapp.com/api/jooxnich?search={}".format(jdl)
            r = requests.get(link)
            resultdictjson = r.json()
            resultdict = resultdictjson
            return make_response(jsonify(resultdict))
        except Exception as error:
            return resultdict

if __name__ == "__main__":
    app.run()
