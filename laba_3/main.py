from game.game import Game


def main():
    g = Game(settings_file='game/settings.json')
    while g.settings.running:
        g.settings.curr_menu.display_menu()
        g.game_loop()


if __name__ == "__main__":
    main()
