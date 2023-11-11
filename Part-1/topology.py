from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class NetworkTopo(Topo):
    def build(self, **_opts):
        
        ra = self.addHost('ra', cls=LinuxRouter, ip='192.168.1.1/24')
        rb = self.addHost('rb', cls=LinuxRouter, ip='192.168.2.1/24')
        rc = self.addHost('rc', cls=LinuxRouter, ip='192.168.3.1/24')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        h1 = self.addHost(name='h1', ip='192.168.1.2/24', defaultRoute='via 192.168.1.1')
        h2 = self.addHost(name='h2', ip='192.168.1.3/24', defaultRoute='via 192.168.1.1')
        h3 = self.addHost(name='h3', ip='192.168.2.2/24', defaultRoute='via 192.168.2.1')
        h4 = self.addHost(name='h4', ip='192.168.2.3/24', defaultRoute='via 192.168.2.1')
        h5 = self.addHost(name='h5', ip='192.168.3.2/24', defaultRoute='via 192.168.3.1')
        h6 = self.addHost(name='h6', ip='192.168.3.3/24', defaultRoute='via 192.168.3.1')

        self.addLink(s1, ra, intfName2='ra-eth1', params2={'ip': '192.168.1.1/24'})
        self.addLink(s2, rb, intfName2='rb-eth1', params2={'ip': '192.168.2.1/24'})
        self.addLink(s3, rc, intfName2='rc-eth1', params2={'ip': '192.168.3.1/24'})


        self.addLink(ra, rb, intfName1='ra-eth2', intfName2='rb-eth2', params1={'ip': '192.168.100.1/24'}, params2={'ip': '192.168.100.2/24'})
        self.addLink(rb, rc, intfName1='rb-eth3', intfName2='rc-eth2', params1={'ip': '192.168.101.1/24'}, params2={'ip': '192.168.101.2/24'})
        self.addLink(rc, ra, intfName1='rc-eth3', intfName2='ra-eth3', params1={'ip': '192.168.102.1/24'}, params2={'ip': '192.168.102.2/24'})

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)

        # connect ra and rc
        self.addLink(s1, s3)

def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo)

    info(net['ra'].cmd("ip route add 192.168.3.0/24 via 192.168.102.1 dev ra-eth3"))
    info(net['ra'].cmd("ip route add 192.168.2.0/24 via 192.168.100.2 dev ra-eth2"))
    info(net['rb'].cmd("ip route add 192.168.3.0/24 via 192.168.101.2 dev rb-eth3"))
    info(net['rb'].cmd("ip route add 192.168.1.0/24 via 192.168.100.1 dev rb-eth2"))
    info(net['rc'].cmd("ip route add 192.168.1.0/24 via 192.168.102.2 dev rc-eth3"))
    info(net['rc'].cmd("ip route add 192.168.2.0/24 via 192.168.101.1 dev rc-eth2"))

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
