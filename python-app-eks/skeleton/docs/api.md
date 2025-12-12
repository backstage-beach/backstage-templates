# API Reference

## Endpoints

### GET /

Returns the application status message.

**Response:**
```
${{ values.name }} is running!
```

---

### GET /health

Kubernetes liveness probe endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

---

### GET /ready

Kubernetes readiness probe endpoint.

**Response:**
```json
{
  "status": "ready"
}
```

---

### GET /s3/buckets

Lists S3 buckets accessible with the current AWS credentials.

!!! note
    This endpoint requires valid AWS credentials. In EKS, use IAM Roles for Service Accounts (IRSA).

**Success Response:**
```json
{
  "buckets": ["bucket-1", "bucket-2", "bucket-3"]
}
```

**Error Response (500):**
```json
{
  "error": "NoCredentialProviders: no valid providers in chain"
}
```
