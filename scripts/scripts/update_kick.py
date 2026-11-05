#!/usr/bin/env python3
"""Fetch Kick stream state via the official Kick API. Never output access tokens."""
import json, os, sys, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'data' / 'kick-status.json'

def request(url, *, payload=None, token=None):
    headers={'User-Agent':'WrenchxooSite/1.0', 'Accept':'application/json'}
    if payload is not None: headers['Content-Type']='application/x-www-form-urlencoded'
    if token: headers['Authorization']='Bearer '+token
    req=urllib.request.Request(url,data=payload,headers=headers)
    with urllib.request.urlopen(req,timeout=20) as resp:
        return json.load(resp)

def main():
    result={'channel':'wrenchxoo','status':'unknown','checked_at':None}
    client_id=os.getenv('KICK_CLIENT_ID','').strip()
    client_secret=os.getenv('KICK_CLIENT_SECRET','').strip()
    if client_id and client_secret:
        try:
            payload=urllib.parse.urlencode({'grant_type':'client_credentials','client_id':client_id,'client_secret':client_secret}).encode()
            auth=request('https://id.kick.com/oauth/token',payload=payload)
            access_token=auth['access_token']
            channel=request('https://api.kick.com/public/v1/channels?slug=wrenchxoo',token=access_token)
            records=channel.get('data',[]) if isinstance(channel,dict) else []
            row=next((r for r in records if r.get('slug','').lower()=='wrenchxoo'),None)
            if row is None: raise ValueError('Kick channel missing from response')
            stream=row.get('stream') or {}
            if not isinstance(stream.get('is_live'),bool):raise ValueError('Kick live state unavailable')
            result['status']='live' if stream['is_live'] else 'offline'
            result['checked_at']=datetime.now(timezone.utc).isoformat()
        except Exception as ex:
            print('Kick check failed:',type(ex).__name__,file=sys.stderr)
    else:
        print('Kick Secrets not configured; writing unknown state')
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Kick state:',result['status'])

if __name__=='__main__':main()
