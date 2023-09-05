<p align="center">
 <a href="#-About-the-project">About</a> •
 <a href="#-Features">Features</a> •
 <a href="#-How-to-run-the-project">How to Run</a> •
 <a href="#-Technologies">Technologies</a> •
 <a href="#-License">License</a>
</p>

## 💻 About the project

The Gitignore Creator is a Python utility that allows you to generate .gitignore files for specific development environments or languages by fetching data from the [toptal.com API](https://www.toptal.com/developers/gitignor).

In software development, a `.gitignore` file specifies intentionally untracked files that Git should ignore. These files typically include temporary files, build artifacts, and sensitive information like API keys. Managing a `.gitignore` file can be challenging, especially when working on different projects with different requirements. The Gitignore Creator simplifies this process by automating the generation of `.gitignore` files tailored to your project's needs.

---

## ⚙️ Features

- **Generate .gitignore files:** You can use the Gitignore Creator to quickly create `.gitignore` files for various development environments, languages, and tools commonly used in software development.

- **User-friendly CLI:** The tool provides a user-friendly command-line interface (CLI) that allows you to generate `.gitignore` files with a simple command.

- **Accurate and up-to-date data:** The Gitignore Creator fetches data from the well-known [toptal.com API](https://www.toptal.com/developers/gitignor), ensuring that the generated `.gitignore` files are accurate and up to date with the latest recommendations.

Whether you're working on a web development project, a mobile app, or any other software project, the Gitignore Creator streamlines the process of creating `.gitignore` files, helping you keep your version control repositories clean and organized.

---

## 🚀 How to run the project

You can use the Gitignore Creator as a command-line tool. Here's how to set it up:

### Installation

1. Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Open your terminal and install the Gitignore Creator with pip3 by running the following command:

```BASH
pip3 install .
```

### Generating .gitignore Files

Once installed, you can generate a `.gitignore` file for your specific development environment or language by following these steps:

1. Open a terminal.

2. Run the Gitignore Creator by typing the following command:

```BASH
gitignore-creator TYPE
```

Replace `TYPE` with the desired development environment or language. For example: `gitignore-creator Node`

3. The Gitignore Creator will fetch the appropriate `.gitignore` template and create a file named `.gitignore` in the current directory.

That's it! You now have a customized `.gitignore` file tailored to your project's needs.

---

## 🛠 Technologies

- Python
- Click (for the CLI)
- Requests (for making HTTP requests)

---

## 💪 How to contribute to the project

1. Fork the project.
2. Create a new branch with your changes: `git checkout -b my-feature`.
3. Save your changes and create a commit message explaining what you did: `git commit -m "feature: My new feature"`.
4. Send your changes: `git push origin my-feature`.

---

## 📝 License

This project is licensed under the [license-here](./LICENSE).
