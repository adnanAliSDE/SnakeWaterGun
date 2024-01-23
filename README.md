# Snake Water Gun Game with Multithreading

## Overview

This project is a Python-based implementation of the Snake Water Gun game with multithreading support for handling multiple players concurrently. The game follows the classic rules, where Snake defeats Water, Water defeats Gun, and Gun defeats Snake. It provides a command-line interface (CLI) for players to connect, make their choices, and compete against each other.


## Features

- Random matching: Allows you to play with random people over the network
- Multithreading: Supports multiple players connecting to a central game server at the same time.
- Real-time Gameplay: Players can make their game choices and engage in matches against each other.
- Fair Outcomes: The game server evaluates player choices and determines the winner based on classic rules.
- Resilience: Gracefully handles client disconnections for a seamless gaming experience.

## Prerequisites

- Python 3.x installed on your system.

## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/adnanalisde/snakewatergun.git
   ```

2. Navigate to the project directory:

   ```shell
   cd snakewatergun
   ```

3. Run the server:

   ```shell
   python server.py 
   ```

4. Run clients (in separate terminal windows or tabs):

   ```shell
   python client.py
   ```

   You can run multiple clients to play against each other on the same or different computers over the same network.

## Usage

- Once connected, players can enter their choice of Snake, Water, or Gun in the CLI.
- The game server will determine the winner after all players have made their choices.
- Players can continue playing additional rounds by making new choices and by restarting the client.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: 
`git checkout -b feature/your-feature-name `.
3. Make your changes, commit them with a descriptive message.
4. Push your changes to the branch.
5. Create a pull request to merge your changes into the main project.

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](LICENSE) file.

## Acknowledgments

- Thanks to the Python community for providing multithreading support.
- Special thanks to anyone who contributes to this project.

## Contact

If you have any questions, issues, or suggestions related to the Snake Water Gun Game with Multithreading project, please feel free to contact the project maintainer at adnann3077@gmail.com.