import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )


    def test_search_löytää_pelaajat(self):
        player = self.stats.search("Semenko")

        self.assertEqual(player.name, "Semenko")
    
    def test_search_ei_löydä_pelaajaa(self):
        player = self.stats.search("Korianteri")

        self.assertEqual(player, None)

    def test_team_löytää_pelaajat(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)

    def test_näytä_top_pelaajat(self):
        players = self.stats.top(3)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

    def test_näytä_top_pelaajat_maaleilla(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Kurri")
    
    def test_näytä_top_pelaajat_syötöillä(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Lemieux")
