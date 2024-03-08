### never forget
* docker inspect [image]
* docker history --no-trunc [image]
* docker run -it [image] /bin/sh
* docker exec -it [image] /bin/sh
* -p [HOST-port]:[CONTAINER-port] 
* docker images | grep "blabla" | awk '{print $1 ":" $2}' | xargs docker rmi
  
### DEBUG (rhel/centos) 
* RUN yum install -y net-tools
* RUN yum install -y procps
