# Base container image with OS, updates, and labels

FROM library/fedora:latest AS base

LABEL maintainer="DataStax Docs Team"

VOLUME [ "/workspace" ]

WORKDIR /workspace

# Disable until caching is in place on CI
# RUN dnf update --refresh -y \
#   && dnf clean all

# Spellcheck tooling

FROM base as spellchecker

RUN dnf install -y aspell aspell-en \
  && dnf clean all

# Build tooling

FROM base as builder

RUN dnf install -y nodejs \
  && dnf clean all

COPY package.json /workspace/package.json

RUN npm install