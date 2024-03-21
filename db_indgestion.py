import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

# Create a document
def create_document(collection, document_id, data):
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.set(data)
    print(f"Document '{document_id}' created successfully.")

# Read a document
def read_document(collection, document_id):
    doc_ref = db.collection(collection).document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
    else:
        print("Document does not exist.")

# Update a document
def update_document(collection, document_id, data):
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(data)
    print(f"Document '{document_id}' updated successfully.")

# Delete a document
def delete_document(collection, document_id):
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.delete()
    print(f"Document '{document_id}' deleted successfully.")

# Query documents
def query_documents(collection, query):
    docs = db.collection(collection).where(*query).stream()
    for doc in docs:
        print(f"Document ID: {doc.id}, Data: {doc.to_dict()}")

# Example usage
if __name__ == "__main__":
    # Create a document
    create_document("users", "user1", {"name": "John", "age": 30, "city": "New York"})

    # Read a document
    read_document("users", "user1")

    # Update a document
    update_document("users", "user1", {"city": "San Francisco"})

    # Read updated document
    read_document("users", "user1")

    # Query documents
    query_documents("users", [("age", ">=", 25)])
