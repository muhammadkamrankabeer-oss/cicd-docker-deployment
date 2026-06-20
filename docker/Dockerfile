# =========================
# Stage 1: Build Dependencies
# =========================
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt


# =========================
# Stage 2: Runtime Image
# =========================
FROM python:3.11-slim

WORKDIR /app

# Install curl for container health checks
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder stage
COPY --from=builder /install /usr/local

# Copy application source code
COPY app/ /app

# Create non-root user
RUN useradd -m appuser

USER appuser

EXPOSE 5000

# Container health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD curl --fail http://localhost:5000/health || exit 1

# Start application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
