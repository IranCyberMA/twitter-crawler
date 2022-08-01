from urllib.parse import quote_plus
from json import loads,dumps
from requests import get
from random import uniform
from time import sleep

#get info about hashtag trend
def get_hashtag_trend(check_hashtag=True,url='https://twitter.com/i/api/2/guide.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&count=20&candidate_source=trends&include_page_configuration=false&entity_tokens=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control',c = 0,max = 0,hashtag_trend = '',meta_data = '',s_n = {'K':1000,'M':1000000,'B':1000000000,'T':1000000000000}):
    """_summary_

    Args:
        check_hashtag (bool, optional): _description_. Defaults to True.
        url (str, optional): _description_. Defaults to 'https://twitter.com/i/api/2/guide.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&count=20&candidate_source=trends&include_page_configuration=false&entity_tokens=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control'.
        c (int, optional): _description_. Defaults to 0.
        max (int, optional): _description_. Defaults to 0.
        hashtag_trend (str, optional): _description_. Defaults to ''.
        meta_data (str, optional): _description_. Defaults to ''.
        s_n (dict, optional): _description_. Defaults to {'K':1000,'M':1000000,'B':1000000000,'T':1000000000000}.

    Returns:
        _type_: _description_
    """
    request_hashtag = get(url,headers={
        'authority': 'twitter.com',
        'method': 'GET',
        'path': '/i/api/2/guide.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&count=20&candidate_source=trends&include_page_configuration=false&entity_tokens=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control',
        'scheme': 'https',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'cookie': 'guest_id_marketing=v1%3A165874291184956618; guest_id_ads=v1%3A165874291184956618; _gid=GA1.2.442816053.1658742913; _sl=1; kdt=mG35D7wI0ZboiYq51Hbl5pmYWIqEmFYDnGjYAxZx; lang=en; at_check=true; _ga_BYKEBDM7DS=GS1.1.1658748666.2.1.1658748829.0; mbox=PC#481ced069511418785f0062fe726c0b0.34_0#1721993631|session#d7fa329235614b8aa3311130b9fd5d3e#1658750691; gt=1551531244760010761; _ga=GA1.2.770637681.1658742913; att=1-ZoWqPhPCVhaB9UKHOSZMMTTNKBR4sX28QyUv4zGW; personalization_id="v1_J45Tbu7Zdg/tbwmnSmOLXQ=="; guest_id=v1%3A165874912720129752; auth_token=d9507a3a6c42aed340f24bbcdedb25c3eec32f03; ct0=652ed601b72eb0e2ccc5d9bdccb5a7058effc621d575a114af1f0b05f590c71ea55f81de390eb382e572fe90d503dc866e9e80ba750fe4a6ed47a563a70c007cb0c787fbc3e288386a3b36489a8feeeb; twid=u%3D1551532947068620800; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoHaWQiJWYwNzMyMjQ2N2ExZmVkMTA5ZTU5MDQ3%250AZTljMTVkYzM1Og9jcmVhdGVkX2F0bCsIrDk%252BNYIBOgxjc3JmX2lkIiUxYTlh%250AODgxMTc1NDYyZmI5MmU2M2ZiODY0NTU5NWM0OA%253D%253D--02e8a1cb9ecbf26795abdb685d109cdeb8efcbee; g_state={"i_l":1,"i_p":1658758025639}',
        'referer': 'https://twitter.com/i/trends',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token': '652ed601b72eb0e2ccc5d9bdccb5a7058effc621d575a114af1f0b05f590c71ea55f81de390eb382e572fe90d503dc866e9e80ba750fe4a6ed47a563a70c007cb0c787fbc3e288386a3b36489a8feeeb',
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en',
        'x-twitter-utcoffset': '+0430'
    })

    json_hashtag = loads(request_hashtag.content)
    with open('hashtag_json.json','w') as hashtag_json:
        hashtag_json.write(dumps(json_hashtag,indent=4,sort_keys=True))
    sleep(float(format(uniform(0.7,1.5),'.1f')))
    while check_hashtag:
        try:
            number_tweets =str(json_hashtag['timeline']['instructions'][1]['addEntries']['entries'][1]['content']['timelineModule']['items'][c]['item']['content']['trend']['trendMetadata']['metaDescription'][:-7])
            name = json_hashtag['timeline']['instructions'][1]['addEntries']['entries'][1]['content']['timelineModule']['items'][c]['item']['content']['trend']['name']
            domainContext = json_hashtag['timeline']['instructions'][1]['addEntries']['entries'][1]['content']['timelineModule']['items'][c]['item']['content']['trend']['trendMetadata']['domainContext']
            number_tweets = number_tweets.replace('.','').replace(',','')
            for i in s_n:
                if i in number_tweets:
                    number_tweets = int(number_tweets.split(i)[0])*s_n[i]
                    break
            if int(number_tweets) > int(max) and 'Iran' in domainContext and '#' in name:
                max = int(number_tweets)
                hashtag_trend = name
                meta_data = domainContext
        except:
            check_hashtag = False
        c += 1
    print('hashtag name =>\t'+hashtag_trend,'\n'+meta_data,'\nNumber of tweets =>\t'+str(max))
    return [hashtag_trend,max]


