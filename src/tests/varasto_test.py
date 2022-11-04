import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        varasto = Varasto(-8)
        # self.assertEqual(varasto.paljonko_mahtuu(), 0)

    def test_varastoon_ei_voi_lisata_negatiivista(self):
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_varstoon_ei_voi_lisata_enempaa_kuin_mahtuu(self):
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)
        self.varasto.lisaa_varastoon(11)
        self.varasto.ota_varastosta(10)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_alkusaldo_ei_voi_olla_negatiivinen(self):
        varasto = Varasto(10, -5)
        self.assertEqual(varasto.paljonko_mahtuu(), 10)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        varasto = Varasto(10,5)
        mita_saatiin = varasto.ota_varastosta(-2)
        self.assertEqual(mita_saatiin, 0)

    def test_varastosta_ei_voi_ottaa_enempaa_kuin_sen_saldo(self):
        varasto = Varasto(10,5)
        mita_saatiin = varasto.ota_varastosta(7)
        self.assertEqual(mita_saatiin, 5)

    def test_merkkijonoesitys_toimii(self):
        varasto = Varasto(10, 5)
        assert str(varasto) == "saldo = 5, vielä tilaa 5"
