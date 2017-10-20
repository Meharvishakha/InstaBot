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
Function declaration to get the Insta ID of a user by username
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
                while i <= len(user_post):                                          #this loop will check post with the minimum no. of likes
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

'''
Function declaration to get post ID of another user
'''

def get_post_id(username):
    user_id = get_user_id(username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    req_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (req_url)
    post_id = requests.get(req_url).json()
    if post_id['meta']['code'] == 200:
        if len(post_id['data']):
            return post_id['data'][0]['id']
        else:
            print 'There is not recent post'
    else:
        print 'Not valid status!'
    return None

'''
Function declaration to like a post of another user
'''

def like_a_post(username):
    media_id = get_post_id(username)
    req_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {'access_token' : ACCESS_TOKEN}
    print 'POST request url : %s' % (req_url)
    post_a_like = requests.post(req_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

'''
Function declaration to get list of comments of another user
'''

def get_comment_list(username):
    media_id = get_post_id(username)
    req_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id,ACCESS_TOKEN)
    print 'GET request url : %s' % (req_url)
    comment_list = requests.get(req_url).json()

    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            print 'List of comments are:'
            i = 0
            while i <= len(comment_list):
                print comment_list['data'][i]['text']
                i = i + 1
        else:
            print 'There is no comments'
    else:
        print 'Not valid status!'

'''
Function declaration make a comment on a post of another user
'''

def make_a_comment(username):
    media_id = get_post_id(username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": ACCESS_TOKEN, "text": comment_text}
    req_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (req_url)
    make_comment = requests.post(req_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"


def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        #print "5.Get a list of people who have liked the recent post of a user\n"
        print "6.Like the recent post of a user\n"
        print "7.Get a list of comments on the recent post of a user\n"
        print "8.Make a comment on the recent post of a user\n"
        #print "9.Delete negative comments from the recent post of a user\n"
        print '10.Exit\n'

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
        #elif choice==5:
        #    insta_username = raw_input("Enter the username of the user: ")
        #    get_like_list(insta_username)
        elif choice==6:
            username = raw_input("Enter the username of the user: ")
            like_a_post(username)
        elif choice==7:
            username = raw_input("Enter the username of the user: ")
            get_comment_list(username)
        elif choice==8:
            username = raw_input("Enter the username of the user: ")
            make_a_comment(username)
        #elif choice==9:
        #    insta_username = raw_input("Enter the username of the user: ")
        #    delete_negative_comment(insta_username)
        elif choice == 10:
            exit()
        else:
            print "wrong choice"

start_bot()