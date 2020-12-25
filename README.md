# AROM-DRL: Adaptive Routing Optimization Model for QoS-Aware Software Defined Networks using Deep Reinforcement Learning

<p float="left">
 <img src="https://img.shields.io/badge/Floodlight-v1.2-brightgreen"/>
 <img src="https://img.shields.io/badge/Mininet-v2.2.1-blue"/>
 <img src="https://img.shields.io/badge/DITG-v2.8.1-orange"/>
 <img src="https://img.shields.io/badge/Python-v2.7.6-yellow"/>
 <img src="https://img.shields.io/badge/Java-v7-red"/>
 <img src="https://img.shields.io/badge/Ubuntu-v14.04-lightgrey"/>
</p>

### Abstract
Software Defined Networking (SDN) has been recognized as the next-generation networking paradigm that decouples the data plane and control plane, allowing network resources to be managed by a logically centralized controller. The inclusion of Machine Learning (ML) techniques can improve network optimization and the automated provisioning of the network's service capabilities, as well as enhancing the SDN's ability to fulfil Quality of Service (QoS) requirements in a variety of applications. In particular, the recent emergence of Deep Reinforcement Learning (DRL) allowed more complex problems with high-dimensional state and action space to be solved, making them ideal for Routing Optimization (RO) in complex network environments with rapid changes in continuous time. In this paper, we introduce an Adaptive RO Model for QoS-aware SDNs using DRL (AROM-DRL). AROM-DRL dynamically considers various QoS parameters, such as latency, throughput, packet loss, and jitter, in combination with statically determined parameters, to generate a powerful and dynamically determined action-reward strategy for the DRL system as part of an iterative RO mechanism. In a QoS-aware SDN system, network operators and service providers can use AROM-DRL to assist in offering high-quality services to increase customer satisfaction and reduce customer churn. Future work will include an AROM-DRL implementation to be evaluated against both SDN and non-SDN benchmarks, which have been discussed, implemented, and evaluated in this paper.

### User Manual
This is all found in `Code_User_Manual`.

<ol>
  <li>Launch Oracle VM Virtual box, followed by launching the Floodlight-Ubuntu VM, which is already configured with Mininet v.2.2.1, Floodlight v1.1, and OpenvSwitch. 
  	<ul>
  		<li> https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/8650780/Floodlight+VM </li>
  	</ul>
  </li>
  <li>Upgrade Floodlight v1.1 to Floodlight v1.2
  	<ul>
  		<li> https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/1343544/Installation+Guide </li>
  	</ul>
  </li>
  <li>Download and install D-ITG
    <ul>
      <li> http://sdnopenflow.blogspot.com/2015/05/using-of-d-itg-traffic-generator-in.html </li>
    </ul>
  </li>
  <li>Place our code folder (or git clone repo) inside the launched VM </li>
  <li>To build and run the non-SDN network described in the paper:
    <ul>
      <li> Navigate to code by running `cd ~/AROM-DRL_Adaptive-Routing-Optimization-for-QoS-aware-SDNs-using-Deep-Reinforcement-Learning/code/` </li>
      <li> Run `sudo python advancedtopo_no_sdn.py` in terminal </li>
      <li> Once the network is built, you will be prompted with the Mininet CLI. Run `sh ovs-ofctl add-flow <switch> action=normal`  in the Mininet CLI for every single switch (s1, s2, … , s15) to manually add flows to the flow table and turn them into normal L2 devices. E.g. for switch 1: `sh ovs-ofctl add-flow s1 action=normal`  </li>
      <li> Now proceed to step 8. Otherwise, proceed to step 6 to build SDN topo </li>
    </ul>
  </li>
  <li>Launch the Floodlight controller in Terminal (Only applies when you are running the SDN simulation)
    <ul>
      <li> https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/8650780/Floodlight+VM </li>
    </ul>
  </li>
  <li>Place our code folder (or git clone repo) inside the launched VM </li>
  <li>To build and run the SDN network described in the paper:
    <ul>
      <li> Navigate to code by running `cd ~/AROM-DRL_Adaptive-Routing-Optimization-for-QoS-aware-SDNs-using-Deep-Reinforcement-Learning/code/` </li>
      <li> Run `sudo python advancedtopo_with_sdn.py` in terminal </li>
      <li> You will then be prompted with the Mininet CLI, proceed with Step 8 </li>
    </ul>
  </li>
</ol>
