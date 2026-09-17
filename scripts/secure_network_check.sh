#!/usr/bin/env bash

# Secure Network Check Script
# Syfte: Det här skriptet kontrollerar nätverket och lokala tjänster på ett säkert sätt.
# Säkerhetsgräns: Kontrollerna gäller endast den egna Linux-miljön och localhost.

date +%T

LOG_FILE="secure_network_check.log"
TEST_PORT="8080"
TEST_HOST="127.0.0.1"
DNS_HOST="google.com"
OK_COUNT=0
FAIL_COUNT=0
CHECKS=("dns" "service" "ports")

log() {
echo "$(date +%T) - $1" >> "$LOG_FILE"
}

show_environment() {
    ip address
    ip route
}

check_dns() {
    if [ -z "$DNS_HOST" ]
    then
        log "[WARN] DNS host är tom."
        return
    fi

    if getent hosts "$DNS_HOST" > /dev/null
    then
        log "[OK] DNS fungerar."
        OK_COUNT=$((OK_COUNT + 1))
    else
        log "[FAIL] DNS fungerar inte."
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
}

check_local_service() {
    if curl -I "http://$TEST_HOST:$TEST_PORT" > /dev/null
    then
        log "[OK] Local service fungerar."
        OK_COUNT=$((OK_COUNT + 1))
    else
        log "[FAIL] Local service fungerar inte."
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
}

show_ports() {
    ss -tuln
    log "[INFO] Port overview completed."
}

run_checks() {
    for check in "${CHECKS[@]}"
    do
        log "[INFO] Running check: $check"
        done
}

final_summary() {
    echo "OK: $OK_COUNT"
    echo "FAIL: $FAIL_COUNT"
    echo "LOG: $LOG_FILE"

    if [ "$FAIL_COUNT" -eq 0 ]
    then
        exit 0
    else
        exit 1
    fi
}

log "[INFO] Kontroll startad."

show_environment
check_dns
check_local_service
show_ports
run_checks
final_summary
