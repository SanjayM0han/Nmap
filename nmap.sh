#!/bin/bash


    
    for i in {1..20}; do
        
        result=$(nmap -sP "192.168.85.$i")

        
        mysql -u root -p"" -D network_scans -e "INSERT INTO scan_results (ip_address, result) VALUES ('192.168.85.$i', '$result');"
    done