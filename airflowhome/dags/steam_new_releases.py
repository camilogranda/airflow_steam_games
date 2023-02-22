from selectolax.parser import HTMLParser
import pandas as pd
import requests
import json
import time

def steam_new_releases():
    
    resp = requests.get('https://store.steampowered.com/explore/new/')

    html = HTMLParser(resp.text)

    game_info = html.css('div.home_tabs_content div.tab_content a')


    def clean_platforms(platform):
        if 'win' in platform:
            platform = 'Windows'
        elif 'mac' in platform:
            platform = 'Mac OS'
        elif 'linux' in platform:
            platform = 'Linux'
        else:
            platform = 'VR Supported'
        
        return platform

    def rm_list(lst):
        return ', '.join(lst) if isinstance(lst, list) else lst

    games_list = []       
    for game in game_info:
        tags = [node.text() for node in game.css('div.tab_item_top_tags > span')]
        platform_list = [p.attributes['class'] for p in game.css('div.tab_item_details > span')]
        
        if game.css_matches('div.tab_item_name'):
            if game.css_matches('div.discount_original_price'):
                original_price = game.css_first('div.discount_original_price').text()
            else:
                original_price = 'None'
            
            games = {
                'game': game.css_first('div.tab_item_name').text(),
                'game_url': game.attributes['href'],
                'tags': rm_list([tag.replace(', ', '') for tag in tags]),
                'platforms': rm_list(list(map(clean_platforms, platform_list))),
                'final price': game.css_first('div.discount_final_price').text(),
                'original_price': original_price
            }
            
            games_list.append(games)
            
            
    return games_list
            
            
if __name__ == "__main__":
    
    games = steam_new_releases()
