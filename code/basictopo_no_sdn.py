from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class BasicNoSDNTopo( Topo ):

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts, name and numbers 
        leftHost1 = self.addHost( 'h1' )
        leftHost2 = self.addHost( 'h2' )
        leftHost3 = self.addHost( 'h3' )
        leftHost4 = self.addHost( 'h4' )
        rightHost5 = self.addHost( 'h5' )
        rightHost6 = self.addHost( 'h6' )
        rightHost7 = self.addHost( 'h7' )
        rightHost8 = self.addHost( 'h8' )

        # Add switches, name and numbers 
        leftSwitch1 = self.addSwitch( 's1' )
        leftSwitch2 = self.addSwitch( 's2' )
        rightSwitch3 = self.addSwitch( 's3' )
        rightSwitch4 = self.addSwitch( 's4' )
        leftSwitch5 = self.addSwitch( 's5' )
        rightSwitch6 = self.addSwitch( 's6' )
        centralSwitch7 = self.addSwitch( 's7' )
        

        # Add links
        #Host1 --- Switch1
        self.addLink( leftHost1, leftSwitch1 )
        #Host2 --- Switch1
        self.addLink( leftHost2, leftSwitch1 )
        #Switch1 --- Switch2 & Switch5
        #self.addLink( leftSwitch1, leftSwitch2 )
        self.addLink( leftSwitch1, leftSwitch5 )
        #Host3 --- Switch2
        self.addLink( leftHost3, leftSwitch2 )
        #Host4 --- Switch2
        self.addLink( leftHost4, leftSwitch2 )
        #Switch2 --- Switch5
        self.addLink( leftSwitch2, leftSwitch5 )
        #Switch5 --- Switch6 & Switch7
        #self.addLink( leftSwitch5, rightSwitch6 )
        self.addLink( leftSwitch5, centralSwitch7 )
        #Switch6 --- Switch3 & Switch4 & Switch 7
        self.addLink( rightSwitch6, rightSwitch3 )
        self.addLink( rightSwitch6, rightSwitch4 )
        self.addLink( rightSwitch6, centralSwitch7 )
        #Switch3 --- Host5 & Host6
        self.addLink( rightSwitch3, rightHost5 )
        self.addLink( rightSwitch3, rightHost6 )
        #Switch4 --- Host7 & Host8
        self.addLink( rightSwitch4, rightHost7 )
        self.addLink( rightSwitch4, rightHost8 )
        #Switch3 --- Switch4
        #self.addLink( rightSwitch3, rightSwitch4 )


def run():
    net = Mininet(topo=BasicNoSDNTopo(), controller=None, autoSetMacs=True)
    net.start()

    # Add basic flows without specifying the table value and check the flow working via the ovs-appctl command
    info( '*** sh ovs-ofctl dump-flows s1\n')
    info( '*** sh ovs-ofctl add-flow s1 action=normal\n')
    info( '*** sh ovs-ofctl dump-flows s1\n')
    # Hosts 1 and 2 able to ping each other now
    info( '*** h1 ping h2 -c 3\n')
    # Add basic flows to all remaining switches
    info( '*** sh ovs-ofctl add-flow s2 action=normal\n')
    info( '*** sh ovs-ofctl add-flow s3 action=normal\n')
    info( '*** sh ovs-ofctl add-flow s4 action=normal\n')
    info( '*** sh ovs-ofctl add-flow s5 action=normal\n')
    info( '*** sh ovs-ofctl add-flow s6 action=normal\n')
    info( '*** sh ovs-ofctl add-flow s7 action=normal\n')
    # Confirm all hosts able to ping each other now
    net.pingAll()

    CLI(net)
    net.stop()

# if the script is run directly (sudo python basictopo_no_sdn.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()