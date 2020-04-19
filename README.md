# cs4700-project5

1. Briefly describe the design decisions you are making in your DSN server and HTTP server.

For our HTTP server, we used the built in http.server functionality to return only GET requests. It bound to it's local IP, and would get the file from the server if it didn't exist, but if it did we just return the cached file. The server runs until it is terminated by the user.
{INSERT HOW DSN SERVER WORKDS}

2. How would you change your DNS server to dynamically return an IP, instead of a hard coded IP?
{INSERT DSN WORK}

3. Explain how you would implement the mapping of incoming client requests to CDN servers, if you had several servers to pick from. Notice the CDN servers are geographically distributed, and so are clients. Be specific about what kind of measurement system you would implement, where exactly the data would be collected, and how you would then decide which server is the best option for a particular client.
{INSERT ANSWER}

4. Explain how you would implement caching for your HTTP server, if we were to send a range of requests to your HTTP server. What cache replacement strategy would you implement if content popularity followed a Zipfian distribution. How would your HTTP server respond to a request for a content that is not currently in the cache.

We would implement a caching method for the HTTP server that stored up to 10 files at a time. It would pull the files and store the names in an array, with the most frequently accessed files at the front of the array and the least frequently used files at the end. We would keep track of how many times each file had been accessed in order to track this. The files would not be stored in python memory but they would be pulled and stored on the server, which is different from our current implementation. Each server would have its own cache, but over time we would expect these all to converge. As new files were accessed, they would replace the least used files in memory and in the array if they were not already cached. In other words, we would first check to see if the content existed, if it did, return it, and if it did not we would pull the new file and return that to the user. After that, we would calculate the new cache.