#encode hashtag name
def encode_hashtag(trend_hashtag):
    encoded_query = quote_plus(trend_hashtag)
    return encoded_query


#main crwler
def crwler(encoded_query,max,tweets = 0):
    url = f'https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q={encoded_query}&count=20&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control%2Cvibe'
    response = get(url,headers={
        'authority': 'twitter.com',
        'method': 'GET',
        'path': f'/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q={encoded_query}&count=20&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control%2Cvibe',
        'scheme': 'https',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'cookie': 'guest_id_marketing=v1%3A165875854462735474; guest_id_ads=v1%3A165875854462735474; personalization_id="v1_PcpUHhmPPCb+nt1L3CXHUA=="; guest_id=v1%3A165875854462735474; _gid=GA1.2.1977635703.1658758550; _sl=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIjitjWCAToMY3NyZl9p%250AZCIlN2U4ZDdmZDhmZGFiZWYxMjZkNDY0NTRjYTUyNjhhNTU6B2lkIiVjZjM2%250AZWYyMTQ3ZTA3MGU4YmVkOTJmZWY2N2M5MTFlYQ%253D%253D--d7dee96d5b38d9e2b6dac7b034f77576aed281e6; kdt=FpzwP7rXKc1OGJpB5m1bLGFJ2FDRFLcQpgY6kba4; auth_token=cd61c08853312d3005ab3ac3b8c93fdea806b413; ct0=c3532add5a6fad9e2bc5cc3f440409440d2363ec258e72c50580963170571953982ed33fa67fdc1a935075eaf44263bbdfe3c5ce7707ce74965848e6cc3f25478a94096cef9ffa82d0e6e6aa8c35eae7; att=1-sO1FAKVzFvr958SEmoEdeo2ZWnDuCKIxjJ7J7W1F; twid=u%3D1551532947068620800; lang=en; at_check=true; mbox=PC#43734fc3919748a396daf4856d9c3d1c.35_0#1722014604|session#6408169bdb00400b83fef593a91819fb#1658771664; _ga_34PHSZMC42=GS1.1.1658769806.1.1.1658769821.0; _ga=GA1.2.1031361875.1658758550; _ga_BYKEBDM7DS=GS1.1.1658770753.2.0.1658770753.0',
        'referer': f'https://twitter.com/search?q={encoded_query}&src=typed_query&f=top',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token': 'c3532add5a6fad9e2bc5cc3f440409440d2363ec258e72c50580963170571953982ed33fa67fdc1a935075eaf44263bbdfe3c5ce7707ce74965848e6cc3f25478a94096cef9ffa82d0e6e6aa8c35eae7',
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en'
    })
    json_request = loads(response.content)
    with open('request 0.json','w') as js:
        js.write(dumps(json_request,indent=4,sort_keys=True))
    tweets += len(json_request['globalObjects']['tweets'])
    c = 1
    number = len(json_request['timeline']['instructions'][0]['addEntries']['entries'])-1
    cursor = quote_plus(json_request['timeline']['instructions'][0]['addEntries']['entries'][number]['content']['operation']['cursor']['value'])
    while True:
    
        sleep(float(format(uniform(0.7,1.5),'.1f')))
        url = f'''https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q={encoded_query}&count=20&query_source=typed_query&cursor={cursor}&pc=1&spelling_corrections=1&include_ext_edit_control=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control%2Cvibe'''
        response = get(url,headers={
        'authority': 'twitter.com',
        'method': 'GET',
        'path': f"""/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q={encoded_query}&count=20&query_source=typed_query&cursor={cursor}&pc=1&spelling_corrections=1&include_ext_edit_control=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2CbirdwatchPivot%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control%2Cvibe""",
        'scheme': 'https',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'cookie': 'guest_id_marketing=v1%3A165875854462735474; guest_id_ads=v1%3A165875854462735474; personalization_id="v1_PcpUHhmPPCb+nt1L3CXHUA=="; guest_id=v1%3A165875854462735474; _gid=GA1.2.1977635703.1658758550; _sl=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIjitjWCAToMY3NyZl9p%250AZCIlN2U4ZDdmZDhmZGFiZWYxMjZkNDY0NTRjYTUyNjhhNTU6B2lkIiVjZjM2%250AZWYyMTQ3ZTA3MGU4YmVkOTJmZWY2N2M5MTFlYQ%253D%253D--d7dee96d5b38d9e2b6dac7b034f77576aed281e6; kdt=FpzwP7rXKc1OGJpB5m1bLGFJ2FDRFLcQpgY6kba4; auth_token=cd61c08853312d3005ab3ac3b8c93fdea806b413; ct0=c3532add5a6fad9e2bc5cc3f440409440d2363ec258e72c50580963170571953982ed33fa67fdc1a935075eaf44263bbdfe3c5ce7707ce74965848e6cc3f25478a94096cef9ffa82d0e6e6aa8c35eae7; att=1-sO1FAKVzFvr958SEmoEdeo2ZWnDuCKIxjJ7J7W1F; twid=u%3D1551532947068620800; lang=en; at_check=true; mbox=PC#43734fc3919748a396daf4856d9c3d1c.35_0#1722014604|session#6408169bdb00400b83fef593a91819fb#1658771664; _ga_34PHSZMC42=GS1.1.1658769806.1.1.1658769821.0; _ga=GA1.2.1031361875.1658758550; _ga_BYKEBDM7DS=GS1.1.1658770753.2.0.1658770753.0;lv-uid=AAAAEIC5H2fZyxIoZE2RkR58AOGgO6Fq4GcekpamBQLYIBbsYTZ3XE3VtRAVTfhQ',
        'referer': f'https://twitter.com/search?q={encoded_query}&src=typed_query&f=top',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token': 'c3532add5a6fad9e2bc5cc3f440409440d2363ec258e72c50580963170571953982ed33fa67fdc1a935075eaf44263bbdfe3c5ce7707ce74965848e6cc3f25478a94096cef9ffa82d0e6e6aa8c35eae7',
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en'
        })
        json_request = loads(response.content)
        if len(json_request['globalObjects']['tweets']) != 0:
            tweets += len(json_request['globalObjects']['tweets'])
            with open(f'request {c}.json','w') as js:
                js.write(dumps(json_request,indent=4,sort_keys=True))
            print(f'process {tweets}/{max}')
            c += 1
        cursor = quote_plus(json_request['timeline']['instructions'][len(json_request['timeline']['instructions'])-1]['replaceEntry']['entry']['content']['operation']['cursor']['value'])



#hashtag_trend,max = get_hashtag_trend()
crwler(encode_hashtag('"فیلیمو"'),int(10000000000000))