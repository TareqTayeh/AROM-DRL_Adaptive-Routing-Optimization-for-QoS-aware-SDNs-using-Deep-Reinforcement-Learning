#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info, lg
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.util import waitListening
import time

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6653)

    info( '*** Add switches\n')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(s1, h2)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    net.addLink(h7, s4)
    net.addLink(h8, s4)
    net.addLink(h9, s5)
    net.addLink(h10, s5)
    net.addLink(h11, s6)
    net.addLink(h12, s6)
    net.addLink(h13, s7)
    net.addLink(h14, s7)
    net.addLink(h15, s8)
    net.addLink(h16, s8)
    net.addLink(s7, s12)
    net.addLink(s12, s8)
    net.addLink(s5, s11)
    net.addLink(s11, s6)
    net.addLink(s3, s10)
    net.addLink(s10, s4)
    net.addLink(s1, s9)
    net.addLink(s9, s2)
    net.addLink(s9, s13)
    net.addLink(s13, s10)
    net.addLink(s11, s14)
    net.addLink(s14, s12)
    net.addLink(s13, s15)
    net.addLink(s15, s14)
    net.addLink(h17, s15)
    net.addLink(s1, s2)
    net.addLink(s3, s4)
    net.addLink(s5, s6)
    net.addLink(s7, s8)
    net.addLink(s11, s12)
    net.addLink(s9, s10)
    net.addLink(s13, s14)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s3').start([c0])
    net.get('s9').start([c0])
    net.get('s4').start([c0])
    net.get('s10').start([c0])
    net.get('s5').start([c0])
    net.get('s15').start([c0])
    net.get('s11').start([c0])
    net.get('s6').start([c0])
    net.get('s14').start([c0])
    net.get('s12').start([c0])
    net.get('s1').start([c0])
    net.get('s7').start([c0])
    net.get('s2').start([c0])
    net.get('s8').start([c0])
    net.get('s13').start([c0])

    info( '*** Post configure switches and hosts\n')

    info( '*** pingall\n')
    net.pingAll()

    #hosts = net.hosts
    #server = {hosts[ 5 ],hosts[ 6 ],hosts[ 7 ]}


    #info( '*** Establishing D-ITG Log Host\n')
    #h7.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    #h7.cmdPrint('./ITGLog &')# if having trouble try running with 0>/dev/null &'
    #h7.cmdPrint('echo $!')
    #h7.cmdPrint('h7PID=$!')
    #h7.cmdPrint('echo $h7PID')

    #info( '*** Establishing Destination Servers / Hosts\n')
    #h5.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    #h5.cmdPrint('./ITGRecv &')
    #h5.cmdPrint('h5PID=$!')
    #h5.cmdPrint('echo $h5PID')
    #h6.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    #h6.cmdPrint('./ITGRecv &')
    #h6.cmdPrint('h6PID=$!')
    #h6.cmdPrint('echo $h6PID')

    #this is here to give the ITG Log and Receiver hosts time to launch properly
    #info( '*** ITG Receiver and Log hosts launching ....')
    #time.sleep(30)

    #info( '*** Launching ITGSend in daemon mode\n')
    #h1.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    #h1.cmdPrint('./ITGSend -Q')
    #h2.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    #h2.cmdPrint('./ITGSend -Q')

    # Ensure that 'script_file_h1toh5' is under '~/D-ITG-2.8.1-r1023/bin'
    #info( '*** Running D-ITG Traffic Flows\n')
    #h1.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    #h1.cmdPrint('./ITGSend script_file_h1toh5 -l h1send_log_file -L 10.0.0.7 UDP -X 10.0.0.7 UDP -x h1toh5_recv_log_file &')
    #h1.cmdPrint('h1PID=$!')
    #h1.cmdPrint('echo $h1PID')
    #h2.cmdPrint('cd ~/D-ITG-2.8.1-r1023/bin')
    #h2.cmdPrint('./ITGSend script_file_h2toh6 -l h2send_log_file -L 10.0.0.7 UDP -X 10.0.0.7 UDP -x h2toh6_recv_log_file &')
    #h2.cmdPrint('h2PID=$!')
    #h2.cmdPrint('echo $h2PID')

    #to be used in conjunction with kill commands.  This provides time for flows to complete prior to kill commands.
    #time.sleep(240)

    #info( '*** Manual CLI - background D-ITG processes for ITGRecv and ITGLog still running...')
    #info( ' to close ITG servers issue the following commands in CLI: ')
    #info( '"> h5 bash"')
    #info( '"$ ps"')
    #info( '"$ kill -INT <enter PID for Recv or Log server here>"')
    #info( 'you will then be instructed to finish with Ctrl-C')
    #info( '"$ exit"')
    #info( ' repeat for all ITGRecv hosts, then for ITGLog host, then type exit to continue to automated ITGDec')
    #CLI(net)

    #h1.cmdPrint('while ps -p $h1PID > /dev/null; do sleep 1; done')

    #kill commands are to be used it the CLI is not initialize above
    #h5.cmdPrint('kill -KILL $h5PID')
    #h6.cmdPrint('kill -KILL $h6PID')
    #h7.cmdPrint('kill -KILL $h7PID')

    #info(' *** ITGDec launching ... this may take a minute.')
    #time.sleep(20)
    #h7.cmdPrint('./ITGDec h1toh5_recv_log_file')
    #h7.cmdPrint('./ITGDec h1send_log_file')
    #h7.cmdPrint('./ITGDec h2toh6_recv_log_file')
    #h7.cmdPrint('./ITGDec h2send_log_file')

    info( '*** Starting CLI\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

