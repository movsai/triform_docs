# Working with Modules

Modules are at the heart of Triform, allowing you to create and run custom Python scripts powered by the Langchain framework. This section will guide you through creating, managing, and utilizing Modules.

## Creating a Module

Creating a Module is the first step to harnessing the power of AI-scripts on Triform.

### Steps to Create a Module:

1. **Navigate to the Modules Section**:
   - From the main dashboard, click on 'Modules' in the left-hand menu.

2. **Initiate Module Creation**:
   - Click on 'Create Module' at the top of the Modules page.

3. **Configure Your Module**:
   - Set a 'Module Name' and provide a 'Module Description' for clarity.
   - Choose between 'Blank Template' or 'Langchain' for your script template:
     - Blank Template: Starts with a basic structure, allowing you to script from scratch.
     - Langchain: Provides a pre-filled script with Langchain imported and defined inputs/outputs.

4. **Editing Your Module**:
   - The 'Code Editor' will open, where you can write or paste your Python script.
   - Utilize the inputs and outputs defined in the template to structure your script.

5. **Saving Your Module**:
   - After editing, click 'Save' to deploy your script as a Lambda function.
   - Each save increments the version number, allowing you to track changes over time.

## Managing Modules

Once you've created Modules, managing them is straightforward.

### Viewing and Editing Modules:

- To view a Module, navigate to the Modules list and click 'View Module' next to the desired one.
- In the 'Code Editor', you can make changes to your script.
- Remember to save your changes to update the Module.

## Module Execution and Outputs

Running your Modules and analyzing outputs is essential for testing and utilization.

### Running a Module:

- Click 'Run' in the 'Code Editor'.
- Define the input parameters in the provided box.
- Execute the script to see the output, which is crucial for debugging and understanding your Module's functionality.

## Best Practices for Module Creation

- Keep your scripts concise and well-commented for ease of understanding and collaboration.
- Regularly test and update your Modules to ensure they function as expected.
- Utilize version control to manage changes and maintain script integrity.

In this section, we've covered creating and managing Modules in Triform. Next, we'll dive into how you can string these Modules together into powerful workflows using Flows.

