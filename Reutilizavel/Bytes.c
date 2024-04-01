#include <stdio.h>
#include <string.h>

void bytes_da_string(const char *str) {
    int i;
    for (i = 0; i < strlen(str); i++) {
        printf("%d", str[i]);
        if (i < strlen(str) - 1) {
            printf(", ");
        }
    }
    printf("\n");
}

int main() {
    const char *texto = "Olá, mundo!";
    printf("Bytes da string \"%s\": ", texto);
    bytes_da_string(texto);
    return 0;
}
