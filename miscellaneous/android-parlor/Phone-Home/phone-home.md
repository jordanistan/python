# Here is an example Python script that creates a reverse SSH connection to a server using an SSH key that is encoded in base64:

```python 
import base64
import paramiko

# Read the base64-encoded private key
with open('id_rsa.b64', 'r') as f:
  encoded_key = f.read()

# Decode the private key
private_key = base64.b64decode(encoded_key)

# Load the private key
private_key = paramiko.RSAKey.from_private_key(io.BytesIO(private_key))

# Set the server IP address and port
server_ip = 'YOUR_SERVER_IP_ADDRESS'
server_port = 22

# Set the username for the server
username = 'YOUR_SERVER_USERNAME'

# Create a Paramiko SSH client
client = paramiko.SSHClient()

# Add the server's host key to the client's known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
client.connect(server_ip, port=server_port, username=username, pkey=private_key)

# Create a reverse SSH tunnel to the server
tunnel = client.get_transport().open_channel("direct-tcpip", ("127.0.0.1", 8000), ("127.0.0.1", 8080))

# Keep the connection alive
while True:
  pass

# Close the connection
client.close()
```


To use this script, you will need to do the following:

Install the paramiko library. You can do this by running the following command:

```bash
pip install paramiko
```

Encode the private key file in base64 using the base64 command-line tool. 

For example:
```bash
base64 ~/.ssh/id_rsa > id_rsa.b64
```
