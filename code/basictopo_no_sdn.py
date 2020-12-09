#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8',
                   controller=None,
                   autoSetMacs=True)

    info( '*** Add switches\n')
    s7 = net.addSwitch('s7', cls=OVSSwitch)
    s3 = net.addSwitch('s3', cls=OVSSwitch)
    s5 = net.addSwitch('s5', cls=OVSSwitch)
    s1 = net.addSwitch('s1', cls=OVSSwitch)
    s4 = net.addSwitch('s4', cls=OVSSwitch)
    s6 = net.addSwitch('s6', cls=OVSSwitch)
    s2 = net.addSwitch('s2', cls=OVSSwitch)

    info( '*** Add hosts\n')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s2, s5)
    net.addLink(s1, s5)
    net.addLink(s5, s7)
    net.addLink(s7, s6)
    net.addLink(s6, s3)
    net.addLink(s6, s4)
    net.addLink(s3, h5)
    net.addLink(s3, h6)
    net.addLink(s4, h7)
    net.addLink(s4, h8)

    info( '*** Starting network\n')
    net.build()
    # info( '*** Starting controllers\n')
    # for controller in net.controllers:
    #     controller.start()

    # info( '*** Starting switches\n')
    # net.get('s7').start([])
    # net.get('s3').start([])
    # net.get('s5').start([])
    # net.get('s1').start([])
    # net.get('s4').start([])
    # net.get('s6').start([])
    # net.get('s2').start([])

    # info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

