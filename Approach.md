# Approach to solving the assignment

##The problem
Download a customer file, where each customer is represented by a line in the file, with a JSON containing 
the longitude and latitude of their location, their user id and their name. Select those customers that are within
100 km to the Dublin office and output their user id and name onto a file, ordered by ascending user id. To calculate
the distance, use the first formula in [this](https://en.wikipedia.org/wiki/Great-circle_distance) wikipedia article.

     
## Assumptions
   
- I assumed the file can be read entirely into memory. If the customer file were to be too big to be kept in memory, 
it could be processed in chunks, keeping in memory only those customers that are within the specified distance. 

- I assumed there are no duplicate users in the input file. If the input file can have duplicate users and "inviting" them more than once is not desired, 
 duplicates can easily be dropped using pandas.


## Tools and libraries
- I chose python as my language since I am very comfortable with it and I prefer it for data processing and manipulating, 
since pandas provides so many great functionalities.
- To calculate the distance, I used the great_circle distance from the geopy library.
There's two main advantages here: 
    1. This library is more likely to be better tested and designed that any algorithm one can write in one week
    2. If, for example, the requirements change and the distance needs to be calculated, for example, with the haversine function,
     it's just a matter of changing two lines.
- I added a Makefile to generate a virtual environment and install all required packages. 


     