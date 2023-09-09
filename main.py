import paramiko

def create_udp_tunnel(ssh_host, ssh_port, ssh_username, ssh_password, local_host, local_port, remote_host, remote_port):
    # Establish SSH connection
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ssh_host, ssh_port, ssh_username, ssh_password)

    # Create a UDP tunnel
    transport = ssh_client.get_transport()
    transport.request_port_forward('', local_port, remote_host, remote_port, "udp")

    # Print tunnel details
    print(f"UDP tunnel created: {local_host}:{local_port} -> {remote_host}:{remote_port} via {ssh_host}:{ssh_port}")

    # Keep the program running until interrupted
    while True:
        pass

    # Close the SSH connection
    ssh_client.close()

# Enter your SSH and tunnel details here
ssh_host = 'your_ssh_host'
ssh_port = 22
ssh_username = 'your_ssh_username'
ssh_password = 'your_ssh_password'
local_host = '127.0.0.1'  # Local machine's IP address
local_port = 12345  # Local port for the tunnel
remote_host = 'remote_server_ip'  # IP address of the remote server
remote_port = 54321  # Port on the remote server to forward to

# Call the function to create the UDP tunnel
create_udp_tunnel(ssh_host, ssh_port, ssh_username, ssh_password, local_host, local_port, remote_host, remote_port)
