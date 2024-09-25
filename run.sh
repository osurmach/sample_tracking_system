#!/bin/bash

case $1 in
   "-start")
      docker-compose -f docker-compose.yml up
      ;;
   "-stop")
      docker-compose -f docker-compose.yml down
      ;;
   "-rebuild")
      docker-compose -f docker-compose.yml down --volumes --rmi all --remove-orphans
      docker-compose -f docker-compose.yml up
      ;;
   "-help")
      echo "Usage:
            run.sh [OPTION]...
            Options:
              -start              starts dockerized version of the application
              -stop               stops dockerized version of the application
              -rebuild            rebuilds dockerized version of the applictaion and starts the container
              -help               shows this help, then exit"
      exit 1 # Command to come out of the program with status 1
      ;;
esac