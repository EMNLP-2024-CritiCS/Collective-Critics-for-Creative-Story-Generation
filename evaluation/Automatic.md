# GPT-4 Automatic Evaluation Script

This page allows you to run an evaluation with GPT-4 using a Python script. The script automates the process of passing required arguments like start and end indices, directories for Story A and B, evaluation criteria, OpenAI API key, and the prompt type to the Python script (`evaluation_gpt4.py`).

## Prerequisites

Before running the script, make sure you have:
- Python 3 installed.
- OpenAI's GPT-4 API access.

## Usage

The `run_evaluation.sh` script can be run in two ways:
1. **Using default values**: If you don't specify any values, the script will use predefined default values.
2. **Providing custom values**: You can specify your own values for each argument when running the script.

### Default Values
If you run the script without providing any arguments, the following default values will be used:

- `START_INDEX`: 1
- `END_INDEX`: 3
- `ROOT_DIR_A`: `./story/A`
- `ROOT_DIR_B`: `./story/B`
- `CRITERIA`: `Interesting,Coherence,Creative,Closer`
- `API_KEY`: `your_openai_api_key`


### Explanation of Each Value:

1. **`start_index` (Integer)**:
   - The starting index for the evaluation process. It refers to the first data point or item in a sequence that will be evaluated.
   - Example: `518`

2. **`end_index` (Integer)**:
   - The ending index for the evaluation process. It defines the last data point or item in the sequence that will be evaluated.
   - Example: `599`

3. **`root_dir_A` (String)**:
   - The file path to the directory where Story A is stored. Each evaluation compares Story A with Story B, and this path points to the folder containing Story A files (e.g., `1.txt`, `2.txt`).
   - Example: `./story_plan/A`

4. **`root_dir_B` (String)**:
   - The file path to the directory where Story B is stored. Like `root_dir_A`, this path points to the folder containing Story B files that will be evaluated and compared with Story A.
   - Example: `./story_plan/B`

5. **`criteria` (String)**:
   - The evaluation criteria, separated by commas. These are the qualities or attributes on which the stories will be evaluated, such as how interesting or coherent the stories are.
   - Common criteria include:
     - **Interesting**: How engaging the story is.
     - **Coherence**: How well the story flows and makes sense.
     - **Creative**: How original or imaginative the story is.
     - **Closer**: How well the story comes to a satisfying conclusion.
   - Example: `Interesting,Coherence,Creative,Closer`

6. **`api_key` (String)**:
   - Your OpenAI API key, which is required to access the GPT-4 model. This key is used for authenticating your requests to OpenAI’s API. You should replace `your_openai_api_key` with your actual API key.
   - Example: `sk-xxxxxx`

### Running with Default Values

To run the script using the default values, simply execute:

```bash
$ ./run_evaluation.sh