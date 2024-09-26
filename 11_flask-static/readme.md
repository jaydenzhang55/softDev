## K11: Some Things Never Change
### Due: 2024-09-26r before class

The first app.route('/') will lead us to a page displaying "No hablo queso!".

We predict that accessing http://localhost:5000/static/foo.html will lead us to a route that accesses the localhost displaying the html file. We believe that this will only work when we uncomment the 
app.route('/') and use the other app.route. 

In reality, the file is found but it does not produce the same terminal results as if the app.route were to be commented (so the method doesn't run). 

When trying to run http://localhost:5000/static/foo, we thought that it would default to an html file. In actuality, it downloads the foo file when you run the localhost link.
