# check_to_lift_and_cast
checks the current number of votes. When there are enough votes it calls lift on the chief contract and cast on the slate

you will need to change/add some lines to get this to work for future slates

I've put in comments describing each alteration in the file. Here is a summary:
line 6 - change to your web3 provider
line 12/13 - put in your address/key
line 23 - put in the new slate contract address
line 47 - add in a new variable containing the storage address of the new slate
line 72 - add in a new variable for the vote count of the new slate
line 82 - print out the new vote count
line 86 - change the if statement to check for the new count vs the slate with the hat (the one with the most votes)
line 89 - uncomment do_it() when everything is set up correctly
