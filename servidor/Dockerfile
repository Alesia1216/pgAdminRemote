FROM postgres:15

RUN apt-get update && apt-get install -y --no-install-recommends \
      openssh-server iptables iproute2 net-tools nano curl wget ca-certificates tar procps libatomic1 \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /run/sshd \
    && echo 'root:practica' | chpasswd \
    && sed -Ei 's/^#?PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -Ei 's/^#?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && echo 'export PGDATA=/var/lib/postgresql/data' >> /root/.bashrc

COPY entrypoint-servidor.sh /usr/local/bin/entrypoint-servidor.sh
RUN chmod +x /usr/local/bin/entrypoint-servidor.sh

ENTRYPOINT ["entrypoint-servidor.sh"]