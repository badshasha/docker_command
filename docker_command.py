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



# how to restart docker progam again 


docker run busybox echo hi there   # [docker  run  imagename   command ]
docker ps --all     # find all dockers 
# find the docker id for hte information 

CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
f1d384d3cc47   busybox       "echo hello shavendra"   27 seconds ago   Exited (0) 25 seconds ago             peaceful_turing
# 683d864bcf01   busybox       "echo hi there"          42 seconds ago   Exited (0) 40 seconds ago             great_chatelet
# fcde4a9d0f49   hello-world   "/hello"                 9 minutes ago    Exited (0) 8 minutes ago              focused_lalande
# ec45260a3405   hello-world   "/hello"                 3 hours ago      Exited (0) 3 hours ago                agitated_knuth

docker start -a f1d384d3cc47   # output ==> hi there


# after you create docker container : you connot change command [docker  run  imagename   😖 command ]


# delete all clearn the memory 
docker system prune   # after you did this it's need to reinstall all the image that u user previously 

# dont use fequently 
# it's only use for some time that you really need to clean space 
# or done work with docker 