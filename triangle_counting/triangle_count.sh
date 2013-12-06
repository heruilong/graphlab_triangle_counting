#!/bin/bash

./triangle_counting --graph /home/ubuntu/data/p0.05-1kgraph.txt --format adj
./triangle_counting --graph /home/ubuntu/data/p0.05-10kgraph.txt --format adj
./triangle_counting --graph /home/ubuntu/data/p0.1-1kgraph.txt --format adj
./triangle_counting --graph /home/ubuntu/data/p0.1-10kgraph.txt --format adj
./triangle_counting --graph /home/ubuntu/data/p0.2-1kgraph.txt --format adj
./triangle_counting --graph /home/ubuntu/data/p0.2-10kgraph.txt --format adj
./triangle_counting --graph /home/ubuntu/data/p0.1-20kgraph.txt --format adj
./triangle_counting --graph /home/ubuntu/data/p0.05-20kgraph.txt --format adj

