# SDN Real-Time Edge Computing with NFV Firewall and Load Balancer

## 1. Introduction

This project demonstrates the integration of **Software-Defined Networking (SDN)** with **Network Function Virtualization (NFV)** for real-time edge computing. SDN enables centralized control over network traffic, while NFV provides dynamic management of virtualized network functions (VNFs), such as firewalls and load balancers, which can be deployed at the network edge.

### Key Technologies:
- **SDN Controller (Ryu)**: To manage traffic flow and enforce security policies.
- **Docker**: To virtualize and run network functions (firewall and load balancer) as containers.
- **Mininet**: To simulate network topology.
- **iptables**: For configuring firewall rules within the Docker container.

## 2. Essence and Use Case

### Essence:
This project showcases how SDN can dynamically manage edge computing resources by deploying VNFs in real-time. The setup is useful in edge networks where traffic is unpredictable, and security policies need to be adjusted dynamically.

### Use Case:
In a real-world scenario, a network administrator could:
- **Deploy a firewall dynamically** to block malicious traffic from specific IP addresses.
- **Deploy a load balancer** to distribute network traffic across multiple servers efficiently.

Such a system is crucial in environments like **5G edge computing**, **smart cities**, or **IoT networks**, where real-time traffic management and security are essential.

## 3. Technologies Used

- **Mininet**: Network simulator.
- **Docker**: Container platform used to run VNFs.
- **Ryu SDN Controller**: OpenFlow-based SDN controller.
- **iptables**: Firewall utility for configuring firewall rules.
- **Python**: Used to write SDN controller scripts.

## 4. Project Setup

### Step 1: Install Docker
On your Mininet VM, install Docker using the following commands:

```bash
sudo apt-get update
sudo apt-get install docker.io
```

### Step 2: Create Load Balancer VNF (Using NGINX)
1. Pull the NGINX Docker image:
```bash
sudo docker pull nginx
```
2. Run the NGINX container:
```bash
sudo docker run -d --name load_balancer -p 8080:80 nginx
```
3. Verify the load balancer is running by visiting:
```bash
curl http://localhost:8080
```

### Step 3: Create Firewall VNF (Using iptables)
1. Run a privileged Ubuntu Docker container:
```bash
sudo docker run -it --privileged --name firewall_vnf2 ubuntu
```
2. Inside the container, install **iptables**:
```bash
apt-get update
apt-get install iptables
```
3. Set up a firewall rule to block traffic from a specific IP:
```bash
iptables -A INPUT -s 10.0.0.1 -j DROP
```
4. Save the Docker container as an image for reuse:
```bash
sudo docker commit firewall_vnf2 firewall_image
```

### Step 4: Set Up Mininet and Ryu SDN Controller
1. Install Ryu SDN controller:
```bash
sudo apt-get install python3-ryu
```
2. Start Mininet with a tree topology:
```bash
sudo mn --topo=tree,depth=2,fanout=2 --controller=remote
```
3. Start the Ryu controller:
```bash
ryu-manager your_controller_script.py
```

### Step 5: Integrating SDN with Docker VNFs
```bash
import os
os.system('sudo docker start firewall_vnf2')
```
This allows SDN to manage VNFs dynamically depending on network traffic or policies.

### 5. Architecture Diagram
Here's a basic diagram of how traffic flows between the SDN controller, the load balancer, and the firewall:
```bash
            +----------------------+
            |    Ryu SDN Controller |
            +----------------------+
                       |
      +----------------+------------------+
      |                                   |
+------------+                     +-------------+
| Load Balancer|                   | Firewall VNF|
|  (NGINX)    |                   |  (iptables)  |
+------------+                     +-------------+
      |                                   |
  +-------------------+           +----------------+
  |                   |           |                |
Host 1            Host 2      Host 3        Host 4
```

### Output
![image](https://github.com/user-attachments/assets/3f433900-36ec-457d-8feb-86e814460e65)


### 6. Future Enhancements
**Traffic Monitoring**: Add monitoring to automate VNF deployment based on real-time traffic patterns.
**Scaling VNFs**: Implement dynamic scaling of load balancers and firewalls based on network load.
**Advanced Firewall Rules**: Include dynamic threat detection and mitigation mechanisms.


### 7. Conclusion
This project demonstrates the integration of SDN with NFV for managing edge computing resources. By virtualizing network functions like firewalls and load balancers using Docker, and dynamically managing them using the Ryu SDN controller, the project provides a scalable, flexible approach to network management.
