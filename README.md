# cs4700-project5

1. Briefly describe the design decisions you are making in your DSN server and HTTP server.

For our HTTP server, we used the built in http.server functionality to return only GET requests. It bound to it's local IP, and would get the file from the server if it didn't exist, but if it did we just return the cached file. The server runs until it is terminated by the user.
{INSERT HOW DSN SERVER WORKDS}

2. How would you change your DNS server to dynamically return an IP, instead of a hard coded IP?
{INSERT DSN WORK}

3. Explain how you would implement the mapping of incoming client requests to CDN servers, if you had several servers to pick from. Notice the CDN servers are geographically distributed, and so are clients. Be specific about what kind of measurement system you would implement, where exactly the data would be collected, and how you would then decide which server is the best option for a particular client.
{INSERT ANSWER}

4. Explain how you would implement caching for your HTTP server, if we were to send a range of requests to your HTTP server. What cache replacement strategy would you implement if content popularity followed a Zipfian distribution. How would your HTTP server respond to a request for a content that is not currently in the cache.

If the content popularity followed a Zipfian distribution, it would make the most sense for our HTTP server to follow a LFU (Least Frequently Used) cache replacement strategy. In the context of our HTTP server, we would achieve this by storing an array of 10 files that get used, and keep track of how many times each is accessed. The array would only store the location of the files on the server, and we would still need to load the files into memory, but this would be considerably faster than having to pull the file every time. When a request came in for data that was not already in the cache, that data would be pulled and compared to the least recently used piece of data, item 10 in the array, to see how many times that had been pulled. In a tie, we would keep the new file and remove the old one from the cache. After we serviced the client requesting the data, the array would be recalculated so that this computation time does not affect the speed at which the client's data is returned.
