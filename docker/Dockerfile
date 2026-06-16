# Stage 1: Build dependencies
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# Stage 2: Runtime image
FROM python:3.10-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY app/ /app

# Create non-root user
RUN useradd -m appuser
USER appuser

# Expose port
EXPOSE 5000

# Run with gunicorn (production WSGI server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
