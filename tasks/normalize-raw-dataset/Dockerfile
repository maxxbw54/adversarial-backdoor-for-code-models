FROM python:3.7.3

# FROM https://github.com/github/CodeSearchNet/blob/b1bf7b06908762011563106026c97c75c26d5bd1/function_parser/Dockerfile
RUN touch /etc/inside-container

RUN set -ex && pip3 install --upgrade pip
RUN set -ex && pip3 --no-cache-dir install --upgrade jupyter\
    tree_sitter \
    requests \
    pyhive \
    tqdm \
    pandas \
    python-arango \
    docopt \
    elasticsearch \
    dpu_utils

RUN mkdir -p /src/vendor
RUN mkdir -p /src/build
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-python.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-javascript.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-typescript.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-go.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-ruby.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-java.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-cpp.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-c-sharp.git
RUN cd /src/vendor && git clone https://github.com/tree-sitter/tree-sitter-php.git
# checkout certain version v20 of php as the latest one is using different repo structure
RUN cd /src/vendor/tree-sitter-php && git checkout 0a99dec
# checkout certain version v20 of php as the latest one is using different repo structure
RUN cd /src/vendor/tree-sitter-php && git checkout 0a99dec

RUN echo "deb http://archive.debian.org/debian/ stretch main contrib non-free" > /etc/apt/sources.list \
    && echo "deb http://archive.debian.org/debian-security/ stretch/updates main contrib non-free" >> /etc/apt/sources.list \
    && apt-get -o Acquire::Check-Valid-Until=false update \
    && apt-get install --no-install-recommends -y jq parallel

RUN set -ex && pip3 --no-cache-dir install --upgrade sentencepiece javalang fissix requests

COPY vendor/CodeSearchNet/function_parser/ /src/function-parser/

RUN cd /src/function-parser/script && python setup.py
WORKDIR /src/function-parser

COPY task/entrypoint.sh /src/entrypoint.sh

ENTRYPOINT [ "/src/entrypoint.sh" ]
