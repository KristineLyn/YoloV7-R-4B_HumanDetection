import argparse
import firebase_admin
from firebase_admin import credentials, storage

# Initialize the Firebase app with your credentials JSON file
cred = credentials.Certificate("cfg/deploy/mikky-storage.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'mikky-a0eea.appspot.com'
})

# Create a reference to the storage bucket
bucket = storage.bucket()

def upload_image(image_path, destination_blob_name):
    # The image_path is the path to the image file on your local computer
    # The destination_blob_name is the name you want to give to the file in Firebase Storage

    # Create a blob (reference to a file in Firebase Storage)
    blob = bucket.blob(destination_blob_name)

    # Upload the local image file to Firebase Storage
    blob.upload_from_filename(image_path)

    # Optionally, you can make the image publicly accessible
    blob.make_public()

    print(f'File {image_path} uploaded to {destination_blob_name}.')
    print(f'File URL: {blob.public_url}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload Foto atau Video ke  Firebase Storage.")
    parser.add_argument("--source", required=True, help="Path ke File yang mau di upload.")
    parser.add_argument("--destination", required=True, help="Path ke Lokasi File mau di upload di Firebase.")
    
    args = parser.parse_args()
    
    upload_image(args.source, args.destination)