import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.administration import KeyVaultAccessPolicyManager
from azure.keyvault.administration import AccessPolicy

def create_access_policy(vault_name, email):
    # Set up the credentials and client
    credential = DefaultAzureCredential()
    client = KeyVaultAccessPolicyManager(vault_name, credential)

    # Define the access policy
    access_policy = AccessPolicy(
        email=email,
        permissions={"secrets": ["get", "list"], "keys": ["get", "list"]}  # Specify permissions as needed
    )

    # Create the access policy
    try:
        client.create_access_policy(access_policy)
        print(f"Access policy created for {email} in Key Vault {vault_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    vault_name = input("Enter Key Vault Name: ")
    email = input("Enter Email ID: ")
    create_access_policy(vault_name, email)
