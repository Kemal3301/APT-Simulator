# APT Simulator

## Description

Information from Mitre ATT&CK regarding the APT1 group is as follows:

APT1 used the commands net localgroup,net user, and net group to find accounts on the system.

APT1 has used RAR to compress files before moving them outside of the victim network.

APT1 used a batch script to perform a series of discovery techniques and saves it to a text file.
	
APT1 has collected files from a local victim.

APT1 listed connected network shares.

APT1 has been known to use credential dumping using Mimikatz.

APT1 gathered a list of running processes on the system using tasklist /v.

APT1 used the ipconfig /all command to gather network configuration information.

APT1 used the net use command to get a listing on network connections.

APT1 used the commands net start and tasklist to get a listing of the services on the system.

## Usage

First of all we will run apt1_server.py in server machine. After we will start apt1.py in victim machine.

