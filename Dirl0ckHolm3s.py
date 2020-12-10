import threading
import argparse
import requests
import pymp

logo = r'''
  _____  _      _      ___       _      _    _       _           ____      
 |  __ \(_)    | |    / _ \     | |    | |  | |     | |         |___ \     
 | |  | |_ _ __| |   | | | | ___| | __ | |__| | ___ | |_ __ ___   __) |___ 
 | |  | | | '__| |   | | | |/ __| |/ / |  __  |/ _ \| | '_ ` _ \ |__ </ __|
 | |__| | | |  | |___| |_| | (__|   <  | |  | | (_) | | | | | | |___) \__ \
 |_____/|_|_|  |______\___/ \___|_|\_\ |_|  |_|\___/|_|_| |_| |_|____/|___/ V1.0
 '''
print(logo)


class cl:
    ENDC = '\033[0m'
    # ADD more colors for different responses







parser = argparse.ArgumentParser()
parser.add_argument( "-l", '--list', help="path of the list file (required)", required=True , type=argparse.FileType('r') )
parser.add_argument( "-u", '--url', help="Target website [https://site.com] (required)", required=True, type=str )
parser.add_argument( "-t", '--threads', help="Number of threads (default=1)", choices=list(range(1,11)), default=1, type=int )
args = parser.parse_args()



url = args.url
if url[-1] == '/': url = url[:-1] # fix url format
if url[0:4] != 'http': url = 'https://' + url # fix url format

paths_list = args.list.read().split('\n')
threads = args.threads


def brute_dir():

	with pymp.Parallel(threads) as p:

		for i in p.range(len(paths_list)):

			cur_path = paths_list[i]
			response_code = requests.get( url + cur_path ).status_code
			
			if response_code == 200: BEGC = '\033[93m'
			else: BEGC = '\033[31m'

			print( 'Response: [ {}{}{} ] |'.format(BEGC, response_code, cl.ENDC) , url + cur_path )


brute_dir()
