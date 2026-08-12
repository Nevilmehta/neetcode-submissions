class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)       

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1
        self.tweets[userId].append((self.time, tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        # Gather tweets from user and their followees
        users = self.following[userId] | {userId}
        heap = []
        
        for u in users:
            for t in self.tweets[u][-10:]:   # only last 10 per user (optimization)
                heapq.heappush(heap, t)
                if len(heap) > 10:           # keep only 10 most recent
                    heapq.heappop(heap)

        # Sort by time desc, extract tweetIds
        return [x[1] for x in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:   # cannot follow self
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
