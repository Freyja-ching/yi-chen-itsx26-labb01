failed_logins = 0
ip_counts = {}
skipped_rows = 0

with open("data/auth.log", "r") as file:
    for line in file:
        source_found = False
        parts = line.split()

        if "Failed login" in line:
            failed_logins += 1

        for part in parts:
            if part.startswith("src="):
                ip = part.split("=")[1]
                source_found = True

                if ip in ip_counts:
                        ip_counts[ip] += 1
                else:
                        ip_counts[ip] = 1

        if not source_found:
            skipped_rows += 1
            print("Överhoppad rad: saknar source IP")

print("Misslyckade inloggningar:", failed_logins)
print("IP-antal:", ip_counts)                        
                
suspicious_ips = []

with open("data/suspicious_ips.txt", "r") as file:
    for line in file:
        ip = line.strip()
        suspicious_ips.append(ip)

print("Misstänkta IP-adresser:", suspicious_ips)

for ip in ip_counts:
    if ip in suspicious_ips:
        print("Match med indikatorlista:", ip)

unauthorized_requests = 0
access_ip_counts = {}

with open("data/access.log", "r") as file:
    for line in file:
        if "status=401" in line:
            unauthorized_requests += 1

        parts = line.split()

        for part in parts:
            if part.startswith("src="):
                ip = part.split("=")[1]

                if ip in access_ip_counts:
                    access_ip_counts[ip] += 1
                else:
                    access_ip_counts[ip] = 1

print("401-svar:", unauthorized_requests)
print("IP-antal i access.log:", access_ip_counts)

with open("output/security_report.txt", "w") as file:
    file.write("Säkerhetsrapport\n")
    file.write(f"Misslyckade inloggningar: {failed_logins}\n")
    file.write(f"Misstänkta IP-adresser: {suspicious_ips}\n")

    for ip, count in ip_counts.items():
        file.write(f"{ip}: {count}\n")

    file.write("Matchningar med indikatorlistan:\n")

    for ip in ip_counts:
        if ip in suspicious_ips:
            file.write(f"{ip}\n")

    file.write(f"401-svar: {unauthorized_requests}\n")
    file.write(f"Överhoppade rader: {skipped_rows}\n")