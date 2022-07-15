docker run appnameorid  == > docker-compose up

docker build .
docker run appnameorid  == >  docker-compose up --build


# run background
docker-compose up -d  

# stop process 
docker-compose down 


# build docker file with docker file name
docker build -f dockerfile.dev .


# docker wtih volum

docker run -p 3000:3000 -v $(pws):/app imagename

# docker with working volumns 

docker run -p 3000:3000 -v /app/node_modules -v $(pws):/app imagename