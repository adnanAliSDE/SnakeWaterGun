# swg_csproject
# Snake, Water, Gun Game with Multithreading

## Introduction

This project is a command-line interface (CLI) based implementation of the Snake, Water, Gun game, utilizing Python's multithreading capabilities for handling multiple clients concurrently. The game follows the classic rules, where Snake defeats Water, Water defeats Fire, and Fire defeats Snake.

## Features

- Supports multiple clients connecting to a central game server concurrently.
- Clients can make their game choices (Snake, Water, or Gun) and play against each other.
- The game server evaluates the choices and declares the winner.
- Gracefully handles client disconnections.

## Prerequisites

- Python 3.x installed on your system.

## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/multithreaded-snake-water-gun.git

2. Navigate to the project directory:

```shell
cd multithreaded-snake-water-gun
```
3. Run the server:

```html
python server.py 
```
4. Run clients (in separate terminal windows or tabs):

```shell
python client.py
```
You can run multiple clients to play against each other.

## Usage
When a client connects, they can enter their choice (Snake, Water, or Gun) in the CLI.
The game server will announce the winner after both clients have made their choices.
Clients can play additional rounds by making new choices.
## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix: git checkout -b feature/your-feature-name.
- Make your changes and commit them: git commit -m 'Add a new feature'.
- Push to the branch: git push origin feature/your-feature-name.
- Create a pull request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thanks to the Python community for providing multithreading support.
Special thanks to anyone who contributes to this project.
Contact
If you have any questions, issues, or suggestions, please feel free to contact us at adnann3077@gmail.com.
