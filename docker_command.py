docker logout
docker login

---------------------------------

# create and start command 

docker create hello-world  # output ==> fcde4a9d0f49e941d4e10e931cfff5f485f2a5202665ba89913738afb9a7632b  [id of the container]
docker strat -a fcde4a9d0f49e941d4e10e931cfff5f485f2a5202665ba89913738afb9a7632b  # output ==> run the container

# -a is the run command for container without it , it's only print the ID

# there is a different between run and start :
    # run printed all the terminal output + progam output  
    # start olny pring progamm output 