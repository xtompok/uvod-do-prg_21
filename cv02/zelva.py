# Importujeme funkce pro pohyb dopředu, otočení doleva a ukončení až po kliknutí do okna
from turtle import forward,left, exitonclick

# Pohni se dopředu o 30 kroků
forward(30)
# Otoč se doleva o 30 stupňů
left(30)
forward(30)
# Nech okno otevřené, než do něj uživatel klikne (jinak hned zmizí)
exitonclick()