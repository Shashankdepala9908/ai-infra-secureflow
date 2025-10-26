CREATE TABLE IF NOT EXISTS flow_audit (
  id SERIAL PRIMARY KEY,
  request_id TEXT,
  created_at TIMESTAMP DEFAULT now(),
  status TEXT
);
