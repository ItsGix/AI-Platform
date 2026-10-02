# Exercise 1: Gaming PC
cpu_model = "AMD Ryzen 9 9850X3D"
ram_size = 32  # in GB
gpu_model = "NVIDIA GeForce RTX 4090"
windows_version = "Windows 11 Pro"
pc_specs = (
    f"CPU: {cpu_model}\n"
    f"RAM: {ram_size}GB\n"
    f"GPU: {gpu_model}\n"
    f"OS: {windows_version}"
)

# Exercise 2: k3s AI cluster setup
cluster_name = "AI-Platform-Cluster"
control_plane_nodes = 1
worker_nodes = 2
gpu_nodes = 1
kubernetes_version = "v1.35.5+k3s1"
cluster_specs = (
    f"Cluster Name: {cluster_name}\n"
    f"Control Plane Nodes: {control_plane_nodes}\n"
    f"Worker Nodes: {worker_nodes}\n"
    f"GPU Nodes: {gpu_nodes}\n"
    f"Kubernetes Version: {kubernetes_version}"
)

# Exercise 3: Current usages (learning Floats)
cpu_utilization = 75.5  # in percentage
ram_utilization = 60.2  # in percentage
gpu_temperature = 65.0  # in Celsius
usages = (
    f"CPU Utilization: {cpu_utilization}%\n"
    f"RAM Utilization: {ram_utilization}%\n"
    f"GPU Temperature: {gpu_temperature}°C"
)

# Exercise 4: Booleans
internet_connected = True
docker_running = True
gpu_available = True
cloudflare_tunnel_connected = False
boolean_status = (
    f"Internet Connected: {internet_connected}\n"
    f"Docker Running: {docker_running}\n"
    f"GPU Available: {gpu_available}\n"
    f"Cloudflare Tunnel Connected: {cloudflare_tunnel_connected}"
)

print("=== PC Specs ===")
print(pc_specs)
print()
print("=== Cluster Specs ===")
print(cluster_specs)
print()
print("=== Current Usages ===")
print(usages)
print()
print("=== Status ===")
print(boolean_status)
