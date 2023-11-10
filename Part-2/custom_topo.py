from mininet.topo import Topo
from mininet.node import OVSSwitch, Host

class MyTopology(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(h1, s1, bw = 10000)
        self.addLink(h2, s1, bw = 10000)
        self.addLink(h3, s2, bw = 10000)
        self.addLink(h4, s2, bw = 10000)
        self.addLink(s1, s2, loss=0)  # Link loss can be changed between either 0% or 1% or 3%

topos = {'mytopology': MyTopology}
