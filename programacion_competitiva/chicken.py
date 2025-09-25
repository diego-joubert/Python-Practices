#include <iostream>

int main() {
    int n;
    std::cin >> n; // Leer el número de casos de prueba

    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x; // Leer la cantidad de trozos que quiere David
        bool canBuy = false;

        // Probar diferentes valores de b (porciones grandes)
        for (int b = 0; b <= x / 7; ++b) {
            if ((x - 7 * b) % 3 == 0) {
                canBuy = true;
                break; // Encontramos una combinación válida
            }
        }

        if (canBuy) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }

    return 0;
}