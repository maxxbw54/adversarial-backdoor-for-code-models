FROM debian:stretch

# Update sources to use the archived repositories
RUN echo "deb http://archive.debian.org/debian/ stretch main contrib non-free" > /etc/apt/sources.list \
    && echo "deb http://archive.debian.org/debian-security/ stretch/updates main contrib non-free" >> /etc/apt/sources.list \
    && apt-get -o Acquire::Check-Valid-Until=false update \
    && apt-get install -y --no-install-recommends parallel jq unzip curl ca-certificates
    
COPY task/entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]
