workers = 2
control_plane = 1
gpu_available = True
ram = 40

cluster_ready = (
    workers >= 2
    and control_plane == 1
    and gpu_available
    and ram >= 32
)

if cluster_ready:
    print("Cluster Ready")
else:
    print("Cluster Not Ready")


# Creating a status variable using a conditional (ternary) expression.
# This is for practice, so the result is intentionally printed twice.
status = "Cluster Ready" if cluster_ready else "Cluster Not Ready"

print(status)