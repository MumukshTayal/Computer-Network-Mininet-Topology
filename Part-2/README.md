# Assignment Part-2 README

This part of the assignment involves the implementation of a Mininet topology and the analysis of throughput for different congestion control schemes using custom Python scripts.

## Steps to Execute the Assignment

### 1. Start Mininet Topology

Open a terminal and run the following command to start Mininet with the custom topology:

```
sudo mn --custom custom_topo.py --topo mytopo

```

### 2. Open xterms for H1 and H4

In the Mininet CLI, open xterm windows for H1 and H4 using the following commands:

```
xterm h1 h4
```

### 3. Open Additional xterms for H2, H3, and Extra H4 (for Part c)

For Part (c), open xterm windows for H2, H3, and two additional xterms for H4:

```
xterm h2 h3 h4 h4 h4
```

### 4. Run Wireshark

From each xterm window (except for the extra xterms for H4 in Part c), run Wireshark to capture network traffic.

```
wireshark &
```

### 5. Execute Python Script (ser-cli.py)

Run the Python script `ser-cli.py` to perform the throughput analysis. Use the following command format:

```
python ser-cli.py --role [server, client] --port [port_number] --config [b, c] --congestion [vegas, reno, cubic, bbr]
```

Replace the placeholders (`[...]`) with appropriate values for your experiment.

### Example Command (for Part b):

```
python ser-cli.py --role server --port 5001 --config b --congestion vegas
```

### Example Command (for Part c):
For part c, all three need to be executed in separated xterms for h1, h2, h3 and similarly the server configuration for all three on the three xterms for h4.

```
python ser-cli.py --role client --port 5001 --config c --congestion reno
python ser-cli.py --role client --port 5002 --config c --congestion reno
python ser-cli.py --role client --port 5003 --config c --congestion reno
```

### Example Command (for Part d):

```
python ser-cli.py --role server --port 5001 --config b --congestion cubic

```

Explanation of Flags
--------------------

-   `--role`: Specifies the role, either 'server' or 'client'.
-   `--port`: Specifies the port number for the server.
-   `--config`: Specifies the configuration, either 'b' or 'c'.
-   `--congestion`: Specifies the congestion control scheme, choose from 'vegas', 'reno', 'cubic', 'bbr'.
-   `--loss` (for Part d only): Specifies the link loss percentage.
