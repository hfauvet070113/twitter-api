from app.apis.tweets import ma
from app.models import Tweet

class TweetSchema(ma.Schema):
    class Meta:
        model = Tweet
        fields = ('id', 'text', 'created_at') # These are the fields we want in the JSON!

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)
