
# zgpt 🐚🤖

A versatile and easy-to-use command-line AI assistant powered by the **Google Gemini API**.

## 🚀 Features

- **Simple Interface**: Get answers directly in your terminal.
- **Easy Setup**: Configure your API key with a single command.
- **Secure**: Your API key is stored locally in your user configuration directory.

## 📦 Installation

First, clone the repository and navigate into the directory:

```bash
git clone [https://github.com/your-username/zgpt.git](https://github.com/your-username/zgpt.git)
cd zgpt
```

Then, install the package in editable mode. This is great for development and ensures the `zgpt` command is available system-wide.

```bash
pip install -e .
```

## 🔑 Setup

Before you can use `zgpt`, you need to set your Gemini API key. Run the `--init` command:

```bash
zgpt --init
```

You will be prompted to enter your API key. Once saved, you're ready to go!

You can remove the key at any time:

```bash
zgpt --revoke
```

## 💡 Usage

To ask a question, simply type `zgpt` followed by your prompt:

```bash
zgpt "explain what a decorator is in python with a simple example"
```bash
zgpt "give me a 5-line summary of the movie Inception"
```

## 🛠 Example

```bash
$ zgpt "hello"

🤔 Thinking...
🤖

Hello there! How can I help you today?
```
