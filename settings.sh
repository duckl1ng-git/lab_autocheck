#!/bin/bash

sleep 3
clear

INTERFACE="ens3"

try_dhcp() {
    if [ $(ip -br -4 a sh $INTERFACE | awk '{print length($3)}') -ne 0 ]; then
        echo "DHCP Success"
        echo ""
        systemctl start lab_checker.service
        echo "Statring Checker..."
        echo ""
        echo "Go to: http://$(ip -br a sh $INTERFACE | awk '{print substr($3, 0, length($3) - 3)}')/"
        echo ""
        return 0
    else
        echo ""
        echo "DHCP Failed"
        echo ""
        return 1
    fi
}

is_valid() {
    local ip=$1
    if [[ $ip =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
        for octet in $(echo $ip | tr '.' ' '); do
            if ((octet < 0 || octet > 255)); then
                return 1
            fi
        done
        return 0
    else
        return 1
    fi
}

manual_ip_set() {
    ip addr flush $INTERFACE
    
    while true; do
        echo "Enter IP: "
        read IP
        if is_valid $IP; then
            break
        else
            echo "Invalid IP address format. Please try again"
        fi
    done

    while true; do
        echo "Enter mask (for example 255.255.255.0): "
        read NETMASK
        if is_valid $NETMASK; then
            break
        else
            echo "Invalid IP address format. Please try again"
        fi
    done
    
    while true; do
        echo "Enter gateway: "
        read GATEWAY
        if is_valid $GATEWAY; then
            break
        else
            echo "Invalid IP address format. Please try again"
        fi
    done
    
    echo ""
    echo "Applying..."
    ip addr add $IP/$NETMASK dev $INTERFACE
    ip route add default via $GATEWAY
    echo "nameserver 8.8.8.8" > /etc/resolv.conf
    echo ""
    echo "Settings applied"
    ip -br addr show $INTERFACE
    echo ""
    systemctl start lab_checker.service
    echo ""
    echo "Go to: http://$(ip -br a sh $INTERFACE | awk '{print substr($3, 0, length($3) - 3)}')/"
    echo ""
}

menu() {
    echo "==================================================="
    echo "                      Settings                     "
    echo "==================================================="
    echo "1. Manual set IP address"
    echo "2. Show Checker status (Press 'q' to quit)"
    echo "3. Download latest updates (Internet access needed)"
    echo "4. Restart Checker"
    echo "---------------------------------------------------"
    read -p "Enter choice (1-5): " CHOICE
    echo ""

    case $CHOICE in
        1)
            manual_ip_set
            ;;
        2)
            systemctl status lab_checker.service
            ;;
        3)
            git pull
            echo ""
            ;;
        4)
            systemctl restart lab_checker.service
            echo "Service restarted"
            ;;
        *)
            echo "Invalid choice! Try again"
            ;;
    esac
    echo ""
    echo "Press Enter to return menu"
    read
    clear
    menu
}

try_dhcp

if [ $? -ne 0 ]; then
    echo "To start Checker set IP address manually ('1' option in menu)"
fi

menu
