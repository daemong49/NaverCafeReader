# -*- coding: utf-8 -*-


from time import time
import base64
import uuid
import hmac
import hashlib
import urllib, urllib2


CONSUMER_KEY='5GTmwzXm9s8TxDEVX5L9'
CONSUMER_SECRET_KEY = 'vyfJVXmdbE'


def make_signature(key, param):
    hashed = hmac.new(key, param, hashlib.sha1).digest()
    b = base64.encodestring(hashed)
    b = b.rstrip()
    b = urllib.quote_plus(b.encode('utf8'))
    return b


def generate_url():
    url='https://nid.naver.com/naver.oauth'
    timestamp = str(int(time()))
    nonce = base64.b32encode(uuid.uuid4().bytes).lower().replace('=', '')

    param = 'GET&' + urllib.quote_plus(url)
    param += '&oauth_callback=oob'
    param += '&oauth_consumer_key=' + CONSUMER_KEY
    param += '&oauth_nonce=' + nonce
    param += '&oauth_signature_method=HMAC-SHA1'
    param += '&oauth_timestamp=' + timestamp
    param += '&oauth_version=1.0a'

    param = urllib.quote_plus(param)
    print param

    signature = make_signature(CONSUMER_SECRET_KEY, param)
    print signature

    request_url = url + '?mode=req_req_token'
    request_url += '&oauth_callback=oob'
    request_url += '&oauth_consumer_key=' + CONSUMER_KEY
    request_url += '&oauth_nonce=' + nonce
    request_url += '&oauth_signature=' + signature
    request_url += '&oauth_signature_method=HMAC-SHA1'
    request_url += '&oauth_timestamp=' + timestamp
    request_url += '&oauth_version=1.0a'

    print request_url


    response = urllib2.urlopen(request_url)
    data = response.read()

    print data

generate_url()

