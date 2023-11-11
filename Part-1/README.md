# Assignment Part-1 README

This part of the assignment involves the implementation of a Mininet topology and the analysis packets and routing tables of the routers.

## Steps to Execute the Assignment

### 1. Start Mininet Topology

Open a terminal and run the following command to start Mininet with the custom topology:

```
sudo python topology.py 

```

### 2. Open xterms for ra node

In the Mininet CLI, open xterm windows for ra  using the following commands:

```
xterm ra
```

### 3. Write tcpdump in xterm ra (new terminal)

For Part b, write the following command this will start capturing packets and save in the partb file:

```
tcpdump -n -i ra-eth2 -w partb.pcap
```

### 4. Ping ra and rb routers

In the Mininet, ping both the routers and it will start sending packets

```
ra ping rb
```

### 5. For routing tables 

Run the following commands for ra, rb and rc routers

```
ra route -n
```

Replace the rb and rc for router rb and rc

