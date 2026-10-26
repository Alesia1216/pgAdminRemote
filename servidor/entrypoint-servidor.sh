#!/bin/bash

# Firewall inicial: solo loopback, conexiones ya establecidas, SSH y Odoo
iptables -F INPUT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 8069 -j ACCEPT
iptables -P INPUT DROP

# SSH para Remote-SSH
ssh-keygen -A
/usr/sbin/sshd

# PostgreSQL en segundo plano
docker-entrypoint.sh postgres &

# Parada limpia al apagar el contenedor
trap 'gosu postgres pg_ctl stop -D $PGDATA -m fast; exit 0' TERM INT
tail -f /dev/null &
wait $!