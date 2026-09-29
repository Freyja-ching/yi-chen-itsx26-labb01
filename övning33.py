import re

def count_ip_addresses(loggrader):
    ip_counts = {}

    for line in loggrader:
        match = re.search(r"\d+\.\d+\.\d+\.\d+", line)

        if match:
            ip = match.group()

            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

    sorted_ips = sorted(
        ip_counts.items(),     # Hämtar IP-adresser + antal
        key=lambda x: x[1],    # Sorterar efter antal
        reverse=True           # Störst till minst
    )

    top_3 = sorted_ips[:3]

    return top_3

with open("onsdag.example.log", "r") as file:
    loggrader = file.readlines() 

top_3 = count_ip_addresses(loggrader)

print(top_3)