FROM python:3.11-slim
RUN useradd -m -u 10001 appuser
WORKDIR /app
# copy the FastAPI code
COPY src /app/src
# install minimal deps
RUN pip install --no-cache-dir fastapi==0.115.2 uvicorn==0.30.6
USER appuser
EXPOSE 6060
CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","6060"]
