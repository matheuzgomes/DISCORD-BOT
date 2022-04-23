import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("TlFfAC221FN1cr6IiBvlDt5TS", 
    "uUM7JXJY6xBOBsYqZr02yWWxlTejKf9kvofj6hBwTxwp9firiY")
auth.set_access_token("776799975594422272-tEu7i7RmqSQbueJEcVszyfhATD0kb24", 
    "Lr55FCXUB8ps5pMn7bR5ar9oVYcstV1HKsJqviksjDPxv")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")