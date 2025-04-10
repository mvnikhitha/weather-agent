import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

# Config
api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME", "weather-agent-index")
dimension = 768  # Updated to match embedding-001 output

# Initialize Pinecone client
pc = Pinecone(api_key=api_key)

# Free plan-compatible serverless spec
spec = ServerlessSpec(cloud="aws", region="us-east-1")

# Check if index exists
existing_indexes = pc.list_indexes().names()
if index_name in existing_indexes:
    # Check dimension of existing index
    description = pc.describe_index(index_name)
    existing_dimension = description.dimension

    if existing_dimension != dimension:
        print(f"[WARNING] Index '{index_name}' has dimension {existing_dimension}, but expected {dimension}.")
        print(f"[INFO] Deleting index '{index_name}' to recreate with correct dimension.")
        pc.delete_index(index_name)

if index_name not in pc.list_indexes().names():
    print(f"[INFO] Creating Pinecone index: {index_name} (dim: {dimension})")
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",
        spec=spec
    )
else:
    print(f"[INFO] Pinecone index '{index_name}' already exists and is compatible.")

# Connect to index
index = pc.Index(index_name)
