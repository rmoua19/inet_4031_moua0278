import unittest
import sphere

class sphereTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(sphere.volume(10) == 4188.790204786391)

    def test_volume2(self):
        assert(sphere.volume(5) == 523.5987755982989)

    def test_sa(self):
        assert(sphere.surfaceArea(3) == 113.09733552923255 )
    #failing test
    #def test_volume3(self):
    #    assert(cylinder.volume(10,1000) == 0)


if __name__ == '__main__':
    unittest.main()
