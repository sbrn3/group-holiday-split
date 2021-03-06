# group-holiday-split
Have you ever booked out an apartment or house as part of a group holiday? A common problem is figuring out the prices 
that everyone should pay especially if the rooms have different utilities. 

This is extremely similar to a rent splitting strategy except there are a few variables that may be different in this 
particular case. It is possible that there are couples that would prefer to be in the same room (and same bed) together. 

There may also be people who are not able to stay for the full length of the holiday. This means that good rooms would 
be wasted if they are left vacant for parts of the trip.

Therefore this gets everyone to bid on each room depending on how much they would be willing to pay for what that room
offers. This way people will get the rooms that they prefer and people will pay depending on how much that room is in
demand. 

# Rules of the auction

1. Bid a price per night that you would pay to have a bed in a particular room

2. The total of your bids must be equal to (or more than) 100. Would be too hard doing the math otherwise. 

# Result

The combination of assigning people to rooms which results in the highest total bids will be the chosen combination. 

e.g. If Sam bids $80 for room 1, $20 for room 2. And Michael bids $20 for room 1 and $80 for room 2. Then in the case 
where Sam gets room 1 and Michael room 2 the total amount bid is 160. But for the inverse, the total amount bid is 
$40. Therefore the best option is for Sam to get room 1 and Michael to get Room 2. This is then scaled down to have 
a correct total($100). So both would end up paying $50 each.

The person who bids the highest on a room is most likely to get that room. If you bid more than other people, then you
will only have to pay the average that people valued that room. 

We have also decided that while different genders are allowed to share a room together, they will not be sharing a bed 
unless they are a couple. 

# Tips

### Picking a value
If you bid too high you will pay too much for that room. If you bid too low you will not get the room. 
The amount that you should bid should determine how much you value the features of that room. Remember everyone probably
has different priorities. Different people may prefer having nice views, having an en suite or having a bigger bed. Therefore you can
price each of those things based on how important it is to you. 

### Sharing a room with a friend
If you want to share a room with a friend then you have to bid more on the room you want to share. Hopefully you will 
win that auction and both be assigned to that room. In this case you may wish to collude and enter the same price bid. 
Therefore if you win you both win, and if you lose you both lose. So not just one person gets the room. 

### Staying fewer than the maximum nights
If you are not there for all the nights you will be disadvantaged because you are paying less by not staying. Because 
this gives the best rooms to the people who pay the most you will probably not get good rooms. A way to make up for this 
is to have the total of your bids be more than the price of the house per night. This means that you are willing to 
pay for more than you are actually staying. Of course you are then subsidizing everyone else's stay, but if you are 
willing to pay to leave a good room empty, then it is up to you. 

### Playing it cheap
So what if you don't care where you sleep as long as you get the absolute cheapest option? Well you have to value 
the popular rooms lower than everyone else (so that you don't win them), but that means that you will have to increase 
your value on a lower popularity rule to have the correct total cost across rooms. Actually the cheapest way is to 
bid as high as possible on the popular rooms but to only slightly lose. 

e.g. Sam wants to have a really cheep room. Therefore if Michael bids $80 on room 1 and $20 on room 2, then Sam 
should bid $79 on room 1 and $21 on room 2. Slightly losing the bid for room 1 and securing a low bid for room 2. 

You are probably better off just bidding normally instead of trying to game the system because it is difficult to know how exactly 
other people will bid.   

### Even split 
Some people will claim that this is too complicated and that you should just split the costs evenly between everyone. And whoever ends up in whichever room doesn't matter. It's a holiday after all. Well if that is the case then these people can bid on every room evenly beacuse they believe all the rooms have equal value. The reality is though, most rational people will realise pretty quickly that the rooms are probably not of equal value. So... they will then decide to bid based on how they actually feel. 

# How to use
main.py is an example where 10 people were sorted into 4 rooms. There is a couple and people who are staying for 
different time periods. 

# Examples 
Here is what the input data for main.py looks like
![example input](https://github.com/sbrn3/group-holiday-split/blob/master/media/input.PNG)

Here is what the output of main.py looks like
![example output](https://github.com/sbrn3/group-holiday-split/blob/master/media/output.PNG)
