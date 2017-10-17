import requests
import urllib

BASE_URL = 'https://api.instagram.com/v1/'
ACCESS_TOKEN = '4870715640.a48e759.874aba351e5147eca8a9d36b9688f494'

'''
Function declaration to get your own info
'''

def self_info():
    req_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (req_url)
    user_info = requests.get(req_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to get the ID of a user by username
'''

def get_user_id(username):
  req_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (username, ACCESS_TOKEN)
  print 'GET request url : %s' % (req_url)
  user_info = requests.get(req_url).json()
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          return user_info['data'][0]['id']
      else:
          return None
  else:
      print 'Not valid status!'
      exit()

'''
Function declaration to get the info of a user by username
'''

def get_user_info(username):
  user_id = get_user_id(username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  req_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, ACCESS_TOKEN)
  print 'GET request url : %s' % (req_url)
  user_info = requests.get(req_url).json()

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'There is no data for this user!'
  else:
    print 'Not valid status!'

'''
Function declaration to get your own posts
'''

def get_own_post():
    req_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (req_url)
    my_post = requests.get(req_url).json()

    if my_post['meta']['code'] == 200:
        if len(my_post['data']):
            image_name = my_post['data'][0]['id'] + '.jpeg'
            image_url = my_post['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)                           #this is for downloading a post/an image
            print 'Your image has been downloaded!'
        else:
            print 'post does\'nt exist'
    else:
        print 'Not valid status!'

'''
Function declaration to get the posts of a user by username
'''

def get_user_post(username):
    user_id = get_user_id(username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    print '1.Download recent post'
    print '2.Download post with minimum no. of likes'
    ch=int(raw_input("Enter your choice: "))
    req_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (req_url)
    user_post = requests.get(req_url).json()
    if ch == 1:
        if user_post['meta']['code'] == 200:
            if len(user_post['data']):
                image_name = user_post['data'][0]['id'] + '.jpeg'
                image_url = user_post['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)                       #this is for downloading a post/an image
                print 'Your image has been downloaded!'
            else:
                print 'There is not recent post'
        else:
            print 'Not valid status!'
    elif ch == 2:
        if user_post['meta']['code'] == 200:
            if len(user_post['data']):
                i = 0
                no = 0
                cnt = user_post['data'][0]['likes']['count']
                print cnt
                while i <= 10:                                          #this loop will check max 10 post and find the minimum liked post
                    if user_post['data'][i]['likes']['count'] < cnt:
                        no = i
                        cnt = user_post['data'][i]['likes']['count']
                        i = i+1
                image_name = user_post['data'][no]['id'] + '.jpeg'
                image_url = user_post['data'][no]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print 'Your image has been downloaded!'
            else:
                print 'There is not recent post'
        else:
            print 'Not valid status!'
    else:
        print 'Wrong choice'

def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get user recent post\n"
        print "5.Exit"

        choice = int(raw_input("Enter you choice: "))
        if choice == 1:
            self_info()
        elif choice == 2:
            username = raw_input("Enter the username of the user: ")
            get_user_info(username)
        elif choice == 3:
            get_own_post()
        elif choice == 4:
            username = raw_input("Enter the username of the user: ")
            get_user_post(username)
        elif choice == 5:
            exit()
        else:
            print "wrong choice"

start_bot()