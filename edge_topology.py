from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.log import setLogLevel

class EdgeTopology(Topo):
    def build(self):
        # Create Edge Switch (represents the Edge node)
        edge_switch = self.addSwitch('s1')
        
        # Create Hosts
        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')
        h3 = self.addHost('h3', ip='10.0.0.3')

        # Connect Hosts to Edge Switch
        self.addLink(h1, edge_switch)
        self.addLink(h2, edge_switch)
        self.addLink(h3, edge_switch)

if __name__ == '__main__':
    setLogLevel('info')

    # Initialize the network
    topo = EdgeTopology()
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6633))

    # Start the network
    net.start()

    # Open the Mininet CLI
    net.pingAll()
    net.interact()

    # Stop the network when done
    net.stop()
