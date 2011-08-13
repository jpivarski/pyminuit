import unittest
import minuit

def f(x, y):
    return ((x-2) / 3)**2 + y**2 + y**4

class Test(object):

    def __init__(self, xmin, ymin):
        self.xmin = xmin
        self.ymin = ymin

    def __call__(self, x, y):
        return ((x-self.xmin) / 3)**2 + (y - self.ymin)**2 + (y - self.ymin)**4

    def func(self, x, y):
        return ((x-self.xmin) / 3)**2 + (y - self.ymin)**2 + (y - self.ymin)**4

class TestFunction(unittest.TestCase):

    def setUp(self):
        self.minuit = minuit.Minuit(f, x=10, y=10)

    def test_minimization(self):
        self.minuit.migrad()
        x = self.minuit.values["x"]
        y = self.minuit.values["y"]
        self.assertAlmostEqual(x,2.0,2)
        self.assertAlmostEqual(y,0.0,2)

class TestCallable(unittest.TestCase):

    def setUp(self):
        self.xmin = 2.0
        self.ymin = 5.0
        self.callable = Test(self.xmin,self.ymin)
        self.minuit = minuit.Minuit(self.callable, x=10, y=10)

    def test_minimization(self):
        self.minuit.migrad()
        x = self.minuit.values["x"]
        y = self.minuit.values["y"]
        self.assertAlmostEqual(x,self.xmin,2)
        self.assertAlmostEqual(y,self.ymin,2)

class TestClassMethod(unittest.TestCase):

    def setUp(self):
        self.xmin = 2.0
        self.ymin = 5.0
        self.callable = Test(self.xmin,self.ymin)
        self.minuit = minuit.Minuit(self.callable.func, x=10, y=10)

    def test_minimization(self):
        self.minuit.migrad()
        x = self.minuit.values["x"]
        y = self.minuit.values["y"]
        self.assertAlmostEqual(x,self.xmin,2)
        self.assertAlmostEqual(y,self.ymin,2)

if __name__ == '__main__':
    unittest.main()
