class Constants:
    def __init__(self):
        """
        Здесь параметры чёрной дыры - параметра Солнца.
        """
        self.m = 1.989 * (10 ** 30)  # масса чёрной дыры
        self.c = 299792458  # скорость света
        self.g = 6.67408 * 10 ** (-11)  # гравитационная постоянная
        self.d = 149597870700  # расстояние до чёрной дыры
        self.width = 1000  # ширина экрана, условность
        self.x0 = self.width / 2  # координата x центра чёрной дыры на экране
        self.height = 500  # высота экрана, условность
        self.y0 = self.height / 2  # координата y центра чёрной дыры на экране
        self.s = 1500
        self.r_bh_screen = 50


c = Constants()
