import requests

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


def get_own_post():
    req_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
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

def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Exit"

        choice = int(raw_input("Enter you choice: "))
        if choice == 1:
            self_info()
        elif choice == 2:
            username = raw_input("Enter the username of the user: ")
            get_user_info(username)
        elif choice==3:
            get_own_post()
        elif choice == 4:
            exit()
        else:
            print "wrong choice"

start_bot()