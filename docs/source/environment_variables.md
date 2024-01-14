## Understanding Environment Variables

Environment variables are key-value pairs stored outside your scripts, making it easier to manage settings that can change based on the environment (like API keys, database URLs, etc.).

## Creating Environment Variables

Setting up environment variables allows your modules and flows to access necessary configuration data securely.

### Steps to Create an Environment Variable:

1. **Navigating to Environment Variables**:
   - From the main dashboard, click on 'Environment' in the left-hand menu.

2. **Adding a New Variable**:
   - Click 'Add Variable'.
   - Enter the 'Name' for the variable, its 'Value', and a brief 'Description'.
   - Click 'Save' to store the new variable.

## Using Environment Variables in Your Scripts

You can access these variables in your Python scripts, which is especially useful for sensitive data like API keys.

### Accessing Variables in Python:

```python
import os

# Example of accessing an environment variable
api_key = os.environ.get('API_KEY')

## Managing Existing Variables

You can view, edit, or delete your existing environment variables as needed.

### Editing and Deleting Variables:

- **Viewing Variables**:
  - Navigate to the 'Environment' section in Triform to see a list of all your environment variables.

- **Editing a Variable**:
  - Click 'Edit' next to the variable you wish to modify.
  - Update the 'Value' or 'Description' as needed.
  - Save the changes to update the variable.

- **Deleting a Variable**:
  - If a variable is no longer needed, you can remove it by clicking 'Delete' next to the respective variable.
  - Confirm the deletion to permanently remove the variable.

## Best Practices for Environment Variables

- **Security**: Avoid storing sensitive information like passwords directly in your scripts. Use environment variables to keep such data secure.
- **Consistency**: Maintain consistent naming conventions for your environment variables. This practice helps in managing and identifying variables across different environments.
- **Documentation**: Document each environment variable, explaining its purpose and usage. This step is crucial for maintaining clarity, especially in team settings.

By effectively managing environment variables in Triform, you enhance the security and scalability of your modules and flows.