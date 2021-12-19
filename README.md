# Семестровый проект - Гравитационное линзирование.

Программное обеспечение включает в себя:
 1. main - основной модуль, описание смотри ниже;
 2. 3d-двигатель, он же - симулятор телескопа; содержит: threeD_main, object_3d, camera, projection, matrix_functions;
 3. model - мозг, просчитывает эффект;
 4. buttons - обеспечивает возможность взаимодествия пользователя с продуктом;
 5. plots - поставщик графиков;
 6. constants - содержит физические величины, настройки моделирования.
 
 Запуск программы осуществляется посредством модуля main. После запуска начинает открывается начальный экранy, на котором расположены кнопки запуска моделирования и получения справки. При запуске появляется космическое пространство, которое можно вращать. Для ориентации посмотрите на коориднатные оси. Для того, чтобы наблюдать эффект, добавьте черную дыру. Пользователю также доступны графики зависимостей угла отклонения от углового расстояние от звезды до чёрной дыры, угла отклонения от массы чёрной дыры, зависимость угла отклонения от расстояния до чёрной дыры, которые могут быть открыты посредством соответствующих кнопок.
 
 Корректная работа проверена с следующими версиями стороннего обепечения:
 Программное обеспечение включает в себя:
 1. Python 3.9.7
 2. pygame 2.0.1
 3. SDL 2.0.14
 4. numba
 5. numpy
 6. math
 7. matplotlib.pyplot
