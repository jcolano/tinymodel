# TinyModel

TinyModel is a Python package designed to interact with specialized, efficient machine learning models known as "Tiny Models".

## What are Tiny Models?

A Tiny Model is a paradigm shift in machine learning, emphasizing compactness and efficiency. Unlike Large Language Models (LLMs), which require significant computational resources, Tiny Models are built to be lightweight and efficient. They are ideal for use on consumer-grade computers, requiring minimal resources.

### Key Features:

- **Efficient and Lightweight**: Designed to run efficiently on limited resources, making them suitable for consumer-grade hardware.
- **Specialized Performance**: Although smaller in size, they deliver very good results for specific domains or tasks.
- **Cost-Effective**: A viable alternative for domain-specific solutions, reducing the need for substantial computational infrastructure.

### Use Cases:

- Ideal for organizations seeking efficient, domain-specific machine learning solutions.
- Suitable for applications where minimizing computational overhead is crucial.
- Perfect for researchers and hobbyists with limited access to high-end computational resources.

## Installation

Install TinyModel using pip:

```bash
pip install tinymodel

### Usage

TinyModel currently supports completion and Q&A models trained on philosophy books and classic literature.

### Example usage:

```python
from tinymodel import TinyModel

# Initialize the client with your API key
client = TinyModel(api_key="your_api_key_here")

# Get a completion from the philosophy model
philosophy_response = client.completions.create(
    model="philosophy",
    prompt="What is the essence of happiness?",
    max_tokens=512
)

# Get a completion from the literature model
literature_response = client.completions.create(
    model="literature",
    prompt="Describe the themes in 19th-century British literature.",
    max_tokens=512
)

print(philosophy_response)
print(literature_response)


### Contributing

Contributions to TinyModel are welcome. Please read the contributing guidelines to get started.

### License

TinyModel is released under the MIT License.

### Contact

For questions or feedback, contact Juan Olano at jcolano@teams.us
