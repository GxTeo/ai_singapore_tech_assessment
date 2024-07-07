### README for `text_generation.py`


# Text Generation using GPT-2

This Python script interacts with the Hugging Face API to generate text based on a given input prompt using the GPT-2 model.

## How It Works

1. **API URL and Token**: The script uses the GPT-2 model hosted on Hugging Face. You need to set your Hugging Face API token in the environment variable `HUGGINGFACE_API_TOKEN`.
2. **User Prompt**: The script takes an input prompt from the user.
3. **Query the API**: It sends a request to the API with the prompt and additional parameters like `max_new_tokens`, `num_return_sequences`, and `temperature`.
4. **Retrieve and Display Output**: The script processes the API response and prints both the input prompt and the generated text.

### README for `word_frequency.py`
# Word Frequency Counter

This Python script calculates the frequency of words in a text file and prints the words ranked from 10th to 20th by frequency.

## How It Works

1. **Reading the Text File**: The script reads the content of a text file
2. **Splitting the Text**: The text is split into individual words.
3. **Counting Word Frequencies**: The script counts how many times each word appears in the text.
4. **Sorting by Frequency**: The words are sorted by their frequency in descending order.

