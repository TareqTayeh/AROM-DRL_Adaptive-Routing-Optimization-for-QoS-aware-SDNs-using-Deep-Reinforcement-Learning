#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(s1, h2)
    net.addLink(s1, s5)
    net.addLink(s2, s5)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    net.addLink(s1, s2)
    net.addLink(s3, s6)
    net.addLink(s6, s4)
    net.addLink(s4, s3)
    net.addLink(h7, s4)
    net.addLink(s4, h8)
    net.addLink(s6, s7)
    net.addLink(s5, s7)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s5').start([c0])
    net.get('s2').start([c0])
    net.get('s6').start([c0])
    net.get('s4').start([c0])
    net.get('s1').start([c0])
    net.get('s7').start([c0])
    net.get('s3').start([c0])

    info( '*** Post configure switches and hosts\n')

    info( '*** Establishing D-ITG Log Host\n')
    h7.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    h7.cmdPrint('./ITGLog')

    info( '*** Establishing Destination Servers / Hosts\n')
    h5.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    h5.cmdPrint('./ITGRecv')
    h6.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    h6.cmdPrint('./ITGRecv')

    info( '*** Running D-ITG Traffic Flows\n')
    h1.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    h1.cmdPrint('./ITGSend script_file_h1toh5 -l h1send_log_file -L 10.0.0.4 UDP -X 10.0.0.4 UDP -x h1toh5_recv_log_file &')
    h2.cmdPrint('./ITGSend script_file_h2toh6 -l h2send_log_file -L 10.0.0.4 UDP -X 10.0.0.4 UDP -x h2toh6_recv_log_file')

    info( '*** Starting CLI\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

