from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import OVSSwitch

class AdvancedNoSDNTopo( Topo ):

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts, name and numbers 
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
        host5 = self.addHost( 'h5' )
        host6 = self.addHost( 'h6' )
        host7 = self.addHost( 'h7' )
        host8 = self.addHost( 'h8' )
        host9 = self.addHost( 'h9' )
        host10 = self.addHost( 'h10' )
        host11 = self.addHost( 'h11' )
        host12 = self.addHost( 'h12' )
        host13 = self.addHost( 'h13' )
        host14 = self.addHost( 'h14' )
        host15 = self.addHost( 'h15' )
        host16 = self.addHost( 'h16' )
        loghost17 = self.addHost( 'h17' )

        # Add switches, name and numbers 
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
        switch5 = self.addSwitch( 's5' )
        switch6 = self.addSwitch( 's6' )
        switch7 = self.addSwitch( 's7' )
        switch8 = self.addSwitch( 's8' )
        switch9 = self.addSwitch( 's9' )
        switch10 = self.addSwitch( 's10' )
        switch11 = self.addSwitch( 's11' )
        switch12 = self.addSwitch( 's12' )
        switch13 = self.addSwitch( 's13' )
        switch14 = self.addSwitch( 's14' )
        switch15 = self.addSwitch( 's15' )
        

        # Add links
        #Host1 --- Switch1
        self.addLink( host1, switch1 )
        #Host2 --- Switch1
        self.addLink( host2, switch1 )
        #Host3 --- Switch2
        self.addLink( host3, switch2 )
        #Host4 --- Switch2
        self.addLink( host4, switch2 )
        #Host5 --- Switch3
        self.addLink( host5, switch3 )
        #Host6 --- Switch3
        self.addLink( host6, switch3 )
        #Host7 --- Switch4
        self.addLink( host7, switch4 )
        #Host8 --- Switch4
        self.addLink( host8, switch4 )
        #Host9 --- Switch5
        self.addLink( host9, switch5 )
        #Host10 --- Switch5
        self.addLink( host10, switch5 )
        #Host11 --- Switch6
        self.addLink( host11, switch6 )
        #Host12 --- Switch6
        self.addLink( host12, switch6 )
        #Host13 --- Switch7
        self.addLink( host13, switch7 )
        #Host14 --- Switch7
        self.addLink( host14, switch7 )
        #Host15 --- Switch8
        self.addLink( host15, switch8 )
        #Host16 --- Switch8
        self.addLink( host16, switch8 )
        #Switch9 --- Switch1 & Switch2
        self.addLink( switch9, switch1 )
        self.addLink( switch9, switch2 )
        #Switch10 --- Switch3 & Switch4
        self.addLink( switch10, switch3 )
        self.addLink( switch10, switch4 )
        #Switch11 --- Switch5 & Switch6
        self.addLink( switch11, switch5 )
        self.addLink( switch11, switch6 )
        #Switch12 --- Switch7 & Switch8
        self.addLink( switch12, switch7 )
        self.addLink( switch12, switch8 )
        #Switch13 --- Switch9 & Switch10
        self.addLink( switch13, switch9 )
        self.addLink( switch13, switch10 )
        #Switch14 --- Switch11 & Switch12
        self.addLink( switch14, switch11 )
        self.addLink( switch14, switch12 )
        #Switch15 --- Switch13 & Switch14 & Host17
        self.addLink( switch15, switch13 )
        self.addLink( switch15, switch14 )
        self.addLink( switch15, loghost17 )


def run():
    net = Mininet(topo=BasicNoSDNTopo(), controller=None, autoSetMacs=True)
    net.start()

    # Add basic flows without specifying the table value and check the flow working via the ovs-appctl command
    #info( '*** sh ovs-ofctl dump-flows s1\n')
    #leftSwitch1.dpctl("add-flow action=normal")
    #info( '*** sh ovs-ofctl add-flow s1 action=normal\n')
    #info( '*** sh ovs-ofctl dump-flows s1\n')
    # Hosts 1 and 2 able to ping each other now
    #info( '*** h1 ping h2 -c 3\n')
    # Add basic flows to all remaining switches
    #info( '*** sh ovs-ofctl add-flow s2 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s3 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s4 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s5 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s6 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s7 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s8 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s9 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s10 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s11 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s12 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s13 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s14 action=normal\n')
    #info( '*** sh ovs-ofctl add-flow s15 action=normal\n')
    # Confirm all hosts able to ping each other now
    #net.pingAll()

    CLI(net)
    net.stop()

# if the script is run directly (sudo python basictopo_no_sdn.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()