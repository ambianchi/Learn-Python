peanut_butter=4
jelly=4
bread=8

if peanut_butter>=1 and jelly>=1 and bread>=2:
    print "Yeehaw! It's peanut butter jelly time!"
else:
    print "Oh no! No lunch for you"
#if peanut_butter>=1:
    #if jelly>=1:
        #if bread >=2:
        #print: "PBJ Time!"
    #else:
        #print "I have enough PBJ but not enough bread"
    #else:
        #print: "I have enough PB but not enough J"
#else:
    #print: "I don't have enough PB"


#indendations line up with assumption
    
#Second Goal
peanut_butter=4
jelly=4
bread=8

if peanut_butter>=1 and jelly>=1 and bread >=2:
    sandwiches = bread/2
    if peanut_butter<=sandwiches:
        sandwiches = peanut_butter
    if jelly<=sandwiches:
        sandwiches = jelly
    print "You can make {0} sandwiches".format(sandwiches)
else:
    print "You can't make any sandwiches"

#Third Goal

bread=7
peanut_butter=3
jelly=2

if bread>=2 and peanut_butter>=1 and jelly>=1:
    sandwiches=bread/2
    if peanut_butter<sandwiches:
        sandwiches=peanut_butter
    if jelly<sandwiches:
        sandwiches=jelly
    print "You can make {0} sandwiches".format(sandwiches)
    if bread % 2 == 1:
        print "You can make an open faced sandwich"
else:
    print "No peanut butter jelly time"

#Fourth Goal

bread=4
peanut_butter=0
jelly=2

if bread>=2 and peanut_butter>=1 and jelly>=1:
    sandwiches=bread/2
    if peanut_butter<sandwiches:
        sandwiches=peanut_butter
    if jelly<sandwiches:
        sandwiches=jelly
    print "You can make {0} sandwiches".format(sandwiches)
    if bread % 2 == 1:
        print "You can make an open faced sandwich"
else:
    print "No peanut butter jelly time"
    if bread<2:
        print "You need bread"
    if peanut_butter<1:
        print "You need peanut butter"
    if jelly<1:
        print "You need jelly"

#Fifth Goal

bread=4
peanut_butter=2
jelly=0

if bread>=2 and peanut_butter>=1 and jelly>=1:
    sandwiches=bread/2
if peanut_butter<sandwiches:
        sandwiches=peanut_butter
if jelly<sandwiches:
        sandwiches=jelly
    print "You can make {0} sandwiches".format(sandwiches)
if bread % 2 == 1:
        print "You can make an open faced sandwich"
if bread/2 > jelly and peanut_butter > jelly:
if bread/2 > peanut_butter:
        print "You can make {0} peanut butter sandwiches".format(peanut_butter-jelly)
        else:
            print "You can make {0} peanut butter sandwiches, but you need to think about your life choices".format(bread/2 - jelly)
            



