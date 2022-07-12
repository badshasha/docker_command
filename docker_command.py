docker logs a17666613276bc2fc947c38f04c5033dd8f85007979ab33277ae612236e5a4c3
# this command not re running or execute the program 
# it's just showing information form log information of previous run 


# stap commandd
docker stop id  # send to the pirmary process [ SIGTERM ]
                # this thing is safe [ internal processor can do additional thing like safe time , save point  ]

                # nearly takes 10 secound 

docker kill id  # SIGKILL -> immediate kill the process 
                # instance do it 


# speialci not 
#  but if process not working for stop it's automatically change to docker kill command 


# some times we need different commands 
# හිතන්න පළවෙනියට sever එක on කරනවා . 127.0.0.1
# ඊට පස්සේ එකට command ලියනවා කියලා 
# docker ඇතුලේ server run වෙනකොට අපිට වෙනවා අලුත් command ඉන්ජෙච්ට් කරන්න 

docker exec -it contianerId  command


without -it flag it's automatically terminal the secound command 


# getting shell power 

docker exec -it 43234ig432  sh  # provide full terminal power 
#  exit usienr 
ctrl + D 
