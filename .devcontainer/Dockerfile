# Base image
FROM python:3.12

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=1000

# Create group and user
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd \
        --uid ${USER_UID} \
        --gid ${USER_GID} \
        --create-home \
        --shell /bin/bash \
        ${USERNAME}


# Set working directory
WORKDIR /python_work

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1


# Give the user ownership of the workspace
RUN chown -R ${USERNAME}:${USERNAME} /python_work

# Switch to non-root user
USER ${USERNAME}

# Default command
CMD ["bash"]




