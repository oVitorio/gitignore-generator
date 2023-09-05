import requests
import click

@click.command()
@click.argument('type', type=str)
def create_gitignore(type):
    """
    Create a .gitignore file based on the type of project specified by the user.

    Args:
        type (str): The type of project for which the .gitignore file needs to be created.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the process.

    Example Usage:
        $ python create_gitignore.py python
        File .gitignore created successfully for type python.
    """
    # Build the URL based on the type passed via the terminal
    url = f"https://www.toptal.com/developers/gitignore/api/{type}"

    try:
        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            # Get the content from the response
            content = response.text

            # Create the .gitignore file with the obtained content
            with open('.gitignore', 'w') as file:
                file.write(content)

            print(f'File .gitignore created successfully for type {type}.')
        else:
            print(f'Error: Unable to find a .gitignore template for type {type}.')
            print(f'Please visit https://www.toptal.com/developers/gitignore/ to check if the type is valid.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    create_gitignore()
