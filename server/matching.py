'''Player Matching algroithm'''

import threading
import game

players_queue = []
games = []


def match_players(player,lock):
    lock.acquire()
    if players_queue == []:
        players_queue.append(player)
        lock.release()
        return

    else:
        p1 = players_queue[0]
        g = game.Game(p1, player)
        games.append(g.id)
        print(f"{len(games)}th Game started")

        players_queue.remove(p1)
        lock.release()
        player.sendMsg(f"Game started with {p1.username}")
        p1.sendMsg(f"Game started with {player.username}")
        games.append(g)

        t = threading.Thread(target=game.handle_game, args=(g,))
        t.daemon = True
        t.start()